

def ap_import():
    from maya.app.renderSetup.model import renderSetup
    import mtoa.aovs as aovs
    import maya.cmds as cmds
    import json
    import os


    real_root = "Q:\\lt_team\\LT\\Lit_set\\AP_set"
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
    fx_orange = [fx for fx in fx_mesh if "tracerOrange" in fx]
    fx_blue = [fx for fx in fx_mesh if "tracerBlue" in fx]

    fx_sh = cmds.ls(type="ramp")
    print(fx_sh)
    fx_orange_sh = [fx for fx in fx_sh if "tracerOrange" in fx]
    fx_blue_sh = [fx for fx in fx_sh if "tracerBlue" in fx]
    fx_lit_grp = cmds.ls(type="aiMeshLight")

    print(fx_lit_grp)

    if fx_orange:
        for i in fx_orange:
            o_name = i.replace("Shape", "")
            cmds.select(o_name)
            if not "light_" + i in fx_lit_grp:
                mutils.createMeshLight()
                fx_lit = "light_" + i
                cmds.connectAttr(fx_orange_sh[0] + ".outColor", fx_lit + ".color")
                cmds.setAttr(fx_lit + ".aiNormalize", 0)
                cmds.setAttr(fx_lit + ".aiIndirect", 0)

    if fx_blue:
        for j in fx_blue:

            b_name = j.replace("Shape", "")
            cmds.select(b_name)
            if not "light_" + i in fx_lit_grp:
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


    real_root = "Q:\\lt_team\\LT\\Lit_set\\deft_set"
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




def etr_import():
    from maya.app.renderSetup.model import renderSetup
    import mtoa.aovs as aovs
    import maya.cmds as cmds
    import json
    import os


    real_root = "Q:\\lt_team\\LT\\Lit_set\\ETR_set"
    file_name = "ETR_set"
    selected_item_mb = os.path.join(real_root, file_name+".json").replace('\\', '/')

    print('etr_import()')
    rs = renderSetup.instance()
    if selected_item_mb:
        with open(selected_item_mb, "r") as f:
            data = json.load(f)
            print(data)
            lit_file = os.path.join(real_root, file_name+"_lit.mb").replace('\\', '/')
            aovsh_file = os.path.join(real_root, file_name+"_aov.mb").replace('\\', '/')
            cmds.file(lit_file, i=True, namespace=":")
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




def beam_set():
    from maya.app.renderSetup.model import renderSetup
    import mtoa.aovs as aovs
    import maya.cmds as cmds
    import json
    import os

    real_root = "P:\\DNF\\sequences\\DNF\\DNF_0330\\LGT\\wip\\maya\\data"
    file_name = "DNF_0330_LGT_test_v001"
    selected_item_mb = os.path.join(real_root, file_name + ".json").replace('\\', '/')

    print('beam_import()')
    aovsh_file = os.path.join(real_root, file_name + "_aov.mb").replace('\\', '/')

    cmds.file(aovsh_file, i=True, namespace=":")
    rs = renderSetup.instance()
    if selected_item_mb:
        with open(selected_item_mb, "r") as f:
            data = json.load(f)
            print(data)
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

            aovjson_file_path = os.path.join(real_root, file_name + "_aov.json").replace('\\', '/')
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








def beam_lit():
    import maya.cmds as cmds
    import mtoa.utils as mutils

    setlist = cmds.ls(et='objectSet')
    if not 'beam_set' in setlist:
        cmds.sets(n="beam_set")

    if not 'backlit_set' in setlist:
        cmds.sets(n="backlit_set")

    list = cmds.ls(type="mesh")

    for x in list:
        try:
            if "spotlight_glass" in x:
                spot_glass = x.replace("Shape", "")
                cmds.select(spot_glass)
                cmds.sets(spot_glass, add='backlit_set')
                mutils.createMeshLight()
                cmds.setAttr("light_" + spot_glass + ".color", 1, 0, 0)
                cmds.setAttr("light_" + spot_glass + ".aiNormalize", 0)
                cmds.setAttr("light_" + spot_glass + ".lightVisible", 1)
                cmds.setAttr("light_" + spot_glass + ".intensity", 0.1)
                cmds.setAttr("light_" + spot_glass + ".aiExposure", 0.5)
                cmds.setAttr("light_" + spot_glass + ".aiSpecular", 0)
                cmds.setAttr("light_" + spot_glass + ".aiSss", 0)
                cmds.setAttr("light_" + spot_glass + ".aiIndirect", 0)
                cmds.setAttr("light_" + spot_glass + ".aiSamples", 8)

            elif "spotlight_top_glass" in x:
                top_glass = x.replace("Shape", "")

                cmds.select(top_glass)
                cmds.sets(top_glass, add='backlit_set')
                mutils.createMeshLight()
                cmds.setAttr("light_" + top_glass + ".color", 0, 1, 0)
                cmds.setAttr("light_" + top_glass + ".aiNormalize", 0)
                cmds.setAttr("light_" + top_glass + ".lightVisible", 1)
                cmds.setAttr("light_" + top_glass + ".intensity", 0.1)
                cmds.setAttr("light_" + top_glass + ".aiExposure", 0.5)
                cmds.setAttr("light_" + top_glass + ".aiSpecular", 0)
                cmds.setAttr("light_" + top_glass + ".aiSss", 0)
                cmds.setAttr("light_" + top_glass + ".aiIndirect", 0)
                cmds.setAttr("light_" + top_glass + ".aiSamples", 8)

            elif "spotlight_side_glass" in x:
                side_glass = x.replace("Shape", "")
                cmds.select(side_glass)
                cmds.sets(side_glass, add='backlit_set')
                mutils.createMeshLight()
                cmds.setAttr("light_" + side_glass + ".color", 0, 0, 1)
                cmds.setAttr("light_" + side_glass + ".aiNormalize", 0)
                cmds.setAttr("light_" + side_glass + ".lightVisible", 1)
                cmds.setAttr("light_" + side_glass + ".intensity", 0.1)
                cmds.setAttr("light_" + side_glass + ".aiExposure", 0.5)
                cmds.setAttr("light_" + side_glass + ".aiSpecular", 0)
                cmds.setAttr("light_" + side_glass + ".aiSss", 0)
                cmds.setAttr("light_" + side_glass + ".aiIndirect", 0)
                cmds.setAttr("light_" + side_glass + ".aiSamples", 8)

            elif "spotlight_beam" in x:
                spot_beam = x.replace("Shape", "")
                cmds.select(spot_beam)
                cmds.sets(spot_beam, add='beam_set')
                mutils.createMeshLight()
                cmds.setAttr("light_" + spot_beam + ".color", 1, 0, 0)
                cmds.setAttr("light_" + spot_beam + ".aiNormalize", 0)
                cmds.setAttr("light_" + spot_beam + ".lightVisible", 1)
                cmds.setAttr("light_" + spot_beam + ".intensity", 1)
                cmds.setAttr("light_" + spot_beam + ".aiExposure", 1)
                cmds.setAttr("light_" + spot_beam + ".aiSpecular", 0)
                cmds.setAttr("light_" + spot_beam + ".aiSss", 0)
                cmds.setAttr("light_" + spot_beam + ".aiIndirect", 0)
                cmds.setAttr("light_" + spot_beam + ".aiSamples", 8)

            elif "spotlight_top_beam" in x:
                top_beam = x.replace("Shape", "")
                cmds.select(top_beam)
                cmds.sets(top_beam, add='beam_set')
                mutils.createMeshLight()
                cmds.setAttr("light_" + top_beam + ".color", 0, 1, 0)
                cmds.setAttr("light_" + top_beam + ".aiNormalize", 0)
                cmds.setAttr("light_" + top_beam + ".lightVisible", 1)
                cmds.setAttr("light_" + top_beam + ".intensity", 1)
                cmds.setAttr("light_" + top_beam + ".aiExposure", 1)
                cmds.setAttr("light_" + top_beam + ".aiSpecular", 0)
                cmds.setAttr("light_" + top_beam + ".aiSss", 0)
                cmds.setAttr("light_" + top_beam + ".aiIndirect", 0)
                cmds.setAttr("light_" + top_beam + ".aiSamples", 8)

            elif "spotlight_side_beam" in x:
                side_beam = x.replace("Shape", "")
                cmds.select(side_beam)
                cmds.sets(side_beam, add='beam_set')
                mutils.createMeshLight()
                cmds.setAttr("light_" + side_beam + ".color", 0, 0, 1)
                cmds.setAttr("light_" + side_beam + ".aiNormalize", 0)
                cmds.setAttr("light_" + side_beam + ".lightVisible", 1)
                cmds.setAttr("light_" + side_beam + ".intensity", 1)
                cmds.setAttr("light_" + side_beam + ".aiExposure", 1)
                cmds.setAttr("light_" + side_beam + ".aiSpecular", 0)
                cmds.setAttr("light_" + side_beam + ".aiSss", 0)
                cmds.setAttr("light_" + side_beam + ".aiIndirect", 0)
                cmds.setAttr("light_" + side_beam + ".aiSamples", 8)
        except Exception as e:
            print("An error occurred:", str(e))
            continue



def fog_set():
    from maya.app.renderSetup.model import renderSetup
    import mtoa.aovs as aovs
    import maya.cmds as cmds
    import json
    import os

    # 현재 씬에서 렌더 레이어 가져오기

    rs = renderSetup.instance()

    rs.clearAll()

    print("모든 렌더 레이어가 삭제되었습니다.")

    # 사용되지 않는 AOV 삭제
    unused_aovs = cmds.ls(type="aiAOV") or []
    used_aovs = cmds.ls(referencedNodes=True)
    used_aovs += cmds.listConnections('defaultRenderGlobals', d=False, s=True, type='aiAOV') or []

    aovs_to_delete = list(set(unused_aovs) - set(used_aovs))
    if aovs_to_delete:
        cmds.delete(aovs_to_delete)
        print("사용되지 않는 AOV가 삭제되었습니다.")
    else:
        print("사용되지 않는 AOV가 없습니다.")
    # 사용되지 않는 쉐이더 삭제
    unused_shaders = cmds.ls(mat=True, long=True, type='shader') or []
    used_shaders = cmds.ls(referencedNodes=True, materials=True)
    used_shaders = cmds.ls(used_shaders, long=True) if used_shaders else []
    used_shaders += cmds.ls(type='shadingEngine')
    used_shaders += cmds.listConnections('defaultRenderGlobals', d=False, s=True, t='shadingEngine') or []

    shaders_to_delete = list(set(unused_shaders) - set(used_shaders))
    if shaders_to_delete:
        cmds.delete(shaders_to_delete)
        print("사용되지 않는 쉐이더가 삭제되었습니다.")
    else:
        print("사용되지 않는 쉐이더가 없습니다.")

    lit_grps=cmds.ls(type="transform")

    for lit_grp in lit_grps:
        if "lit_grp" in lit_grp:
            cmds.delete(lit_grp)
        else :
            pass



    real_root = "P:\\DNF\\sequences\\DNF\\DNF_0600\\LGT\\wip\\maya\\data"
    file_name = "DNF_0600_LGT_volumetest_v001"
    selected_item_mb = os.path.join(real_root, file_name + ".json").replace('\\', '/')

    print('fog_import()')
    aovsh_file = os.path.join(real_root, file_name + "_aov.mb").replace('\\', '/')
    lit_file=os.path.join(real_root, file_name + "_lit.mb").replace('\\', '/')
    cmds.file(lit_file, i=True, namespace=":")
    cmds.file(aovsh_file, i=True, namespace=":")
    rs = renderSetup.instance()
    if selected_item_mb:
        with open(selected_item_mb, "r") as f:
            data = json.load(f)
            print(data)
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

            aovjson_file_path = os.path.join(real_root, file_name + "_aov.json").replace('\\', '/')
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
