import os, sys
from importlib import reload
from PySide2 import QtCore, QtGui, QtWidgets

from LIT_grp.LK_sha.sha_ui import sha_ui
from LIT_grp.LK_sha.sha_handler import mesh_handler
from LIT_grp.LK_sha.sha_model import sha_model



reload(sha_ui)
reload(mesh_handler)
reload(sha_model)

class Main(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setWindowFlag(QtCore.Qt.WindowType(True))

        self.ui = sha_ui.Ui_Form()
        self.ui.setupUi(self)  # setup

        self.file_dir_model_A = None
        self.file_dir_model_B = None

        self.ui.B_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.B_list.customContextMenuRequested.connect(self.context_menu)
        self.connected()

    def connected(self):
        self.ui.Refresh_btn.clicked.connect(self.dev)
        self.set_model_A()
        self.set_model_B()




###########################################
    def dev(self):
        self.set_model_A()
        self.set_model_B()


    def set_model_A(self):
        row_datas = mesh_handler.ch_data()
        data_A = row_datas[0] if len(row_datas) > 1 else []  # 값이 없을 경우 빈 리스트 처리
        self.file_dir_model_A = sha_model.ItemTreeModel(row_datas=data_A)
        self.ui.A_list.setModel(self.file_dir_model_A)
        self.ui.A_list.expandAll() #항목 펼쳐주는 코드


    def set_model_B(self):
        row_datas = mesh_handler.ch_data()
        data_B = row_datas[1] if len(row_datas) > 1 else []
        self.file_dir_model_B = sha_model.ItemTreeModel(row_datas=data_B)
        self.ui.B_list.setModel(self.file_dir_model_B)
        self.ui.B_list.expandAll()

    @QtCore.Slot(QtCore.QPoint)
    def context_menu(self, pos):
        viewport = self.ui.B_list.viewport()
        menu = QtWidgets.QMenu(viewport)
        menuItem_01 = menu.addAction('Shader Assign')
        menuItem_01.triggered[()].connect(self.sha_As)


        menu.exec_(viewport.mapToGlobal(pos))

    def sha_As(self):
        # A_list에서 shader 가져오기
        sel_sha_indexes = self.ui.A_list.selectedIndexes() #혹시라도 여러개 선택할수도 있으니까
        if not sel_sha_indexes:
            return

        sel_sha_index = sel_sha_indexes[0]  #선택된 인덱스 중 첫번째
        item_sha = sel_sha_index.data(role=QtCore.Qt.UserRole)  #데이터 처리
        sha_name = item_sha.shader[0]  # shader의 이름

        # B_list에서 name 가져오기
        sel_mesh_indexes = self.ui.B_list.selectedIndexes() #혹시라도 여러개 선택할수도 있으니까
        if not sel_mesh_indexes:
            return  # 선택된 항목이 없으면 함수 종료

        for sel_mesh_index in sel_mesh_indexes:
            #sel_mesh_index = sel_mesh_indexes[0] 다중 선택 말고 하나만 처리할 때 이거로 수정
            item_mesh = sel_mesh_index.data(role=QtCore.Qt.UserRole)  # 데이터 처리
            mesh_name = item_mesh.name  # mesh 이름

            # 가져온 shader와 mesh 정보를 이용하여 처리
            mesh_handler.sha_AS(sha_name, mesh_name)



def run():
    app = QtWidgets.QApplication()

    execute_main = Main()
    execute_main.show()
    app.exec_()

def run_main_maya():
    from maya import OpenMayaUI as mui
    from shiboken2 import wrapInstance
    mayaMainWindowPtr = mui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QMainWindow) #int는 윈도우 os일때 붙인다.

    global app
    app = QtWidgets.QApplication.instance()
    excute_main = Main(mayaMainWindow)
    excute_main.show()
    app.exec_()



if __name__ == '__main__':
    run_main_maya()


"""


from imp import reload 

import LIT_grp.LK_sha.sha_tool

reload(LIT_grp.LK_sha.sha_tool) 
print(LIT_grp.LK_sha.sha_tool.__file__)
LIT_grp.LK_sha.sha_tool.run_main_maya()

"""

