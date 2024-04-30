import re, os, sys
import sgtk

from CoreModules.handler import connect_sg

def get_context():
    current_engine = sgtk.platform.current_engine()
    context = current_engine.context

    return context


def get_entity(entity=None, sg=None):

    if not sg:
        sgl = connect_sg.Shotgun_Connect()
        sg = sgl.default_script_auth()

    TYPE = entity.get("type")
    fields = sg.schema_field_read(TYPE)

    filters = [
        ["id", "is", entity.get("id")],
    ]

    entity = sg.find_one(TYPE,
                        filters=filters,
                        fields=list(fields.keys()))

    return entity

def get_workspace(context, scene_path, dcc, sg):
    """
    parameter:
        scene_path: dcc scene file path, ex) P:/keyring/assets/Character/belato/MDL/wip/maya/scenes/belato_MDL_main_v027.mb
        dcc: ex) maya, nuke, houdini

    return:
        version, path info dict
    """

    entity = get_entity(entity=context.entity, sg=sg)
    workspace = scene_path.rsplit("wip", 1)[0]
    wip_path = f"{workspace}wip/{dcc}"
    pub_path = f"{workspace}pub/{dcc}"
    path, file_name = os.path.split(scene_path)
    raw_name, ext = os.path.splitext(file_name)
    version_name = raw_name.split('_')[2]

    matches = re.findall(r'v\d{3}', raw_name)
    if matches:
        version_num = int(matches[0][1:])
    else:
        version_num = 0

    data = dict()
    data["workspace"] = workspace
    data["wip_path"] = wip_path
    data["pub_path"] = pub_path
    data["raw_name"] = raw_name
    data["version_name"] = version_name
    data["version_num"] = version_num
    data["entity"] = entity
    data["context"] = context


    return data