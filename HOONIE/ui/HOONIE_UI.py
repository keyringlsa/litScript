# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HOONIE_UI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_HOONIE_QWidget(object):
    def setupUi(self, HOONIE_QWidget):
        if not HOONIE_QWidget.objectName():
            HOONIE_QWidget.setObjectName(u"HOONIE_QWidget")
        HOONIE_QWidget.resize(739, 534)
        self.verticalLayout = QVBoxLayout(HOONIE_QWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(HOONIE_QWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.reload_Btn = QPushButton(HOONIE_QWidget)
        self.reload_Btn.setObjectName(u"reload_Btn")

        self.horizontalLayout_2.addWidget(self.reload_Btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tabWidget = QTabWidget(HOONIE_QWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Import_ViewWidget = QWidget()
        self.Import_ViewWidget.setObjectName(u"Import_ViewWidget")
        self.verticalLayout_2 = QVBoxLayout(self.Import_ViewWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Import_QTreeView = QTreeView(self.Import_ViewWidget)
        self.Import_QTreeView.setObjectName(u"Import_QTreeView")
        self.Import_QTreeView.setMinimumSize(QSize(0, 0))

        self.verticalLayout_2.addWidget(self.Import_QTreeView)

        self.tabWidget.addTab(self.Import_ViewWidget, "")
        self.Imported_ViewWidget = QWidget()
        self.Imported_ViewWidget.setObjectName(u"Imported_ViewWidget")
        self.verticalLayout_3 = QVBoxLayout(self.Imported_ViewWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Imported_QTreeView = QTreeView(self.Imported_ViewWidget)
        self.Imported_QTreeView.setObjectName(u"Imported_QTreeView")

        self.verticalLayout_3.addWidget(self.Imported_QTreeView)

        self.tabWidget.addTab(self.Imported_ViewWidget, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.status_label = QLabel(HOONIE_QWidget)
        self.status_label.setObjectName(u"status_label")

        self.horizontalLayout_3.addWidget(self.status_label)

        self.OpenShotPage_Btn = QPushButton(HOONIE_QWidget)
        self.OpenShotPage_Btn.setObjectName(u"OpenShotPage_Btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenShotPage_Btn.sizePolicy().hasHeightForWidth())
        self.OpenShotPage_Btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.OpenShotPage_Btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(HOONIE_QWidget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(HOONIE_QWidget)
    # setupUi

    def retranslateUi(self, HOONIE_QWidget):
        HOONIE_QWidget.setWindowTitle(QCoreApplication.translate("HOONIE_QWidget", u"HOONIE Alembic Manager", None))
        self.label.setText(QCoreApplication.translate("HOONIE_QWidget", u"HOONIE", None))
        self.reload_Btn.setText(QCoreApplication.translate("HOONIE_QWidget", u"reload", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Import_ViewWidget), QCoreApplication.translate("HOONIE_QWidget", u"Published", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Imported_ViewWidget), QCoreApplication.translate("HOONIE_QWidget", u"Imported", None))
        self.status_label.setText(QCoreApplication.translate("HOONIE_QWidget", u"TextLabel", None))
        self.OpenShotPage_Btn.setText(QCoreApplication.translate("HOONIE_QWidget", u"Open Shot Page", None))
    # retranslateUi

