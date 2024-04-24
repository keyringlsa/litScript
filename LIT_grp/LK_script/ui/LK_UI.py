# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LK_UIacKeAc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(787, 681)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 1, 1, 1)

        self.Tool_Tab = QTabWidget(self.centralwidget)
        self.Tool_Tab.setObjectName(u"Tool_Tab")
        self.Tool_Tab.setMinimumSize(QSize(450, 0))
        self.Render = QWidget()
        self.Render.setObjectName(u"Render")
        self.render_set_JH = QPushButton(self.Render)
        self.render_set_JH.setObjectName(u"render_set_JH")
        self.render_set_JH.setGeometry(QRect(10, 60, 91, 41))
        self.render_set_SA = QPushButton(self.Render)
        self.render_set_SA.setObjectName(u"render_set_SA")
        self.render_set_SA.setGeometry(QRect(110, 60, 91, 41))
        self.Render_set = QLabel(self.Render)
        self.Render_set.setObjectName(u"Render_set")
        self.Render_set.setGeometry(QRect(10, 30, 111, 21))
        self.sampling_Mid = QPushButton(self.Render)
        self.sampling_Mid.setObjectName(u"sampling_Mid")
        self.sampling_Mid.setGeometry(QRect(110, 230, 91, 41))
        self.sampling_low = QPushButton(self.Render)
        self.sampling_low.setObjectName(u"sampling_low")
        self.sampling_low.setGeometry(QRect(10, 230, 91, 41))
        self.Sampling = QLabel(self.Render)
        self.Sampling.setObjectName(u"Sampling")
        self.Sampling.setGeometry(QRect(10, 200, 111, 21))
        self.sampling_High = QPushButton(self.Render)
        self.sampling_High.setObjectName(u"sampling_High")
        self.sampling_High.setGeometry(QRect(210, 230, 91, 41))
        self.sampling_Vol = QPushButton(self.Render)
        self.sampling_Vol.setObjectName(u"sampling_Vol")
        self.sampling_Vol.setGeometry(QRect(10, 280, 91, 41))
        self.sampling_Fil = QPushButton(self.Render)
        self.sampling_Fil.setObjectName(u"sampling_Fil")
        self.sampling_Fil.setGeometry(QRect(110, 280, 91, 41))
        self.render_set_Deep = QPushButton(self.Render)
        self.render_set_Deep.setObjectName(u"render_set_Deep")
        self.render_set_Deep.setGeometry(QRect(210, 60, 91, 41))
        self.render_set_W = QPushButton(self.Render)
        self.render_set_W.setObjectName(u"render_set_W")
        self.render_set_W.setGeometry(QRect(10, 110, 91, 41))
        self.Tool_Tab.addTab(self.Render, "")
        self.render_set_JH.raise_()
        self.render_set_SA.raise_()
        self.Render_set.raise_()
        self.sampling_Mid.raise_()
        self.Sampling.raise_()
        self.sampling_High.raise_()
        self.sampling_Vol.raise_()
        self.sampling_Fil.raise_()
        self.render_set_Deep.raise_()
        self.render_set_W.raise_()
        self.sampling_low.raise_()
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.Expression_set = QLabel(self.tab_2)
        self.Expression_set.setObjectName(u"Expression_set")
        self.Expression_set.setGeometry(QRect(10, 140, 111, 21))
        self.Exp_OK_btn = QPushButton(self.tab_2)
        self.Exp_OK_btn.setObjectName(u"Exp_OK_btn")
        self.Exp_OK_btn.setGeometry(QRect(290, 290, 91, 31))
        self.Custom_AT_set = QLabel(self.tab_2)
        self.Custom_AT_set.setObjectName(u"Custom_AT_set")
        self.Custom_AT_set.setGeometry(QRect(10, 20, 111, 21))
        self.AT_name = QLineEdit(self.tab_2)
        self.AT_name.setObjectName(u"AT_name")
        self.AT_name.setGeometry(QRect(80, 50, 171, 31))
        font = QFont()
        font.setFamily(u"\ub098\ub214\uace0\ub515")
        font.setPointSize(10)
        self.AT_name.setFont(font)
        self.at_name = QLabel(self.tab_2)
        self.at_name.setObjectName(u"at_name")
        self.at_name.setGeometry(QRect(10, 50, 71, 30))
        self.at_name.setMinimumSize(QSize(0, 30))
        self.at_type_float = QRadioButton(self.tab_2)
        self.at_type_float.setObjectName(u"at_type_float")
        self.at_type_float.setGeometry(QRect(80, 100, 92, 16))
        self.at_type_string = QRadioButton(self.tab_2)
        self.at_type_string.setObjectName(u"at_type_string")
        self.at_type_string.setGeometry(QRect(180, 100, 92, 16))
        self.at_type_set = QLabel(self.tab_2)
        self.at_type_set.setObjectName(u"at_type_set")
        self.at_type_set.setGeometry(QRect(10, 90, 71, 30))
        self.at_type_set.setMinimumSize(QSize(0, 30))
        self.AT_add_btn = QPushButton(self.tab_2)
        self.AT_add_btn.setObjectName(u"AT_add_btn")
        self.AT_add_btn.setGeometry(QRect(280, 90, 91, 31))
        self.layoutWidget = QWidget(self.tab_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 200, 371, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Expression_inputC = QLineEdit(self.layoutWidget)
        self.Expression_inputC.setObjectName(u"Expression_inputC")
        self.Expression_inputC.setMinimumSize(QSize(0, 30))
        self.Expression_inputC.setFont(font)

        self.horizontalLayout_4.addWidget(self.Expression_inputC)

        self.at_type_set_3 = QLabel(self.layoutWidget)
        self.at_type_set_3.setObjectName(u"at_type_set_3")
        self.at_type_set_3.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_4.addWidget(self.at_type_set_3)

        self.Expression_inputD = QLineEdit(self.layoutWidget)
        self.Expression_inputD.setObjectName(u"Expression_inputD")
        self.Expression_inputD.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_4.addWidget(self.Expression_inputD)

        self.layoutWidget_2 = QWidget(self.tab_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 240, 371, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Expression_inputE = QLineEdit(self.layoutWidget_2)
        self.Expression_inputE.setObjectName(u"Expression_inputE")
        self.Expression_inputE.setMinimumSize(QSize(0, 30))
        self.Expression_inputE.setFont(font)

        self.horizontalLayout_5.addWidget(self.Expression_inputE)

        self.at_type_set_4 = QLabel(self.layoutWidget_2)
        self.at_type_set_4.setObjectName(u"at_type_set_4")
        self.at_type_set_4.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_5.addWidget(self.at_type_set_4)

        self.Expression_inputF = QLineEdit(self.layoutWidget_2)
        self.Expression_inputF.setObjectName(u"Expression_inputF")
        self.Expression_inputF.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_5.addWidget(self.Expression_inputF)

        self.layoutWidget1 = QWidget(self.tab_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 160, 371, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Expression_inputA = QLineEdit(self.layoutWidget1)
        self.Expression_inputA.setObjectName(u"Expression_inputA")
        self.Expression_inputA.setMinimumSize(QSize(0, 30))
        self.Expression_inputA.setFont(font)

        self.horizontalLayout_3.addWidget(self.Expression_inputA)

        self.at_type_set_2 = QLabel(self.layoutWidget1)
        self.at_type_set_2.setObjectName(u"at_type_set_2")
        self.at_type_set_2.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.at_type_set_2)

        self.Expression_inputB = QLineEdit(self.layoutWidget1)
        self.Expression_inputB.setObjectName(u"Expression_inputB")
        self.Expression_inputB.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.Expression_inputB)

        self.Tool_Tab.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.Project_set = QLabel(self.tab)
        self.Project_set.setObjectName(u"Project_set")
        self.Project_set.setGeometry(QRect(10, 30, 111, 21))
        self.verticalLayoutWidget_6 = QWidget(self.tab)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 60, 401, 131))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Project_list = QListView(self.verticalLayoutWidget_6)
        self.Project_list.setObjectName(u"Project_list")
        self.Project_list.setFont(font)

        self.verticalLayout_4.addWidget(self.Project_list)

        self.Project_input = QLineEdit(self.tab)
        self.Project_input.setObjectName(u"Project_input")
        self.Project_input.setGeometry(QRect(10, 200, 261, 31))
        self.Project_input.setFont(font)
        self.verticalLayoutWidget_7 = QWidget(self.tab)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(280, 200, 131, 32))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Project_export_btn = QPushButton(self.verticalLayoutWidget_7)
        self.Project_export_btn.setObjectName(u"Project_export_btn")
        self.Project_export_btn.setMinimumSize(QSize(0, 30))

        self.verticalLayout_5.addWidget(self.Project_export_btn)

        self.verticalLayoutWidget_8 = QWidget(self.tab)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(280, 240, 131, 32))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Project_import_btn = QPushButton(self.verticalLayoutWidget_8)
        self.Project_import_btn.setObjectName(u"Project_import_btn")
        self.Project_import_btn.setMinimumSize(QSize(0, 30))

        self.verticalLayout_7.addWidget(self.Project_import_btn)

        self.verticalLayoutWidget_9 = QWidget(self.tab)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(10, 240, 261, 32))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Project_refresh = QPushButton(self.verticalLayoutWidget_9)
        self.Project_refresh.setObjectName(u"Project_refresh")
        self.Project_refresh.setMinimumSize(QSize(0, 30))
        self.Project_refresh.setIconSize(QSize(16, 16))

        self.verticalLayout_8.addWidget(self.Project_refresh)

        self.Tool_Tab.addTab(self.tab, "")

        self.gridLayout.addWidget(self.Tool_Tab, 0, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LKD_type = QComboBox(self.centralwidget)
        self.LKD_type.addItem("")
        self.LKD_type.addItem("")
        self.LKD_type.addItem("")
        self.LKD_type.setObjectName(u"LKD_type")
        self.LKD_type.setMinimumSize(QSize(0, 40))
        self.LKD_type.setFont(font)
        self.LKD_type.setEditable(True)

        self.verticalLayout.addWidget(self.LKD_type)

        self.lkdlist = QListView(self.centralwidget)
        self.lkdlist.setObjectName(u"lkdlist")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lkdlist.sizePolicy().hasHeightForWidth())
        self.lkdlist.setSizePolicy(sizePolicy)
        self.lkdlist.setMinimumSize(QSize(0, 0))
        self.lkdlist.setMaximumSize(QSize(16777215, 150))
        self.lkdlist.setFont(font)

        self.verticalLayout.addWidget(self.lkdlist)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Seach_name = QLabel(self.centralwidget)
        self.Seach_name.setObjectName(u"Seach_name")
        self.Seach_name.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.Seach_name)

        self.Seach_input = QLineEdit(self.centralwidget)
        self.Seach_input.setObjectName(u"Seach_input")
        self.Seach_input.setMinimumSize(QSize(0, 30))
        self.Seach_input.setFont(font)

        self.horizontalLayout.addWidget(self.Seach_input)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.datalayout = QVBoxLayout()
        self.datalayout.setObjectName(u"datalayout")
        self.datalist = QTableView(self.centralwidget)
        self.datalist.setObjectName(u"datalist")
        self.datalist.setMinimumSize(QSize(320, 0))
        self.datalist.setFont(font)

        self.datalayout.addWidget(self.datalist)


        self.verticalLayout.addLayout(self.datalayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Refresh_btn = QPushButton(self.centralwidget)
        self.Refresh_btn.setObjectName(u"Refresh_btn")
        self.Refresh_btn.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.Refresh_btn)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.export_All = QPushButton(self.centralwidget)
        self.export_All.setObjectName(u"export_All")
        self.export_All.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.export_All.sizePolicy().hasHeightForWidth())
        self.export_All.setSizePolicy(sizePolicy1)
        self.export_All.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_2.addWidget(self.export_All)

        self.import_All = QPushButton(self.centralwidget)
        self.import_All.setObjectName(u"import_All")
        self.import_All.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_2.addWidget(self.import_All)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 787, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Tool_Tab.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lkd_tool_beta", None))
        self.render_set_JH.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.render_set_SA.setText(QCoreApplication.translate("MainWindow", u"Old", None))
        self.Render_set.setText(QCoreApplication.translate("MainWindow", u"Render_set", None))
        self.sampling_Mid.setText(QCoreApplication.translate("MainWindow", u"MIDDLE", None))
        self.sampling_low.setText(QCoreApplication.translate("MainWindow", u"LOW", None))
        self.Sampling.setText(QCoreApplication.translate("MainWindow", u"Sampling", None))
        self.sampling_High.setText(QCoreApplication.translate("MainWindow", u"HIGH", None))
        self.sampling_Vol.setText(QCoreApplication.translate("MainWindow", u"VOLUME", None))
        self.sampling_Fil.setText(QCoreApplication.translate("MainWindow", u"Flickr", None))
        self.render_set_Deep.setText(QCoreApplication.translate("MainWindow", u"Deep", None))
        self.render_set_W.setText(QCoreApplication.translate("MainWindow", u"W_default", None))
        self.Tool_Tab.setTabText(self.Tool_Tab.indexOf(self.Render), QCoreApplication.translate("MainWindow", u"Render", None))
        self.Expression_set.setText(QCoreApplication.translate("MainWindow", u"Expression_set", None))
        self.Exp_OK_btn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.Custom_AT_set.setText(QCoreApplication.translate("MainWindow", u"Custom AT_set", None))
        self.at_name.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.at_type_float.setText(QCoreApplication.translate("MainWindow", u"Float", None))
        self.at_type_string.setText(QCoreApplication.translate("MainWindow", u"String", None))
        self.at_type_set.setText(QCoreApplication.translate("MainWindow", u"Type:", None))
        self.AT_add_btn.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.at_type_set_3.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.at_type_set_4.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.at_type_set_2.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.Tool_Tab.setTabText(self.Tool_Tab.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Attr", None))
        self.Project_set.setText(QCoreApplication.translate("MainWindow", u"Project_set", None))
        self.Project_export_btn.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.Project_import_btn.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.Project_refresh.setText(QCoreApplication.translate("MainWindow", u"Refesh", None))
        self.Tool_Tab.setTabText(self.Tool_Tab.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Turntable/Project", None))
        self.LKD_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Character", None))
        self.LKD_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Env", None))
        self.LKD_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Prop", None))

        self.Seach_name.setText(QCoreApplication.translate("MainWindow", u"seach :", None))
        self.Refresh_btn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.export_All.setText(QCoreApplication.translate("MainWindow", u"All_Export", None))
        self.import_All.setText(QCoreApplication.translate("MainWindow", u"All_Import", None))
    # retranslateUi

