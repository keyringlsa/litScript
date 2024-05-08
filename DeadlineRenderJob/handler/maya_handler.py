import os, sys
import re
import maya.cmds as cmds
import maya.mel as mel



def get_default_cameras():

    cameras = cmds.ls(type='camera')
    none_default_cameras = []
    for _camera in cameras:
        if not cmds.camera(_camera, query=True, startupCamera=True):
            cam_tf = cmds.listRelatives(_camera, p=True)[0]
            none_default_cameras.append(cam_tf)
    return none_default_cameras

def get_maya_setting():
    current_scene = cmds.file(q=True, sn=True)
    version_name, ext = os.path.splitext(current_scene.rsplit('/', 1)[-1])
    project_directory = cmds.workspace(q=True, rd=True)[:-1]
    maya_version = cmds.about(version=True)
    ext_type = mel.eval("getImfImageType()")

    pattern = r'v\d{3}'
    version_num = int(re.findall(pattern, version_name)[0][1:])
    render_dir = current_scene.split('scenes')[0] + "images"
    current_render = cmds.getAttr("defaultRenderGlobals.currentRenderer")
    render_layer_dict = [{'name': layer, 'render': cmds.getAttr('{0}.renderable'.format(layer))} for layer in
                         cmds.ls(type='renderLayer') if ':' not in layer]
    cams_list = get_default_cameras()
    s_frame, e_frame = int(cmds.playbackOptions(q=True, min=True)), int(cmds.playbackOptions(q=True, max=True))

    width, height = cmds.getAttr("defaultResolution.width"), cmds.getAttr("defaultResolution.height")

    return render_layer_dict, cams_list, s_frame, e_frame, \
        (width, height), current_render, current_scene, \
        version_name, version_num, render_dir, project_directory, \
        maya_version, ext_type

def get_cam_longname(cam):

    long_name = cmds.ls(cam, l=True)

    if long_name:
        return long_name[0]
    else:
        return '|persp'
