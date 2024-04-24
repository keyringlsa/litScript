
from CoreModules.handler.connect_sg import Shotgun_Connect
import sgtk
from LIT_grp.LT_script.handler.shotgun import shotgun_output
from pprint import pprint

def shot_info() :
    sgl = Shotgun_Connect()
    sg = sgl.default_script_auth()


    toolkit = sgtk.platform.current_engine()
    tk_contxt = toolkit.context
    tk_project = tk_contxt.project
    tk_shot = tk_contxt.entity


    project = 'Project'
    shot = 'Shot'
    project_fields = sg.schema_field_read(project)
    shot_fields = sg.schema_field_read(shot)

    project_id = tk_project.get('id')
    shot_id = tk_shot.get('id')


    found_projects = sg.find(project,
                            filters=[
                                ["id", "is", project_id]
                            ],
                            fields=list(project_fields.keys()))


    found_shots = sg.find(shot,
                            filters=[
                                ["id", "is", shot_id]
                            ],
                            fields=list(shot_fields.keys()))


    item = {'resolution' : found_projects[0].get('sg_sg_project_resolution'),
            'fps' : found_projects[0].get('sg_sg_project_fps'),
            'cut_in' : found_shots[0].get('sg_cut_in'),
            'cut_out' : found_shots[0].get('sg_cut_out')}

    return item
def output_sa():
    import maya.cmds as cmds
    item = shotgun_output.shot_info()
    if item.get('resolution') is not None:
        width = item.get('resolution').split('*')[0]
        height = item.get('resolution').split('*')[-1]

        set_resolution(width, height)

    if item.get('fps') is not None:
        fps = item.get('fps')

        set_fps(fps)

    if item.get('cut_in') is not None :
        cut_in = item.get('cut_in')
        cut_out = item.get('cut_out')
        set_frame_range(cut_in, cut_out)



    cmds.setAttr('defaultRenderGlobals.imageFilePrefix', '<Scene>/<RenderLayer>/<RenderLayer>', type='string')
    cmds.setAttr('defaultArnoldDriver.ai_translator', 'exr', type='string')
    cmds.setAttr('defaultArnoldDriver.halfPrecision',0)
    cmds.setAttr('defaultArnoldDriver.preserveLayerName',0)
    cmds.setAttr('defaultArnoldDriver.exrTiled',1)
    cmds.setAttr('defaultArnoldDriver.multipart',0)
    cmds.setAttr('defaultArnoldDriver.autocrop',1)
    cmds.setAttr('defaultArnoldDriver.append',0)
    cmds.setAttr('defaultArnoldDriver.mergeAOVs', 1)
    cmds.setAttr('defaultRenderGlobals.outFormatControl', 0)
    cmds.setAttr('defaultRenderGlobals.animation', 1)
    cmds.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
    cmds.setAttr('defaultRenderGlobals.extensionPadding', 4)
    cmds.setAttr('defaultRenderGlobals.periodInExt', 1)
    cmds.setAttr('defaultArnoldRenderOptions.autotx', 0)
    cmds.setAttr('defaultArnoldRenderOptions.textureAcceptUnmipped', 1) \

    start = cmds.playbackOptions(q=True, min=True)
    end = cmds.playbackOptions(q=True, max=True)

    cmds.setAttr('defaultRenderGlobals.startFrame', start)
    cmds.setAttr('defaultRenderGlobals.endFrame', end)


def output_jh():
    import maya.cmds as cmds
    item = shotgun_output.shot_info()
    if item.get('resolution') is not None:
        width = item.get('resolution').split('*')[0]
        height = item.get('resolution').split('*')[-1]

        set_resolution(width, height)

    if item.get('fps') is not None:
        fps = item.get('fps')

        set_fps(fps)

    if item.get('cut_in') is not None:
        cut_in = item.get('cut_in')
        cut_out = item.get('cut_out')
        set_frame_range(cut_in, cut_out)

    cmds.setAttr('defaultRenderGlobals.imageFilePrefix', '<Scene>/<RenderLayer>/<RenderLayer>', type='string')
    cmds.setAttr('defaultArnoldDriver.ai_translator', 'exr', type='string')
    cmds.setAttr('defaultArnoldDriver.halfPrecision', 1)
    cmds.setAttr('defaultArnoldDriver.preserveLayerName', 0)
    cmds.setAttr('defaultArnoldDriver.exrTiled', 0)
    cmds.setAttr('defaultArnoldDriver.multipart', 0)
    cmds.setAttr('defaultArnoldDriver.autocrop', 1)
    cmds.setAttr('defaultArnoldDriver.append', 0)
    cmds.setAttr('defaultArnoldDriver.mergeAOVs', 1)
    cmds.setAttr('defaultRenderGlobals.outFormatControl', 0)
    cmds.setAttr('defaultRenderGlobals.animation', 1)
    cmds.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
    cmds.setAttr('defaultRenderGlobals.extensionPadding', 4)
    cmds.setAttr('defaultRenderGlobals.periodInExt', 1)
    cmds.setAttr('defaultArnoldRenderOptions.autotx', 0)
    cmds.setAttr("defaultArnoldRenderOptions.autotile", 1)
    cmds.setAttr('defaultArnoldRenderOptions.textureAcceptUnmipped', 0)
    cmds.setAttr('defaultArnoldRenderOptions.textureMaxMemoryMB', 4096000.000)


    start = cmds.playbackOptions(q=True, min=True)
    end = cmds.playbackOptions(q=True, max=True)

    cmds.setAttr('defaultRenderGlobals.startFrame', start)
    cmds.setAttr('defaultRenderGlobals.endFrame', end)


def output_w():
    import maya.cmds as cmds
    import os, sys

    item = shotgun_output.shot_info()
    if item.get('resolution') is not None:
        width = item.get('resolution').split('*')[0]
        height = item.get('resolution').split('*')[-1]

        set_resolution(width, height)

    if item.get('fps') is not None:
        fps = item.get('fps')

        set_fps(fps)

    if item.get('cut_in') is not None:
        cut_in = item.get('cut_in')
        cut_out = item.get('cut_out')
        set_frame_range(cut_in, cut_out)

    file_dir = cmds.file(q=True, sceneName=True)
    # file_dir = os.path.realpath(file)
    real_root = os.path.join(file_dir.replace('P:', 'W:').rsplit('scenes', 1)[0], 'images').replace("\\", "/")
    cmds.setAttr('defaultRenderGlobals.imageFilePrefix', real_root + '/<Scene>/<RenderLayer>/<RenderLayer>',
                 type='string')

    cmds.setAttr('defaultArnoldDriver.ai_translator', 'exr', type='string')
    cmds.setAttr('defaultArnoldDriver.halfPrecision', 1)
    cmds.setAttr('defaultArnoldDriver.preserveLayerName', 0)
    cmds.setAttr('defaultArnoldDriver.exrTiled', 0)
    cmds.setAttr('defaultArnoldDriver.multipart', 0)
    cmds.setAttr('defaultArnoldDriver.autocrop', 1)
    cmds.setAttr('defaultArnoldDriver.append', 0)
    cmds.setAttr('defaultArnoldDriver.mergeAOVs', 1)
    cmds.setAttr('defaultRenderGlobals.outFormatControl', 0)
    cmds.setAttr('defaultRenderGlobals.animation', 1)
    cmds.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
    cmds.setAttr('defaultRenderGlobals.extensionPadding', 4)
    cmds.setAttr('defaultRenderGlobals.periodInExt', 1)
    cmds.setAttr('defaultArnoldRenderOptions.autotx', 0)
    cmds.setAttr("defaultArnoldRenderOptions.autotile", 1)
    cmds.setAttr('defaultArnoldRenderOptions.textureAcceptUnmipped', 0)
    cmds.setAttr('defaultArnoldRenderOptions.textureMaxMemoryMB', 4096000.000)

    start = cmds.playbackOptions(q=True, min=True)
    end = cmds.playbackOptions(q=True, max=True)

    cmds.setAttr('defaultRenderGlobals.startFrame', start)
    cmds.setAttr('defaultRenderGlobals.endFrame', end)



def output_deep():
    import maya.cmds as cmds
    cmds.setAttr('defaultRenderGlobals.imageFilePrefix', '<Scene>/<RenderLayer>/<RenderLayer>', type='string')
    cmds.setAttr('defaultArnoldDriver.ai_translator', 'deepexr', type='string')
    cmds.setAttr('defaultArnoldRenderOptions.aovMode', 0)
    cmds.setAttr('defaultArnoldRenderOptions.ignoreLights', 1)
    cmds.setAttr('defaultArnoldRenderOptions.ignoreShadows', 1)




#######################################################

def set_frame_range(cut_in, cut_out):
    import maya.cmds as cmds
    cmds.playbackOptions(minTime=cut_in, maxTime=cut_out, animationStartTime=cut_in, animationEndTime=cut_out)

def set_resolution(width, height):
    import maya.cmds as cmds
    cmds.setAttr("defaultResolution.width", int(width))
    cmds.setAttr("defaultResolution.height", int(height))
    cmds.setAttr("defaultResolution.pixelAspect", 1)

def set_fps(fps):
    import maya.cmds as cmds
    if int(fps) == 24:
        cmds.currentUnit(time="film")
    elif int(fps) == 30:
        cmds.currentUnit(time="ntsc")


######################## sampling ##########################

def sam_low():
    import maya.cmds as cmds
    cmds.setAttr('defaultArnoldRenderOptions.AASamples', 3)

    cmds.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', 2)

    cmds.setAttr('defaultArnoldRenderOptions.GISpecularSamples', 2)

    cmds.setAttr('defaultArnoldRenderOptions.GITransmissionSamples', 2)

    cmds.setAttr('defaultArnoldRenderOptions.GISssSamples', 2)

    cmds.setAttr('defaultArnoldRenderOptions.GIVolumeSamples', 0)

    cmds.setAttr("defaultArnoldRenderOptions.autotx", 0)

    cmds.setAttr("defaultArnoldRenderOptions.motion_blur_enable", 0)

    cmds.setAttr("defaultArnoldRenderOptions.outputVarianceAOVs", 1)


def sam_middle():
    import maya.cmds as cmds
    cmds.setAttr('defaultArnoldRenderOptions.AASamples', 6)

    cmds.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', 3)

    cmds.setAttr('defaultArnoldRenderOptions.GISpecularSamples', 3)

    cmds.setAttr('defaultArnoldRenderOptions.GITransmissionSamples', 2)

    cmds.setAttr('defaultArnoldRenderOptions.GISssSamples', 3)

    cmds.setAttr('defaultArnoldRenderOptions.GIVolumeSamples', 0)

    cmds.setAttr("defaultArnoldRenderOptions.autotx", 0)

    cmds.setAttr("defaultArnoldRenderOptions.motion_blur_enable", 1)
    cmds.setAttr("defaultArnoldRenderOptions.ignoreMotionBlur", 1)
    cmds.setAttr("defaultArnoldRenderOptions.mb_object_deform_enable", 1)
    cmds.setAttr("defaultArnoldRenderOptions.mb_camera_enable", 1)
    cmds.setAttr("defaultArnoldRenderOptions.range_type", 0)
    cmds.setAttr("defaultArnoldRenderOptions.outputVarianceAOVs", 1)



def sam_high():
    import maya.cmds as cmds
    cmds.setAttr('defaultArnoldRenderOptions.AASamples', 8)

    cmds.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', 3)

    cmds.setAttr('defaultArnoldRenderOptions.GISpecularSamples', 3)

    cmds.setAttr('defaultArnoldRenderOptions.GITransmissionSamples', 3)

    cmds.setAttr('defaultArnoldRenderOptions.GISssSamples', 3)

    cmds.setAttr('defaultArnoldRenderOptions.GIVolumeSamples', 0)

    cmds.setAttr("defaultArnoldRenderOptions.autotx", 0)

    cmds.setAttr("defaultArnoldRenderOptions.motion_blur_enable", 1)
    cmds.setAttr("defaultArnoldRenderOptions.ignoreMotionBlur", 1)
    cmds.setAttr("defaultArnoldRenderOptions.mb_object_deform_enable", 1)
    cmds.setAttr("defaultArnoldRenderOptions.mb_camera_enable", 1)
    cmds.setAttr("defaultArnoldRenderOptions.range_type", 0)

    cmds.setAttr("defaultArnoldRenderOptions.outputVarianceAOVs", 1)



def sam_vol():
    import maya.cmds as cmds
    cmds.setAttr('defaultArnoldRenderOptions.AASamples', 6)

    cmds.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', 0)

    cmds.setAttr('defaultArnoldRenderOptions.GISpecularSamples', 0)

    cmds.setAttr('defaultArnoldRenderOptions.GITransmissionSamples', 0)

    cmds.setAttr('defaultArnoldRenderOptions.GISssSamples', 0)

    cmds.setAttr('defaultArnoldRenderOptions.GIVolumeSamples', 3)

    cmds.setAttr("defaultArnoldRenderOptions.autotx", 0)

    cmds.setAttr("defaultArnoldRenderOptions.outputVarianceAOVs", 1)



def filckr():
    import maya.cmds as cmds
    cmds.setAttr("defaultArnoldRenderOptions.use_sample_clamp", 1)
    cmds.setAttr("defaultArnoldRenderOptions.AASampleClamp", 2)