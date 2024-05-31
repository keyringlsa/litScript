import os, sys
from imp import reload
from PySide2 import QtCore, QtGui, QtWidgets

from LIT_grp.unreal_LK.ui import unreal_LK_UI
from LIT_grp.unreal_LK.handler.render import render_set
from LIT_grp.unreal_LK.handler.list import Lkdlist, Datalist, export_import
from LIT_grp.unreal_LK.handler.unreal import shader_handler


from LIT_grp.unreal_LK.model import Lkd_model, file_model



reload(unreal_LK_UI)
reload(render_set)

reload(Lkdlist)
reload(Datalist)
reload(export_import)
reload(Lkd_model)
reload(file_model)
reload(shader_handler)



class Main(QtWidgets.QMainWindow):  # 이 예제에서는 QWidget을 쓰지만 QMainWindow도 가능

    def __init__(self, parent=None):  # parent는 반드시 None
        super(Main, self).__init__(parent)
        # 혹은 QtWidgets.QWidget.__init__(parent)도 가능하다.

        self.ui = unreal_LK_UI.Ui_MainWindow()  # UI 클래스로 선언
        self.ui.setupUi(self)  # setup

        self.ui.LKD_type.currentIndexChanged.connect(self.on_lkd_type_changed)

        # self.ui.datalist.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        # self.ui.datalist.customContextMenuRequested.connect(self.context_menu)

        self.file_dir_model = None
        self.data_dir_model = None

        self.project_dir_model = None



        self.connected()



    def connected(self):



        # List
        self.ui.Refresh_btn.clicked.connect(self.refresh_data)
        self.set_model()
        self.ui.lkdlist.clicked.connect(self.file_model)
        self.ui.lkdlist.doubleClicked.connect(self.on_double_click)
        self.ui.Seach_input.textChanged.connect(self.filter_shotlist)

        self.ui.datalist.clicked.connect(self.on_table_clicked)



        # Export&Import
        self.ui.txt_imp.clicked.connect(self.unreal_txt_import)
        #self.ui.import_All.clicked.connect(self.lkd_import)










    ############################################### list tab

    def on_lkd_type_changed(self):
        # LKD_type 값이 변경될 때마다 모델 업데이트
        self.set_model()


    def set_model(self):

        lkd_type = self.ui.LKD_type.currentText()
        row_datas = Lkdlist.make_file_structure(lkd_type)

        self.file_dir_model = Lkd_model.lkdModel(row_datas=row_datas)

        self.ui.lkdlist.setModel(self.file_dir_model)


        self.ui.lkdlist.clicked.connect(self.file_model)
        self.ui.lkdlist.doubleClicked.connect(self.on_double_click)
        self.ui.datalist.clicked.connect(self.on_table_clicked)




    def on_double_click(self):
        lkd_type = self.ui.LKD_type.currentText()
        sel = self.ui.lkdlist.currentIndex()
        item = self.file_dir_model.data(sel, role=QtCore.Qt.UserRole)

        Datalist.on_double_click(item.name, lkd_type)

    def filter_shotlist(self):

        search_text = self.ui.Seach_input.text().lower()  # 입력된 검색어 가져오기
        filtered_indices = []

        for index, item in enumerate(self.file_dir_model.entri_data):
            if search_text in item.name.lower():
                filtered_indices.append(index)

        # 검색 결과에 해당하는 항목들만 보여주도록 Shotlist 모델에 적용
        self.file_dir_model.filtered_indices = filtered_indices
        self.ui.lkdlist.setModel(self.file_dir_model)



    def file_model(self):
        sel = self.ui.lkdlist.currentIndex()

        item = self.file_dir_model.data(sel, role=QtCore.Qt.UserRole)
        name = item.name
        lkd_type = self.ui.LKD_type.currentText()


        row_datas_file = Datalist.datalist(name, lkd_type)
        self.data_dir_model = file_model.fileModel(row_data=row_datas_file)

        self.ui.datalist.setModel(self.data_dir_model)
        self.ui.datalist.setColumnWidth(0, 200)

    def on_table_clicked(self):
        sel = self.ui.datalist.currentIndex()
        item = self.data_dir_model.data(sel, role=QtCore.Qt.UserRole)
        if item:
            file_path = item.path
            print(file_path)


    def refresh_data(self):
        # 데이터 모델을 다시 설정하여 새로고침
        self.file_model()


    ############################################### list tab



    def unreal_txt_import(self):
        lkd_type = self.ui.LKD_type.currentText()
        sel_shot = self.ui.lkdlist.currentIndex()
        item_shot = self.file_dir_model.data(sel_shot, role=QtCore.Qt.UserRole)
        sel = item_shot.name
        sel_data = self.ui.datalist.currentIndex()
        item = self.data_dir_model.data(sel_data, role=QtCore.Qt.UserRole)

        if item:
            file_path = item.path
            shader_handler.unreal_txt_import(sel, file_path, lkd_type)

























    ############################################### Project tab





    def refresh_project(self):
        self.project_model()




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





def main():
    """
    Create tool window.
    """
    app = QtWidgets.QApplication.instance()  # Check if QApplication instance exists
    if not app:
        app = QtWidgets.QApplication(sys.argv)

    # Id any current instances of tool and destroy
    for win in QtWidgets.QApplication.allWindows():
        if 'toolWindow' in win.objectName():
            win.destroy()

    # load UI into QApp instance
    Main.window = Main()
    Main.window.setObjectName('toolWindow')  # Unique object name
    Main.window.setWindowTitle('Sample Tool')
    Main.window.show()




# def main():
#
#     """
#         Create tool window.
#         """
#     #언리얼 실행 시
#     if QtWidgets.QApplication.instance():
#         # Id any current instances of tool and destroy
#         for win in (QtWidgets.QApplication.allWindows()):
#             if 'toolWindow' in win.objectName():  # update this name to match name below
#                 win.destroy()
#     else:
#         QtWidgets.QApplication(sys.argv)
#
#     # load UI into QApp instance
#     Main.window = Main()
#     Main.window.show()
#     Main.window.setObjectName('toolWindow')  # update this with something unique to your tool
#     Main.setWindowTitle('Sample Tool')
#     Main.parent_external_window_to_slate(Main.window.winId())



if __name__ == '__main__':
    main()
    #run_main_maya()









"""

import sys
from pprint import pprint

path = "D:\lt_team\maya_scripts"
sys.path.insert(0, path)

from imp import reload 


import LIT_grp.unreal_LK.unreal_LK

reload(LIT_grp.unreal_LK.unreal_LK) 
print(LIT_grp.unreal_LK.unreal_LK.__file__)
LIT_grp.unreal_LK.unreal_LK.main()

"""

