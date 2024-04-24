def test():
    import os
    import json
    from pprint import pprint

    root_path = "Q:\\lt_team\\LT\\psoft_set\\DNF"
    file_path = os.path.join(root_path, "PencilLine_fighter.json").replace('\\', '/')

    with open(file_path, "r") as f:
        data = json.load(f)

    object_index = 0

    for node_id, node_data in data['LineNode'].items():
        node_name = node_data['NodeName']
        params_objects = node_data['Params'].get('Objects')
        if node_name and params_objects:
            for mesh_name in params_objects:
                mesh_part = mesh_name.split(':')
                sc_mesh = cmds.ls(type='mesh')

                for sc in sc_mesh:
                    sc_part = sc.split(":")
                    sc_rep = sc_part[-1].replace("Shape", "")

                    if sc_rep == mesh_part[-1]:
                        mesh_name_f = sc_part[0] + ":" + mesh_part[1]

                        try:

                            object_index += 1
                            cmds.connectAttr(mesh_name_f + ".message", f"{node_name}.objects[{object_index}]")

                        except Exception as e:
                            print(f"Error connecting attributes for node {node_name}: {e}")
                            # 오류 발생 시 패스
                            continue


test()



def test():
    import os
    import json
    from pprint import pprint

    root_path = "Q:\\lt_team\\LT\\psoft_set\\DNF"
    file_path = os.path.join(root_path, "PencilLine_fighter.json").replace('\\', '/')

    with open(file_path, "r") as f:
        data = json.load(f)

    object_index = 0

    for node_id, node_data in data['LineNode'].items():
        node_name = node_data['NodeName']
        params_objects = node_data['Params'].get('Objects')
        if node_name and params_objects:
            for mesh_name in params_objects:
                mesh_part = mesh_name.split(':')
                sc_mesh = cmds.ls(type='transform')

                for sc in sc_mesh:
                    sc_part = sc.split(":")
                    sc_rep = sc_part[-1].replace("Shape", "")


                    if mesh_part[-1] in sc_rep:

                        mesh_name_f = sc_part[0] + ":" + mesh_part[-1]

                        try:
                            object_index += 1
                            cmds.connectAttr(mesh_name_f + ".message", f"{node_name}.objects[{object_index}]")

                        except Exception as e:
                            print(f"Error connecting attributes for node {node_name}: {e}")
                            # 오류 발생 시 패스
                            continue


test()

import maya.cmds as cmds


def connect_material_to_faces():
    import os
    import json
    import maya.cmds as cmds

    root_path = "Q:\\lt_team\\LT\\psoft_set\\DNF"
    face_path = os.path.join(root_path, "set", "PencilLine_gunner_set.json").replace('\\', '/')
    sel = "gunner"

    with open(face_path, "r") as f:
        face_data = json.load(f)

    obj_names = cmds.ls(sel + "*:*__GEO", type='transform')

    if 'face' in face_data:

        face_list = face_data['face']

        for face in face_list:
            parts = face.split(':', 1)  # 첫번째 :만 스플릿하기
            face_name = parts[1]

            obj_name = obj_names[0].split(':')[0]

            shader_name = sel + "_remove_mtl"
            cmds.select(obj_name + ':' + face_name, r=True)
            cmds.hyperShade(assign=shader_name)


connect_material_to_faces()