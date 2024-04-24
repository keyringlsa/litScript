def aov():
    import maya.cmds as cmds
    import mtoa.aovs as aovs

    aovs.AOVInterface().addAOV('N', aovType='vector')
    aovs.AOVInterface().addAOV('P', aovType='vector')
    aovs.AOVInterface().addAOV('Z', aovType='float')
    aovs.AOVInterface().addAOV('motionvector', aovType='rgba')

    aiAOVs = cmds.listConnections('defaultArnoldRenderOptions.aovList')
    basic_list = ['aiAOV_albedo','aiAOV_emission','aiAOV_specular',
                  'aiAOV_sss','aiAOV_transmission','aiAOV_shadow_matte']

    for i in basic_list:
        if not i in aiAOVs:
            aovs.AOVInterface().addAOV(i[6:], aovType='rgb')


def aov_ao():
    import maya.cmds as cmds
    import mtoa.aovs as aovs
    aiAOVs = cmds.listConnections('defaultArnoldRenderOptions.aovList')
    if not 'aiAOV_occ' in aiAOVs:
        aovs.AOVInterface().addAOV('occ', aovType='rgba')
        cmds.shadingNode('aiAmbientOcclusion', n='_aov_occ', asShader=True)
        cmds.connectAttr('_aov_occ.outColor', 'aiAOV_occ.defaultValue', f=True)
        cmds.setAttr('_aov_occ.samples', 10)
        cmds.setAttr('_aov_occ.white', 0, 0, 0)
        cmds.setAttr('_aov_occ.black', 1, 1, 1)


def aov_crypto():
    import maya.cmds as cmds
    import mtoa.aovs as aovs
    aiAOVs = cmds.listConnections('defaultArnoldRenderOptions.aovList')
    if not 'aiAOV_crypto_material' in aiAOVs:
        aovs.AOVInterface().addAOV('crypto_material', aovType='rgb')
        aovs.AOVInterface().addAOV('crypto_object', aovType='rgb')
        aovs.AOVInterface().addAOV('crypto_asset', aovType='rgb')
        # 쉐이더
        cmds.shadingNode('cryptomatte', n='_aov_cryptomatte', asShader=True)
        # 연결
        cmds.connectAttr('_aov_cryptomatte.outColor', 'aiAOV_crypto_material.defaultValue', f=True)
        cmds.connectAttr('_aov_cryptomatte.outColor', 'aiAOV_crypto_object.defaultValue', f=True)
        cmds.connectAttr('_aov_cryptomatte.outColor', 'aiAOV_crypto_asset.defaultValue', f=True)


def aov_lit():
    import maya.cmds as cmds
    import mtoa.aovs as aovs
    aiAOVs = cmds.listConnections('defaultArnoldRenderOptions.aovList')
    lit_list = ['aiAOV_RGBA_dome',
                'aiAOV_RGBA_key',
                'aiAOV_RGBA_keyadd',
                'aiAOV_RGBA_rim',
                'aiAOV_RGBA_fill',
                'aiAOV_RGBA_back']
    for i in lit_list:
        if not i in aiAOVs:
            aovs.AOVInterface().addAOV(i[6:], aovType='rgba')













def samplerinfo():
    import maya.cmds as cmds
    import mtoa.aovs as aovs

    aovs.AOVInterface().addAOV('uPointWorld', aovType='rgba')
    aovs.AOVInterface().addAOV('uPointCamera', aovType='rgba')
    aovs.AOVInterface().addAOV('uNoramlCamera', aovType='rgba')
    # 쉐이더
    cmds.shadingNode('samplerInfo', name='UInfo', asShader=True)
    cmds.shadingNode('aiUtility', name='NormalCam_Util', asShader=True)
    cmds.shadingNode('aiUtility', name='PointCam_Util', asShader=True)
    cmds.shadingNode('aiUtility', name='PointWor_Util', asShader=True)
    cmds.setAttr('NormalCam_Util.shadeMode', 2)
    cmds.setAttr('PointCam_Util.shadeMode', 2)
    cmds.setAttr('PointWor_Util.shadeMode', 2)
    # 연결
    cmds.connectAttr('UInfo.normalCamera', 'NormalCam_Util.color', f=True)
    cmds.connectAttr('UInfo.pointCamera', 'PointCam_Util.color', f=True)
    cmds.connectAttr('UInfo.pointWorld', 'PointWor_Util.color', f=True)
    # AOV
    cmds.connectAttr('NormalCam_Util.outColor', 'aiAOV_uNoramlCamera.defaultValue', f=True)
    cmds.connectAttr('PointCam_Util.outColor', 'aiAOV_uPointCamera.defaultValue', f=True)
    cmds.connectAttr('PointWor_Util.outColor', 'aiAOV_uPointWorld.defaultValue', f=True)

    # UVI
    aovs.AOVInterface().addAOV('uUVI', aovType='rgba')
    # aovs.AOVInterface().addAOV('uUVI_aliased', aovType='rgba')
    # fillter
    # cmds.createNode ('aiAOVFilter', n='uUVI_Filter', s=1)
    # mel.eval('connectAttr -f uUVI_Filter.message aiAOV_uUVI_aliased.outputs[0].filter;')
    # cmds.setAttr( 'uUVI_Filter.ai_translator', 'closest', type='string')
    # 쉐이더
    cmds.shadingNode('ramp', name='UV_U', asShader=True)
    cmds.shadingNode('ramp', name='UV_V', asShader=True)
    cmds.shadingNode('ramp', name='UV_ALL', asShader=True)
    cmds.shadingNode('samplerInfo', name='UVInfo', asShader=True)
    # 타입 변환
    cmds.setAttr('UV_U.type', 1)
    cmds.removeMultiInstance('UV_ALL.colorEntryList[1]')
    # 연결
    cmds.connectAttr('UV_U.outColorR', 'UV_ALL.colorEntryList[0].colorR', f=True)
    cmds.connectAttr('UV_V.outColorG', 'UV_ALL.colorEntryList[0].colorG', f=True)
    # 2d
    cmds.shadingNode('place2dTexture', name='UV2d', asShader=True)
    cmds.connectAttr('UV2d.outUV', 'UV_U.uvCoord', f=True)
    cmds.connectAttr('UV2d.outUV', 'UV_V.uvCoord', f=True)
    # aiutil
    cmds.shadingNode('aiUtility', name='UVI_util', asShader=True)
    cmds.setAttr('UVI_util.shadeMode', 2)
    cmds.connectAttr('UV_ALL.outColorR', 'UVI_util.colorR', f=True)
    cmds.connectAttr('UV_ALL.outColorG', 'UVI_util.colorG', f=True)
    cmds.connectAttr('UVInfo.facingRatio', 'UVI_util.colorB', f=True)
    # Aov
    cmds.connectAttr('UVI_util.outColor', 'aiAOV_uUVI.defaultValue', f=True)
    # cmds.connectAttr( 'UVI_util.outColor' , 'aiAOV_uUVI_aliased.defaultValue' , f=True)




def aov_toonaov():
    import maya.cmds as cmds
    import mtoa.aovs as aovs
    import maya.mel as mel


    aovs.AOVInterface().addAOV('toonFalloff', aovType='rgba')
    aovs.AOVInterface().addAOV('toonLines', aovType='rgba')
    aovs.AOVInterface().addAOV('toonRim_L', aovType='rgba')
    aovs.AOVInterface().addAOV('toonRim_L2', aovType='rgba')
    aovs.AOVInterface().addAOV('toonRim_R', aovType='rgba')
    aovs.AOVInterface().addAOV('toonRim_R2', aovType='rgba')
    # falloff
    # 쉐이더
    cmds.shadingNode('samplerInfo', name='Falloffnfo', asShader=True)
    cmds.shadingNode('ramp', name='toon_r', asShader=True)
    cmds.shadingNode('ramp', name='toon_g', asShader=True)
    cmds.shadingNode('ramp', name='toon_b', asShader=True)
    cmds.shadingNode('aiLayerRgba', name='falloff_layer', asShader=True)
    cmds.shadingNode('aiToon', name='toonFalloff', asShader=True)
    cmds.shadingNode('place2dTexture', name='falloff_2d', asShader=True)

    # 연결
    cmds.connectAttr('Falloffnfo.facingRatio', 'toon_r.uvCoord.uCoord', f=True)
    cmds.connectAttr('Falloffnfo.facingRatio', 'toon_g.uvCoord.uCoord', f=True)
    cmds.connectAttr('Falloffnfo.facingRatio', 'toon_b.uvCoord.uCoord', f=True)

    cmds.connectAttr('falloff_2d.outUV.outV', 'toon_r.uvCoord.vCoord', f=True)
    cmds.connectAttr('falloff_2d.outUV.outV', 'toon_g.uvCoord.vCoord', f=True)
    cmds.connectAttr('falloff_2d.outUV.outV', 'toon_b.uvCoord.vCoord', f=True)

    cmds.connectAttr('toon_r.outColor', 'falloff_layer.input1', f=True)
    cmds.connectAttr('toon_g.outColor', 'falloff_layer.input2', f=True)
    cmds.connectAttr('toon_b.outColor', 'falloff_layer.input3', f=True)

    cmds.connectAttr('falloff_layer.outColor', 'toonFalloff.baseColor', f=True)
    cmds.connectAttr('falloff_layer.outColor', 'toonFalloff.rimLightColor', f=True)

    # 타입 변환
    cmds.setAttr('falloff_layer.enable2', 1)
    cmds.setAttr('falloff_layer.enable3', 1)
    cmds.setAttr('falloff_layer.operation2', 30)
    cmds.setAttr('falloff_layer.operation3', 30)

    cmds.setAttr('toon_r.type', 1)
    cmds.setAttr('toon_r.colorEntryList[0].color', 1, 0, 0)
    cmds.setAttr('toon_r.colorEntryList[1].color', 0, 0, 0)
    cmds.setAttr('toon_r.colorEntryList[1].position', 0.7)

    cmds.setAttr('toon_g.type', 1)
    cmds.setAttr('toon_g.colorEntryList[0].color', 0, 1, 0)
    cmds.setAttr('toon_g.colorEntryList[1].color', 0, 0, 0)
    cmds.setAttr('toon_g.colorEntryList[1].position', 0.55)

    cmds.setAttr('toon_b.type', 1)
    cmds.setAttr('toon_b.colorEntryList[0].color', 0, 0, 1)
    cmds.setAttr('toon_b.colorEntryList[1].color', 0, 0, 0)
    cmds.setAttr('toon_b.colorEntryList[1].position', 0.4)

    cmds.setAttr('toonFalloff.base', 0)

    # Toonlines
    # 필터
    cmds.createNode('aiAOVFilter', n='toonLines_Filter', s=1)
    mel.eval('connectAttr -f toonLines_Filter.message aiAOV_toonLines.outputs[0].filter;')
    cmds.setAttr('toonLines_Filter.ai_translator', 'contour', type='string')
    # 쉐이더 노드 생성
    cmds.shadingNode('aiStateFloat', n='Rl_aiStateFloat', asShader=True)
    cmds.shadingNode('aiMultiply', n='raySceneScale_mult', asShader=True)
    cmds.shadingNode('aiAdd', n='toon_aiAdd', asShader=True)
    cmds.shadingNode('aiReciprocal', n='toon_aiReciprocal', asShader=True)
    cmds.shadingNode('aiMultiply', n='widthScalar_aiMultiply', asShader=True)
    cmds.shadingNode('aiFacingRatio', n='line_aiFacingRatio', asShader=True)
    cmds.shadingNode('aiRange', n='line_aiRange', asShader=True)
    cmds.shadingNode('aiMultiply', n='line_aiMultiply', asShader=True)
    cmds.shadingNode('aiCellNoise', n='line_aiCellNoise', asShader=True)
    cmds.shadingNode('aiRange', n='edgeColor_remap', asShader=True)
    cmds.shadingNode('ramp', n='line_ramp', asShader=True)
    cmds.shadingNode('aiFacingRatio', n='line_aiFacingRatio_2', asShader=True)
    cmds.shadingNode('ramp', n='facingRatio_ramp', asShader=True)
    cmds.shadingNode('aiLayerFloat', n='MaskColor_aiLayerFloat', asShader=True)
    cmds.shadingNode('aiNoise', n='line_aiNoise', asShader=True)
    cmds.shadingNode('aiRange', n='line_aiRange_2', asShader=True)
    cmds.shadingNode('aiCellNoise', n='line_aiCellNoise_2', asShader=True)
    cmds.shadingNode('aiRange', n='edgeBreakup_remap', asShader=True)
    cmds.shadingNode('aiToon', n='toonLine_r', asShader=True)
    cmds.shadingNode('aiFlat', n='toonLines_mtl', asShader=True)

    # 타입 변환
    cmds.setAttr("Rl_aiStateFloat.variable", 5)
    cmds.setAttr("raySceneScale_mult.input2", 0, 0, 0)
    cmds.setAttr("toon_aiAdd.input2", 1, 1, 1)
    cmds.setAttr("widthScalar_aiMultiply.input1", 1.25, 1.25, 1.25)
    cmds.setAttr("line_aiFacingRatio.bias", 0.675)
    cmds.setAttr("line_aiFacingRatio.invert", 1)
    cmds.setAttr("line_aiRange.contrast", 2.2)
    cmds.setAttr("line_aiCellNoise.pattern", 5)
    cmds.setAttr("line_aiCellNoise.octaves", 2)
    cmds.setAttr("line_aiCellNoise.scaleX", 0.2)
    cmds.setAttr("line_aiCellNoise.scaleY", 0.2)
    cmds.setAttr("line_aiCellNoise.scaleZ", 0.2)
    cmds.setAttr("edgeColor_remap.outputMin", 1)
    cmds.setAttr("edgeColor_remap.outputMax", 0)
    cmds.setAttr("edgeColor_remap.contrast", 1.8)
    cmds.setAttr("line_ramp.interpolation", 5)
    cmds.setAttr("line_ramp.colorEntryList[3].color", 0.077, 0.077, 0.077)
    cmds.setAttr("line_ramp.colorEntryList[3].position", 0.274)
    cmds.setAttr("line_ramp.colorEntryList[2].color", 0.5, 0.5, 0.5)
    cmds.setAttr("line_ramp.colorEntryList[2].position", 0.33)
    cmds.setAttr("line_ramp.colorEntryList[4].color", 0.567, 0.567, 0.567)
    cmds.setAttr("line_ramp.colorEntryList[4].position", 0.491)
    cmds.setAttr("line_ramp.colorEntryList[1].color", 1, 1, 1)
    cmds.setAttr("line_ramp.colorEntryList[1].position", 0.533)
    cmds.setAttr("facingRatio_ramp.colorEntryList[0].color", 1, 1, 1)
    cmds.setAttr("facingRatio_ramp.colorEntryList[2].color", 0.086, 0.086, 0.086)
    cmds.setAttr("facingRatio_ramp.colorEntryList[2].position", 0.325)
    cmds.setAttr("facingRatio_ramp.colorEntryList[1].color", 0, 0, 0)
    cmds.setAttr("facingRatio_ramp.colorEntryList[1].position", 0.675)
    cmds.setAttr("MaskColor_aiLayerFloat.input1", 0.5)
    cmds.setAttr("MaskColor_aiLayerFloat.enable2", 1)
    cmds.setAttr("line_aiNoise.distortion", 0.1)
    cmds.setAttr("line_aiNoise.lacunarity", 1.5)
    cmds.setAttr("line_aiNoise.scaleX", 0.3)
    cmds.setAttr("line_aiNoise.scaleY", 0.3)
    cmds.setAttr("line_aiRange_2.outputMax", 0.5)
    cmds.setAttr("line_aiRange_2.contrast", 3)
    cmds.setAttr("line_aiCellNoise_2.lacunarity", 1.2)
    cmds.setAttr("line_aiCellNoise_2.scaleX", 0.06)
    cmds.setAttr("line_aiCellNoise_2.scaleY", 0.06)
    cmds.setAttr("edgeBreakup_remap.outputMin", 0.45)
    cmds.setAttr("edgeBreakup_remap.outputMax", 0.55)
    cmds.setAttr("toonLine_r.edgeColor", 1, 0, 0)
    cmds.setAttr("toonLine_r.angleThreshold", 60)
    cmds.setAttr("toonLine_r.base", 0)

    # 연결
    cmds.connectAttr('Rl_aiStateFloat.outTransparency', 'raySceneScale_mult.input1')
    cmds.connectAttr('raySceneScale_mult.outColor', 'toon_aiAdd.input1')
    cmds.connectAttr('toon_aiAdd.outColor', 'toon_aiReciprocal.input')
    cmds.connectAttr('toon_aiReciprocal.outColor', 'widthScalar_aiMultiply.input2')
    cmds.connectAttr('line_aiFacingRatio.outValue', 'line_aiRange.input.inputR')
    cmds.connectAttr('widthScalar_aiMultiply.outColor', 'line_aiMultiply.input1')
    cmds.connectAttr('line_aiRange.outColor', 'line_aiMultiply.input2')
    cmds.connectAttr('line_aiCellNoise.outColor', 'edgeColor_remap.input')
    cmds.connectAttr('edgeColor_remap.outColor.outColorR', 'line_ramp.uvCoord.vCoord')
    cmds.connectAttr('line_aiFacingRatio_2.outValue', 'facingRatio_ramp.uvCoord.vCoord')
    cmds.connectAttr('facingRatio_ramp.outColor.outColorR', 'MaskColor_aiLayerFloat.mix2')
    cmds.connectAttr('line_aiNoise.outColor', 'line_aiRange_2.input')
    cmds.connectAttr('line_aiRange_2.outColor.outColorR', 'line_aiCellNoise_2.offset.offsetX')
    cmds.connectAttr('line_aiRange_2.outColor.outColorR', 'line_aiCellNoise_2.offset.offsetY')
    cmds.connectAttr('line_aiCellNoise_2.outColor', 'edgeBreakup_remap.input')
    cmds.connectAttr('edgeBreakup_remap.outColor.outColorR', 'MaskColor_aiLayerFloat.input2')
    cmds.connectAttr('line_ramp.outColor.outColorR', 'toonLine_r.edgeOpacity')
    cmds.connectAttr('line_aiMultiply.outColor.outColorR', 'toonLine_r.edgeWidthScale')
    cmds.connectAttr('MaskColor_aiLayerFloat.outTransparency', 'toonLine_r.maskColor')
    cmds.connectAttr('toonLine_r.outColor', 'toonLines_mtl.color')

    # RIM
    # 쉐이더
    # R
    cmds.shadingNode('aiRampRgb', name='airamp_Rr', asShader=True)
    cmds.shadingNode('aiRampRgb', name='airamp_Rg', asShader=True)
    cmds.shadingNode('aiRampRgb', name='airamp_Rb', asShader=True)
    cmds.shadingNode('aiLayerRgba', name='rimR_layer', asShader=True)
    cmds.shadingNode('aiToon', name='toonrimR', asShader=True)

    # R2
    cmds.shadingNode('aiRampRgb', name='airamp_R2r', asShader=True)
    cmds.shadingNode('aiRampRgb', name='airamp_R2g', asShader=True)
    cmds.shadingNode('aiRampRgb', name='airamp_R2b', asShader=True)
    cmds.shadingNode('aiLayerRgba', name='rimR2_layer', asShader=True)
    cmds.shadingNode('aiToon', name='toonrimR2', asShader=True)

    # L
    cmds.shadingNode('aiRampRgb', name='airamp_Lr', asShader=True)
    cmds.shadingNode('aiRampRgb', name='airamp_Lg', asShader=True)
    cmds.shadingNode('aiRampRgb', name='airamp_Lb', asShader=True)
    cmds.shadingNode('aiLayerRgba', name='rimL_layer', asShader=True)
    cmds.shadingNode('aiToon', name='toonrimL', asShader=True)
    # L2
    cmds.shadingNode('aiRampRgb', name='airamp_L2r', asShader=True)
    cmds.shadingNode('aiRampRgb', name='airamp_L2g', asShader=True)
    cmds.shadingNode('aiRampRgb', name='airamp_L2b', asShader=True)
    cmds.shadingNode('aiLayerRgba', name='rimL2_layer', asShader=True)
    cmds.shadingNode('aiToon', name='toonrimL2', asShader=True)

    # 연결
    # R
    cmds.connectAttr('airamp_Rr.outColor', 'rimR_layer.input1', f=True)
    cmds.connectAttr('airamp_Rg.outColor', 'rimR_layer.input2', f=True)
    cmds.connectAttr('airamp_Rb.outColor', 'rimR_layer.input3', f=True)

    cmds.connectAttr('rimR_layer.outColor', 'toonrimR.rimLightColor', f=True)

    # R2
    cmds.connectAttr('airamp_R2r.outColor', 'rimR2_layer.input1', f=True)
    cmds.connectAttr('airamp_R2g.outColor', 'rimR2_layer.input2', f=True)
    cmds.connectAttr('airamp_R2b.outColor', 'rimR2_layer.input3', f=True)

    cmds.connectAttr('rimR2_layer.outColor', 'toonrimR2.rimLightColor', f=True)

    # L
    cmds.connectAttr('airamp_Lr.outColor', 'rimL_layer.input1', f=True)
    cmds.connectAttr('airamp_Lg.outColor', 'rimL_layer.input2', f=True)
    cmds.connectAttr('airamp_Lb.outColor', 'rimL_layer.input3', f=True)

    cmds.connectAttr('rimL_layer.outColor', 'toonrimL.rimLightColor', f=True)

    # L2
    cmds.connectAttr('airamp_L2r.outColor', 'rimL2_layer.input1', f=True)
    cmds.connectAttr('airamp_L2g.outColor', 'rimL2_layer.input2', f=True)
    cmds.connectAttr('airamp_L2b.outColor', 'rimL2_layer.input3', f=True)

    cmds.connectAttr('rimL2_layer.outColor', 'toonrimL2.rimLightColor', f=True)
    # 타입 변환
    # R
    cmds.setAttr('rimR_layer.enable2', 1)
    cmds.setAttr('rimR_layer.enable3', 1)
    cmds.setAttr('rimR_layer.operation2', 30)
    cmds.setAttr('rimR_layer.operation3', 30)

    cmds.setAttr('airamp_Rr.ramp[0].ramp_Color', 0, 0, 0)
    cmds.setAttr('airamp_Rr.ramp[0].ramp_Position', 0.65)
    cmds.setAttr('airamp_Rr.ramp[1].ramp_Color', 1, 0, 0)
    cmds.setAttr('airamp_Rr.ramp[1].ramp_Position', 0.68)

    cmds.setAttr('airamp_Rg.ramp[0].ramp_Color', 0, 0, 0)
    cmds.setAttr('airamp_Rg.ramp[0].ramp_Position', 0.7)
    cmds.setAttr('airamp_Rg.ramp[1].ramp_Color', 0, 1, 0)
    cmds.setAttr('airamp_Rg.ramp[1].ramp_Position', 0.73)

    cmds.setAttr('airamp_Rb.ramp[0].ramp_Color', 0, 0, 0)
    cmds.setAttr('airamp_Rb.ramp[0].ramp_Position', 0.8)
    cmds.setAttr('airamp_Rb.ramp[1].ramp_Color', 0, 0, 1)
    cmds.setAttr('airamp_Rb.ramp[1].ramp_Position', 0.82)

    cmds.setAttr('toonrimR.enable', 0)
    cmds.setAttr('toonrimR.edgeTonemap', 0, 0, 0)
    cmds.setAttr('toonrimR.idDifference', 0)
    cmds.setAttr('toonrimR.shaderDifference', 0)
    cmds.setAttr('toonrimR.silhouetteTonemap', 0, 0, 0)
    cmds.setAttr('toonrimR.base', 0)
    cmds.setAttr('toonrimR.baseColor', 0, 0, 0)
    cmds.setAttr('toonrimR.baseTonemap', 0, 0, 0)
    cmds.setAttr('toonrimR.highlightColor', 0, 0, 0)
    cmds.setAttr('toonrimR.highlightSize', 0)

    # R2
    cmds.setAttr('rimR2_layer.enable2', 1)
    cmds.setAttr('rimR2_layer.enable3', 1)
    cmds.setAttr('rimR2_layer.operation2', 30)
    cmds.setAttr('rimR2_layer.operation3', 30)

    cmds.setAttr('airamp_R2r.ramp[0].ramp_Color', 0, 0, 0)
    cmds.setAttr('airamp_R2r.ramp[0].ramp_Position', 0.5)
    cmds.setAttr('airamp_R2r.ramp[1].ramp_Color', 1, 0, 0)
    cmds.setAttr('airamp_R2r.ramp[1].ramp_Position', 0.6)

    cmds.setAttr('airamp_R2g.ramp[0].ramp_Color', 0, 0, 0)
    cmds.setAttr('airamp_R2g.ramp[0].ramp_Position', 0.65)
    cmds.setAttr('airamp_R2g.ramp[1].ramp_Color', 0, 1, 0)
    cmds.setAttr('airamp_R2g.ramp[1].ramp_Position', 0.75)

    cmds.setAttr('airamp_R2b.ramp[0].ramp_Color', 0, 0, 0)
    cmds.setAttr('airamp_R2b.ramp[0].ramp_Position', 0.75)
    cmds.setAttr('airamp_R2b.ramp[1].ramp_Color', 0, 0, 1)
    cmds.setAttr('airamp_R2b.ramp[1].ramp_Position', 0.85)

    cmds.setAttr('toonrimR2.enable', 0)
    cmds.setAttr('toonrimR2.edgeTonemap', 0, 0, 0)
    cmds.setAttr('toonrimR2.idDifference', 0)
    cmds.setAttr('toonrimR2.shaderDifference', 0)
    cmds.setAttr('toonrimR2.silhouetteTonemap', 0, 0, 0)
    cmds.setAttr('toonrimR2.base', 0)
    cmds.setAttr('toonrimR2.baseColor', 0, 0, 0)
    cmds.setAttr('toonrimR2.baseTonemap', 0, 0, 0)
    cmds.setAttr('toonrimR2.highlightColor', 0, 0, 0)
    cmds.setAttr('toonrimR2.highlightSize', 0)

    # L
    cmds.setAttr('rimL_layer.enable2', 1)
    cmds.setAttr('rimL_layer.enable3', 1)
    cmds.setAttr('rimL_layer.operation2', 30)
    cmds.setAttr('rimL_layer.operation3', 30)

    cmds.setAttr('airamp_Lr.ramp[0].ramp_Color', 0, 0, 0)
    cmds.setAttr('airamp_Lr.ramp[0].ramp_Position', 0.65)
    cmds.setAttr('airamp_Lr.ramp[1].ramp_Color', 1, 0, 0)
    cmds.setAttr('airamp_Lr.ramp[1].ramp_Position', 0.68)

    cmds.setAttr('airamp_Lg.ramp[0].ramp_Color', 0, 0, 0)
    cmds.setAttr('airamp_Lg.ramp[0].ramp_Position', 0.7)
    cmds.setAttr('airamp_Lg.ramp[1].ramp_Color', 0, 1, 0)
    cmds.setAttr('airamp_Lg.ramp[1].ramp_Position', 0.73)

    cmds.setAttr('airamp_Lb.ramp[0].ramp_Color', 0, 0, 0)
    cmds.setAttr('airamp_Lb.ramp[0].ramp_Position', 0.8)
    cmds.setAttr('airamp_Lb.ramp[1].ramp_Color', 0, 0, 1)
    cmds.setAttr('airamp_Lb.ramp[1].ramp_Position', 0.82)

    cmds.setAttr('toonrimL.enable', 0)
    cmds.setAttr('toonrimL.edgeTonemap', 0, 0, 0)
    cmds.setAttr('toonrimL.idDifference', 0)
    cmds.setAttr('toonrimL.shaderDifference', 0)
    cmds.setAttr('toonrimL.silhouetteTonemap', 0, 0, 0)
    cmds.setAttr('toonrimL.base', 0)
    cmds.setAttr('toonrimL.baseColor', 0, 0, 0)
    cmds.setAttr('toonrimL.baseTonemap', 0, 0, 0)
    cmds.setAttr('toonrimL.highlightColor', 0, 0, 0)
    cmds.setAttr('toonrimL.highlightSize', 0)

    # L2
    cmds.setAttr('rimL2_layer.enable2', 1)
    cmds.setAttr('rimL2_layer.enable3', 1)
    cmds.setAttr('rimL2_layer.operation2', 30)
    cmds.setAttr('rimL2_layer.operation3', 30)

    cmds.setAttr('airamp_L2r.ramp[0].ramp_Color', 0, 0, 0)
    cmds.setAttr('airamp_L2r.ramp[0].ramp_Position', 0.5)
    cmds.setAttr('airamp_L2r.ramp[1].ramp_Color', 1, 0, 0)
    cmds.setAttr('airamp_L2r.ramp[1].ramp_Position', 0.6)

    cmds.setAttr('airamp_L2g.ramp[0].ramp_Color', 0, 0, 0)
    cmds.setAttr('airamp_L2g.ramp[0].ramp_Position', 0.65)
    cmds.setAttr('airamp_L2g.ramp[1].ramp_Color', 0, 1, 0)
    cmds.setAttr('airamp_L2g.ramp[1].ramp_Position', 0.75)

    cmds.setAttr('airamp_L2b.ramp[0].ramp_Color', 0, 0, 0)
    cmds.setAttr('airamp_L2b.ramp[0].ramp_Position', 0.75)
    cmds.setAttr('airamp_L2b.ramp[1].ramp_Color', 0, 0, 1)
    cmds.setAttr('airamp_L2b.ramp[1].ramp_Position', 0.85)

    cmds.setAttr('toonrimL2.enable', 0)
    cmds.setAttr('toonrimL2.edgeTonemap', 0, 0, 0)
    cmds.setAttr('toonrimL2.idDifference', 0)
    cmds.setAttr('toonrimL2.shaderDifference', 0)
    cmds.setAttr('toonrimL2.silhouetteTonemap', 0, 0, 0)
    cmds.setAttr('toonrimL2.base', 0)
    cmds.setAttr('toonrimL2.baseColor', 0, 0, 0)
    cmds.setAttr('toonrimL2.baseTonemap', 0, 0, 0)
    cmds.setAttr('toonrimL2.highlightColor', 0, 0, 0)
    cmds.setAttr('toonrimL2.highlightSize', 0)

    # 라이트
    cmds.directionalLight(rotation=(-130, -30, 0))
    cmds.rename("directionalLight1", "toon_R_lit")
    mel.eval('setAttr -type "string" toonrimR.rimLight "toon_R_litShape"')
    mel.eval('setAttr -type "string" toonrimR2.rimLight "toon_R_litShape"')

    cmds.directionalLight(rotation=(-130, 30, 0))
    cmds.rename("directionalLight1", "toon_L_lit")
    mel.eval('setAttr -type "string" toonrimL.rimLight "toon_L_litShape"')
    mel.eval('setAttr -type "string" toonrimL2.rimLight "toon_L_litShape"')

    # aov
    cmds.connectAttr('toonFalloff.outColor', 'aiAOV_toonFalloff.defaultValue', f=True)
    cmds.connectAttr('toonLines_mtl.outColor', 'aiAOV_toonLines.defaultValue', f=True)
    cmds.connectAttr('toonrimL.outColor', 'aiAOV_toonRim_L.defaultValue', f=True)
    cmds.connectAttr('toonrimL2.outColor', 'aiAOV_toonRim_L2.defaultValue', f=True)
    cmds.connectAttr('toonrimR.outColor', 'aiAOV_toonRim_R.defaultValue', f=True)
    cmds.connectAttr('toonrimR2.outColor', 'aiAOV_toonRim_R2.defaultValue', f=True)







def aov_toonUtill():
    import maya.cmds as cmds
    import mtoa.aovs as aovs
    

    aovs.AOVInterface().addAOV('ToonUtill', aovType='rgba')
    aovs.AOVInterface().addAOV('ToonUtill2', aovType='rgba')
    aovs.AOVInterface().addAOV('ToonUtill3', aovType='rgba')
    # toonUtill
    # 쉐이더 노드 생성
    cmds.shadingNode('file', n='c_data', asShader=True)
    cmds.shadingNode('place2dTexture', n='c_data_2d', asShader=True)
    cmds.shadingNode('aiRange', n='toonDIF_Premap', asShader=True)
    cmds.shadingNode('aiRampRgb', n='toonDIF_toneRamp', asShader=True)
    cmds.shadingNode('aiToon', n='toonDiffuse_r', asShader=True)
    cmds.shadingNode('aiRange', n='toonRGH_Premap', asShader=True)
    cmds.shadingNode('aiRampRgb', n='toonRGH_toneRamp', asShader=True)
    cmds.shadingNode('aiToon', n='toonSpec_g', asShader=True)
    cmds.shadingNode('file', n='a_data', asShader=True)
    cmds.shadingNode('place2dTexture', n='a_data_2d', asShader=True)
    cmds.shadingNode('aiRange', n='toonRGH_remap', asShader=True)
    cmds.shadingNode('aiUtility', n='ndoteye', asShader=True)
    cmds.shadingNode('aiLayerRgba', n='toonUtils_aiLayerRgba', asShader=True)
    cmds.shadingNode('aiFlat', n='toonUtils_mtl', asShader=True)

    # 타입 변환
    cmds.setAttr('c_data.fileTextureName', (
        'Q:\\lt_team\\seungah_lee\\ALS17\\03_seq\\ALS_0000\\toonaov\\textures\83edcf\\concept_brushy_data.tif'),
                 type="string")
    cmds.setAttr('c_data.colorSpace', 'Raw', type='string')
    cmds.setAttr("c_data.ignoreColorSpaceFileRules", 1)
    cmds.setAttr("c_data_2d.repeatU", 0.6)
    cmds.setAttr("c_data_2d.repeatV", 0.6)
    cmds.setAttr("toonDIF_Premap.outputMin", 0.05)
    cmds.setAttr("toonDIF_Premap.outputMax", 0.75)
    cmds.setAttr('toonDIF_toneRamp.ramp[0].ramp_Interp', 0)
    cmds.setAttr('toonDIF_toneRamp.ramp[1].ramp_Interp', 0)
    cmds.setAttr('toonDIF_toneRamp.ramp[1].ramp_Color', 1, 0, 0)
    cmds.setAttr("toonDiffuse_r.enable", 0)
    cmds.setAttr("toonDiffuse_r.edgeColor", 0, 0, 1)
    cmds.setAttr("toonDiffuse_r.angleThreshold", 60)
    cmds.setAttr("toonDiffuse_r.base", 1)
    cmds.setAttr("toonDiffuse_r.specularRoughness", 0.3)
    cmds.setAttr("toonDiffuse_r.specularTonemap", 0, 0, 0)
    cmds.setAttr("toonRGH_Premap.outputMin", 0.7)
    cmds.setAttr("toonRGH_Premap.outputMax", 0.99)
    cmds.setAttr('toonRGH_toneRamp.ramp[0].ramp_Interp', 1)
    cmds.setAttr('toonRGH_toneRamp.ramp[1].ramp_Interp', 0)
    cmds.setAttr('toonRGH_toneRamp.ramp[1].ramp_Color', 0, 1, 0)
    cmds.setAttr("toonSpec_g.enable", 0)
    cmds.setAttr("toonSpec_g.base", 0)
    cmds.setAttr("toonSpec_g.specular", 0)
    cmds.setAttr('a_data.fileTextureName', (
        'Q:\\lt_team\\seungah_lee\\ALS17\\03_seq\\ALS_0000\\toonaov\\textures\83edcf\\angular_generic_data.tif'),
                 type="string")
    cmds.setAttr('a_data.colorSpace', 'Raw', type='string')
    cmds.setAttr("a_data.ignoreColorSpaceFileRules", 1)
    cmds.setAttr("a_data_2d.repeatU", 0.75)
    cmds.setAttr("a_data_2d.repeatV", 0.75)
    cmds.setAttr("toonRGH_remap.outputMin", 0.1)
    cmds.setAttr("toonRGH_remap.outputMax", 0.6)
    cmds.setAttr("toonUtils_aiLayerRgba.enable2", 1)
    cmds.setAttr("toonUtils_aiLayerRgba.operation2", 30)
    cmds.setAttr("toonUtils_aiLayerRgba.enable3", 1)
    cmds.setAttr("toonUtils_aiLayerRgba.operation3", 30)
    cmds.setAttr("ndoteye.color", 0, 0, 1)

    # 연결
    cmds.connectAttr('c_data_2d.outUV', 'c_data.uvCoord')
    cmds.connectAttr('c_data_2d.outUvFilterSize', 'c_data.uvFilterSize')
    cmds.connectAttr('c_data_2d.coverage', 'c_data.coverage')
    cmds.connectAttr('c_data_2d.translateFrame', 'c_data.translateFrame')
    cmds.connectAttr('c_data_2d.rotateFrame', 'c_data.rotateFrame')
    cmds.connectAttr('c_data_2d.mirrorU', 'c_data.mirrorU')
    cmds.connectAttr('c_data_2d.mirrorV', 'c_data.mirrorV')
    cmds.connectAttr('c_data_2d.stagger', 'c_data.stagger')
    cmds.connectAttr('c_data_2d.wrapU', 'c_data.wrapU')
    cmds.connectAttr('c_data_2d.wrapV', 'c_data.wrapV')
    cmds.connectAttr('c_data_2d.repeatUV', 'c_data.repeatUV')
    cmds.connectAttr('c_data_2d.vertexUvOne', 'c_data.vertexUvOne')
    cmds.connectAttr('c_data_2d.vertexUvTwo', 'c_data.vertexUvTwo')
    cmds.connectAttr('c_data_2d.vertexUvThree', 'c_data.vertexUvThree')
    cmds.connectAttr('c_data_2d.vertexCameraOne', 'c_data.vertexCameraOne')
    cmds.connectAttr('c_data_2d.noiseUV', 'c_data.noiseUV')
    cmds.connectAttr('c_data_2d.offset', 'c_data.offset')
    cmds.connectAttr('c_data_2d.rotateUV', 'c_data.rotateUV')

    cmds.connectAttr('c_data.outColor', 'toonDIF_Premap.input')
    cmds.connectAttr('toonDIF_Premap.outColorR', 'toonDIF_toneRamp.ramp[1].ramp_Position', force=True)
    cmds.connectAttr('toonDIF_toneRamp.outColor', 'toonDiffuse_r.baseTonemap')
    cmds.connectAttr('toonDiffuse_r.outColor', 'toonUtils_aiLayerRgba.input1')
    cmds.connectAttr('c_data.outColor', 'toonRGH_Premap.input')
    cmds.connectAttr('toonRGH_Premap.outColorR', 'toonRGH_toneRamp.ramp[1].ramp_Position', force=True)
    cmds.connectAttr('toonRGH_toneRamp.outColor', 'toonSpec_g.specularTonemap')

    cmds.connectAttr('a_data_2d.outUV', 'a_data.uvCoord')
    cmds.connectAttr('a_data_2d.outUvFilterSize', 'a_data.uvFilterSize')
    cmds.connectAttr('a_data_2d.coverage', 'a_data.coverage')
    cmds.connectAttr('a_data_2d.translateFrame', 'a_data.translateFrame')
    cmds.connectAttr('a_data_2d.rotateFrame', 'a_data.rotateFrame')
    cmds.connectAttr('a_data_2d.mirrorU', 'a_data.mirrorU')
    cmds.connectAttr('a_data_2d.mirrorV', 'a_data.mirrorV')
    cmds.connectAttr('a_data_2d.stagger', 'a_data.stagger')
    cmds.connectAttr('a_data_2d.wrapU', 'a_data.wrapU')
    cmds.connectAttr('a_data_2d.wrapV', 'a_data.wrapV')
    cmds.connectAttr('a_data_2d.repeatUV', 'a_data.repeatUV')
    cmds.connectAttr('a_data_2d.vertexUvOne', 'a_data.vertexUvOne')
    cmds.connectAttr('a_data_2d.vertexUvTwo', 'a_data.vertexUvTwo')
    cmds.connectAttr('a_data_2d.vertexUvThree', 'a_data.vertexUvThree')
    cmds.connectAttr('a_data_2d.vertexCameraOne', 'a_data.vertexCameraOne')
    cmds.connectAttr('a_data_2d.noiseUV', 'a_data.noiseUV')
    cmds.connectAttr('a_data_2d.offset', 'a_data.offset')
    cmds.connectAttr('a_data_2d.rotateUV', 'a_data.rotateUV')
    cmds.connectAttr('a_data.outColor', 'toonRGH_remap.input')
    cmds.connectAttr('toonRGH_remap.outColor.outColorR', 'toonSpec_g.specularRoughness')
    cmds.connectAttr('toonSpec_g.outColor', 'toonUtils_aiLayerRgba.input2')

    cmds.connectAttr('ndoteye.outColor', 'toonUtils_aiLayerRgba.input3')

    cmds.connectAttr('toonUtils_aiLayerRgba.outColor', 'toonUtils_mtl.color')
    cmds.connectAttr('toonUtils_mtl.outColor', 'aiAOV_ToonUtill.defaultValue')

    # toonUtil2
    # 쉐이더 노드 생성
    cmds.shadingNode('aiRange', n='toonDIF_2_Premap', asShader=True)
    cmds.shadingNode('aiRampRgb', n='toonDIF__2toneRamp', asShader=True)
    cmds.shadingNode('aiToon', n='toonDiffuse_2_r', asShader=True)
    cmds.shadingNode('file', n='c_data_2', asShader=True)
    cmds.shadingNode('place2dTexture', n='c_data_2d_2', asShader=True)
    cmds.shadingNode('file', n='b_data', asShader=True)
    cmds.shadingNode('place2dTexture', n='b_data_2d', asShader=True)
    cmds.shadingNode('aiAmbientOcclusion', n='toonUtill2_occ', asShader=True)
    cmds.shadingNode('aiLayerRgba', n='toonUtils_2_aiLayerRgba', asShader=True)
    cmds.shadingNode('aiFlat', n='toonUtils_2_mtl', asShader=True)

    # 타입 변환
    cmds.setAttr('toonDIF_2_Premap.outputMin', 0.5)
    cmds.setAttr('toonDIF_2_Premap.outputMax', 0.99)
    cmds.setAttr('toonDIF__2toneRamp.ramp[0].ramp_Interp', 0)
    cmds.setAttr('toonDIF__2toneRamp.ramp[1].ramp_Interp', 0)
    cmds.setAttr('toonDIF__2toneRamp.ramp[1].ramp_Color', 1, 0, 0)
    cmds.setAttr('c_data_2.fileTextureName', (
        'Q:\\lt_team\\seungah_lee\\ALS17\\03_seq\\ALS_0000\\toonaov\\textures\83edcf\\concept_brushy_data.tif'),
                 type="string")
    cmds.setAttr('c_data_2.colorSpace', 'Raw', type='string')
    cmds.setAttr("c_data_2.ignoreColorSpaceFileRules", 1)
    cmds.setAttr('b_data.fileTextureName', (
        'Q:\\lt_team\\seungah_lee\\ALS17\\03_seq\\ALS_0000\\toonaov\\textures\83edcf\\brushy_b_desat_data.png'),
                 type="string")
    cmds.setAttr('b_data.colorSpace', 'Raw', type='string')
    cmds.setAttr("c_data.ignoreColorSpaceFileRules", 1)
    cmds.setAttr('toonDiffuse_2_r.enable', 0)
    cmds.setAttr('toonDiffuse_2_r.idDifference', 0)
    cmds.setAttr('toonDiffuse_2_r.shaderDifference', 0)
    cmds.setAttr('toonUtils_2_aiLayerRgba.enable2', 1)
    cmds.setAttr('toonUtils_2_aiLayerRgba.operation2', 30)
    cmds.setAttr('toonUtils_2_aiLayerRgba.input2', 0, 1, 0)
    cmds.setAttr('toonUtils_2_aiLayerRgba.enable3', 1)
    cmds.setAttr('toonUtils_2_aiLayerRgba.operation3', 30)
    cmds.setAttr('toonUtils_2_aiLayerRgba.input3', 0, 0, 1)

    # 연결
    cmds.connectAttr('c_data_2d_2.outUV', 'c_data_2.uvCoord')
    cmds.connectAttr('c_data_2d_2.outUvFilterSize', 'c_data_2.uvFilterSize')
    cmds.connectAttr('c_data_2d_2.coverage', 'c_data_2.coverage')
    cmds.connectAttr('c_data_2d_2.translateFrame', 'c_data_2.translateFrame')
    cmds.connectAttr('c_data_2d_2.rotateFrame', 'c_data_2.rotateFrame')
    cmds.connectAttr('c_data_2d_2.mirrorU', 'c_data_2.mirrorU')
    cmds.connectAttr('c_data_2d_2.mirrorV', 'c_data_2.mirrorV')
    cmds.connectAttr('c_data_2d_2.stagger', 'c_data_2.stagger')
    cmds.connectAttr('c_data_2d_2.wrapU', 'c_data_2.wrapU')
    cmds.connectAttr('c_data_2d_2.wrapV', 'c_data_2.wrapV')
    cmds.connectAttr('c_data_2d_2.repeatUV', 'c_data_2.repeatUV')
    cmds.connectAttr('c_data_2d_2.vertexUvOne', 'c_data_2.vertexUvOne')
    cmds.connectAttr('c_data_2d_2.vertexUvTwo', 'c_data_2.vertexUvTwo')
    cmds.connectAttr('c_data_2d_2.vertexUvThree', 'c_data_2.vertexUvThree')
    cmds.connectAttr('c_data_2d_2.vertexCameraOne', 'c_data_2.vertexCameraOne')
    cmds.connectAttr('c_data_2d_2.noiseUV', 'c_data_2.noiseUV')
    cmds.connectAttr('c_data_2d_2.offset', 'c_data_2.offset')
    cmds.connectAttr('c_data_2d_2.rotateUV', 'c_data_2.rotateUV')

    cmds.connectAttr('c_data_2.outColor', 'toonDIF_2_Premap.input')
    cmds.connectAttr('toonDIF_2_Premap.outColorR', 'toonDIF__2toneRamp.ramp[1].ramp_Position', force=True)
    cmds.connectAttr('toonDIF__2toneRamp.outColor', 'toonDiffuse_2_r.baseTonemap')
    cmds.connectAttr('toonDiffuse_2_r.outColor', 'toonUtils_2_aiLayerRgba.input1')
    cmds.connectAttr('toonUtill2_occ.outColor.outColorR', 'toonUtils_2_aiLayerRgba.mix3')
    cmds.connectAttr('b_data_2d.outUV', 'b_data.uvCoord')
    cmds.connectAttr('b_data_2d.outUvFilterSize', 'b_data.uvFilterSize')
    cmds.connectAttr('b_data_2d.coverage', 'b_data.coverage')
    cmds.connectAttr('b_data_2d.translateFrame', 'b_data.translateFrame')
    cmds.connectAttr('b_data_2d.rotateFrame', 'b_data.rotateFrame')
    cmds.connectAttr('b_data_2d.mirrorU', 'b_data.mirrorU')
    cmds.connectAttr('b_data_2d.mirrorV', 'b_data.mirrorV')
    cmds.connectAttr('b_data_2d.stagger', 'b_data.stagger')
    cmds.connectAttr('b_data_2d.wrapU', 'b_data.wrapU')
    cmds.connectAttr('b_data_2d.wrapV', 'b_data.wrapV')
    cmds.connectAttr('b_data_2d.repeatUV', 'b_data.repeatUV')
    cmds.connectAttr('b_data_2d.vertexUvOne', 'b_data.vertexUvOne')
    cmds.connectAttr('b_data_2d.vertexUvTwo', 'b_data.vertexUvTwo')
    cmds.connectAttr('b_data_2d.vertexUvThree', 'b_data.vertexUvThree')
    cmds.connectAttr('b_data_2d.vertexCameraOne', 'b_data.vertexCameraOne')
    cmds.connectAttr('b_data_2d.noiseUV', 'b_data.noiseUV')
    cmds.connectAttr('b_data_2d.offset', 'b_data.offset')
    cmds.connectAttr('b_data_2d.rotateUV', 'b_data.rotateUV')
    cmds.connectAttr('b_data.outColor.outColorR', 'toonUtils_2_aiLayerRgba.mix2')

    cmds.connectAttr('toonUtils_2_aiLayerRgba.outColor', 'toonUtils_2_mtl.color')
    cmds.connectAttr('toonUtils_2_mtl.outColor', 'aiAOV_ToonUtill2.defaultValue')

    # toonUtil3
    # 쉐이더
    cmds.shadingNode('aiCurvature', n='toonutill_aiCurvature', asShader=True)
    cmds.shadingNode('aiClamp', n='toonutill_aiClamp', asShader=True)
    cmds.shadingNode('aiLayerRgba', name='toonutill_aiLayerRgba', asShader=True)
    cmds.shadingNode('aiFlat', name='toon_util', asShader=True)

    # 타입 변환
    cmds.setAttr('toonutill_aiCurvature.output', 2)
    cmds.setAttr('toonutill_aiCurvature.samples', 5)
    cmds.setAttr('toonutill_aiCurvature.radius', 0.3)
    cmds.setAttr('toonutill_aiCurvature.bias', 0.5)
    cmds.setAttr('toonutill_aiCurvature.multiply', 2)

    # 연결
    cmds.connectAttr('toonutill_aiCurvature.outColor', 'toonutill_aiClamp.input')
    cmds.connectAttr('toonutill_aiClamp.outColor', 'toonutill_aiLayerRgba.input1')
    cmds.connectAttr('toonutill_aiLayerRgba.outColor', 'toon_util.color')
    cmds.connectAttr('toon_util.outColor', 'aiAOV_ToonUtill3.defaultValue')
