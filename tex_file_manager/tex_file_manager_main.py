import os, sys
import traceback

import sgtk
import subprocess
import multiprocessing

from PySide2 import QtWidgets, QtGui, QtCore
from pprint import pprint, pformat
from imp import reload
from tdsg_core.logHandler import TdLog

from tex_file_manager.ui import TFM_UI
from tex_file_manager.handler import maya_handler
from tex_file_manager.model import texnode_model

reload(TFM_UI)
reload(maya_handler)
reload(texnode_model)


filter_dict = {
    "Name": 0,
    "File Path": 1,
    "Tile Mode": 2,
    "Color Space": 3,
    "Multi Tile Files": 4,
}

def thread_fn(cmd=None, msg=None):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed with return code {e.returncode}")

    return msg

class WorkerSignals(QtCore.QObject):

    finished = QtCore.Signal(str)
    error = QtCore.Signal(tuple)
    result = QtCore.Signal(object)
    progress = QtCore.Signal(int)


class WorkerThread(QtCore.QRunnable):
    result_signal = QtCore.Signal(str)

    def __init__(self, fn, *args, **kwargs):
        super(WorkerThread, self).__init__()

        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.cmd = self.args[0]['cmd']
        self.msg = self.args[0]['msg']

        self.kwargs['progress_callback'] = self.signals.progress
    @QtCore.Slot()
    def run(self):

        try:
            result = self.fn(self.cmd, self.msg)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit("THREAD COMPLETE! \n")



class TFM_Main(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.tdlog = TdLog(debug_mode=True, name='TexFileManager')
        self.log = self.tdlog.logger
        self.log.info("-" * 20 + " TexFileManager App Started " + "-" * 20)

        self.current_file = os.path.dirname(os.path.realpath(__file__))
        print('=' * 100)
        print(self.current_file)
        print('=' * 100)

        self.setWindowFlag(QtCore.Qt.WindowType(True))
        self.ui = TFM_UI.Ui_TexFileManager_QWidget()
        self.ui.setupUi(self)

        # set thread pool
        self.threadpool = QtCore.QThreadPool()
        self.progres_value = 0
        self.progres_range = 0
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        # get current context
        current_engine = sgtk.platform.current_engine()
        self.context = current_engine.context
        self.log.debug(self.context)

        # set model

        self.file_node_model = None
        self.file_node_proxy = QtCore.QSortFilterProxyModel()
        self.file_node_proxy.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.FileNode_QTableView.setSortingEnabled(True)

        # set context model

        self.ui.FileNode_QTableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.FileNode_QTableView.customContextMenuRequested.connect(self.context_menu)

        self.connected()

    def connected(self):

        self.ui.Search_QLineEdit.returnPressed.connect(self.search_model)
        self.ui.Filter_QComboBox.currentIndexChanged.connect(self.change_filter_column)
        self.ui.Reload_Btn.clicked.connect(self.set_model)

        self.set_filter_combo()
        self.set_model()

    def change_filter_column(self):
        value = filter_dict[self.ui.Filter_QComboBox.currentText()]
        self.file_node_proxy.setFilterKeyColumn(value)
    def search_model(self):
        filter_text = self.ui.Search_QLineEdit.text()

        if ' ' in filter_text:
            filter_text = ' '.join(filter_text.split(' '))

        if ',' in filter_text:
            filter_text = '|'.join(filter_text.split(','))

        search = QtCore.QRegExp(filter_text,
                                QtCore.Qt.CaseInsensitive,
                                QtCore.QRegExp.RegExp)

        self.file_node_proxy.setFilterRegExp(search)
        self.ui.FileNode_QTableView.setModel(self.file_node_proxy)
    @QtCore.Slot(QtCore.QPoint)
    def context_menu(self, pos):
        viewport = self.ui.FileNode_QTableView.viewport()
        menu = QtWidgets.QMenu(viewport)

        menu_item_01 = menu.addAction('Print - Dev Data')
        menu_item_01.triggered[()].connect(self.dev_print)
        menu_item_02 = menu.addAction('Convert - Tx')
        menu_item_02.triggered[()].connect(self.convert_tx_file)
        menu_item_03 = menu.addAction('Open - Directory')
        menu_item_03.triggered[()].connect(self.open_dir)

        menu.exec_(viewport.mapToGlobal(pos))

    def open_dir(self):

        row_data = self.get_selected_indexes()[0]
        file_path = row_data.file_path
        dir_path, file_name = os.path.split(file_path)

        os.startfile(dir_path)

    def convert_tx_file(self):
        converter = r'C:\"Program Files"\Autodesk\Arnold\maya2022\bin\maketx.exe'
        ocio_file = 'C:/"Program Files"/Nuke13.2v4/plugins/OCIOConfigs/configs/aces_1.0.3/config.ocio'

        row_datas = self.get_selected_indexes()

        cmd_list = list()

        for row_data in row_datas:
            color_space = row_data.color_space
            temp_mode = False

            if color_space == 'scene-linear Rec.709-sRGB':
                temp_mode = True
                color_space = "".join(color_space.split(' '))

            for tex_file in row_data.tex_files:

                if os.path.isfile(tex_file):
                    name, ext = os.path.splitext(tex_file)
                    # tx_file = tex_file.replace(ext, ".tx")
                    tx_file = f"{name}_{color_space}_ACEScg{ext}.tx"

                    if temp_mode:
                        colorConvertString = f'--colorconvert Raw "ACEScg"  '
                    else:
                        colorConvertString = f'--colorconvert {color_space} "ACEScg"  '


                    cmd = f'{converter} {tex_file} -o {tx_file} -v --checknan \
                          --fixnan box3 --unpremult --oiio:overwritemode on -u -colorconfig {ocio_file} {colorConvertString} \
                          --format exr -d half'
                    complite_msg = f"Convert {tex_file} to \n {tx_file}"

                    cmd_dict = {"cmd":cmd, "msg":complite_msg}
                    cmd_list.append(cmd_dict)

        self.progres_range = len(cmd_list)
        self.ui.progressBar.setValue(0)

        for cmd_dict in cmd_list:

            self.worker_thread = WorkerThread(thread_fn, cmd_dict)
            self.worker_thread.signals.result.connect(self.print_output)
            self.worker_thread.signals.finished.connect(self.print_one_thread)
            self.threadpool.start(self.worker_thread)

        self.set_model()

    def print_output(self, msg):
        print(msg)
        self.progres_value += 1
        value = int(self.progres_value / self.progres_range * 100)
        self.ui.progressBar.setValue(value)
    def print_one_thread(self, msg):
        print(msg)

    def get_selected_indexes(self):
        indexes = self.ui.FileNode_QTableView.selectedIndexes()
        row_datas = list()

        for idx in indexes:
            row = idx.row()
            column = idx.column()

            if column == 0:
                row_datas.append(self.file_node_proxy.data(idx, role=QtCore.Qt.UserRole))

        return row_datas

    def dev_print(self):

        row_datas = self.get_selected_indexes()

        for _data in row_datas:
            pprint(_data.item)

    def set_filter_combo(self):

        for key_value in filter_dict:
            self.ui.Filter_QComboBox.addItem(key_value)

    def set_model(self):

        tex_file_row_data = maya_handler.get_file_nodes_from_current_scene()
        self.log.debug(pformat(tex_file_row_data))

        self.file_node_model = texnode_model.TexNodeTableModel(row_data=tex_file_row_data)
        self.file_node_proxy.setSourceModel(self.file_node_model)
        self.ui.FileNode_QTableView.setModel(self.file_node_proxy)

        self.ui.FileNode_QTableView.resizeColumnsToContents()
        self.ui.FileNode_QTableView.resizeRowsToContents()


def maya_main_run():
    from maya import OpenMayaUI as mui
    from shiboken2 import wrapInstance
    mayaMainWindowPtr = mui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QMainWindow)

    global app
    app = QtWidgets.QApplication.instance()
    excute_main = TFM_Main(mayaMainWindow)
    excute_main.show()
    app.exec_()

def main():
    app = QtWidgets.QApplication()
    excute_main = TFM_Main()
    excute_main.show()

    app.exec_()

if __name__ == '__main__':
    main()