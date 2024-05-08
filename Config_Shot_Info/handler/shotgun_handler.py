
from pprint import pprint

def get_info_from_shotgrid(sg=None, context=None):

    project_context = context.project
    shot_context = context.entity

    project_fields = sg.schema_field_read('Project')
    shot_fields = sg.schema_field_read('Shot')

    project_entity = sg.find_one('Project',
                                 filters=[
                                     ['id', 'is', project_context.get('id')]
                                 ],
                                 fields=list(project_fields.keys()))
    shot_entity = sg.find_one('Shot',
                              filters=[
                                  ['id', 'is', shot_context.get('id')]
                              ],
                              fields=list(shot_fields.keys()))

    project_resolution = project_entity.get('sg_sg_project_resolution')
    project_fps = project_entity.get('sg_sg_project_fps')
    cut_in_frame = shot_entity.get('sg_cut_in')
    cut_out_frame = shot_entity.get('sg_cut_out')

    item = {
        'project_resolution': project_resolution,
        'project_fps': project_fps,
        'cut_in_frame': cut_in_frame,
        'cut_out_frame': cut_out_frame
    }

    return item