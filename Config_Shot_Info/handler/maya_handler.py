import maya.cmds as cmds






def set_frame_range(s_f, e_f):

    cmds.playbackOptions(minTime=s_f, maxTime=e_f, animationStartTime=s_f, animationEndTime=e_f)

def set_resolution(width, height):
    cmds.setAttr("defaultResolution.width", width)
    cmds.setAttr("defaultResolution.height", height)
    cmds.setAttr("defaultResolution.pixelAspect", 1)

def set_fps(fps):

    if fps == 24:
        cmds.currentUnit(time="film")
    elif fps == 30:
        cmds.currentUnit(time="ntsc")