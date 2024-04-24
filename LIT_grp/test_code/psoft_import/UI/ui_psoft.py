# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'psoftFeOlzS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(639, 533)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.type = QComboBox(Form)
        self.type.addItem("")
        self.type.addItem("")
        self.type.setObjectName(u"type")
        font = QFont()
        font.setPointSize(10)
        self.type.setFont(font)

        self.horizontalLayout.addWidget(self.type)

        self.ref_btn = QPushButton(Form)
        self.ref_btn.setObjectName(u"ref_btn")
        self.ref_btn.setFont(font)

        self.horizontalLayout.addWidget(self.ref_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.psoft_list = QListView(Form)
        self.psoft_list.setObjectName(u"psoft_list")
        font1 = QFont()
        font1.setPointSize(11)
        self.psoft_list.setFont(font1)

        self.verticalLayout.addWidget(self.psoft_list)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.imp_btn = QPushButton(self.splitter)
        self.imp_btn.setObjectName(u"imp_btn")
        self.imp_btn.setFont(font)
        self.splitter.addWidget(self.imp_btn)
        self.set_btn = QPushButton(self.splitter)
        self.set_btn.setObjectName(u"set_btn")
        self.set_btn.setFont(font)
        self.splitter.addWidget(self.set_btn)
        self.open_btn = QPushButton(self.splitter)
        self.open_btn.setObjectName(u"open_btn")
        self.open_btn.setFont(font)
        self.splitter.addWidget(self.open_btn)

        self.gridLayout.addWidget(self.splitter, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.type.setItemText(0, QCoreApplication.translate("Form", u"DNF", None))
        self.type.setItemText(1, QCoreApplication.translate("Form", u"DNF45", None))

        self.ref_btn.setText(QCoreApplication.translate("Form", u"refresh", None))
        self.imp_btn.setText(QCoreApplication.translate("Form", u"Import", None))
        self.set_btn.setText(QCoreApplication.translate("Form", u"Setting", None))
        self.open_btn.setText(QCoreApplication.translate("Form", u"Open dir", None))
    # retranslateUi

