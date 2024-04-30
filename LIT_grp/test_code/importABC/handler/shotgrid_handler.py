
from pprint import pprint

from CoreModules.handler import connect_sg



def get_category() :
    sgl = connect_sg.Shotgun_Connect()
    sg = sgl.default_script_auth()

    project = {'name': 'DNF45', 'id': 519, 'type': 'Project'}  # context.project
    entity = {'name': 'DNF45_0140', 'id': 3035, 'type': 'Shot'}  # context.entity

    requires_fields = sg.schema_field_read("Asset")
    # pprint(requires_fields)

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



    return asset_type_names


#get_category()
#def get_pub_datas(sg, context) :
def get_pub_datas() :
    sgl = connect_sg.Shotgun_Connect()
    sg = sgl.default_script_auth()


    project = {'name': 'DNF45', 'id': 519, 'type': 'Project'} #context.project
    entity = {'name': 'DNF45_0140', 'id': 3035, 'type': 'Shot'} #context.entity

    requires_fields = sg.schema_field_read('PublishedFile')
    cfx_filters = [
        ['project', 'is', project],
        ['entity', 'is', entity],
        ['task', 'name_is', "cfx"],
        #['task', 'name_is', "anim"],
        {
            "filter_operator": "any",
            "filters": [
                ["published_file_type", "is", {"type": "PublishedFileType", "id": 35}],
                ["published_file_type", "is", {"type": "PublishedFileType", "id": 3}],
                ["published_file_type", "is", {"type": "PublishedFileType", "id": 36}],
            ]
        }
    ]

    anim_filters = [
        ['project', 'is', project],
        ['entity', 'is', entity],
        ['task', 'name_is', "anim"],

        {
            "filter_operator": "any",
            "filters": [
                ["published_file_type", "is", {"type": "PublishedFileType", "id": 35}],
                ["published_file_type", "is", {"type": "PublishedFileType", "id": 3}],
                ["published_file_type", "is", {"type": "PublishedFileType", "id": 36}],
            ]
        }
    ]

    cfx_found = sg.find('PublishedFile',
                       filters=cfx_filters,
                       fields=list(requires_fields.keys()))

    anim_found = sg.find('PublishedFile',
                       filters=anim_filters,
                       fields=list(requires_fields.keys()))

    #pprint(anim_found)
    cfx_dict = dict()
    anim_dict = dict()


    for cfx in cfx_found:
        cfx_name = cfx['name']
        cfx_type = cfx['published_file_type']


        if cfx_name not in cfx_dict:
            cfx_dict[cfx_name] = {"items": [cfx], "type": cfx_type, "task":{"name":"cfx"}}

        else:
            cfx_dict[cfx_name]["items"].append(cfx)

    for anim in anim_found:
        anim_name = anim['name']
        anim_type = anim['published_file_type']



        if anim_name not in anim_dict:
            anim_dict[anim_name] = {"items": [anim], "type": anim_type, "task":{"name":"anim"}}

        else:
            anim_dict[anim_name]["items"].append(anim)

    cfx_dict.update(anim_dict)

    return cfx_dict

get_pub_datas()



