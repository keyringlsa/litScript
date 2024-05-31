# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'unreal_LK_UILgcjXW.ui'
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
        MainWindow.resize(351, 681)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LKD_type = QComboBox(self.centralwidget)
        self.LKD_type.addItem("")
        self.LKD_type.addItem("")
        self.LKD_type.addItem("")
        self.LKD_type.setObjectName(u"LKD_type")
        self.LKD_type.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setFamily(u"\ub098\ub214\uace0\ub515")
        font.setPointSize(10)
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
        self.txt_imp = QPushButton(self.centralwidget)
        self.txt_imp.setObjectName(u"txt_imp")
        self.txt_imp.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.txt_imp.sizePolicy().hasHeightForWidth())
        self.txt_imp.setSizePolicy(sizePolicy1)
        self.txt_imp.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_2.addWidget(self.txt_imp)

        self.mtl_connet = QPushButton(self.centralwidget)
        self.mtl_connet.setObjectName(u"mtl_connet")
        self.mtl_connet.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_2.addWidget(self.mtl_connet)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 351, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lkd_tool_beta", None))
        self.LKD_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Character", None))
        self.LKD_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Env", None))
        self.LKD_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Prop", None))

        self.Seach_name.setText(QCoreApplication.translate("MainWindow", u"seach :", None))
        self.Refresh_btn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.txt_imp.setText(QCoreApplication.translate("MainWindow", u"txt_imp", None))
        self.mtl_connet.setText(QCoreApplication.translate("MainWindow", u"mtl_connet", None))
    # retranslateUi

