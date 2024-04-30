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


def set_model(self):
    cate_items = shotgrid_handler.get_category()
    pub_items = shotgrid_handler.get_pub_datas()

    self.items = pub_model.ItemTreeModel(row_datas=pub_items, head_items=cate_items)
    self.import_proxy_model = QtCore.QSortFilterProxyModel(self)
    self.import_proxy_model.setSourceModel(self.items)
    self.ui.publist.setModel(self.import_proxy_model)

    # 모든 트리 아이템 확장
    self.ui.publist.expandAll()

    # 컬럼 크기 조정
    for i in range(self.ui.publist.header().count()):
        self.ui.publist.resizeColumnToContents(i)

    # 프록시 모델을 반복하여 콤보 상자와 버튼에 대한 편집기 열기
    for i in range(self.import_proxy_model.rowCount()):
        parent_index = self.import_proxy_model.index(i, 0)
        parent_item = parent_index.data(QtCore.Qt.UserRole)

        if parent_item.name == "ALEMBIC":
            # 'ALEMBIC' 부모 아래의 모든 하위 아이템에 대해 반복
            for p_i in range(self.import_proxy_model.rowCount(parent_index)):
                # 각 하위 아이템의 인덱스 가져오기
                child_index = self.import_proxy_model.index(p_i, 0, parent_index)
                child_item = child_index.data(QtCore.Qt.UserRole)

                # 각 하위 아이템의 콤보 상자와 버튼 열기
                combo_index = self.import_proxy_model.index(p_i, 5, child_index)
                button_index = self.import_proxy_model.index(p_i, 6, child_index)

                # 콤보 상자와 버튼의 편집기를 올바른 인덱스로 열기
                self.ui.publist.openPersistentEditor(combo_index)
                self.ui.publist.openPersistentEditor(button_index)
        else:
            # 'ALEMBIC'이 아닌 다른 부모의 콤보 상자와 버튼 열기
            combo_index = self.import_proxy_model.index(i, 5, parent_index)
            button_index = self.import_proxy_model.index(i, 6, parent_index)

            # 올바른 인덱스로 편집기 열기
            self.ui.publist.openPersistentEditor(combo_index)
            self.ui.publist.openPersistentEditor(button_index)