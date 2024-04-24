

import os, sys
from glob import glob
import re
import maya.cmds as cmds
from pprint import pprint


def project_data(pro_type):


    file_dir = "Q:\\lt_team\\LT\\psoft_set"

    root_path = os.path.join(file_dir,pro_type).replace('\\', '/')

    items = os.listdir(root_path)

    row_datas = list()

    for item in items:
        item_a = item.replace('PencilLine_', '')
        item_b=item_a.replace('.json', '')
        row_data = dict()


        row_data['name'] = item_b

        row_datas.append(row_data)

    return row_datas


def psoft_imp():
    import maya.cmds as cmds
    import Pcl4Bridge.ImportJson_maya






    existPencilLineSet = False
    if "PencilLine" in cmds.ls(set=True):
        existPencilLineSet = True
    else:
        cmds.createNode("PencilLine")
        sets = cmds.sets(name="PencilLine")
        if sets == "PencilLine":
            existPencilLineSet = True
        else:
            cmds.delete(sets)



    Pcl4Bridge.ImportJson_maya.importWithFileDialog()



def psoft_set(sel,pro_type):
    import maya.cmds as cmds
    import Pcl4Bridge.ImportJson_maya
    import json




    file_dir = "Q:\\lt_team\\LT\\psoft_set"
    root_path = os.path.join(file_dir, pro_type).replace('\\', '/')

    #펜슬라인 json 불러오기
    file_path = os.path.join(root_path, "PencilLine_"+sel+".json").replace('\\', '/')

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


    #페이스 어싸인 json 불러오기
    face_path = os.path.join(root_path,"set", "PencilLine_" + sel + "_set.json").replace('\\', '/')
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


#
# import maya.cmds as cmds
# import json
# 셋파일 내보내는 거인데 일단 넣어둠
# def get_face_indices(set_name):
#     members_indices = cmds.sets(set_name, q=True)
#
#     face_idx = []
#     for idx in members_indices:
#         face_idx.append(idx)
#     face_info = {"name": set_name, "face": face_idx}
#
#     print(face_info)
#
#     export_path = r"Q:\lt_team\LT\psoft_set\DNF\set\PencilLine_mage_set.json"
#
#     with open(export_path, "w") as f:
#         json.dump(face_info, f)
#
#
# get_face_indices("remove_set")
