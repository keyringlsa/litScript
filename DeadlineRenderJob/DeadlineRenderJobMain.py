import os, sys
import sgtk

from PySide2 import QtWidgets, QtGui, QtCore
from imp import reload
from pprint import pprint

from CoreModules.handler import connect_sg
# from tdsg_core.logHandler import Tdlog
from DeadlineRenderJob.ui import DeadlineRenderJob
from DeadlineRenderJob.handler import maya_handler, deadline_handler, file_handler
from DeadlineRenderJob.model import render_layer_model


reload(DeadlineRenderJob)
reload(maya_handler)
reload(render_layer_model)
reload(deadline_handler)
reload(file_handler)

class JobMain(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.current_path = os.path.dirname(os.path.realpath(__file__))

        self.setWindowFlag(QtCore.Qt.WindowType(True))
        self.ui = DeadlineRenderJob.Ui_render_widgets()
        self.ui.setupUi(self)

        # get shotgun api
        sgl = connect_sg.Shotgun_Connect()
        self.sg = sgl.default_script_auth()

        # get current context info
        current_engine = sgtk.platform.current_engine()
        self.context = current_engine.context

        # render informations
        self.renderer = None
        self.resolution = None
        self.camera_list = None
        self.cutin_frame = None
        self.cutout_frame = None
        self.render_layers = None
        self.current_scene = None
        self.version_name = None
        self.version_num = None
        self.render_dir = None
        self.project_path = None
        self.maya_version = None
        self.ext_type = None


        # render layer model

        self.render_layer_model = None

        self.connected()


    def connected(self):
        self.get_maya_setting()
        self.ui.send_job_btn.clicked.connect(self.summit_job)
        # self.ui.output_size_percent_spb.valueChanged.connect(self.multiple_resolution)
        self.ui.output_size_percent_spb.lineEdit().returnPressed.connect(self.multiple_resolution)
        self.ui.cutin_frame_spb.lineEdit().returnPressed.connect(self.set_start_frame)
        self.ui.cutout_frame_spb.lineEdit().returnPressed.connect(self.set_end_frame)
        self.ui.OverWriteLatestVersionCheckBox.clicked.connect(self.overWriteMode)

    def overWriteMode(self):
        if self.ui.OverWriteLatestVersionCheckBox.isChecked():
            self.ui.cutin_frame_spb.setDisabled(True)
            self.ui.cutout_frame_spb.setDisabled(True)
            self.ui.start_frame_spb.setDisabled(False)
            self.ui.end_frame_spb.setDisabled(False)
        else:
            self.ui.cutin_frame_spb.setDisabled(False)
            self.ui.cutout_frame_spb.setDisabled(False)
            self.ui.start_frame_spb.setDisabled(True)
            self.ui.end_frame_spb.setDisabled(True)

    def set_start_frame(self):
        value = self.ui.cutin_frame_spb.value()

        if value <= self.ui.cutout_frame_spb.value():
            self.ui.start_frame_spb.setValue(value)

    def set_end_frame(self):
        value = self.ui.cutout_frame_spb.value()

        if value >= self.ui.cutin_frame_spb.value():
            self.ui.end_frame_spb.setValue(value)

    def get_maya_setting(self):

        self.render_layers, self.camera_list, \
            self.cutin_frame, self.cutout_frame, \
            self.resolution, self.renderer,\
            self.current_scene, self.version_name, \
            self.version_num, self.render_dir, \
            self.project_path, self.maya_version, self.ext_type = maya_handler.get_maya_setting()


        # set renderer
        self.ui.renderer_lb.setText(self.renderer)

        # set frame range
        self.ui.cutin_frame_spb.setValue(self.cutin_frame)
        self.ui.start_frame_spb.setValue(self.cutin_frame)
        self.ui.cutout_frame_spb.setValue(self.cutout_frame)
        self.ui.end_frame_spb.setValue(self.cutout_frame)

        # set resolution value
        self.ui.output_size_width_lb.setText(str(self.resolution[0]))
        self.ui.output_size_height_lb.setText(str(self.resolution[1]))

        # involving cams
        if len(self.camera_list) > 0:
            self.ui.cam_comboBox.addItems(self.camera_list)

        # config model
        self.render_layer_model = render_layer_model.RenderLayerModel(entries=self.render_layers, project_home=self.current_path)
        self.ui.render_layer_lv.setModel(self.render_layer_model)

    def summit_job(self):

        if self.get_renderable_layers():
            for render_layer in self.get_renderable_layers():

                item_dict = dict()

                if 'rs_' in render_layer:
                    item_dict['render_layer'] = render_layer.split('rs_')[1]
                else:
                    item_dict['render_layer'] = render_layer
                item_dict['ext_type'] = self.ext_type
                item_dict['maya_version'] = self.maya_version
                item_dict['current_scene'] = self.current_scene
                item_dict['project_path'] = self.project_path
                item_dict['cam'] = maya_handler.get_cam_longname(self.ui.cam_comboBox.currentText())
                item_dict['renderer'] = self.renderer
                item_dict['start_frame'] = self.ui.start_frame_spb.value()
                item_dict['end_frame'] = self.ui.end_frame_spb.value()
                item_dict['cutin_frame'] = self.ui.cutin_frame_spb.value()
                item_dict['cutout_frame'] = self.ui.cutout_frame_spb.value()
                item_dict['resolution_width'] = int(self.ui.output_size_width_lb.text())
                item_dict['resolution_height'] = int(self.ui.output_size_height_lb.text())
                item_dict['percentRes'] = self.ui.priority_spbox.value()
                item_dict['version_name'] = self.version_name
                item_dict['version_num'] = self.version_num
                item_dict['PROJECT'] = self.context.project.get('name')
                item_dict['ENTITY'] = self.context.entity.get('name')
                item_dict['USERNAME'] = self.context.user.get('name')
                item_dict['render_dir'] = self.render_dir

                if self.ui.OverWriteLatestVersionCheckBox.isChecked():
                    file_handler.copy_from_latest_version_file(item_dict)

                deadline_handler.render_summit(item_dict, priority=self.ui.priority_spbox.value())

    def get_renderable_layers(self):

        renderable_layers = list()
        for row in range(self.render_layer_model.rowCount(QtCore.QModelIndex)):

            index = self.render_layer_model.index(row)
            row_data = self.render_layer_model.data(index, role=QtCore.Qt.UserRole)
            if row_data._checked:
                renderable_layers.append(row_data.name)

        return renderable_layers

    def multiple_resolution(self):

        mult_val = self.ui.output_size_percent_spb.value() / 100

        mult_width = int(self.resolution[0] * mult_val)
        mult_height = int(self.resolution[1] * mult_val)

        self.ui.output_size_width_lb.setText(str(mult_width))
        self.ui.output_size_height_lb.setText(str(mult_height))


def maya_main_run():
    from maya import OpenMayaUI as mui
    from shiboken2 import wrapInstance
    mayaMainWindowPtr = mui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QMainWindow)

    global app
    app = QtWidgets.QApplication.instance()
    execute_main = JobMain(mayaMainWindow)
    execute_main.show()
    app.exec_()
