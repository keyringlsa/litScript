import os, sys
import maya.cmds as cmds
from imp import reload
from PySide2 import QtCore, QtGui, QtWidgets

from LIT_grp.LK_script.ui import LK_UI
from LIT_grp.LK_script.handler.render import render_set
from LIT_grp.LK_script.handler.list import Lkdlist
from LIT_grp.LK_script.handler.list import Datalist
from LIT_grp.LK_script.handler.list import export_import
from LIT_grp.LK_script.handler.project import project_set
from LIT_grp.LK_script.handler.project import project_list
from LIT_grp.LK_script.handler.attr import attr_set
from LIT_grp.LK_script.model import Lkd_model
from LIT_grp.LK_script.model import file_model
from LIT_grp.LK_script.model import project_model



reload(LK_UI)
reload(render_set)
reload(project_set)
reload(project_list)
reload(attr_set)
reload(Lkdlist)
reload(Datalist)
reload(export_import)
reload(Lkd_model)
reload(file_model)
reload(project_model)


class Main(QtWidgets.QMainWindow):  # 이 예제에서는 QWidget을 쓰지만 QMainWindow도 가능

    def __init__(self, parent=None):  # parent는 반드시 None
        super(Main, self).__init__(parent)
        # 혹은 QtWidgets.QWidget.__init__(parent)도 가능하다.

        self.ui = LK_UI.Ui_MainWindow()  # UI 클래스로 선언
        self.ui.setupUi(self)  # setup

        self.ui.LKD_type.currentIndexChanged.connect(self.on_lkd_type_changed)

        self.ui.datalist.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.datalist.customContextMenuRequested.connect(self.context_menu)

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
        self.ui.export_All.clicked.connect(self.lkd_export)
        self.ui.import_All.clicked.connect(self.lkd_import)





        # Render
        self.ui.render_set_SA.clicked.connect(self.output_sa)
        self.ui.render_set_JH.clicked.connect(self.output_jh)
        self.ui.render_set_Deep.clicked.connect(self.output_deep)
        self.ui.render_set_W.clicked.connect(self.output_w)
        self.ui.sampling_low.clicked.connect(self.sam_low)
        self.ui.sampling_Mid.clicked.connect(self.sam_middle)
        self.ui.sampling_High.clicked.connect(self.sam_high)
        self.ui.sampling_Vol.clicked.connect(self.sam_vol)
        self.ui.sampling_Fil.clicked.connect(self.filckr)




        # Attr
        self.ui.AT_add_btn.clicked.connect(self.custom_at_set)
        self.ui.Exp_OK_btn.clicked.connect(self.exp_set)







        # Project
        self.project_model()
        self.ui.Project_export_btn.clicked.connect(self.project_export)
        self.ui.Project_import_btn.clicked.connect(self.project_import)
        self.ui.Project_refresh.clicked.connect(self.refresh_project)










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
            file_name = item.name+"_v"+item.version
            print(file_name)


    def refresh_data(self):
        # 데이터 모델을 다시 설정하여 새로고침
        self.file_model()


    ############################################### list tab

    def lkd_export(self):
        export_import.lkd_export()



    def lkd_import(self):
        lkd_type = self.ui.LKD_type.currentText()
        sel_shot = self.ui.lkdlist.currentIndex()
        item_shot = self.file_dir_model.data(sel_shot, role=QtCore.Qt.UserRole)
        sel = item_shot.name
        sel_data = self.ui.datalist.currentIndex()
        item = self.data_dir_model.data(sel_data, role=QtCore.Qt.UserRole)

        if item:
            file_name = item.name+"_v"+item.version
            export_import.lkd_import(sel, file_name, lkd_type)



    @QtCore.Slot(QtCore.QPoint)
    def context_menu(self, pos):
        viewport = self.ui.datalist.viewport()
        menu = QtWidgets.QMenu(viewport)
        menuItem_01 = menu.addAction('Import Lit')
        menuItem_01.triggered[()].connect(self.lit_each_import)
        menuItem_02 = menu.addAction('Import Layer')
        menuItem_02.triggered[()].connect(self.layer_each_import)
        menuItem_03 = menu.addAction('Import Aov')
        menuItem_03.triggered[()].connect(self.aov_each_import)
        menuItem_04 = menu.addAction('Import Rivet')
        menuItem_04.triggered[()].connect(self.rivet_imp)
        menuItem_05 = menu.addAction('Import Set')
        menuItem_05.triggered[()].connect(self.set_imp)

        menu.exec_(viewport.mapToGlobal(pos))

    def lit_each_import(self):
        lkd_type = self.ui.LKD_type.currentText()
        sel_shot = self.ui.lkdlist.currentIndex()
        item_shot = self.file_dir_model.data(sel_shot, role=QtCore.Qt.UserRole)
        sel = item_shot.name
        sel_data = self.ui.datalist.currentIndex()
        item = self.data_dir_model.data(sel_data, role=QtCore.Qt.UserRole)

        if item:
            file_name = item.name + "_v" + item.version
            export_import.lit_each_import(sel, file_name, lkd_type)


    def layer_each_import(self):
        lkd_type = self.ui.LKD_type.currentText()
        sel_shot = self.ui.lkdlist.currentIndex()
        item_shot = self.file_dir_model.data(sel_shot, role=QtCore.Qt.UserRole)
        sel = item_shot.name
        sel_data = self.ui.datalist.currentIndex()
        item = self.data_dir_model.data(sel_data, role=QtCore.Qt.UserRole)

        if item:
            file_name = item.name + "_v" + item.version
            export_import.layer_each_import(sel, file_name, lkd_type)

    def aov_each_import(self):
        lkd_type = self.ui.LKD_type.currentText()
        sel_shot = self.ui.lkdlist.currentIndex()
        item_shot = self.file_dir_model.data(sel_shot, role=QtCore.Qt.UserRole)
        sel = item_shot.name
        sel_data = self.ui.datalist.currentIndex()
        item = self.data_dir_model.data(sel_data, role=QtCore.Qt.UserRole)

        if item:
            file_name = item.name + "_v" + item.version
            export_import.aov_each_import(sel, file_name, lkd_type)

    def rivet_imp(self):
        lkd_type = self.ui.LKD_type.currentText()
        sel_shot = self.ui.lkdlist.currentIndex()
        item_shot = self.file_dir_model.data(sel_shot, role=QtCore.Qt.UserRole)
        sel = item_shot.name
        sel_data = self.ui.datalist.currentIndex()
        item = self.data_dir_model.data(sel_data, role=QtCore.Qt.UserRole)

        if item:
            file_name = item.name + "_v" + item.version
            export_import.rivet_imp(sel, file_name, lkd_type)



    def set_imp(self):
        lkd_type = self.ui.LKD_type.currentText()
        sel_shot = self.ui.lkdlist.currentIndex()
        item_shot = self.file_dir_model.data(sel_shot, role=QtCore.Qt.UserRole)
        sel = item_shot.name
        sel_data = self.ui.datalist.currentIndex()
        item = self.data_dir_model.data(sel_data, role=QtCore.Qt.UserRole)

        if item:
            file_name = item.name + "_v" + item.version
            export_import.set_imp(sel, file_name, lkd_type)









    ############################################### Render tab

    def output_sa(self, *args):
        render_set.output_sa()


    def output_jh(self, *args):
        render_set.output_jh()


    def output_deep(self, *args):
        render_set.output_deep()


    def output_w(self, *args):
        render_set.output_w()

    def sam_low(self, *args):
        render_set.sam_low()


    def sam_middle(self, *args):
        render_set.sam_middle()


    def sam_high(self, *args):
        render_set.sam_high()


    def sam_vol(self, *args):
        render_set.sam_vol()


    def filckr(self, *args):
        render_set.filckr()






    ############################################### Attr tab


    def custom_at_set(self):
        at_name = self.ui.AT_name.text()
        at_type = None
        if self.ui.at_type_float.isChecked():
            at_type = "float"
        elif self.ui.at_type_float.isChecked():
            at_type = "string"

        attr_set.custom_at_set(at_name,  at_type)

    def exp_set(self):
        ex_input = {"ex_inputA": self.ui.Expression_inputA.text(),
                    "ex_inputB": self.ui.Expression_inputB.text(),
                    "ex_inputC": self.ui.Expression_inputC.text(),
                    "ex_inputD": self.ui.Expression_inputD.text(),
                    "ex_inputE": self.ui.Expression_inputE.text(),
                    "ex_inputF": self.ui.Expression_inputF.text()}
        attr_set.exp_set(ex_input)












    ############################################### Project tab


    def project_model(self):

        row_datas = project_list.project_data()

        self.project_dir_model = project_model.projectModel(row_datas=row_datas)

        self.ui.Project_list.setModel(self.project_dir_model)


        self.ui.Project_list.clicked.connect(self.file_model)
        self.ui.Project_list.doubleClicked.connect(self.on_double_click)

    def refresh_project(self):
        self.project_model()


    def project_export(self):
        project_name = self.ui.Project_input.text()
        project_list.project_export(project_name)


    def project_import(self):
        sel_project = self.ui.Project_list.currentIndex()
        item_project = self.project_dir_model.data(sel_project, role=QtCore.Qt.UserRole)
        sel = item_project.name
        project_list.project_import(sel)



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

import LIT_grp.LK_script.LK_tool

reload(LIT_grp.LK_script.LK_tool) 
print(LIT_grp.LK_script.LK_tool.__file__)
LIT_grp.LK_script.LK_tool.run_main_maya()

"""
