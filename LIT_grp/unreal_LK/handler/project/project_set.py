

def ap_import():
    from maya.app.renderSetup.model import renderSetup
    import mtoa.aovs as aovs
    import maya.cmds as cmds
    import json
    import os


    real_root = "Q:\\lt_team\\LT\\Lit_set\\ap"
    file_name = "AP_set"
    selected_item_mb = os.path.join(real_root, file_name+".json").replace('\\', '/')

    print('AP_import()')
    rs = renderSetup.instance()
    if selected_item_mb:
        with open(selected_item_mb, "r") as f:
            data = json.load(f)
            print(data)
            for i in data:
                layerData = {'renderSetup': {'renderLayers': i}}
                data_decode = rs.decode(layerData, renderSetup.DECODE_AND_RENAME)
                print(data_decode)
            lit_file = os.path.join(real_root, file_name+"_lit.mb").replace('\\', '/')
            aovsh_file = os.path.join(real_root, file_name+"_aov.mb").replace('\\', '/')
            cmds.file(lit_file, i=True, namespace=":")
            cmds.file(aovsh_file, i=True, namespace=":")

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


def fx_meshlit() :
    import maya.cmds as cmds
    import mtoa.utils as mutils

    fx_mesh = cmds.ls(type="mesh")
    fx_orange = [fx for fx in fx_mesh if "tracer_mesh" in fx]
    fx_blue = [fx for fx in fx_mesh if "tracerBlue_mesh" in fx]

    fx_sh = cmds.ls(type="ramp")
    print(fx_sh)
    fx_orange_sh = [fx for fx in fx_sh if "tracerOrange" in fx]
    fx_blue_sh = [fx for fx in fx_sh if "tracerBlue" in fx]


    if fx_orange:
        for i in fx_orange:
            o_name = i.replace("Shape", "")
            cmds.select(o_name)
            mutils.createMeshLight()
            fx_lit = "light_" + i
            cmds.connectAttr(fx_orange_sh[0] + ".outColor", fx_lit + ".color")
            cmds.setAttr(fx_lit + ".aiNormalize", 0)
            cmds.setAttr(fx_lit + ".aiIndirect", 0)

    if fx_blue:
        for j in fx_blue:
            b_name = j.replace("Shape", "")
        cmds.select(b_name)
        mutils.createMeshLight()
        fx_lit = "light_" + j
        cmds.connectAttr(fx_blue_sh[0] + ".outColor", fx_lit + ".color")
        cmds.setAttr(fx_lit + ".aiNormalize", 0)
        cmds.setAttr(fx_lit + ".aiIndirect", 0)




def deft_import():
    from maya.app.renderSetup.model import renderSetup
    import mtoa.aovs as aovs
    import maya.cmds as cmds
    import json
    import os


    real_root = "Q:\\lt_team\\LT\\Lit_set\\deft"
    file_name = "deft_set"
    selected_item_mb = os.path.join(real_root, file_name+".json").replace('\\', '/')

    print('deft_import()')
    rs = renderSetup.instance()
    if selected_item_mb:
        with open(selected_item_mb, "r") as f:
            data = json.load(f)
            print(data)
            for i in data:
                layerData = {'renderSetup': {'renderLayers': i}}
                data_decode = rs.decode(layerData, renderSetup.DECODE_AND_RENAME)
                print(data_decode)
            lit_file = os.path.join(real_root, file_name+"_lit.mb").replace('\\', '/')
            aovsh_file = os.path.join(real_root, file_name+"_aov.mb").replace('\\', '/')
            cmds.file(lit_file, i=True, namespace=":")
            cmds.file(aovsh_file, i=True, namespace=":")

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

