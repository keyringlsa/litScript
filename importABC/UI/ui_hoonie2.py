# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hoonie2_uiOLvFem.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_HOONIE_ver02(object):
    def setupUi(self, HOONIE_ver02):
        if not HOONIE_ver02.objectName():
            HOONIE_ver02.setObjectName(u"HOONIE_ver02")
        HOONIE_ver02.resize(970, 820)
        self.verticalLayout_2 = QVBoxLayout(HOONIE_ver02)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(HOONIE_ver02)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"\ub098\ub214\uace0\ub515")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)

        self.btn_reload = QPushButton(HOONIE_ver02)
        self.btn_reload.setObjectName(u"btn_reload")
        self.btn_reload.setMinimumSize(QSize(150, 30))
        self.btn_reload.setMaximumSize(QSize(150, 30))
        self.btn_reload.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.btn_reload)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(HOONIE_ver02)
        self.tabWidget.setObjectName(u"tabWidget")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.tabWidget.setFont(font1)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_6 = QHBoxLayout(self.tab)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.publist = QTreeView(self.tab)
        self.publist.setObjectName(u"publist")
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setWeight(50)
        self.publist.setFont(font2)

        self.horizontalLayout_6.addWidget(self.publist)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_7 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.importedlist = QTreeView(self.tab_2)
        self.importedlist.setObjectName(u"importedlist")
        self.importedlist.setFont(font2)

        self.horizontalLayout_7.addWidget(self.importedlist)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(HOONIE_ver02)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.btn_shotgrid = QPushButton(HOONIE_ver02)
        self.btn_shotgrid.setObjectName(u"btn_shotgrid")
        self.btn_shotgrid.setMinimumSize(QSize(150, 30))
        self.btn_shotgrid.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_4.addWidget(self.btn_shotgrid)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(HOONIE_ver02)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(HOONIE_ver02)
    # setupUi

    def retranslateUi(self, HOONIE_ver02):
        HOONIE_ver02.setWindowTitle(QCoreApplication.translate("HOONIE_ver02", u"HOONIE_ver02", None))
        self.label.setText(QCoreApplication.translate("HOONIE_ver02", u"Hoonie ver2", None))
        self.btn_reload.setText(QCoreApplication.translate("HOONIE_ver02", u"Reload", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("HOONIE_ver02", u"Publish", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("HOONIE_ver02", u"Imported", None))
        self.label_2.setText(QCoreApplication.translate("HOONIE_ver02", u"24.05.13", None))
        self.btn_shotgrid.setText(QCoreApplication.translate("HOONIE_ver02", u"Open page Shotgrid", None))
    # retranslateUi

