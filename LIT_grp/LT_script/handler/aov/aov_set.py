def AOV_ONOFF(AOV_ON):
    from maya.app.renderSetup.model import renderSetup
    import maya.cmds as cmds

    selected = AOV_ON
    layer = renderSetup.instance().getVisibleRenderLayer()
    sel = cmds.ls(sl=1, type="aiAOV")
    aovCollection = layer.aovCollectionInstance()
    aovChildCollections = aovCollection.getCollections()
    for aovChildCollection in aovChildCollections:
        aov_encode = aovCollection.encode()
        aov_child = aov_encode['aovCollection']['children']
        aov_over = []
        for x in aov_child:
            aov_over.append(x['aovChildCollection']['selector']['arnoldAOVChildSelector']['arnoldAOVNodeName'])
    if selected == 1:
        for i in sel:
            if i in aov_over:
                cmds.setAttr(i + ".enabled", 1)
            else:
                override_ = layer.createAbsoluteOverride(i, 'enabled')
                print(override_.setAttrValue(1))  # 0은 언에이블 체크 끄기, 1은 언에이블 켜짐

    elif selected == 0:
        for i in sel:
            if i in aov_over:
                cmds.setAttr(i + ".enabled", 0)

            else:
                override_ = layer.createAbsoluteOverride(i, 'enabled')
                print(override_.setAttrValue(0))  # 0은 언에이블 체크 끄기, 1은 언에이블 켜짐




######################## aov_set ##########################




def OFF_Aovset():
    import maya.cmds as cmds
    aov = cmds.ls(type='aiAOV')
    for i in aov:
        cmds.setAttr(i + ".enabled", 0)







def default_Aovset():
    import maya.cmds as cmds
    from maya.app.renderSetup.model import renderSetup

    rs = renderSetup.instance()
    layer1 = rs.getRenderLayer('ch_beauty')
    layer2 = rs.getRenderLayer('bg_beauty')
    aov = cmds.ls(type='aiAOV')
    chlist = ['aiAOV_N', 'aiAOV_P', 'aiAOV_Z', 'aiAOV_albedo', 'aiAOV_coat_direct', 'aiAOV_coat_indirect',
              'aiAOV_crypto_asset', 'aiAOV_crypto_material', 'aiAOV_crypto_object', 'aiAOV_diffuse_direct',
              'aiAOV_diffuse_indirect', 'aiAOV_emission', 'aiAOV_motionvector', 'aiAOV_occ', 'aiAOV_sheen_indirect',
              'aiAOV_sheen_direct', 'aiAOV_specular', 'aiAOV_specular_direct', 'aiAOV_specular_indirect',
              'aiAOV_sss_direct', 'aiAOV_sss_indirect', 'aiAOV_transmission_direct', 'aiAOV_transmission_indirect']

    for i in aov:
        if i in chlist:
            layer1.createAbsoluteOverride(i, 'enabled').setAttrValue(1)
            layer2.createAbsoluteOverride(i, 'enabled').setAttrValue(1)

        else:
            cmds.setAttr(i + ".enabled", 0)


def sh_Aovset():
    import maya.cmds as cmds
    from maya.app.renderSetup.model import renderSetup

    rs = renderSetup.instance()
    layer3 = rs.getRenderLayer('sh_beauty')
    aov = cmds.ls(type='aiAOV')
    shlist = ['aiAOV_occ', 'aiAOV_shadow_matte']
    for i in aov:
        if i in shlist:
            layer3.createAbsoluteOverride(i, 'enabled').setAttrValue(1)
        else:
            cmds.setAttr(i + ".enabled", 0)

    #################################################################


def lit_Aovset():
    import maya.cmds as cmds
    from maya.app.renderSetup.model import renderSetup

    rs = renderSetup.instance()
    layer1 = rs.getRenderLayer('ch_beauty')
    layer2 = rs.getRenderLayer('bg_beauty')
    aov = cmds.ls(type='aiAOV')
    litlist = ['aiAOV_RGBA_dome', 'aiAOV_RGBA_key', 'aiAOV_RGBA_keyadd',
               'aiAOV_RGBA_rim', 'aiAOV_RGBA_fill', 'aiAOV_RGBA_back']
    for i in aov:
        if i in litlist:
            layer1.createAbsoluteOverride(i, 'enabled').setAttrValue(1)
            layer2.createAbsoluteOverride(i, 'enabled').setAttrValue(1)
        else:
            cmds.setAttr(i + ".enabled", 0)


def Toon_Aovset():
    import maya.cmds as cmds
    from maya.app.renderSetup.model import renderSetup

    sh_Aovset()

    rs = renderSetup.instance()

    layer1 = rs.getRenderLayer('ch_beauty')
    layer2 = rs.getRenderLayer('bg_beauty')
    aov = cmds.ls(type='aiAOV')
    toonlist = ['aiAOV_albedo', 'aiAOV_coat_direct', 'aiAOV_coat_indirect',
                'aiAOV_crypto_asset', 'aiAOV_crypto_material', 'aiAOV_crypto_object', 'aiAOV_diffuse_direct',
                'aiAOV_diffuse_indirect', 'aiAOV_emission', 'aiAOV_motionvector', 'aiAOV_occ',
                'aiAOV_sheen_indirect',
                'aiAOV_sheen_direct', 'aiAOV_specular', 'aiAOV_specular_direct', 'aiAOV_specular_indirect',
                'aiAOV_toonLines',
                'aiAOV_sss_direct', 'aiAOV_sss_indirect', 'aiAOV_transmission_direct',
                'aiAOV_transmission_indirect']

    for i in aov:
        if i in toonlist:
            layer1.createAbsoluteOverride(i, 'enabled').setAttrValue(1)
            layer2.createAbsoluteOverride(i, 'enabled').setAttrValue(1)

        else:
            cmds.setAttr(i + ".enabled", 0)


def Utill_Aovset():
    import maya.cmds as cmds
    from maya.app.renderSetup.model import renderSetup

    sh_Aovset()

    rs = renderSetup.instance()

    layer4 = rs.getRenderLayer('ch_Utill_beauty')
    layer5 = rs.getRenderLayer('bg_Utill_beauty')
    aov = cmds.ls(type='aiAOV')
    utilllist = ['aiAOV_N', 'aiAOV_P', 'aiAOV_ToonUtill', 'aiAOV_ToonUtill2', 'aiAOV_ToonUtill3',
                 'aiAOV_Z', 'aiAOV_toonFalloff', 'aiAOV_toonRim_L', 'aiAOV_toonRim_L2',
                 'aiAOV_toonRim_R', 'aiAOV_toonRim_R2', 'aiAOV_uNoramlCamera', 'aiAOV_uPointCamera',
                 'aiAOV_uPointWorld', 'aiAOV_uUVI']

    for i in aov:
        if i in utilllist:
            layer4.createAbsoluteOverride(i, 'enabled').setAttrValue(1)
            layer5.createAbsoluteOverride(i, 'enabled').setAttrValue(1)

        else:
            cmds.setAttr(i + ".enabled", 0)


def fx_Aovset():
    import maya.cmds as cmds
    from maya.app.renderSetup.model import renderSetup

    rs = renderSetup.instance()

    rs.getRenderLayer('fx_lit_beauty').createAbsoluteOverride('defaultArnoldRenderOptions', 'aovMode').setAttrValue(
        0)
    rs.getRenderLayer('trajectory_ch_lit_beauty').createAbsoluteOverride('defaultArnoldRenderOptions',
                                                                         'aovMode').setAttrValue(0)
    rs.getRenderLayer('trajectory_bg_lit_beauty').createAbsoluteOverride('defaultArnoldRenderOptions',
                                                                         'aovMode').setAttrValue(0)

    layer1 = rs.getRenderLayer('trajectory_beauty')
    layer2 = rs.getRenderLayer('fx_spark_beauty')
    layer3 = rs.getRenderLayer('fx_fire_beauty')
    layer4 = rs.getRenderLayer('fx_volume_beauty')
    aov = cmds.ls(type='aiAOV')
    aovlist = ['aiAOV_N', 'aiAOV_P', 'aiAOV_Z', 'aiAOV_crypto_asset', 'aiAOV_crypto_material',
               'aiAOV_crypto_object', 'aiAOV_emission', 'aiAOV_motionvector']
    for i in aov:
        if i in aovlist:
            layer1.createAbsoluteOverride(i, 'enabled').setAttrValue(1)
            layer2.createAbsoluteOverride(i, 'enabled').setAttrValue(1)
            layer3.createAbsoluteOverride(i, 'enabled').setAttrValue(1)
            layer4.createAbsoluteOverride(i, 'enabled').setAttrValue(1)
        else:
            cmds.setAttr(i + ".enabled", 0)

