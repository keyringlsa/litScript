def lkd_export():
    from maya.app.renderSetup.model import renderSetup
    import maya.cmds as cmds
    import json
    import os

    print('lkd_export()')
    file_dir = cmds.file(q=True, sceneName=True)
    file_dir_split = file_dir.split('LKD')[0].replace("/","\\")
    source_path = 'LKD/wip/maya/data'

    root_path = os.path.join(file_dir_split, source_path).replace('\\', '/')

    scene_name = cmds.file(q=True, sceneName=True)


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
    export_aovson_path = os.path.join(root_path, os.path.splitext(os.path.basename(scene_name))[0]+'_aov.json').replace('\\', '/')

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

    export_json_path = os.path.join(root_path, os.path.splitext(os.path.basename(scene_name))[0]+'.json').replace('\\', '/')

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
    export_path_sh = os.path.join(root_path, os.path.splitext(os.path.basename(scene_name))[0]+'_aov.mb').replace('\\', '/')
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






    export_set_path = os.path.join(root_path, os.path.splitext(os.path.basename(scene_name))[0] + '_set.json')

    if set_items:
        with open(export_set_path, "w") as f:
            json.dump(set_items, f)


    # 리벳 rivet 내보내기

    mesh_dic = {}

    rivet_lofts = cmds.ls(type="loft")
    for rivet_loft in rivet_lofts:
        print(rivet_loft)
        # loft에서 연결된 정보 구하기
        loft_list = cmds.listConnections(rivet_loft)

        # 리벳 로케이터 구하기
        point_sur = cmds.listConnections(loft_list, type="transform")
        rivet_loc = cmds.listRelatives(point_sur, type="locator")
        rivet_name = rivet_loc[0].replace("Shape", "")

        # 연결된 메쉬 구하기
        mesh = cmds.listConnections(loft_list, type="shape")
        mesh_name = mesh[0]

        # 연결된 버텍스 정보 구하기
        edge_num = []
        inputCurveA = cmds.listConnections(rivet_loft + ".inputCurve[0]")
        inputCurveB = cmds.listConnections(rivet_loft + ".inputCurve[1]")
        edgeA = cmds.getAttr(inputCurveA[0] + ".edgeIndex[0]")
        edgeB = cmds.getAttr(inputCurveB[0] + ".edgeIndex[0]")
        edge_num.append(edgeB)
        edge_num.append(edgeA)

        rotate_axes = ['rotateX', 'rotateY', 'rotateZ']
        rivet_rotate = []
        for axis in rotate_axes:
            constraints = cmds.listConnections(rivet_name + '.' + axis, source=True, destination=False)
            r_rotate = cmds.getAttr(rivet_name + '.' + axis)
            if constraints:
                rivet_rotate.append("None")
            else:
                rivet_rotate.append(r_rotate)

        mesh_dic[rivet_loft] = {'name': mesh_name, 'edge': edge_num, 'rivet': rivet_name, 'rotate': rivet_rotate}

    print(mesh_dic)

    export_rivet_path = os.path.join(root_path, os.path.splitext(os.path.basename(scene_name))[0] + '_rivet.json')

    if mesh_dic:
        with open(export_rivet_path, "w") as f:
            json.dump(mesh_dic, f)

    # 리벳 삭제

    rivet_cons = cmds.ls(type='pointOnSurfaceInfo')

    for rivet_con in rivet_cons:
        cmds.delete(rivet_con)

    # 라이트 뽑기
    cmds.select(['lit_grp'])
    scene_name = cmds.file(q=True, sceneName=True)
    export_path = os.path.join(root_path, os.path.splitext(os.path.basename(scene_name))[0]) + '_lit.mb'
    cmds.file(export_path, force=True, type='mayaBinary', preserveReferences=True, exportSelected=True)






############################################################








def lkd_import(sel, file_name, lkd_type):
    from maya.app.renderSetup.model import renderSetup
    import mtoa.aovs as aovs
    import maya.cmds as cmds
    import json
    import os


    file_dir = cmds.file(q=True, sceneName=True)
    file_dir_split = file_dir.split('LKD')[0].replace("/","\\")
    file_dir_splitB = file_dir_split.split(os.sep)

    root_path = os.path.join(file_dir_splitB[0], file_dir_splitB[1], 'assets', lkd_type)

    item = sel
    source_path = 'LKD/wip/maya/data'
    real_root = os.path.join(root_path, item, source_path).replace('\\', '/')

    selected_item_mb = os.path.join(real_root, file_name+".json").replace('\\', '/')

    print('lkd_import()')
    rs = renderSetup.instance()
    if selected_item_mb:
        with open(selected_item_mb, "r") as f:
            data = json.load(f)
            print(data)
            lit_file = os.path.join(real_root, file_name + "_lit.mb").replace('\\', '/')
            aovsh_file = os.path.join(real_root, file_name + "_aov.mb").replace('\\', '/')
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

            aovjson_file_path = os.path.join(real_root, file_name+"_aov.json").replace('\\', '/')
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
        set_file_path = os.path.join(real_root, file_name + "_set.json").replace('\\', '/')

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








def lit_each_import(sel, file_name, lkd_type):
    print('each_import()')
    import maya.cmds as cmds
    import os


    file_dir = cmds.file(q=True, sceneName=True)
    file_dir_split = file_dir.split('LKD')[0].replace("/","\\")
    file_dir_splitB = file_dir_split.split(os.sep)

    root_path = os.path.join(file_dir_splitB[0], file_dir_splitB[1], 'assets', lkd_type)

    item = sel
    source_path = 'LKD/wip/maya/data'
    real_root = os.path.join(root_path, item, source_path).replace('\\', '/')

    lit_file = os.path.join(real_root, file_name+"_lit.mb").replace('\\', '/')

    cmds.file(lit_file, i=True, namespace=":")






def layer_each_import(sel, file_name, lkd_type):

    from maya.app.renderSetup.model import renderSetup
    import maya.cmds as cmds
    import json
    import os


    file_dir = cmds.file(q=True, sceneName=True)
    file_dir_split = file_dir.split('LKD')[0].replace("/","\\")
    file_dir_splitB = file_dir_split.split(os.sep)

    root_path = os.path.join(file_dir_splitB[0], file_dir_splitB[1], 'assets', lkd_type)

    item = sel
    source_path = 'LKD/wip/maya/data'
    real_root = os.path.join(root_path, item, source_path).replace('\\', '/')

    selected_item_mb = os.path.join(real_root, file_name+".json").replace('\\', '/')

    rs = renderSetup.instance()
    if selected_item_mb:
        with open(selected_item_mb, "r") as f:
            data = json.load(f)
            for i in data:
                layerData = {'renderSetup': {'renderLayers': i}}
                data_decode = rs.decode(layerData, renderSetup.DECODE_AND_RENAME)
                print(data_decode)



def aov_each_import(sel, file_name, lkd_type):

    import mtoa.aovs as aovs
    import maya.cmds as cmds
    import json
    import os


    file_dir = cmds.file(q=True, sceneName=True)
    file_dir_split = file_dir.split('LKD')[0].replace("/","\\")
    file_dir_splitB = file_dir_split.split(os.sep)

    root_path = os.path.join(file_dir_splitB[0], file_dir_splitB[1], 'assets', lkd_type)

    item = sel
    source_path = 'LKD/wip/maya/data'
    real_root = os.path.join(root_path, item, source_path).replace('\\', '/')

    ### 쉐이더 불러오기
    aovsh_file = os.path.join(real_root, file_name + "_aov.mb").replace('\\', '/')
    if os.path.exists(aovsh_file):
        cmds.file(aovsh_file, i=True, namespace=":")


    ### json 파일 불러오기
    aovjson_file_path = os.path.join(real_root, file_name + "_aov.json").replace('\\', '/')

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
                cmds.setAttr(filter_node + '.ai_translator', filter_settings['aiTranslator'], type='string')
                cmds.setAttr(filter_node + '.width', float(filter_settings['width']))

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



#####################################rivet



def rivet_imp(sel, file_name, lkd_type):

    import maya.cmds as cmds
    import json
    import os
    # 리벳 삭제

    rivet_cons = cmds.ls(type='pointOnSurfaceInfo')

    for rivet_con in rivet_cons:
        cmds.delete(rivet_con)


    ###불러오기

    file_dir = cmds.file(q=True, sceneName=True)
    file_dir_split = file_dir.split('LKD')[0].replace("/", "\\")
    file_dir_splitB = file_dir_split.split(os.sep)

    root_path = os.path.join(file_dir_splitB[0], file_dir_splitB[1], 'assets', lkd_type)

    item = sel
    source_path = 'LKD/wip/maya/data'
    real_root = os.path.join(root_path, item, source_path).replace('\\', '/')

    ### json 파일 불러오기
    rivet_file_path = os.path.join(real_root, file_name + "_rivet.json").replace('\\', '/')

    if rivet_file_path:

        with open(rivet_file_path, "r") as f:

            data = json.load(f)

            print(data)
            for r_data in data.values():

                mesh_name = r_data['name']

                mesh_part = mesh_name.split(':')

                sc_mesh = cmds.ls(type='mesh')
                mesh_name_new = []

                for sc in sc_mesh:
                    sc_part = sc.split(":")

                    if sc_part[0][:-1] == mesh_part[0][:-1]:
                        sc_part_n = sc_part[1].replace("Shape", "")
                        mesh_name_f = sc_part[0] + ":" + mesh_part[1]

                        if not mesh_name_f in mesh_name_new:
                            mesh_name_new.append(mesh_name_f)

                edge_f = r_data['edge'][0]
                edge_s = r_data['edge'][1]
                rivet_name = r_data['rivet']
                rivet_rotate = r_data['rotate']
                print(mesh_name_new, edge_f, edge_s, rivet_name, rivet_rotate)

                edge_f_name = mesh_name_new[0] + '.e[{0}]'.format(edge_f)
                edge_s_name = mesh_name_new[0] + '.e[{0}]'.format(edge_s)
                print(edge_s_name, edge_f_name)

                nameObject = ""
                namePOSI = ""

                parts = []
                list = []

                list.append(edge_s_name)
                list.append(edge_f_name)

                size = len(list)

                if size > 0:
                    if size != 2:
                        cmds.error("No two edges selected")
                        return ""

                    parts = list[0].split(".")
                    nameObject = parts[0]
                    parts = list[0].split("[")
                    e1 = int(parts[1].strip("]"))

                    parts = list[1].split("[")
                    e2 = int(parts[1].strip("]"))

                    nameCFME1 = cmds.createNode("curveFromMeshEdge", name="rivetCurveFromMeshEdge1")
                    cmds.setAttr(nameCFME1 + ".ihi", 1)
                    cmds.setAttr(nameCFME1 + ".ei[0]", e1)

                    nameCFME2 = cmds.createNode("curveFromMeshEdge", name="rivetCurveFromMeshEdge2")
                    cmds.setAttr(nameCFME2 + ".ihi", 1)
                    cmds.setAttr(nameCFME2 + ".ei[0]", e2)

                    nameLoft = cmds.createNode("loft", name="rivetLoft1")
                    cmds.setAttr(nameLoft + ".u", True)
                    cmds.setAttr(nameLoft + ".rsn", True)

                    namePOSI = cmds.createNode("pointOnSurfaceInfo", name="rivetPointOnSurfaceInfo1")
                    cmds.setAttr(namePOSI + ".turnOnPercentage", 1)
                    cmds.setAttr(namePOSI + ".parameterU", 0.5)
                    cmds.setAttr(namePOSI + ".parameterV", 0.5)

                    cmds.connectAttr(nameLoft + ".os", namePOSI + ".is", force=True)
                    cmds.connectAttr(nameCFME1 + ".oc", nameLoft + ".ic[0]")
                    cmds.connectAttr(nameCFME2 + ".oc", nameLoft + ".ic[1]")
                    cmds.connectAttr(nameObject + ".w", nameCFME1 + ".im")
                    cmds.connectAttr(nameObject + ".w", nameCFME2 + ".im")

                nameLocator = rivet_name
                cmds.createNode("locator", name=nameLocator + "Shape", parent=nameLocator)

                nameAC = cmds.createNode("aimConstraint", name=nameLocator + "_rivetAimConstraint1",
                                         parent=nameLocator)
                cmds.setAttr(nameAC + ".tg[0].tw", 1)
                cmds.setAttr(nameAC + ".a", 0, 1, 0, type="double3")
                cmds.setAttr(nameAC + ".u", 0, 0, 1, type="double3")
                cmds.setAttr(nameAC + ".v", lock=True, keyable=False)
                cmds.setAttr(nameAC + ".tx", lock=True, keyable=False)
                cmds.setAttr(nameAC + ".ty", lock=True, keyable=False)
                cmds.setAttr(nameAC + ".tz", lock=True, keyable=False)
                cmds.setAttr(nameAC + ".rx", lock=True, keyable=False)
                cmds.setAttr(nameAC + ".ry", lock=True, keyable=False)
                cmds.setAttr(nameAC + ".rz", lock=True, keyable=False)
                cmds.setAttr(nameAC + ".sx", lock=True, keyable=False)
                cmds.setAttr(nameAC + ".sy", lock=True, keyable=False)
                cmds.setAttr(nameAC + ".sz", lock=True, keyable=False)

                cmds.connectAttr(namePOSI + ".position", nameLocator + ".translate")
                cmds.connectAttr(namePOSI + ".n", nameAC + ".tg[0].tt")
                cmds.connectAttr(namePOSI + ".tv", nameAC + ".wu")
                if rivet_rotate[0] == 'None':
                    cmds.connectAttr(nameAC + ".crx", nameLocator + ".rx")
                    cmds.connectAttr(nameAC + ".cry", nameLocator + ".ry")
                    cmds.connectAttr(nameAC + ".crz", nameLocator + ".rz")

                cmds.select(nameLocator, replace=True)




def set_imp(sel, file_name, lkd_type):

    import maya.cmds as cmds
    import json
    import os



    ###불러오기

    file_dir = cmds.file(q=True, sceneName=True)
    file_dir_split = file_dir.split('LKD')[0].replace("/", "\\")
    file_dir_splitB = file_dir_split.split(os.sep)

    root_path = os.path.join(file_dir_splitB[0], file_dir_splitB[1], 'assets', lkd_type)

    item = sel
    source_path = 'LKD/wip/maya/data'
    real_root = os.path.join(root_path, item, source_path).replace('\\', '/')

    ### json 파일 불러오기
    set_file_path = os.path.join(real_root, file_name + "_set.json").replace('\\', '/')

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
