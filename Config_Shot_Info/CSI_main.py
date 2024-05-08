import os, sys, shutil

import sgtk

from PySide2 import QtWidgets, QtGui, QtCore
from pprint import pprint
from glob import glob
from imp import reload

from CoreModules.handler import connect_sg
from Config_Shot_Info.ui import CSI_UI
from Config_Shot_Info.handler import shotgun_handler, maya_handler

reload(CSI_UI)
reload(shotgun_handler)
reload(maya_handler)




class CSIMain(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowFlag(QtCore.Qt.WindowType(True))
        self.ui = CSI_UI.Ui_CSI_QWidget()
        self.ui.setupUi(self)

        # get shotgun api
        sgl = connect_sg.Shotgun_Connect()
        self.sg = sgl.default_script_auth()

        # get current context
        current_engine = sgtk.platform.current_engine()
        self.context = current_engine.context

        # info
        self.item = None
        self.width_value = None
        self.height_value = None
        self.fps = None
        self.s_f = None
        self.e_f = None


        self.connected()

    def connected(self):
        self.set_data_into_ui()
        self.ui.Set_QButton.clicked.connect(self.dev)

    def dev(self):

        if self.ui.resolution_QCheckBox.isChecked():
            if self.width_value is not None:
                maya_handler.set_resolution(int(self.width_value), int(self.height_value))

        if self.ui.Cutinout_QCheckBox.isChecked():
            if self.fps is not None:
                maya_handler.set_fps(int(self.fps))

        if self.ui.Cutinout_QCheckBox.isChecked():
            if self.s_f is not None:
                maya_handler.set_frame_range(self.s_f, self.e_f)



    def set_data_into_ui(self):
        self.item = shotgun_handler.get_info_from_shotgrid(sg=self.sg, context=self.context)
        if self.item.get('project_resolution') is not None:
            self.width_value = self.item.get('project_resolution').split('*')[0]
            self.height_value = self.item.get('project_resolution').split('*')[-1]

            self.ui.Resolution_Width_QLineEdit.setText(self.width_value)
            self.ui.Resolution_Height_QLineEdit.setText(self.height_value)

        if self.item.get('project_fps') is not None:
            self.fps = self.item.get('project_fps')
            self.ui.Fps_QLineEdit.setText(str(self.item.get('project_fps')))

        if self.item.get('cut_in_frame') is not None:
            self.s_f = self.item.get('cut_in_frame')
            self.ui.StartFrame_QLineEdit.setText(str(self.item.get('cut_in_frame')))

        if self.item.get('cut_out_frame') is not None:
            self.e_f = self.item.get('cut_out_frame')
            self.ui.EndFrame_QLineEdit.setText(str(self.item.get('cut_out_frame')))


def main():
    app = QtWidgets.QApplication()
    excute_main = CSIMain()
    excute_main.show()

    app.exec_()

def maya_main_run():
    from maya import OpenMayaUI as mui
    from shiboken2 import wrapInstance
    mayaMainWindowPtr = mui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QMainWindow)

    global app
    app = QtWidgets.QApplication.instance()
    excute_main = CSIMain(mayaMainWindow)
    excute_main.show()
    app.exec_()

if __name__ == '__main__':
    main()