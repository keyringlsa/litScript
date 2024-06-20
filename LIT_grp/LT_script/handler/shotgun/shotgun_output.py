
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


    item = {'resolution' : found_projects[0].get('sg_sg_project_resolution'),
            'fps' : found_projects[0].get('sg_sg_project_fps'),
            'cut_in' : found_shots[0].get('sg_cut_in'),
            'cut_out' : found_shots[0].get('sg_cut_out')}

    return item


def shot_root():
    shot_root_info = []
    toolkit = sgtk.platform.current_engine()
    tk_context = toolkit.context



    templates = toolkit.sgtk.templates
    #template_names = templates.keys() 사용 가능한 템플릿 키 확인



    # 샷 경로
    shot_root_template = templates["shot_root"]

    fields = tk_context.as_template_fields(shot_root_template)

    #현재 컨텍스트에 대한 경로를 생성
    shot_root_path = shot_root_template.apply_fields(fields)

    # 'shot_root' 경로를 출력
    print("Shot root path:", shot_root_path)
    shot_root_info.append(shot_root_path)

    return shot_root_info


def sequence_root():
    sequence_root_info = []
    toolkit = sgtk.platform.current_engine()
    tk_context = toolkit.context



    templates = toolkit.sgtk.templates
    #template_names = templates.keys() 사용 가능한 템플릿 키 확인



    # 샷 경로
    sequence_root_template = templates["sequence_root"]

    fields = tk_context.as_template_fields(sequence_root_template)

    #현재 컨텍스트에 대한 경로를 생성
    sequence_root_path = sequence_root_template.apply_fields(fields)

    # 'shot_root' 경로를 출력
    print("sequence root path:", sequence_root_path)
    sequence_root_info.append(sequence_root_path)

    return sequence_root_info


