# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CSI_UI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CSI_QWidget(object):
    def setupUi(self, CSI_QWidget):
        if not CSI_QWidget.objectName():
            CSI_QWidget.setObjectName(u"CSI_QWidget")
        CSI_QWidget.resize(398, 293)
        self.verticalLayout_2 = QVBoxLayout(CSI_QWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.resolution_QCheckBox = QCheckBox(CSI_QWidget)
        self.resolution_QCheckBox.setObjectName(u"resolution_QCheckBox")
        self.resolution_QCheckBox.setChecked(True)

        self.horizontalLayout_5.addWidget(self.resolution_QCheckBox)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(CSI_QWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.Resolution_Width_QLineEdit = QLineEdit(CSI_QWidget)
        self.Resolution_Width_QLineEdit.setObjectName(u"Resolution_Width_QLineEdit")
        self.Resolution_Width_QLineEdit.setEnabled(False)

        self.horizontalLayout_6.addWidget(self.Resolution_Width_QLineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(CSI_QWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.Resolution_Height_QLineEdit = QLineEdit(CSI_QWidget)
        self.Resolution_Height_QLineEdit.setObjectName(u"Resolution_Height_QLineEdit")
        self.Resolution_Height_QLineEdit.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.Resolution_Height_QLineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Cutinout_QCheckBox = QCheckBox(CSI_QWidget)
        self.Cutinout_QCheckBox.setObjectName(u"Cutinout_QCheckBox")
        self.Cutinout_QCheckBox.setChecked(True)

        self.horizontalLayout_3.addWidget(self.Cutinout_QCheckBox)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label = QLabel(CSI_QWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_9.addWidget(self.label)

        self.StartFrame_QLineEdit = QLineEdit(CSI_QWidget)
        self.StartFrame_QLineEdit.setObjectName(u"StartFrame_QLineEdit")
        self.StartFrame_QLineEdit.setEnabled(False)

        self.horizontalLayout_9.addWidget(self.StartFrame_QLineEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(CSI_QWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.EndFrame_QLineEdit = QLineEdit(CSI_QWidget)
        self.EndFrame_QLineEdit.setObjectName(u"EndFrame_QLineEdit")
        self.EndFrame_QLineEdit.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.EndFrame_QLineEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Fps_QCheckBox = QCheckBox(CSI_QWidget)
        self.Fps_QCheckBox.setObjectName(u"Fps_QCheckBox")
        self.Fps_QCheckBox.setChecked(True)

        self.horizontalLayout_2.addWidget(self.Fps_QCheckBox)

        self.Fps_QLineEdit = QLineEdit(CSI_QWidget)
        self.Fps_QLineEdit.setObjectName(u"Fps_QLineEdit")
        self.Fps_QLineEdit.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.Fps_QLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Set_QButton = QPushButton(CSI_QWidget)
        self.Set_QButton.setObjectName(u"Set_QButton")

        self.horizontalLayout.addWidget(self.Set_QButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(CSI_QWidget)

        QMetaObject.connectSlotsByName(CSI_QWidget)
    # setupUi

    def retranslateUi(self, CSI_QWidget):
        CSI_QWidget.setWindowTitle(QCoreApplication.translate("CSI_QWidget", u"CSI", None))
        self.resolution_QCheckBox.setText(QCoreApplication.translate("CSI_QWidget", u"Resolution", None))
        self.label_4.setText(QCoreApplication.translate("CSI_QWidget", u"Width", None))
        self.label_5.setText(QCoreApplication.translate("CSI_QWidget", u"Height", None))
        self.Cutinout_QCheckBox.setText(QCoreApplication.translate("CSI_QWidget", u"Cun in out", None))
        self.label.setText(QCoreApplication.translate("CSI_QWidget", u"Start Frame", None))
        self.label_6.setText(QCoreApplication.translate("CSI_QWidget", u"End Frame", None))
        self.Fps_QCheckBox.setText(QCoreApplication.translate("CSI_QWidget", u"FPS", None))
        self.Set_QButton.setText(QCoreApplication.translate("CSI_QWidget", u"Set Scene Setting", None))
    # retranslateUi

