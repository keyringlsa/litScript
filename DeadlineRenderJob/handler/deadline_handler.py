import os
import Deadline.DeadlineConnect as Connect

from pprint import pprint


CONN = Connect.DeadlineCon('http://192.168.0.200', 8081)

def render_summit(item_dict, priority=50):

    short_name = item_dict['version_name']

    if not os.path.isdir(item_dict['render_dir']):
        os.makedirs(item_dict['render_dir'])

    JOB_NAME = f"[Maya] {short_name} {item_dict['render_layer']} Rendering {item_dict['start_frame']} to {item_dict['end_frame']}"
    BATCH_NAME = f"[{item_dict['PROJECT']}]{short_name} Rendering With Maya {item_dict['renderer']}"

    JobInfo = {
        "Name": JOB_NAME,
        "BatchName": BATCH_NAME,
        "Plugin": "MayaBatch",
        "Pool": f"maya{item_dict['maya_version']}",
        "UserName": os.environ['USERNAME'],
        "Frames": f"{item_dict['start_frame']}-{item_dict['end_frame']}",
        "OutputDirectory0": item_dict['render_dir'],
        "OutputFilename0": f"{item_dict['render_layer']}.####.{item_dict['ext_type']}",
        "Priority": priority
    }
    PluginInfo = {
        "Animation": 1,
        "ArnoldVerbose": 2,
        "Build": '64bit',
        "Camera": item_dict['cam'],
        "CountRenderableCameras": 0,
        "EnableOpenColorIO": 1,
        "FrameNumberOffset": 0,
        "IgnoreError211": 0,
        "ImageHeight": item_dict['resolution_height'],
        "ImageWidth": item_dict['resolution_width'],
        "LocalRendering": 0,
        "MaxProcessors": 0,
        "MayaToArnoldVersion": 5,
        "OCIOConfigFile": "<MAYA_RESOURCES>/OCIO-configs/Maya2022-default/config.ocio",
        "OutputFilePath": item_dict['render_dir'],
        "ProjectPath": item_dict['project_path'],
        "RenderHalfFrames": 0,
        "RenderLayer": item_dict['render_layer'],
        "RenderSetupIncludeLights": 1,
        "Renderer": item_dict['renderer'],
        "SceneFile": item_dict['current_scene'],
        "StrictErrorChecking": 1,
        "UseLegacyRenderLayers": 0,
        "UseLocalAssetCaching": 0,
        "UsingRenderLayers": 1,
        "Version": item_dict['maya_version'],
    }

    # print(CMD_ARG)
    try:
        new_job = CONN.Jobs.SubmitJob(JobInfo, PluginInfo)
        print("Job created with id {}".format(new_job['_id']))
        # return new_job
    except:
        print("Submission failed")
        # return None


