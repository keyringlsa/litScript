# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'unreal_asset_UIueDvfC.ui'
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
        MainWindow.resize(1427, 699)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.asset_type = QListView(self.centralwidget)
        self.asset_type.setObjectName(u"asset_type")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.asset_type.sizePolicy().hasHeightForWidth())
        self.asset_type.setSizePolicy(sizePolicy)
        self.asset_type.setMinimumSize(QSize(0, 0))
        self.asset_type.setMaximumSize(QSize(16777215, 150))
        font = QFont()
        font.setFamily(u"\ub098\ub214\uace0\ub515")
        font.setPointSize(10)
        self.asset_type.setFont(font)

        self.verticalLayout.addWidget(self.asset_type)

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

        self.Refresh_btn = QPushButton(self.centralwidget)
        self.Refresh_btn.setObjectName(u"Refresh_btn")
        self.Refresh_btn.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.Refresh_btn)

        self.fol_btn = QPushButton(self.centralwidget)
        self.fol_btn.setObjectName(u"fol_btn")
        self.fol_btn.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.fol_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_12.addLayout(self.verticalLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line)

        self.asset_list = QTreeView(self.centralwidget)
        self.asset_list.setObjectName(u"asset_list")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(50)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.asset_list.sizePolicy().hasHeightForWidth())
        self.asset_list.setSizePolicy(sizePolicy1)
        self.asset_list.setMinimumSize(QSize(0, 0))
        self.asset_list.setSizeIncrement(QSize(500, 0))
        font1 = QFont()
        font1.setFamily(u"\ub098\ub214\uace0\ub515")
        font1.setPointSize(11)
        self.asset_list.setFont(font1)

        self.horizontalLayout_12.addWidget(self.asset_list)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1427, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Unporter", None))
        self.Seach_name.setText(QCoreApplication.translate("MainWindow", u"seach :", None))
        self.Refresh_btn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.fol_btn.setText(QCoreApplication.translate("MainWindow", u"folder_create", None))
    # retranslateUi

