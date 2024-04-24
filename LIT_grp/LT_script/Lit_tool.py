import os, sys
import maya.cmds as cmds
from imp import reload
from PySide2 import QtCore, QtGui, QtWidgets

from LIT_grp.LT_script.ui import Lit_UI
from LIT_grp.LT_script.handler.layer import layer_set
from LIT_grp.LT_script.handler.lit import lit_set
from LIT_grp.LT_script.handler.aov import aov_set
from LIT_grp.LT_script.handler.aov import aov_make
from LIT_grp.LT_script.handler.render import render_set
from LIT_grp.LT_script.handler.list import Litlist
from LIT_grp.LT_script.handler.list import Datalist
from LIT_grp.LT_script.handler.list import export_import
from LIT_grp.LT_script.handler.project import project_set
from LIT_grp.LT_script.handler.project import project_list
from LIT_grp.LT_script.model import Lit_model
from LIT_grp.LT_script.model import file_model
from LIT_grp.LT_script.model import project_model


reload(Lit_UI)
reload(layer_set)
reload(lit_set)
reload(aov_set)
reload(aov_make)
reload(render_set)
reload(project_set)
reload(project_list)
reload(Litlist)
reload(Datalist)
reload(export_import)
reload(Lit_model)
reload(file_model)
reload(project_model)




class Main(QtWidgets.QMainWindow):  # 이 예제에서는 QWidget을 쓰지만 QMainWindow도 가능

    def __init__(self, parent=None):  # parent는 반드시 None
        super(Main, self).__init__(parent)
        # 혹은 QtWidgets.QWidget.__init__(parent)도 가능하다.

        self.ui = Lit_UI.Ui_MainWindow()  # UI 클래스로 선언
        self.ui.setupUi(self)  # setup


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
        self.ui.Shotlist.clicked.connect(self.file_model)
        self.ui.Shotlist.doubleClicked.connect(self.on_double_click)
        self.ui.Seach_input.textChanged.connect(self.filter_shotlist)

        self.ui.datalist.clicked.connect(self.on_table_clicked)



        # Export&Import
        self.ui.export_All.clicked.connect(self.lit_export)
        self.ui.import_All.clicked.connect(self.lit_import)





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





        # Light
        self.ui.Basic_lit.clicked.connect(self.lit_base)
        self.ui.CH_lit.clicked.connect(self.lit_ch)
        self.ui.Rivet.clicked.connect(self.rivet)
        self.ui.Lit_btn.clicked.connect(self.lit_make)
        self.ui.Normal_btn.clicked.connect(self.lit_normal)
        self.ui.Lit_AT_btn.clicked.connect(self.LIT_AT)
        self.ui.LG_btn.clicked.connect(self.lit_grp)






        # Layer
        self.ui.Basic_set.clicked.connect(self.basic_set)
        self.ui.Basic_layer.clicked.connect(self.layer_base)
        self.ui.Utill_layer.clicked.connect(self.layer_utill)
        self.ui.CH_layer.clicked.connect(self.layer_ch)
        self.ui.BG_layer.clicked.connect(self.layer_bg)
        self.ui.SH_layer.clicked.connect(self.layer_sh)





        # Aov
        self.ui.AOV_btn.clicked.connect(self.AOV_ONOFF)
        self.ui.Basic_aov.clicked.connect(self.aov)
        self.ui.occ_aov.clicked.connect(self.aov_ao)
        self.ui.crypto_aov.clicked.connect(self.aov_crypto)
        self.ui.lit_aov.clicked.connect(self.aov_lit)
        self.ui.SamplerInfo.clicked.connect(self.samplerinfo)
        self.ui.ToonUtill.clicked.connect(self.aov_toonUtill)
        self.ui.Toon_aov.clicked.connect(self.aov_toonaov)
        self.ui.OFF_Aovset.clicked.connect(self.OFF_Aovset)






        # Project
        self.project_model()
        self.ui.Project_export_btn.clicked.connect(self.project_export)
        self.ui.Project_import_btn.clicked.connect(self.project_import)
        self.ui.Project_refresh.clicked.connect(self.refresh_project)
        self.ui.FX_set.clicked.connect(self.fx_set)
        self.ui.FX_layer.clicked.connect(self.layer_fx)
        self.ui.FX_lit.clicked.connect(self.fx_lit)
        self.ui.beam_lit.clicked.connect(self.beam_lit)
        self.ui.beam_set.clicked.connect(self.beam_set)
        self.ui.fog_btn.clicked.connect(self.fog_set)







    ############################################### list tab

    def set_model(self):
        row_datas = Litlist.make_file_structure()
        self.file_dir_model = Lit_model.litModel(row_datas=row_datas)

        self.ui.Shotlist.setModel(self.file_dir_model)


        self.ui.Shotlist.clicked.connect(self.file_model)
        self.ui.Shotlist.doubleClicked.connect(self.on_double_click)
        self.ui.datalist.clicked.connect(self.on_table_clicked)




    def on_double_click(self):
        sel = self.ui.Shotlist.currentIndex()
        item = self.file_dir_model.data(sel, role=QtCore.Qt.UserRole)

        Datalist.on_double_click(item.name)

    def filter_shotlist(self):

        search_text = self.ui.Seach_input.text().lower()  # 입력된 검색어 가져오기
        filtered_indices = []

        for index, item in enumerate(self.file_dir_model.entri_data):
            if search_text in item.name.lower():
                filtered_indices.append(index)

        # 검색 결과에 해당하는 항목들만 보여주도록 Shotlist 모델에 적용
        self.file_dir_model.filtered_indices = filtered_indices
        self.ui.Shotlist.setModel(self.file_dir_model)



    def file_model(self):
        sel = self.ui.Shotlist.currentIndex()

        item = self.file_dir_model.data(sel, role=QtCore.Qt.UserRole)
        name = item.name



        row_datas_file = Datalist.datalist(name)
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

    def lit_export(self):
        export_import.lit_export()



    def lit_import(self):
        sel_shot = self.ui.Shotlist.currentIndex()
        item_shot = self.file_dir_model.data(sel_shot, role=QtCore.Qt.UserRole)
        sel = item_shot.name
        sel_data = self.ui.datalist.currentIndex()
        item = self.data_dir_model.data(sel_data, role=QtCore.Qt.UserRole)

        if item:
            file_name = item.name+"_v"+item.version
            export_import.lit_import(sel, file_name)



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
        sel_shot = self.ui.Shotlist.currentIndex()
        item_shot = self.file_dir_model.data(sel_shot, role=QtCore.Qt.UserRole)
        sel = item_shot.name
        sel_data = self.ui.datalist.currentIndex()
        item = self.data_dir_model.data(sel_data, role=QtCore.Qt.UserRole)

        if item:
            file_name = item.name + "_v" + item.version
            export_import.lit_each_import(sel, file_name)


    def layer_each_import(self):
        sel_shot = self.ui.Shotlist.currentIndex()
        item_shot = self.file_dir_model.data(sel_shot, role=QtCore.Qt.UserRole)
        sel = item_shot.name
        sel_data = self.ui.datalist.currentIndex()
        item = self.data_dir_model.data(sel_data, role=QtCore.Qt.UserRole)

        if item:
            file_name = item.name + "_v" + item.version
            export_import.layer_each_import(sel, file_name)

    def aov_each_import(self):
        sel_shot = self.ui.Shotlist.currentIndex()
        item_shot = self.file_dir_model.data(sel_shot, role=QtCore.Qt.UserRole)
        sel = item_shot.name
        sel_data = self.ui.datalist.currentIndex()
        item = self.data_dir_model.data(sel_data, role=QtCore.Qt.UserRole)

        if item:
            file_name = item.name + "_v" + item.version
            export_import.aov_each_import(sel, file_name)

    def rivet_imp(self):
        sel_shot = self.ui.Shotlist.currentIndex()
        item_shot = self.file_dir_model.data(sel_shot, role=QtCore.Qt.UserRole)
        sel = item_shot.name
        sel_data = self.ui.datalist.currentIndex()
        item = self.data_dir_model.data(sel_data, role=QtCore.Qt.UserRole)

        if item:
            file_name = item.name + "_v" + item.version
            export_import.rivet_imp(sel, file_name)



    def set_imp(self):
        sel_shot = self.ui.Shotlist.currentIndex()
        item_shot = self.file_dir_model.data(sel_shot, role=QtCore.Qt.UserRole)
        sel = item_shot.name
        sel_data = self.ui.datalist.currentIndex()
        item = self.data_dir_model.data(sel_data, role=QtCore.Qt.UserRole)

        if item:
            file_name = item.name + "_v" + item.version
            export_import.set_imp(sel, file_name)



    ############################################### light tab


    def lit_base(self, *args):
        lit_set.lit_base()

    def lit_ch(self, *args):
        lit_set.lit_ch()


    def rivet(self, *args):
        lit_set.rivet()

    def lit_make(self, *args):

        lit_type = self.ui.Lit_type.currentText()
        lit_name = self.ui.Lit_name.text()

        lit_set.lit_make(lit_type, lit_name)



    def lit_normal(self, *args):
        Normal_ON = self.ui.Normal_ON.isChecked()

        lit_set.Lit_normal(Normal_ON)



    def LIT_AT(self, *args) :
        Lit_AT_type = self.ui.Lit_AT_type.currentText()
        Lit_AT_value = self.ui.Lit_AT_value.text()

        lit_set.LIT_AT(Lit_AT_type, Lit_AT_value)

    def lit_grp(self, *args):
        LG_type = self.ui.LG_type.currentText()

        lit_set.Lit_grp(LG_type)



    ############################################### layer tab

    def basic_set(self, *args):
        layer_set.basic_set()


    def layer_base(self, *args):
        layer_set.layer_ch()
        layer_set.layer_bg()
        layer_set.layer_sh()

    def layer_ch(self, *args):
        layer_set.layer_ch()

    def layer_bg(self, *args):
        layer_set.layer_bg()

    def layer_sh(self, *args):
        layer_set.layer_sh()

    def layer_utill(self, *args):
        layer_set.layer_utill()




    ############################################### AOV tab

    def AOV_ONOFF(self, *args):
        AOV_ON = self.ui.AOV_ON.isChecked()

        aov_set.AOV_ONOFF(AOV_ON)


    def aov(self, *args):
        aov_make.aov()


    def aov_ao(self, *args):
        aov_make.aov_ao()


    def aov_crypto(self, *args):
        aov_make.aov_crypto()


    def aov_lit(self, *args):
        aov_make.aov_lit()


    def samplerinfo(self, *args):
        aov_make.samplerinfo()


    def aov_toonUtill(self, *args):
        aov_make.aov_toonUtill()


    def aov_toonaov(self, *args):
        aov_make.aov_toonaov()


    def OFF_Aovset(self, *args):
        aov_set.OFF_Aovset()





    ############################################### Render tab


    # def set_shot_info(self, *args):
    #     item = shotgun_output.shot_info()
    #     if item.get('resolution') is not None :
    #         width = item.get('resolution').split('*')[0]
    #         height = item.get('resolution').split('*')[-1]
    #
    #         self.ui.RE_Width.setText(width)
    #         self.ui.RE_Hieght.setText(height)
    #
    #     if item.get('fps') is not None :
    #         fps = item.get('fps')
    #
    #         self.ui.FPS_int.setText(str(fps))
    #
    #     if item.get('cut_in') is not None :
    #         cut_in = item.get('cut_in')
    #
    #         self.ui.FR_start.setText(str(cut_in))
    #
    #     if item.get('cut_out') is not None :
    #         cut_out = item.get('cut_out')
    #
    #         self.ui.FR_end.setText(str(cut_out))

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

    def layer_fx(self, *args):
        layer_set.layer_fx()


    def fx_set(self, *args):
        layer_set.fx_set()


    def fx_lit(self, *args):
        project_set.fx_meshlit()


    def beam_set(selfs, *args):
        project_set.beam_set()

    def beam_lit(selfs, *args):
        project_set.beam_lit()

    def fog_set(self, *args):
        project_set.fog_set()





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

import LIT_grp.LT_script.Lit_tool

reload(LIT_grp.LT_script.Lit_tool) 
print(LIT_grp.LT_script.Lit_tool.__file__)
LIT_grp.LT_script.Lit_tool.run_main_maya()

"""







