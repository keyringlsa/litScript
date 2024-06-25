
import sys

require_paths = [
    "P:/TD/maya/2024/packages/Lib/site-packages",
    "P:/config/STUDIO/install/core/python",
    "P:/TD/maya/2022/inhousetools"
]
for i in require_paths:
    sys.path.append(i)

#import os, yaml, unreal
import os, yaml
from pprint import pprint
import sgtk
from CoreModules.handler import connect_sg


def get_category() :
    sgl = connect_sg.Shotgun_Connect()
    sg = sgl.default_script_auth()

    #project = context.project
    #entity = context.entity
    project = {'type': 'Project', 'id': 749, 'name': 'DNFA'} # context.project
    #entity = {'name': 'DNF45_0140', 'id': 3035, 'type': 'Shot'}  # context.entity

    requires_fields = sg.schema_field_read("Asset")


    found_pub_files = sg.find("Asset",
                              filters=[
                                  ['project', 'is', project],
                                  ['sg_published_files', 'is_not', None],
                              ],
                              fields=list(requires_fields.keys()),
                              filter_operator='and')

    # 'sg_asset_type'의 타입 및 그룹화

    asset_type_names = {}
    for asset in found_pub_files:
        asset_type = asset.get('sg_asset_type')
        asset_name = asset.get('cached_display_name')
        if asset_type:
            if asset_type not in asset_type_names:
                asset_type_names[asset_type] = {'type': asset_type, 'name': []}
            asset_type_names[asset_type]['name'].append(asset_name)

    pprint(asset_type_names)

    return asset_type_names


get_category()



def get_pub_datas() :
    sgl = connect_sg.Shotgun_Connect()
    sg = sgl.default_script_auth()

    toolkit = sgtk.platform.current_engine()

    project = {'type': 'Project', 'id': 749, 'name': 'DNFA'}

    requires_fields = sg.schema_field_read('PublishedFile')
    filters = [
        ['project', 'is', project],
        #['entity', 'name_is', asset_name],
        {
            "filter_operator": "any",
            "filters": [
                ['task', 'name_is', 'lookdev'],
                ['task', 'name_is', 'lkd'],
                ['task', 'name_is', 'mdl'],
                ['task', 'name_is', 'model'],
            ]
        },
        ["published_file_type", "is", {"type": "PublishedFileType", "id": 265}]
    ]

    sg_found = sg.find('PublishedFile',
                       filters=filters,
                       fields=list(requires_fields.keys()))

    #
    fbx_dict = dict()

    for fbx in sg_found:
        file_path = fbx.get('path').get('local_path')

        if 'fbx' in file_path:
            fbx_name = fbx['name']
            fbx_type = fbx['published_file_type']

            if fbx_name not in fbx_dict:
                fbx_dict[fbx_name] = {"items": [fbx], "type": fbx_type, "task": {"name": "Motion Builder FBX"}}

    pprint(fbx_dict)

    return fbx_dict


get_pub_datas()




def get_published_shd_file(asset_name):
    sgl = connect_sg.Shotgun_Connect()
    sg = sgl.default_script_auth()

    toolkit = sgtk.platform.current_engine()

    project = {'type': 'Project', 'id': 749, 'name': 'DNFA'}



    requires_fields = sg.schema_field_read('PublishedFile')
    filters = [
        ['project', 'is', project],
        ['entity', 'name_is', asset_name],
        {
            "filter_operator": "any",
            "filters":[
                ['task', 'name_is', 'lookdev'],
                ['task', 'name_is', 'lkd'],
                ['task', 'name_is', 'mdl'],
                ['task', 'name_is', 'model'],
            ]
        },
        ['published_file_type', 'is', {'id': 35, 'name': 'Yml File', 'type': 'PublishedFileType'}]
    ]

    sg_found = sg.find('PublishedFile',
                       filters=filters,
                       fields=list(requires_fields.keys()))

    # filtered not shade yaml files
    filtering_shade_yaml_files = list()

    for pub in sg_found:
        file_path = pub.get('path').get('local_path')

        if 'shade' in file_path:
            filtering_shade_yaml_files.append(pub)

    return filtering_shade_yaml_files