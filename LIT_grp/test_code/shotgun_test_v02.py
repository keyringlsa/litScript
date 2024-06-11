

from pprint import pprint
from CoreModules.handler import connect_sg


def get_list():
    sgl = connect_sg.Shotgun_Connect()
    sg = sgl.default_script_auth()

    entity_list = sg.schema_entity_read()


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


    pprint(found_projects)

get_list()