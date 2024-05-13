import sgtk, os
from pprint import pprint
from importlib import reload
from PySide2 import QtWidgets, QtCore

from CoreModules.handler import connect_sg
from LIT_grp.test_code.importABC.UI import ui_hoonie2
from importABC.model import imported_model, pub_model
from importABC.handler import maya_handler, shotgrid_handler, shader_importer

# 모듈 리로드
reload(connect_sg)
reload(ui_hoonie2)
reload(pub_model)
reload(imported_model)
reload(shotgrid_handler)
reload(shader_importer)
reload(maya_handler)

class HoonieMain(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(QtCore.Qt.WindowType(True))
        self.ui = ui_hoonie2.Ui_Form()
        self.ui.setupUi(self)

        # Shotgun 연결
        sgl = connect_sg.Shotgun_Connect()
        self.sg = sgl.default_script_auth()

        # get current context
        current_engine = sgtk.platform.current_engine()
        self.context = current_engine.context
        #self.log.debug(self.context)

        # pub 모델 및 델리게이트 설정
        self.pub_items = None
        self.import_proxy_model = QtCore.QSortFilterProxyModel()
        self.ImportButtonDelegate = pub_model.ImportButtonDelegate()
        self.ui.publist.setItemDelegate(self.ImportButtonDelegate)
        self.ui.publist.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        #imported 모델 및 델리게이트 설정
        self.imported_items = None
        self.imported_proxy_model = QtCore.QSortFilterProxyModel()
        self.ImportedItemDelegate = imported_model.ImportedItemDelegate()
        self.ui.importedlist.setItemDelegate(self.ImportedItemDelegate)
        self.ui.importedlist.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        # context menu item
        self.ui.publist.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.publist.customContextMenuRequested.connect(self.importView_context_menu)

        self.ui.importedlist.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.importedlist.customContextMenuRequested.connect(self.importedView_context_menu)


        self.connected()

    def connected(self):
        self.set_model()
        self.ui.btn_reload.clicked.connect(self.set_model)
        self.ui.btn_shotgrid.clicked.connect(self.open_shot_page)

        self.ImportButtonDelegate.cmb_index_changed.connect(self.change_import_item_version)
        self.ImportButtonDelegate.button_clicked.connect(self.import_into_current_scene)

        #self.ui.publist.clicked.connect(self.on_item_clicked)

        # delegate = self.ui.publist.itemDelegate()
        # if isinstance(delegate, pub_model.ImportButtonDelegate):
        #     delegate.cmb_index_changed.connect(self.change_import_item_version)
        #     delegate.button_clicked.connect(self.import_into_current_scene)

        self.ui.importedlist.clicked.connect(self.select_item)
        self.ImportedItemDelegate.cmb_index_changed.connect(self.change_imported_item_version)
        self.ImportedItemDelegate.button_clicked.connect(self.replace_imported_item)
        self.ImportedItemDelegate.shader_assign_clicked.connect(self.assign_shader)

    def open_shot_page(self):
        shotgrid_handler.open_shot_url(sg=self.sg, context=self.context)

    @QtCore.Slot(QtCore.QPoint)
    def importView_context_menu(self, pos):
        viewport = self.ui.publist.viewport()
        menu = QtWidgets.QMenu(viewport)

        multi_item_import_menu = menu.addAction('Import - Selected Items')
        multi_item_import_menu.triggered[()].connect(lambda: self.import_selected_items())
        open_item_directory_menu = menu.addAction('Open - Item Directory')
        open_item_directory_menu.triggered[()].connect(lambda: self.open_sel_item_dir())
        dev_print_menu = menu.addAction("Dev - Print")
        dev_print_menu.triggered[()].connect(self.dev_print)
        menu.exec_(viewport.mapToGlobal(pos))

    @QtCore.Slot(QtCore.QPoint)
    def importedView_context_menu(self, pos):
        viewport = self.ui.importedlist.viewport()
        menu = QtWidgets.QMenu(viewport)

        multi_item_import_menu = menu.addAction('Print - Dev Data')
        multi_item_import_menu.triggered[()].connect(self.print_data)


        menu.exec_(viewport.mapToGlobal(pos))



    def set_model(self):
        self.set_pub_model()
        self.set_imported_model()

    ## pub view actions ##
    def set_pub_model(self):
        exist_file_names = maya_handler.already_exists_files()
        cate_items = shotgrid_handler.get_category(sg=self.sg, context=self.context)
        pub_items = shotgrid_handler.get_pub_datas(sg=self.sg, context=self.context)

        self.pub_items = pub_model.ItemTreeModel(row_datas=pub_items, head_items=cate_items, exist_files=exist_file_names)
        self.import_proxy_model.setSourceModel(self.pub_items)

        self.import_proxy_model.sort(2, QtCore.Qt.DescendingOrder)


        self.ui.publist.setModel(self.import_proxy_model)

        for i in range(self.import_proxy_model.rowCount()):
            parent_index = self.import_proxy_model.index(i, 0)
            parent_item = parent_index.data(QtCore.Qt.UserRole)

            for p_i in range(self.import_proxy_model.rowCount(parent_index)):

                combo_index = self.import_proxy_model.index(p_i, 5, parent_index)
                button_index = self.import_proxy_model.index(p_i, 6, parent_index)
                #부모가 알엠빅일 경우 한 번 더 row 넘기기
                if parent_item.name == "ALEMBIC":
                    child_index = self.import_proxy_model.index(p_i, 0, parent_index)
                    child_item = child_index.data(QtCore.Qt.UserRole)
                    for p_j in range(self.import_proxy_model.rowCount(child_index)):
                        combo_j_index = self.import_proxy_model.index(p_j, 5, child_index)
                        button_j_index = self.import_proxy_model.index(p_j, 6, child_index)
                        self.ui.publist.openPersistentEditor(combo_j_index)
                        self.ui.publist.openPersistentEditor(button_j_index)



                else:
                    self.ui.publist.openPersistentEditor(combo_index)
                    self.ui.publist.openPersistentEditor(button_index)


        self.ui.publist.expandAll()
        for i in range(self.ui.publist.header().count()):
            self.ui.publist.resizeColumnToContents(i)

    @QtCore.Slot(int, object)
    def change_import_item_version(self, version, index):
        self.import_proxy_model.setData(index, version, QtCore.Qt.UserRole + 1)

    @QtCore.Slot(object)
    def import_into_current_scene(self, index):
        row_data = self.import_proxy_model.data(index, role=QtCore.Qt.UserRole)

        maya_handler.import_pub_item(row_data=row_data, context=self.context)
        self.set_model()


    # @QtCore.Slot(QtCore.QModelIndex)
    # def on_item_clicked(self, index):
    #     # 아이템 클릭 이벤트를 처리합니다.
    #     if index.column() == 6:  # 6은 가져오기 버튼이 있는 열을 가정합니다.
    #         self.import_into_current_scene(index)

    def get_selected_indexes_from_import_view(self):

        sel_indexes = self.ui.publist.selectedIndexes()
        filtered_indexes = list()

        for sel_idx in sel_indexes:
            column = sel_idx.column()
            data = self.import_proxy_model.data(sel_idx, QtCore.Qt.UserRole)

            if column == 0 and data.row_data is not None:
                filtered_indexes.append(data)

        return filtered_indexes

    def import_selected_items(self):

        sel_items = self.get_selected_indexes_from_import_view()

        for item in sel_items:
            maya_handler.import_pub_item(row_data=item, context=self.context)

        self.set_model()

    def open_sel_item_dir(self):

        sel_items = self.get_selected_indexes_from_import_view()

        dir, file_name = os.path.split(sel_items[0].file_path)

        os.startfile(dir)

    def dev_print(self):
        sel_items = self.get_selected_indexes_from_import_view()

        for item in sel_items:
            pprint(item.row_data)

    ## imported view actions ##

    def set_imported_model(self):

        imported_pub_items = maya_handler.get_imported_item_model()
        pub_items = shotgrid_handler.get_pub_datas(sg=self.sg, context=self.context)

        row_datas = dict()

        for imp_pub_item in imported_pub_items:
            for pub_name, pub_item in pub_items.items():

                versions = pub_item['items']

                for version in versions:
                    if imp_pub_item['id'] == version['id']:
                        current_version = version

                        data_dict = dict()
                        data_dict[imp_pub_item['name']] = {
                            'current_version': current_version,
                            'all_versions': versions,
                            'type': pub_item['type']
                        }
                        asset_name = imp_pub_item['entity']

                        if asset_name not in row_datas:
                            row_datas[asset_name] = {'geometry': [data_dict], 'shader': []}
                        else:
                            row_datas[asset_name]['geometry'].append(data_dict)

        for asset_name in row_datas:
            shaders = shotgrid_handler.get_published_shd_file(sg=self.sg,
                                                              context=self.context,
                                                              asset_name=asset_name)
            row_datas[asset_name]['shader'].extend(shaders)


        self.imported_model = imported_model.PubItemTreeModel(row_datas=row_datas)
        self.imported_proxy_model.setSourceModel(self.imported_model)
        self.ui.importedlist.setModel(self.imported_proxy_model)

        for i in range(self.imported_proxy_model.rowCount()):
            asset_index = self.imported_proxy_model.index(i, 0)
            for a_i in range(self.imported_proxy_model.rowCount(asset_index)):
                type_index = self.imported_proxy_model.index(a_i, 0, asset_index)

                for t_i in range(self.imported_proxy_model.rowCount(type_index)):
                    for t_c in range(self.imported_proxy_model.columnCount(type_index)):
                        item_index = self.imported_proxy_model.index(t_i, t_c, type_index)

                        self.ui.importedlist.openPersistentEditor(item_index)

        self.ui.importedlist.expandAll()
        for i in range(self.ui.importedlist.header().count()):
            self.ui.importedlist.resizeColumnToContents(i)


    @QtCore.Slot(str, object)
    def change_imported_item_version(self, version_str, row_index):
        self.imported_proxy_model.setData(row_index, version_str, QtCore.Qt.UserRole + 1)

    @QtCore.Slot(object)
    def replace_imported_item(self, index):
        row_data = self.imported_proxy_model.data(index, role=QtCore.Qt.UserRole)
        maya_handler.replace_alembic_reference(row_data=row_data)

        self.imported_proxy_model.setData(index, None, QtCore.Qt.UserRole + 2)

    @QtCore.Slot(object)
    def assign_shader(self, index):
        shader_row_data = self.imported_proxy_model.data(index, role=QtCore.Qt.UserRole)

        asset_name_index = index.parent().parent()
        asset_name = self.imported_proxy_model.data(asset_name_index, role=QtCore.Qt.UserRole).name
        target_meshes = list()

        for row in range(self.imported_proxy_model.rowCount(asset_name_index)):
            second_row_index = self.imported_proxy_model.index(row, 0, asset_name_index)

            for p_row in range(self.imported_proxy_model.rowCount(second_row_index)):
                third_row_index = self.imported_proxy_model.index(p_row, 0, second_row_index)
                third_row_data = self.imported_proxy_model.data(third_row_index, role=QtCore.Qt.UserRole)
                if third_row_data.data_type == "GEO":
                    target_meshes.append(third_row_data.name)

        # print(f"shader is {shader_row_data.name}")
        # print(f"asset name is {asset_name}")
        # print(target_meshes)

        shader_importer.import_shader(row_data=shader_row_data, target_geos=target_meshes)

    def get_selected_indexes_from_imported_view(self):

        sel_indexes = self.ui.importedlist.selectedIndexes()
        filtered_indexes = list()

        for sel_idx in sel_indexes:
            column = sel_idx.column()
            data = self.imported_proxy_model.data(sel_idx, QtCore.Qt.UserRole)

            if column == 0 and data.current_version is not None:
                filtered_indexes.append(data)

        return filtered_indexes
    def select_item(self):
        sel_data = self.get_selected_indexes_from_imported_view()

        for i in sel_data:
            if i.prefix != '__MAT':
                maya_handler.select_imported_item(i)

    def print_data(self):
        sel_data = self.get_selected_indexes_from_imported_view()

        for i in sel_data:
            pprint(i.current_version)




def main():

    app = QtWidgets.QApplication()
    excute_main =HoonieMain()
    excute_main.show()

    app.exec_()


def run_main_maya():
    from maya import OpenMayaUI as mui
    from shiboken2 import wrapInstance
    mayaMainWindowPtr = mui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QMainWindow) #int는 윈도우 os일때 붙인다.

    global app
    app = QtWidgets.QApplication.instance()
    excute_main = HoonieMain(mayaMainWindow)
    excute_main.show()
    app.exec_()



if __name__ == '__main__':
    run_main_maya()
    #main()

