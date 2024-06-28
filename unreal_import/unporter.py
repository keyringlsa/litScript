import sys

require_paths = [
    "P:/TD/maya/2024/packages/Lib/site-packages",
    "P:/config/STUDIO/install/core/python",
    "P:/TD/maya/2022/inhousetools"
]
for i in require_paths:
    sys.path.append(i)
from imp import reload
from PySide2 import QtCore, QtGui, QtWidgets

from unreal_import.UI import unreal_asset_UI

from unreal_import.handler import shotgrid_handler, unreal_handler, shader_importer
from unreal_import.model import astype_model, pub_model
import sgtk
from CoreModules.handler import connect_sg




reload(unreal_asset_UI)
reload(astype_model)
reload(pub_model)
reload(shotgrid_handler)
reload(shader_importer)
reload(unreal_handler)
reload(connect_sg)


class Worker(QtCore.QObject):
    finished = QtCore.Signal()

    def run(self, function, *args):
        function(*args)
        self.finished.emit()


class Main(QtWidgets.QMainWindow):

    def __init__(self, parent=None):  # parent는 반드시 None
        super(Main, self).__init__(parent)


        self.ui = unreal_asset_UI.Ui_MainWindow()  # UI 클래스로 선언
        self.ui.setupUi(self)  # setup

        # Shotgun 연결
        sgl = connect_sg.Shotgun_Connect()
        self.sg = sgl.default_script_auth()



        current_engine = sgtk.platform.current_engine()
        self.context = current_engine.context
        self.project = self.context.project

        self.file_dir_model = None
        self.data_dir_model = None
        # pub 모델 및 델리게이트 설정
        self.pub_items_model = None
        self.import_proxy_model = QtCore.QSortFilterProxyModel()
        self.ImportButtonDelegate = pub_model.ImportedItemDelegate()

        self.ui.asset_list.setItemDelegate(self.ImportButtonDelegate)
        self.ui.asset_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        self.ui.asset_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.asset_list.customContextMenuRequested.connect(self.importedView_context_menu)


        self.connected()



    def connected(self):



        # List
        #self.ui.Refresh_btn.clicked.connect(self.refresh_data)
        self.set_model()

        self.ui.asset_list.clicked.connect(self.select_item)
        self.ImportButtonDelegate.cmb_index_changed.connect(self.change_imported_item_version)
        self.ImportButtonDelegate.button_clicked.connect(self.replace_imported_item)
        self.ImportButtonDelegate.shader_assign_clicked.connect(self.assign_shader)

        self.ui.fol_btn.clicked.connect(self.create_folder_in_unreal)








    ############################################### list tab

    def on_lkd_type_changed(self):
        # LKD_type 값이 변경될 때마다 모델 업데이트
        self.set_model()


    def set_model(self):
        row_datas = shotgrid_handler.get_category(sg=self.sg, project=self.project)
        self.file_dir_model = astype_model.type_Model(row_datas=row_datas)
        self.ui.asset_type.setModel(self.file_dir_model)
        self.ui.asset_type.clicked.connect(self.file_model)




    def file_model(self):
        sel_index = self.ui.asset_type.currentIndex()
        item_type = self.file_dir_model.data(sel_index, role=QtCore.Qt.UserRole)
        sel_type = item_type.type

        exist_file_names = unreal_handler.already_exists_files(sel_type)
        cate_items = shotgrid_handler.get_category(sg=self.sg, project=self.project)
        pub_items = shotgrid_handler.get_pub_datas(sg=self.sg, project=self.project)

        row_datas = dict()

        for pub_name, pub_item in pub_items.items():
            versions = pub_item['items']

            for version in versions:
                current_version = version

                data_dict = dict()
                data_dict[pub_name] = {
                    'current_version': current_version,
                    'all_versions': versions,
                    'type': pub_item['type']

                }

                asset_name = pub_name

                if asset_name not in row_datas:
                    row_datas[asset_name] = {'geometry': [data_dict], 'shader': []}
                else:
                    row_datas[asset_name]['geometry'].append(data_dict)

        for asset_name in row_datas:
            shaders = shotgrid_handler.get_published_shd_file(sg=self.sg, project=self.project, asset_name=asset_name)
            row_datas[asset_name]['shader'].extend(shaders)


        self.pub_items_model = pub_model.PubItemTreeModel(row_datas=row_datas, head_items=cate_items, asset_type=sel_type)
        self.import_proxy_model.setSourceModel(self.pub_items_model)

        self.import_proxy_model.sort(2, QtCore.Qt.DescendingOrder)

        self.ui.asset_list.setModel(self.import_proxy_model)

        for i in range(self.import_proxy_model.rowCount()):
            asset_index = self.import_proxy_model.index(i, 0)
            for a_i in range(self.import_proxy_model.rowCount(asset_index)):
                type_index = self.import_proxy_model.index(a_i, 0, asset_index)

                for t_i in range(self.import_proxy_model.rowCount(type_index)):
                    for t_c in range(self.import_proxy_model.columnCount(type_index)):
                        item_index = self.import_proxy_model.index(t_i, t_c, type_index)

                        self.ui.asset_list.openPersistentEditor(item_index)

        self.ui.asset_list.expandAll()
        for i in range(self.ui.asset_list.header().count()):
            self.ui.asset_list.resizeColumnToContents(i)



    @QtCore.Slot(QtCore.QPoint)
    def importedView_context_menu(self, pos):
        viewport = self.ui.asset_list.viewport()
        menu = QtWidgets.QMenu(viewport)

        multi_item_import_menu = menu.addAction('Print - Dev Data')



        menu.exec_(viewport.mapToGlobal(pos))

    @QtCore.Slot(str, object)
    def change_imported_item_version(self, version_str, row_index):
        self.import_proxy_model.setData(row_index, version_str, QtCore.Qt.UserRole + 1)

    @QtCore.Slot(object)
    def replace_imported_item(self, index):
        sel_index = self.ui.asset_type.currentIndex()
        item_type = self.file_dir_model.data(sel_index, role=QtCore.Qt.UserRole)
        sel_type = item_type.type
        row_data = self.import_proxy_model.data(index, role=QtCore.Qt.UserRole)
        unreal_handler.import_pub_item(row_data=row_data, type_datas=sel_type)

        self.import_proxy_model.setData(index, None, QtCore.Qt.UserRole + 2)

    @QtCore.Slot(object)
    def assign_shader(self, index):
        sel_index = self.ui.asset_type.currentIndex()
        item_type = self.file_dir_model.data(sel_index, role=QtCore.Qt.UserRole)
        sel_type = item_type.type

        imported_ver = unreal_handler.already_exists_files(sel_type)



        shader_row_data = self.import_proxy_model.data(index, role=QtCore.Qt.UserRole)

        asset_name_index = index.parent().parent()
        asset_name = self.import_proxy_model.data(asset_name_index, role=QtCore.Qt.UserRole).name
        target_meshes = list()

        for row in range(self.import_proxy_model.rowCount(asset_name_index)):
            second_row_index = self.import_proxy_model.index(row, 0, asset_name_index)

            for p_row in range(self.import_proxy_model.rowCount(second_row_index)):
                third_row_index = self.import_proxy_model.index(p_row, 0, second_row_index)
                third_row_data = self.import_proxy_model.data(third_row_index, role=QtCore.Qt.UserRole)
                if third_row_data.data_type == "GEO":
                    target_meshes.append(third_row_data.name)


        shader_importer.import_shader(row_data=shader_row_data, target_type=sel_type, imported_ver=imported_ver)


    def get_selected_indexes_from_imported_view(self):

        sel_indexes = self.ui.asset_list.selectedIndexes()
        filtered_indexes = list()

        for sel_idx in sel_indexes:
            column = sel_idx.column()
            data = self.import_proxy_model.data(sel_idx, QtCore.Qt.UserRole)

            if column == 0 and data.current_version is not None:
                filtered_indexes.append(data)

        return filtered_indexes
    def select_item(self):
        sel_data = self.get_selected_indexes_from_imported_view()

        for i in sel_data:
            if i.prefix != '__MAT':
                pass



    def create_folder_in_unreal(self):
        sel_index = self.ui.asset_type.currentIndex()
        item_type = self.file_dir_model.data(sel_index, role=QtCore.Qt.UserRole)
        sel_type = item_type.type
        row_datas = shotgrid_handler.get_category(sg=self.sg, project=self.project)

        shader_importer.create_folder_in_unreal(row_datas=row_datas, target_type=sel_type)






def main():
    """
    Create tool window.
    """
    app = QtWidgets.QApplication.instance()  # Check if QApplication instance exists
    if not app:
        app = QtWidgets.QApplication(sys.argv)


    for win in QtWidgets.QApplication.allWindows():
        if 'toolWindow' in win.objectName():
            win.destroy()


    Main.window = Main()
    Main.window.setObjectName('toolWindow')  # Unique object name
    Main.window.setWindowTitle('Unporter')
    Main.window.show()




if __name__ == '__main__':
    main()










"""

import sys
from pprint import pprint

path = "D:\lt_team\maya_scripts"
sys.path.insert(0, path)

from imp import reload 


import unreal_import.unporter

reload(unreal_import.unporter) 
print(unreal_import.unporter.__file__)
unreal_import.unporter.main()

"""

