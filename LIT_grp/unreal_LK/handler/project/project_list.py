import os, sys
from glob import glob
import re
import maya.cmds as cmds


def project_data():


    file_dir = "Q:\\lt_team\\LT\\Lit_set"

    root_path = file_dir.replace('\\', '/')

    items = os.listdir(root_path)

    row_datas = list()

    for item in items:

        row_data = dict()


        row_data['name'] = item

        row_datas.append(row_data)

    return row_datas


def project_export(project_name):
    from maya.app.renderSetup.model import renderSetup
    import maya.cmds as cmds
    import json
    import os

    print('project_export()')
    file_dir = "Q:\\lt_team\\LT\\Lit_set"
    root_path = os.path.join(file_dir, project_name).replace('\\', '/')

    if not os.path.isdir(root_path):
        os.makedirs(root_path)

    scene_name = project_name

    # aov쉐이더 뽑기
    aiAOVs = cmds.listConnections('defaultArnoldRenderOptions.aovList')
    aov_sh = []
    aovs_filter_dic = {}
    for i in aiAOVs:
        # 쉐이더
        aov_con = cmds.listConnections(i + ".defaultValue", source=True, plugs=True)
        if aov_con:
            source_node = cmds.ls(aov_con[0].split('.')[0])
            aov_sh.append(source_node[0])

        # aov json
        aov_name = cmds.getAttr(i + '.name')
        aov_enable = cmds.getAttr(i + '.enabled')
        aov_defaultValue = cmds.listConnections(i + '.defaultValue', source=True, plugs=True)
        aov_defaultValue = "" if aov_defaultValue is None else aov_defaultValue[0]

        aov_type = cmds.getAttr(i + '.type')

        connected_filters = cmds.listConnections(i, type="aiAOVFilter")
        connected_filter = "" if not connected_filters else connected_filters[0]

        filter_settings = cmds.listAttr(connected_filter, settable=True)
        filter_data = {}

        for setting in filter_settings:
            filter_data[setting] = cmds.getAttr(connected_filter + '.' + setting)

        aovs_filter_dic[i] = {
            'name': aov_name,
            'enable': aov_enable,
            'defaultValue': aov_defaultValue,
            'type': aov_type,
            'connectedFilter': {
                'name': connected_filter,
                'settings': filter_data
            }
        }


    # aov json 내보내기2
    export_aovson_path = os.path.join(root_path, scene_name+'_aov.json').replace('\\', '/')

    with open(export_aovson_path, "w") as f:
        json.dump(aovs_filter_dic, f)

    # render_layer 내보내기

    rs = renderSetup.instance()
    render_layers = rs.getRenderLayers()
    layer = []
    for x in render_layers:
        layer.append(x.name())

    layer_list = []
    for i in layer:
        layer_data = []
        layer_data.append(rs.getRenderLayer(i).encode())
        layer_list.append(layer_data)

    export_json_path = os.path.join(root_path, scene_name+'.json').replace('\\', '/')

    with open(export_json_path, "w") as f:
        json.dump(layer_list, f)

    #  레이어 연결된 쉐이더 뽑기

    for layer_j in layer_list:
        layer_sh_dic = layer_j[0]['renderSetupLayer']

        layer_coll = layer_sh_dic['collections']
        for collection_data in layer_coll:
            collection_type = [(collection_data.keys())][0]

            if collection_type == 'collection':
                collection_c = collection_data['collection']['children']

                for child_data in collection_c:

                    children_type = [(child_data.keys())][0]

                    children_list = child_data[children_type]

                    child_data_b = [(children_list.keys())]
                    for shader in child_data_b:
                        if shader == 'children':
                            ch_data = children_list['children'][0]
                            ch_data_type = [(ch_data.keys())][0]
                            if ch_data_type == 'shaderOverride':
                                shader_conn = ch_data['shaderOverride']['connectionStr']
                                shader_name = shader_conn.split('.')[0]
                                aov_sh.append(shader_name)
                            else:
                                continue

            else:
                continue


    # aov 쉐이더 내보내기 & 레이어 연결 쉐이더도 같이 보내기 위해 위치조정
    export_path_sh = os.path.join(root_path, scene_name+'_aov.mb').replace('\\', '/')
    print(export_path_sh)
    if aov_sh:
        cmds.select(aov_sh)
        cmds.file(export_path_sh, exportSelected=True, type='mayaBinary')

    #set 내보내기
    list = cmds.ls(type="objectSet")
    set_list = [set for set in list if "_set" in set]

    set_items = []

    for set_ in set_list:
        set_at = cmds.listAttr(set_)
        set_at_list = set_at[42:]

        set_dict = dict()

        set_name = set_
        ob_list = cmds.listConnections(set_)

        set_attributes = []
        for set_info in set_at_list:
            attribute_info = {}

            attribute_info['name'] = set_info

            # 속성의 at 가져오기
            attr_type = cmds.getAttr(set_name + '.' + set_info, type=True)
            attribute_info['type'] = attr_type

            # 속성의 dv 가져오기
            if cmds.attributeQuery(set_info, node=set_name, exists=True):
                default_value = cmds.attributeQuery(set_info, node=set_name, listDefault=True)[0]
                attribute_info['default_value'] = default_value

            set_attributes.append(attribute_info)

        set_dict['name'] = set_name
        set_dict['object'] = ob_list
        set_dict['attributes'] = set_attributes

        set_items.append(set_dict)






    export_set_path = os.path.join(root_path, scene_name + '_set.json')

    if set_items:
        with open(export_set_path, "w") as f:
            json.dump(set_items, f)


    # 리벳 rivet 내보내기

    mesh_dic = {}
    mesh = cmds.ls(type="mesh")
    rivetCurve = cmds.ls(type="curveFromMeshEdge")

    for mesh_i in mesh:
        connect = cmds.listConnections(mesh_i)

        for con_y in connect:
            if con_y in rivetCurve:
                mesh_name = mesh_i.replace("Shape", "")

                edge_num = []
                for con_j in connect:

                    if con_j[:22] == 'rivetCurveFromMeshEdge':
                        edge = cmds.getAttr(con_j + ".edgeIndex[0]")

                        edge_num.append(edge)

                        rivet_f = cmds.listConnections(con_j)
                        rivet_rivetLoft = [rivetLoft for rivetLoft in rivet_f if 'rivetLoft' in rivetLoft]

                        rivet_s = cmds.listConnections(rivet_rivetLoft[0])

                        rivet_SurfaceInfo = [SurfaceInfo for SurfaceInfo in rivet_s if
                                             'rivetPointOnSurfaceInfo' in SurfaceInfo]

                        rr = cmds.listConnections(rivet_SurfaceInfo[0] + ".result.position")

                        rivet_t = cmds.listConnections(rivet_SurfaceInfo[0] + ".result.position")

                        rivet_name = rivet_t[0]
                        print(rivet_name)
                        rotate_axes = ['rotateX', 'rotateY', 'rotateZ']
                        rivet_rotate = []
                        for axis in rotate_axes:
                            constraints = cmds.listConnections(rivet_name + '.' + axis, source=True, destination=False)
                            r_rotate = cmds.getAttr(rivet_name + '.' + axis)
                            if constraints:
                                rivet_rotate.append("None")
                            else:
                                rivet_rotate.append(r_rotate)

                print(edge_num)

                mesh_dic[mesh_i] = {'name': mesh_name, 'edge': edge_num, 'rivet': rivet_name, 'rotate':rivet_rotate}

    print(mesh_dic)

    export_rivet_path = os.path.join(root_path, scene_name + '_rivet.json')

    if mesh_dic:
        with open(export_rivet_path, "w") as f:
            json.dump(mesh_dic, f)






    # 리벳 삭제

    rivet_cons = cmds.ls(type='pointOnSurfaceInfo')

    for rivet_con in rivet_cons:
        cmds.delete(rivet_con)

    # 라이트 뽑기
    cmds.select(['lit_grp'])
    export_path = os.path.join(root_path, scene_name + '_lit.mb')
    cmds.file(export_path, force=True, type='mayaBinary', preserveReferences=True, exportSelected=True)








def project_import(sel):
    from maya.app.renderSetup.model import renderSetup
    import mtoa.aovs as aovs
    import maya.cmds as cmds
    import json
    import os


    file_dir = "Q:\\lt_team\\LT\\Lit_set"
    file_name = sel
    root_path = os.path.join(file_dir, file_name)
    selected_item_mb = os.path.join(root_path, file_name + ".json").replace('\\', '/')

    print('project_import()')
    rs = renderSetup.instance()
    if selected_item_mb:
        with open(selected_item_mb, "r") as f:
            data = json.load(f)
            print(data)
            lit_file = os.path.join(root_path, file_name + "_lit.mb").replace('\\', '/')
            aovsh_file = os.path.join(root_path, file_name + "_aov.mb").replace('\\', '/')
            cmds.file(lit_file, i=True, namespace=":")
            if os.path.exists(aovsh_file):
                cmds.file(aovsh_file, i=True, namespace=":")

            for i in data:
                layerData = {'renderSetup': {'renderLayers': i}}
                data_decode = rs.decode(layerData, renderSetup.DECODE_AND_RENAME)
                print(data_decode)


            def create_aov_with_filter(aov_data):
                aov_name = aov_data['name']
                aov_type = aov_data['type']
                aov_enable = aov_data.get('enable', True)
                aov_defaultValue = aov_data.get('defaultValue', "")

                aov_node = aovs.AOVInterface().addAOV(aov_name, aov_type)

                cmds.setAttr("aiAOV_" + aov_name + ".enabled", aov_enable)

                if aov_defaultValue:
                    cmds.connectAttr(aov_defaultValue, "aiAOV_" + aov_name + ".defaultValue")

                if 'connectedFilter' in aov_data:
                    filter_data = aov_data['connectedFilter']
                    filter_name = filter_data['name']
                    filter_settings = filter_data['settings']

                    # 필터 생성
                    if not cmds.objExists(filter_name):
                        filter_node = cmds.createNode('aiAOVFilter', name=filter_name)
                    else:
                        filter_node = filter_name

                        # 필터 셋팅
                    for setting, value in filter_settings.items():
                        # print( filter_settings)
                        # print(filter_settings['aiTranslator'])
                        cmds.setAttr(filter_node + '.ai_translator', filter_settings['aiTranslator'], type='string')
                        cmds.setAttr(filter_node + '.width', float(filter_settings['width']))

            aovjson_file_path = os.path.join(root_path, file_name+"_aov.json").replace('\\', '/')
            with open(aovjson_file_path, 'r') as file:
                aovs_data = json.load(file)

            for aov_data in aovs_data.values():
                create_aov_with_filter(aov_data)
                connections = cmds.listConnections('aiAOV_' + aov_data['name'] + '.outputs[0].filter', source=True,
                                                   destination=False)
                if connections:
                    for x in connections:
                        cmds.disconnectAttr(x + '.message', 'aiAOV_' + aov_data['name'] + '.outputs[0].filter')

                cmds.connectAttr(aov_data['connectedFilter']['name'] + '.message',
                                 'aiAOV_' + aov_data['name'] + '.outputs[0].filter')

        ### json 파일 불러오기
        set_file_path = os.path.join(root_path, file_name + "_set.json").replace('\\', '/')

        if set_file_path:
            with open(set_file_path, "r") as f:
                set_datas = json.load(f)
                print(set_datas)

                set_list = cmds.ls(type="objectSet")
                all_list = cmds.ls()

                for set_data in set_datas:
                    set_name = set_data['name']
                    set_objects = set_data['object']
                    set_attributes = set_data['attributes']

                    if not set_name in set_list:

                        cmds.sets(n=set_name)
                        for set_attribute in set_attributes:
                            at_name = set_attribute['name']
                            at_type = set_attribute['type']
                            at_dv = set_attribute['default_value']

                            if at_type == 'enum':
                                cmds.addAttr(set_name, ln=at_name, at=at_type, en='none:catclark:linear', dv=int(at_dv))
                            else:
                                cmds.addAttr(set_name, ln=at_name, at=at_type, dv=int(at_dv))

                    for set_object in set_objects:
                        if set_object in all_list:
                            cmds.sets(set_object, add=set_name)
                        else:
                            pass




