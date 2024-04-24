# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sha_uilxYFht.ui'
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
        Form.resize(1167, 1012)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Refresh_btn = QPushButton(Form)
        self.Refresh_btn.setObjectName(u"Refresh_btn")
        self.Refresh_btn.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.Refresh_btn)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.A_list = QTreeView(Form)
        self.A_list.setObjectName(u"A_list")

        self.horizontalLayout_2.addWidget(self.A_list)

        self.B_list = QTreeView(Form)
        self.B_list.setObjectName(u"B_list")
        self.B_list.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.horizontalLayout_2.addWidget(self.B_list)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Shader_Tool", None))
        self.Refresh_btn.setText(QCoreApplication.translate("Form", u"Refresh", None))
    # retranslateUi

