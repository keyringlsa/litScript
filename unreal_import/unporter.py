import os, sys
from imp import reload
from PySide2 import QtCore, QtGui, QtWidgets

from unreal_import.UI import unreal_asset_UI

from unreal_import.handler import shotgrid_handler
from unreal_import.model import astype_model




reload(unreal_asset_UI)
reload(astype_model)
reload(shotgrid_handler)


class Worker(QtCore.QObject):
    finished = QtCore.Signal()

    def run(self, function, *args):
        function(*args)
        self.finished.emit()


class Main(QtWidgets.QMainWindow):  # 이 예제에서는 QWidget을 쓰지만 QMainWindow도 가능

    def __init__(self, parent=None):  # parent는 반드시 None
        super(Main, self).__init__(parent)
        # 혹은 QtWidgets.QWidget.__init__(parent)도 가능하다.

        self.ui = unreal_asset_UI.Ui_MainWindow()  # UI 클래스로 선언
        self.ui.setupUi(self)  # setup


        self.file_dir_model = None
        self.data_dir_model = None

        self.project_dir_model = None



        self.connected()



    def connected(self):



        # List
        self.ui.Refresh_btn.clicked.connect(self.refresh_data)
        self.set_model()











    ############################################### list tab

    def on_lkd_type_changed(self):
        # LKD_type 값이 변경될 때마다 모델 업데이트
        self.set_model()


    def set_model(self):
        row_datas = shotgrid_handler.get_category()

        self.project_dir_model = astype_model.type_Model(row_datas=row_datas)

        self.ui.asset_type.setModel(self.project_dir_model)

        #self.ui.asset_type.clicked.connect(self.file_model)
        #self.ui.Project_list.doubleClicked.connect(self.on_double_click)






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





# def main():
#     """
#     Create tool window.
#     """
#     app = QtWidgets.QApplication.instance()  # Check if QApplication instance exists
#     if not app:
#         app = QtWidgets.QApplication(sys.argv)
#
#     # Id any current instances of tool and destroy
#     for win in QtWidgets.QApplication.allWindows():
#         if 'toolWindow' in win.objectName():
#             win.destroy()
#
#     # load UI into QApp instance
#     Main.window = Main()
#     Main.window.setObjectName('toolWindow')  # Unique object name
#     Main.window.setWindowTitle('Sample Tool')
#     Main.window.show()
#     sys.exit(app.exec_())


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


import unreal_import.unporter

reload(unreal_import.unporter) 
print(unreal_import.unporter.__file__)
unreal_import.unporter.main()

"""

