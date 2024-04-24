import os, sys
import maya.cmds as cmds
from imp import reload
from PySide2 import QtCore, QtGui, QtWidgets

from LIT_grp.test_code.psoft_import.handler import psoft_handler
from LIT_grp.test_code.psoft_import.model import psoft_model
from LIT_grp.test_code.psoft_import.UI import ui_psoft


reload(psoft_handler)
reload(psoft_model)
reload(ui_psoft)




class Main(QtWidgets.QWidget):  # 이 예제에서는 QWidget을 쓰지만 QMainWindow도 가능

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setWindowFlag(QtCore.Qt.WindowType(True))

        self.ui = ui_psoft.Ui_Form()  # UI 클래스로 선언
        self.ui.setupUi(self)  # setup


        self.psoft_dir_model = None



        self.connected()




    def connected(self):





        # Project
        self.project_model()
        self.ui.imp_btn.clicked.connect(self.import_psoft)
        self.ui.set_btn.clicked.connect(self.set_psoft)
        self.ui.ref_btn.clicked.connect(self.refresh)
        #self.ui.open_btn.clicked.connect(self.open_dir)











    ############################################### Project tab


    def project_model(self):
        pro_type = self.ui.type.currentText()
        row_datas = psoft_handler.project_data(pro_type)

        self.psoft_dir_model = psoft_model.projectModel(row_datas=row_datas)

        self.ui.psoft_list.setModel(self.psoft_dir_model)

    def refresh(self):
        self.project_model()


    def import_psoft(self):
        psoft_handler.psoft_imp()


    def set_psoft(self):
        pro_type = self.ui.type.currentText()
        sel_project = self.ui.psoft_list.currentIndex()
        item_project = self.psoft_dir_model.data(sel_project, role=QtCore.Qt.UserRole)
        sel = item_project.name
        psoft_handler.psoft_set(sel,pro_type)



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

import LIT_grp.test_code.psoft_import.psoft_tool

reload(LIT_grp.test_code.psoft_import.psoft_tool) 
print(LIT_grp.test_code.psoft_import.psoft_tool.__file__)
LIT_grp.test_code.psoft_import.psoft_tool.run_main_maya()

"""