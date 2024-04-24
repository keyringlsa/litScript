
from CoreModules.handler.connect_sg import Shotgun_Connect
import sgtk
from pprint import pprint

def shot_info() :
    sgl = Shotgun_Connect()
    sg = sgl.default_script_auth()


    toolkit = sgtk.platform.current_engine()
    tk_contxt = toolkit.context
    tk_project = tk_contxt.project
    tk_shot = tk_contxt.entity


    project = 'Project'
    shot = 'Shot'
    project_fields = sg.schema_field_read(project)
    shot_fields = sg.schema_field_read(shot)

    project_id = tk_project.get('id')
    shot_id = tk_shot.get('id')


    found_projects = sg.find(project,
                            filters=[
                                ["id", "is", project_id]
                            ],
                            fields=list(project_fields.keys()))


    found_shots = sg.find(shot,
                            filters=[
                                ["id", "is", shot_id]
                            ],
                            fields=list(shot_fields.keys()))



    pprint(found_projects[0].get('sg_sg_project_resolution'))
    pprint(found_projects[0].get('sg_sg_project_fps'))
    pprint(found_shots[0].get('sg_cut_in'))
    pprint(found_shots[0].get('sg_cut_out'))


