import os, sys
from pprint import pprint
from importlib import reload
from PySide2 import QtWidgets, QtGui, QtCore

from CoreModules.handler import connect_sg
from LIT_grp.test_code.importABC.UI import ui_hoonie2
from LIT_grp.test_code.importABC.model import pub_model
from LIT_grp.test_code.importABC.handler import shotgrid_handler

# 모듈 리로드
reload(connect_sg)
reload(ui_hoonie2)
reload(pub_model)
reload(shotgrid_handler)

class HoonieMain(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(QtCore.Qt.WindowType(True))
        self.ui = ui_hoonie2.Ui_Form()
        self.ui.setupUi(self)

        # Shotgun 연결
        sgl = connect_sg.Shotgun_Connect()
        self.sg = sgl.default_script_auth()

        # 모델 및 델리게이트 설정
        self.items = None
        self.ImportButtonDelegate = pub_model.ImportButtonDelegate()
        self.ui.publist.setItemDelegate(self.ImportButtonDelegate)

        self.set_model()

    def set_model(self):
        cate_items = shotgrid_handler.get_category()
        pub_items = shotgrid_handler.get_pub_datas()
        self.items = pub_model.ItemTreeModel(row_datas=pub_items, head_items=cate_items)
        self.import_proxy_model = QtCore.QSortFilterProxyModel(self)
        self.import_proxy_model.setSourceModel(self.items)
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
    #run_main_maya()
    main()

