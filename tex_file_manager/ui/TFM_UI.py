# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TFM_UI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TexFileManager_QWidget(object):
    def setupUi(self, TexFileManager_QWidget):
        if not TexFileManager_QWidget.objectName():
            TexFileManager_QWidget.setObjectName(u"TexFileManager_QWidget")
        TexFileManager_QWidget.resize(732, 547)
        self.verticalLayout_2 = QVBoxLayout(TexFileManager_QWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(TexFileManager_QWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.Reload_Btn = QPushButton(TexFileManager_QWidget)
        self.Reload_Btn.setObjectName(u"Reload_Btn")

        self.horizontalLayout.addWidget(self.Reload_Btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Filter_QComboBox = QComboBox(TexFileManager_QWidget)
        self.Filter_QComboBox.setObjectName(u"Filter_QComboBox")

        self.horizontalLayout_2.addWidget(self.Filter_QComboBox)

        self.Search_QLineEdit = QLineEdit(TexFileManager_QWidget)
        self.Search_QLineEdit.setObjectName(u"Search_QLineEdit")

        self.horizontalLayout_2.addWidget(self.Search_QLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.FileNode_QTableView = QTableView(TexFileManager_QWidget)
        self.FileNode_QTableView.setObjectName(u"FileNode_QTableView")
        self.FileNode_QTableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.FileNode_QTableView)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.progressBar = QProgressBar(TexFileManager_QWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_2.addWidget(self.progressBar)


        self.retranslateUi(TexFileManager_QWidget)

        QMetaObject.connectSlotsByName(TexFileManager_QWidget)
    # setupUi

    def retranslateUi(self, TexFileManager_QWidget):
        TexFileManager_QWidget.setWindowTitle(QCoreApplication.translate("TexFileManager_QWidget", u"Keyring Maya Tool", None))
        self.label.setText(QCoreApplication.translate("TexFileManager_QWidget", u"Texture File Manager", None))
        self.Reload_Btn.setText(QCoreApplication.translate("TexFileManager_QWidget", u"Reload", None))
    # retranslateUi

