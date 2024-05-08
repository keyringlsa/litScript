
from pprint import pprint
import webbrowser

def get_published_files(sg=None, context=None):

    project = context.project
    entity = context.entity

    requires_fields = sg.schema_field_read('PublishedFile')
    filters = [
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

    sg_found = sg.find('PublishedFile',
                       filters=filters,
                       fields=list(requires_fields.keys()))

    # pprint(sg_found)

    data_dict = dict()

    for pub in sg_found:
        pub_name = pub['name']
        pub_type = pub['published_file_type']

        if pub_name not in data_dict:
            data_dict[pub_name] = {"items": [pub], "type": pub_type}

        else:
            data_dict[pub_name]["items"].append(pub)

    # pprint(data_dict)

    return data_dict

def get_published_shd_file(sg=None, context=None, asset_name=None):

    project = context.project

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

def get_shotgun_page_id(sg=None, project=None):

    fields = ['name', 'project']
    filters = [
        ['name', 'is', 'Shots'],
        ['project', 'is', project],
    ]

    page = sg.find_one('Page',
                       filters=filters,
                       fields=fields)
    page_id = page.get('id')

    return page_id

def open_shot_url(sg=None, context=None):

    page_id = get_shotgun_page_id(sg=sg, project=context.project)
    shot_id = context.entity.get("id")

    sg_url = f"https://keyring-studio.shotgrid.autodesk.com/page/{page_id}#Shot_{shot_id}"
    webbrowser.open(sg_url)

    return sg_url