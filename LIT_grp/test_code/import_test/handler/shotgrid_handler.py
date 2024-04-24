
from pprint import pprint

from CoreModules.handler import connect_sg



def get_category() :
    sgl = connect_sg.Shotgun_Connect()
    sg = sgl.default_script_auth()

    project = {'name': 'RFO', 'id': 254, 'type': 'Project'}  # context.project
    entity = {'name': 'RFP_0920', 'id': 1595, 'type': 'Shot'}  # context.entity

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



    pprint(asset_type_names)
    return asset_type_names

#def get_pub_datas(sg, context) :
def get_pub_datas() :
    sgl = connect_sg.Shotgun_Connect()
    sg = sgl.default_script_auth()


    project = {'name': 'RFO', 'id': 254, 'type': 'Project'} #context.project
    entity = {'name': 'RFP_0920', 'id': 1595, 'type': 'Shot'} #context.entity

    requires_fields = sg.schema_field_read('PublishedFile')
    filters = [
        ['project', 'is', project],
        ['entity', 'is', entity],
        {
            "filter_operator": "any",
            "filters": [
                ["published_file_type", "is", {"type": "PublishedFileType", "id": 35}],
                ["published_file_type", "is", {"type": "PublishedFileType", "id": 3}],
                ["published_file_type", "is", {"type": "PublishedFileType", "id": 36}],
            ]
        }
    ]

    sg_found = sg.find('PublishedFile',
                       filters=filters,
                       fields=list(requires_fields.keys()))



    data_dict = dict()

    for pub in sg_found:
        pub_name = pub['name']
        pub_type = pub['published_file_type']

        if pub_name not in data_dict:
            data_dict[pub_name] = {"items": [pub], "type": pub_type}

        else:
            data_dict[pub_name]["items"].append(pub)

    pprint(data_dict)

    return data_dict




