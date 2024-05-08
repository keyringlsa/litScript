# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DeadlineRenderJob.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_render_widgets(object):
    def setupUi(self, render_widgets):
        if not render_widgets.objectName():
            render_widgets.setObjectName(u"render_widgets")
        render_widgets.resize(775, 446)
        render_widgets.setMinimumSize(QSize(0, 446))
        self.verticalLayout = QVBoxLayout(render_widgets)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(render_widgets)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.splitter_2 = QSplitter(self.frame_3)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter_2.setOpaqueResize(True)
        self.frame_5 = QFrame(self.splitter_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMinimumSize(QSize(200, 0))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.render_layer_lv = QListView(self.frame_5)
        self.render_layer_lv.setObjectName(u"render_layer_lv")
        sizePolicy1.setHeightForWidth(self.render_layer_lv.sizePolicy().hasHeightForWidth())
        self.render_layer_lv.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(11)
        self.render_layer_lv.setFont(font)
        self.render_layer_lv.setEditTriggers(QAbstractItemView.CurrentChanged|QAbstractItemView.EditKeyPressed)
        self.render_layer_lv.setAlternatingRowColors(True)
        self.render_layer_lv.setSelectionMode(QAbstractItemView.NoSelection)
        self.render_layer_lv.setViewMode(QListView.ListMode)
        self.render_layer_lv.setModelColumn(0)
        self.render_layer_lv.setSelectionRectVisible(True)

        self.verticalLayout_4.addWidget(self.render_layer_lv)

        self.splitter_2.addWidget(self.frame_5)
        self.frame_6 = QFrame(self.splitter_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy2)
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setMaximumSize(QSize(550, 16777215))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.line_4 = QFrame(self.frame_6)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_4)

        self.MakePreviewCheckBox = QCheckBox(self.frame_6)
        self.MakePreviewCheckBox.setObjectName(u"MakePreviewCheckBox")

        self.horizontalLayout_2.addWidget(self.MakePreviewCheckBox)

        self.OverWriteLatestVersionCheckBox = QCheckBox(self.frame_6)
        self.OverWriteLatestVersionCheckBox.setObjectName(u"OverWriteLatestVersionCheckBox")

        self.horizontalLayout_2.addWidget(self.OverWriteLatestVersionCheckBox)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 2, -1, 2)

        self.horizontalLayout_2.addWidget(self.frame_10)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.frame = QFrame(self.frame_6)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 2, -1, 2)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.cutin_frame_spb = QSpinBox(self.frame)
        self.cutin_frame_spb.setObjectName(u"cutin_frame_spb")
        self.cutin_frame_spb.setEnabled(True)
        self.cutin_frame_spb.setMinimum(1)
        self.cutin_frame_spb.setMaximum(99999999)
        self.cutin_frame_spb.setValue(101)

        self.horizontalLayout_3.addWidget(self.cutin_frame_spb)

        self.start_frame_spb = QSpinBox(self.frame)
        self.start_frame_spb.setObjectName(u"start_frame_spb")
        self.start_frame_spb.setEnabled(False)
        self.start_frame_spb.setMinimum(1)
        self.start_frame_spb.setMaximum(999999999)
        self.start_frame_spb.setValue(101)

        self.horizontalLayout_3.addWidget(self.start_frame_spb)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.end_frame_spb = QSpinBox(self.frame)
        self.end_frame_spb.setObjectName(u"end_frame_spb")
        self.end_frame_spb.setEnabled(False)
        self.end_frame_spb.setFrame(True)
        self.end_frame_spb.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.end_frame_spb.setMinimum(1)
        self.end_frame_spb.setMaximum(99999999)
        self.end_frame_spb.setValue(101)

        self.horizontalLayout_3.addWidget(self.end_frame_spb)

        self.cutout_frame_spb = QSpinBox(self.frame)
        self.cutout_frame_spb.setObjectName(u"cutout_frame_spb")
        self.cutout_frame_spb.setEnabled(True)
        self.cutout_frame_spb.setMaximum(9999999)
        self.cutout_frame_spb.setValue(101)

        self.horizontalLayout_3.addWidget(self.cutout_frame_spb)


        self.verticalLayout_5.addWidget(self.frame)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(6, 2, -1, 2)
        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(99, 16777215))

        self.horizontalLayout_7.addWidget(self.label_7)

        self.output_size_percent_spb = QSpinBox(self.frame_7)
        self.output_size_percent_spb.setObjectName(u"output_size_percent_spb")
        self.output_size_percent_spb.setMinimumSize(QSize(60, 0))
        self.output_size_percent_spb.setMinimum(10)
        self.output_size_percent_spb.setMaximum(200)
        self.output_size_percent_spb.setSingleStep(5)
        self.output_size_percent_spb.setValue(100)

        self.horizontalLayout_7.addWidget(self.output_size_percent_spb)

        self.line_2 = QFrame(self.frame_7)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, -1, -1, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")

        self.horizontalLayout_10.addWidget(self.label)

        self.output_size_width_lb = QLabel(self.frame_7)
        self.output_size_width_lb.setObjectName(u"output_size_width_lb")

        self.horizontalLayout_10.addWidget(self.output_size_width_lb)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.output_size_height_lb = QLabel(self.frame_7)
        self.output_size_height_lb.setObjectName(u"output_size_height_lb")

        self.horizontalLayout_5.addWidget(self.output_size_height_lb)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_7.addLayout(self.verticalLayout_8)

        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.sg_resolution_pushButton = QPushButton(self.frame_7)
        self.sg_resolution_pushButton.setObjectName(u"sg_resolution_pushButton")
        self.sg_resolution_pushButton.setMinimumSize(QSize(165, 0))

        self.horizontalLayout_7.addWidget(self.sg_resolution_pushButton)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)


        self.verticalLayout_5.addWidget(self.frame_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_24 = QLabel(self.frame_6)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_4.addWidget(self.label_24)

        self.cam_comboBox = QComboBox(self.frame_6)
        self.cam_comboBox.setObjectName(u"cam_comboBox")
        self.cam_comboBox.setMinimumSize(QSize(350, 0))

        self.horizontalLayout_4.addWidget(self.cam_comboBox)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 2, -1, 2)
        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_8.addWidget(self.label_12)

        self.priority_spbox = QSpinBox(self.frame_8)
        self.priority_spbox.setObjectName(u"priority_spbox")
        self.priority_spbox.setMaximum(1000)
        self.priority_spbox.setValue(50)

        self.horizontalLayout_8.addWidget(self.priority_spbox)


        self.horizontalLayout_14.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 2, -1, 2)
        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_9.addWidget(self.label_9)

        self.frame_for_task_spb = QSpinBox(self.frame_9)
        self.frame_for_task_spb.setObjectName(u"frame_for_task_spb")
        self.frame_for_task_spb.setEnabled(False)
        self.frame_for_task_spb.setMinimum(1)

        self.horizontalLayout_9.addWidget(self.frame_for_task_spb)


        self.horizontalLayout_14.addWidget(self.frame_9)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, -1, -1, -1)
        self.mr_frame = QFrame(self.frame_6)
        self.mr_frame.setObjectName(u"mr_frame")
        self.mr_frame.setFrameShape(QFrame.StyledPanel)
        self.mr_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.mr_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 2, -1, 2)
        self.label_6 = QLabel(self.mr_frame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_11.addWidget(self.label_6)

        self.renderer_lb = QLabel(self.mr_frame)
        self.renderer_lb.setObjectName(u"renderer_lb")

        self.horizontalLayout_11.addWidget(self.renderer_lb)

        self.label_5_empty = QLabel(self.mr_frame)
        self.label_5_empty.setObjectName(u"label_5_empty")

        self.horizontalLayout_11.addWidget(self.label_5_empty)


        self.horizontalLayout_16.addWidget(self.mr_frame)

        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 2, -1, 2)
        self.label_10 = QLabel(self.frame_13)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_18.addWidget(self.label_10)

        self.render_division_spb = QSpinBox(self.frame_13)
        self.render_division_spb.setObjectName(u"render_division_spb")
        self.render_division_spb.setEnabled(False)
        self.render_division_spb.setMinimum(1)
        self.render_division_spb.setMaximum(100)

        self.horizontalLayout_18.addWidget(self.render_division_spb)


        self.horizontalLayout_16.addWidget(self.frame_13)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.splitter_2.addWidget(self.frame_6)

        self.verticalLayout_2.addWidget(self.splitter_2)


        self.verticalLayout.addWidget(self.frame_3)

        self.send_job_btn = QPushButton(render_widgets)
        self.send_job_btn.setObjectName(u"send_job_btn")

        self.verticalLayout.addWidget(self.send_job_btn)


        self.retranslateUi(render_widgets)

        QMetaObject.connectSlotsByName(render_widgets)
    # setupUi

    def retranslateUi(self, render_widgets):
        render_widgets.setWindowTitle(QCoreApplication.translate("render_widgets", u"DeadlineRenderJob", None))
        self.label_4.setText(QCoreApplication.translate("render_widgets", u"Render Layer", None))
        self.MakePreviewCheckBox.setText(QCoreApplication.translate("render_widgets", u"Make Preview", None))
        self.OverWriteLatestVersionCheckBox.setText(QCoreApplication.translate("render_widgets", u"Overwrite empty frames with the latest version", None))
        self.label_2.setText(QCoreApplication.translate("render_widgets", u"start frame", None))
        self.label_3.setText(QCoreApplication.translate("render_widgets", u"end frame", None))
        self.label_7.setText(QCoreApplication.translate("render_widgets", u"output size % : ", None))
        self.label.setText(QCoreApplication.translate("render_widgets", u"width  :", None))
        self.output_size_width_lb.setText(QCoreApplication.translate("render_widgets", u"2048", None))
        self.label_11.setText(QCoreApplication.translate("render_widgets", u"Height :", None))
        self.output_size_height_lb.setText(QCoreApplication.translate("render_widgets", u"1668", None))
        self.label_5.setText(QCoreApplication.translate("render_widgets", u" << ", None))
        self.sg_resolution_pushButton.setText(QCoreApplication.translate("render_widgets", u"Get ShotGrid Resolution", None))
        self.label_24.setText(QCoreApplication.translate("render_widgets", u" Camera : ", None))
        self.label_12.setText(QCoreApplication.translate("render_widgets", u"Priority: ", None))
        self.label_9.setText(QCoreApplication.translate("render_widgets", u"frame for Task: ", None))
        self.label_6.setText(QCoreApplication.translate("render_widgets", u"Renderer : ", None))
        self.renderer_lb.setText(QCoreApplication.translate("render_widgets", u"renderer", None))
        self.label_5_empty.setText("")
        self.label_10.setText(QCoreApplication.translate("render_widgets", u"Region Division", None))
        self.send_job_btn.setText(QCoreApplication.translate("render_widgets", u"Send Job", None))
    # retranslateUi

