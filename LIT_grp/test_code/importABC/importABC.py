

import os, sys
#import sgtk
from pprint import pprint
from importlib import reload
from PySide2 import QtWidgets, QtGui, QtCore


from CoreModules.handler import connect_sg
from LIT_grp.test_code.importABC.UI import ui_hoonie2
from LIT_grp.test_code.importABC.model import pub_model
from LIT_grp.test_code.importABC.handler import shotgrid_handler

reload(connect_sg)
reload(ui_hoonie2)
reload(pub_model)
reload(shotgrid_handler)

# data = [
#     {"name": "A", "child": [
#         {"name": "a", "child": []}
#     ]},
#     {"name": "B", "child": [
#         {"name": "b", "child": []}
#     ]},
# ]

class HoonieMain(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowFlag(QtCore.Qt.WindowType(True))
        self.ui = ui_hoonie2.Ui_Form()
        self.ui.setupUi(self)


        # get shotgun api
        sgl = connect_sg.Shotgun_Connect()
        self.sg = sgl.default_script_auth()

        # get current context
        #current_engine = sgtk.platform.current_engine()
        #self.context = current_engine.context


        self.items = None

        self.model_init()

    def model_init(self):
        cate_items = shotgrid_handler.get_category()
        pub_items = shotgrid_handler.get_pub_datas()
        self.items = pub_model.ItemTreeModel(row_datas=pub_items, head_items=cate_items)
        self.ui.publist.setModel(self.items)



    #def shotgun_data(self):
        #pub_items = shotgrid_handler.get_pub_datas()
        #pub_items = shotgrid_handler.get_pub_datas(sg=self.sg, context=self.context)


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
    main()

