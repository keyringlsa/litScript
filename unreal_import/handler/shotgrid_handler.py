
import sys

require_paths = [
    "P:/TD/maya/2024/packages/Lib/site-packages",
    "P:/config/STUDIO/install/core/python",
    "P:/TD/maya/2022/inhousetools"
]
for i in require_paths:
    sys.path.append(i)


from CoreModules.handler import connect_sg

def get_category(sg=None, project=None) :


    requires_fields = sg.schema_field_read("Asset")


    found_pub_files = sg.find("Asset",
                              filters=[
                                  ['project', 'is', project],
                                  ['sg_published_files', 'is_not', None],
                              ],
                              fields=list(requires_fields.keys()),
                              filter_operator='and')



    asset_type_names = {}
    for asset in found_pub_files:
        asset_type = asset.get('sg_asset_type')
        asset_name = asset.get('cached_display_name')
        if asset_type:
            if asset_type not in asset_type_names:
                asset_type_names[asset_type] = {'type': asset_type, 'name': []}
            asset_type_names[asset_type]['name'].append(asset_name)



    return asset_type_names




def get_pub_datas(sg=None, project=None) :


    requires_fields = sg.schema_field_read('PublishedFile')
    filters = [
        ['project', 'is', project],

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


    return fbx_dict






def get_published_shd_file(sg=None, project=None, asset_name=None):




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


    filtering_shade_yaml_files = list()

    for pub in sg_found:
        file_path = pub.get('path').get('local_path')

        if 'shade' in file_path:
            filtering_shade_yaml_files.append(pub)

    return filtering_shade_yaml_files