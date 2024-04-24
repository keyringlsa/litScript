
def basic_set():
    import maya.cmds as cmds
    cmds.select(clear=True)
    setlist = cmds.ls(et='objectSet')
    if not "bg_set" in setlist:
        cmds.sets(n="bg_set")
        cmds.addAttr("bg_set", ln='primaryVisibility', at='bool', dv=1)
        cmds.addAttr("bg_set", ln='aiMatte', at='bool', dv=0)
        cmds.addAttr("bg_set", ln='aiVisibleInSpecularReflection', at='bool', dv=1)
        cmds.addAttr("bg_set", ln='overrideMatte', at='bool', dv=0)

    if not "ch_set" in setlist:
        cmds.sets(n="ch_set")
        cmds.addAttr("ch_set", ln='primaryVisibility', at='bool', dv=1)
        cmds.addAttr("ch_set", ln='aiMatte', at='bool', dv=0)
        cmds.addAttr("ch_set", ln='aiVisibleInSpecularReflection', at='bool', dv=1)

    if not "subdiv_set" in setlist:
        cmds.sets(n="subdiv_set")
        cmds.addAttr("subdiv_set", ln='aiSubdivType', at='enum', en='none:catclark:linear', dv=1)
        cmds.addAttr("subdiv_set", ln='aiSubdivIterations', at='byte', dv=4)

    if not "shadow_set" in setlist:
        cmds.sets(n="shadow_set")
        cmds.addAttr("shadow_set", ln='castsShadows', at='bool', dv=1)

    if not "shadow_off_set" in setlist:
        cmds.sets(n="shadow_off_set")
        cmds.addAttr("shadow_off_set", ln='castsShadows', at='bool', dv=0)

def fx_set():
    import maya.cmds as cmds
    cmds.select(clear=True)
    setlist = cmds.ls(et='objectSet')
    if not "bg_set" in setlist:
        cmds.sets(n="bg_set")
        cmds.addAttr("bg_set", ln='primaryVisibility', at='bool', dv=1)
        cmds.addAttr("bg_set", ln='aiMatte', at='bool', dv=0)
        cmds.addAttr("bg_set", ln='aiVisibleInSpecularReflection', at='bool', dv=1)
        cmds.addAttr("bg_set", ln='overrideMatte', at='bool', dv=0)

    if not "ch_set" in setlist:
        cmds.sets(n="ch_set")
        cmds.addAttr("ch_set", ln='primaryVisibility', at='bool', dv=1)
        cmds.addAttr("ch_set", ln='aiMatte', at='bool', dv=0)
        cmds.addAttr("ch_set", ln='aiVisibleInSpecularReflection', at='bool', dv=1)

    cmds.sets(n="fire_set")
    cmds.sets(n="fire_lit_set")
    cmds.sets(n="orange_set")
    cmds.sets(n="blue_set")
    cmds.sets(n="volume_set")
    cmds.sets(n="spark_set")





def layer_ch():

    from maya.app.renderSetup.model import renderSetup

    rs = renderSetup.instance()
    rs.createRenderLayer('ch_beauty')
    lit_hide = rs.getRenderLayer('ch_beauty').createCollection('lit_hide')
    lit_hide.getSelector().staticSelection.add(['lit_grp'])
    lit_hide.setSelfEnabled(False)
    ch_layer = rs.getRenderLayer('ch_beauty').createCollection('ch')
    ch_layer.getSelector().staticSelection.add(['ch_set'])
    bg_layer = rs.getRenderLayer('ch_beauty').createCollection('bg')
    bg_layer.getSelector().staticSelection.add(['bg_set'])
    bg_layer.createAbsoluteOverride('bg_set', 'aiMatte').setAttrValue(True)
    bg_layer.createAbsoluteOverride('bg_set', 'overrideMatte').setAttrValue(True)
    rs.getRenderLayer('ch_beauty').createCollection('lit')


def layer_bg():

    from maya.app.renderSetup.model import renderSetup

    rs = renderSetup.instance()
    rs.createRenderLayer('bg_beauty')
    lit_hide1 = rs.getRenderLayer('bg_beauty').createCollection('lit_hide')
    lit_hide1.getSelector().staticSelection.add(['lit_grp'])
    lit_hide1.setSelfEnabled(False)
    ch_layer1 = rs.getRenderLayer('bg_beauty').createCollection('ch')
    ch_layer1.getSelector().staticSelection.add(['ch_set'])
    ch_layer1.setSelfEnabled(False)
    bg_layer1 = rs.getRenderLayer('bg_beauty').createCollection('bg')
    bg_layer1.getSelector().staticSelection.add(['bg_set'])
    rs.getRenderLayer('bg_beauty').createCollection('lit')


def layer_sh():

    from maya.app.renderSetup.model import renderSetup

    rs = renderSetup.instance()
    rs.createRenderLayer('sh_beauty')
    lit_hide2 = rs.getRenderLayer('sh_beauty').createCollection('lit_hide')
    lit_hide2.getSelector().staticSelection.add(['lit_grp'])
    lit_hide2.setSelfEnabled(False)
    ch_layer2 = rs.getRenderLayer('sh_beauty').createCollection('ch')
    ch_layer2.getSelector().staticSelection.add(['ch_set'])
    ch_layer2.createAbsoluteOverride('ch_set', 'primaryVisibility').setAttrValue(False)
    bg_layer2 = rs.getRenderLayer('sh_beauty').createCollection('bg')
    bg_layer2.getSelector().staticSelection.add(['shadow_set'])
    bg_layer2.createAbsoluteOverride('shadow_set', 'castsShadows').setAttrValue(False)
    rs.getRenderLayer('sh_beauty').createCollection('lit')


def layer_utill():

    from maya.app.renderSetup.model import renderSetup

    rs = renderSetup.instance()
    rs.createRenderLayer('ch_Utill_beauty')
    lit_hide3 = rs.getRenderLayer('ch_Utill_beauty').createCollection('lit_hide')
    lit_hide3.getSelector().staticSelection.add(['lit_grp'])
    lit_hide3.setSelfEnabled(False)
    ch_layer3 = rs.getRenderLayer('ch_Utill_beauty').createCollection('ch')
    ch_layer3.getSelector().staticSelection.add(['ch_set'])
    bg_layer3 = rs.getRenderLayer('ch_Utill_beauty').createCollection('bg')
    bg_layer3.getSelector().staticSelection.add(['bg_set'])
    bg_layer3.createAbsoluteOverride('bg_set', 'aiMatte').setAttrValue(True)
    bg_layer3.createAbsoluteOverride('bg_set', 'overrideMatte').setAttrValue(True)

    rs.createRenderLayer('bg_Utill_beauty')
    lit_hide4 = rs.getRenderLayer('bg_Utill_beauty').createCollection('lit_hide')
    lit_hide4.getSelector().staticSelection.add(['lit_grp'])
    lit_hide4.setSelfEnabled(False)
    ch_layer4 = rs.getRenderLayer('bg_Utill_beauty').createCollection('ch')
    ch_layer4.getSelector().staticSelection.add(['ch_set'])
    ch_layer4.setSelfEnabled(False)
    bg_layer4 = rs.getRenderLayer('bg_Utill_beauty').createCollection('bg')
    bg_layer4.getSelector().staticSelection.add(['bg_set'])


def layer_fx():
    import mtoa.utils as mutils
    from maya.app.renderSetup.model import renderSetup
    from maya.app.renderSetup.model import typeIDs
    import maya.cmds as cmds

    cmds.shadingNode('aiStandardSurface', n="fx_base_mtl", asShader=True)
    cmds.setAttr('fx_base_mtl.specular', 0)
    cmds.sets(name="fx_base_mtlSG", empty=True, renderable=True, noSurfaceShader=True)
    cmds.connectAttr("fx_base_mtl.outColor", "fx_base_mtlSG.surfaceShader")
    sphere = cmds.polySphere(name='set_lit')[0]
    mutils.createMeshLight()
    rs = renderSetup.instance()

    rs.createRenderLayer('fx_fire_beauty')
    rs.getRenderLayer('fx_fire_beauty').createCollection('lit_hide').setSelfEnabled(False)
    ch_over = rs.getRenderLayer('fx_fire_beauty').createCollection('ch')
    ch_over.getSelector().staticSelection.add(['ch_set'])
    ch_over.createAbsoluteOverride('ch_set', 'primaryVisibility').setAttrValue(False)
    bg_over = rs.getRenderLayer('fx_fire_beauty').createCollection('bg')
    bg_over.getSelector().staticSelection.add(['bg_set'])
    bg_over.createAbsoluteOverride('bg_set', 'primaryVisibility').setAttrValue(False)
    rs.getRenderLayer('fx_fire_beauty').createCollection('fx').createAbsoluteOverride('persp',
                                                                                      'visibility').setAttrValue(
        True)
    fire_lit_hide = rs.getRenderLayer('fx_fire_beauty').createCollection('fire_lit_hide')
    fire_lit_hide.getSelector().staticSelection.add(['fire_lit_set'])
    fire_lit_hide.setSelfEnabled(False)

    rs.createRenderLayer('fx_lit_beauty')
    rs.getRenderLayer('fx_lit_beauty').createCollection('lit_hide').setSelfEnabled(False)
    ch_over1 = rs.getRenderLayer('fx_lit_beauty').createCollection('ch')
    ch_over1.getSelector().staticSelection.add(['ch_set'])
    ch_mtl1 = ch_over1.createOverride('fx_base_mtl', typeIDs.materialOverride)
    ch_mtl1.setMaterial('fx_base_mtlSG')
    bg_over1 = rs.getRenderLayer('fx_lit_beauty').createCollection('bg')
    bg_over1.getSelector().staticSelection.add(['bg_set'])
    bg_over1.createAbsoluteOverride('bg_set', 'aiMatte').setAttrValue(True)
    bg_over1.createAbsoluteOverride('bg_set', 'overrideMatte').setAttrValue(True)
    rs.getRenderLayer('fx_lit_beauty').createCollection('fx').createAbsoluteOverride('persp',
                                                                                     'visibility').setAttrValue(
        True)
    fire_hide = rs.getRenderLayer('fx_lit_beauty').createCollection('fire_hide')
    fire_hide.getSelector().staticSelection.add(['fire_set'])
    fire_hide.setSelfEnabled(False)
    orange_lit1 = rs.getRenderLayer('fx_lit_beauty').createCollection('orange')
    orange_lit1.getSelector().staticSelection.add(['orange_set'])
    orange_lit1.createAbsoluteOverride('light_set_litShape', 'color').setAttrValue((1, 0, 0))
    orange_lit1.createAbsoluteOverride('light_set_litShape', 'intensity').setAttrValue(5)
    orange_lit1.createAbsoluteOverride('light_set_litShape', 'aiExposure').setAttrValue(5)
    orange_lit1.createAbsoluteOverride('light_set_litShape', 'lightVisible').setAttrValue(0)
    blue_lit1 = rs.getRenderLayer('fx_lit_beauty').createCollection('blue')
    blue_lit1.getSelector().staticSelection.add(['blue_set'])
    blue_lit1.createAbsoluteOverride('light_set_litShape', 'color').setAttrValue((0, 0, 1))
    blue_lit1.createAbsoluteOverride('light_set_litShape', 'intensity').setAttrValue(5)
    blue_lit1.createAbsoluteOverride('light_set_litShape', 'aiExposure').setAttrValue(5)
    blue_lit1.createAbsoluteOverride('light_set_litShape', 'lightVisible').setAttrValue(0)

    rs.createRenderLayer('fx_volume_beauty')
    rs.getRenderLayer('fx_volume_beauty').createCollection('lit_hide').setSelfEnabled(False)
    ch_over2 = rs.getRenderLayer('fx_volume_beauty').createCollection('ch')
    ch_over2.getSelector().staticSelection.add(['ch_set'])
    ch_over2.createAbsoluteOverride('ch_set', 'aiMatte').setAttrValue(True)
    bg_over2 = rs.getRenderLayer('fx_volume_beauty').createCollection('bg')
    bg_over2.getSelector().staticSelection.add(['bg_set'])
    bg_over2.createAbsoluteOverride('bg_set', 'aiMatte').setAttrValue(True)
    bg_over2.createAbsoluteOverride('bg_set', 'overrideMatte').setAttrValue(True)
    rs.getRenderLayer('fx_volume_beauty').createCollection('fx').createAbsoluteOverride('persp',
                                                                                        'visibility').setAttrValue(
        True)
    spark_hide = rs.getRenderLayer('fx_volume_beauty').createCollection('spark_hide')
    spark_hide.getSelector().staticSelection.add(['spark_set'])
    spark_hide.setSelfEnabled(False)

    rs.createRenderLayer('fx_spark_beauty')
    rs.getRenderLayer('fx_spark_beauty').createCollection('lit_hide').setSelfEnabled(False)
    ch_over3 = rs.getRenderLayer('fx_spark_beauty').createCollection('ch')
    ch_over3.getSelector().staticSelection.add(['ch_set'])
    ch_over3.createAbsoluteOverride('ch_set', 'aiMatte').setAttrValue(True)
    bg_over3 = rs.getRenderLayer('fx_spark_beauty').createCollection('bg')
    bg_over3.getSelector().staticSelection.add(['bg_set'])
    bg_over3.createAbsoluteOverride('bg_set', 'aiMatte').setAttrValue(True)
    bg_over3.createAbsoluteOverride('bg_set', 'overrideMatte').setAttrValue(True)
    rs.getRenderLayer('fx_spark_beauty').createCollection('fx').createAbsoluteOverride('persp',
                                                                                       'visibility').setAttrValue(
        True)
    volume_hide = rs.getRenderLayer('fx_spark_beauty').createCollection('volume_hide')
    volume_hide.getSelector().staticSelection.add(['volume_set'])
    volume_hide.setSelfEnabled(False)

    rs.createRenderLayer('trajectory_beauty')
    rs.getRenderLayer('trajectory_beauty').createCollection('lit_hide').setSelfEnabled(False)
    ch_over4 = rs.getRenderLayer('trajectory_beauty').createCollection('ch')
    ch_over4.getSelector().staticSelection.add(['ch_set'])
    ch_over4.createAbsoluteOverride('ch_set', 'aiMatte').setAttrValue(True)
    bg_over4 = rs.getRenderLayer('trajectory_beauty').createCollection('bg')
    bg_over4.getSelector().staticSelection.add(['bg_set'])
    bg_over4.createAbsoluteOverride('bg_set', 'aiMatte').setAttrValue(True)
    bg_over4.createAbsoluteOverride('bg_set', 'overrideMatte').setAttrValue(True)
    rs.getRenderLayer('trajectory_beauty').createCollection('fx').createAbsoluteOverride('persp',
                                                                                         'visibility').setAttrValue(
        True)

    rs.createRenderLayer('trajectory_ch_lit_beauty')
    rs.getRenderLayer('trajectory_ch_lit_beauty').createCollection('lit_hide').setSelfEnabled(False)
    ch_over5 = rs.getRenderLayer('trajectory_ch_lit_beauty').createCollection('ch')
    ch_over5.getSelector().staticSelection.add(['ch_set'])
    ch_mtl5 = ch_over5.createOverride('fx_base_mtl', typeIDs.materialOverride)
    ch_mtl5.setMaterial('fx_base_mtlSG')
    bg_over5 = rs.getRenderLayer('trajectory_ch_lit_beauty').createCollection('bg')
    bg_over5.getSelector().staticSelection.add(['bg_set'])
    bg_over5.createAbsoluteOverride('bg_set', 'aiMatte').setAttrValue(True)
    bg_over5.createAbsoluteOverride('bg_set', 'overrideMatte').setAttrValue(True)
    rs.getRenderLayer('trajectory_ch_lit_beauty').createCollection('fx').createAbsoluteOverride('persp',
                                                                                                'visibility').setAttrValue(
        True)
    orange_lit5 = rs.getRenderLayer('trajectory_ch_lit_beauty').createCollection('orange')
    orange_lit5.getSelector().staticSelection.add(['orange_set'])
    orange_lit5.createAbsoluteOverride('light_set_litShape', 'color').setAttrValue((1, 0, 0))
    orange_lit5.createAbsoluteOverride('light_set_litShape', 'intensity').setAttrValue(5)
    orange_lit5.createAbsoluteOverride('light_set_litShape', 'aiExposure').setAttrValue(5)
    orange_lit5.createAbsoluteOverride('light_set_litShape', 'lightVisible').setAttrValue(0)
    blue_lit5 = rs.getRenderLayer('trajectory_ch_lit_beauty').createCollection('blue')
    blue_lit5.getSelector().staticSelection.add(['blue_set'])
    blue_lit5.createAbsoluteOverride('light_set_litShape', 'color').setAttrValue((0, 0, 1))
    blue_lit5.createAbsoluteOverride('light_set_litShape', 'intensity').setAttrValue(5)
    blue_lit5.createAbsoluteOverride('light_set_litShape', 'aiExposure').setAttrValue(5)
    blue_lit5.createAbsoluteOverride('light_set_litShape', 'lightVisible').setAttrValue(0)

    rs.createRenderLayer('trajectory_bg_lit_beauty')
    rs.getRenderLayer('trajectory_bg_lit_beauty').createCollection('lit_hide').setSelfEnabled(False)
    ch_over6 = rs.getRenderLayer('trajectory_bg_lit_beauty').createCollection('ch')
    ch_over6.getSelector().staticSelection.add(['ch_set'])
    ch_over6.setSelfEnabled(False)
    bg_over6 = rs.getRenderLayer('trajectory_bg_lit_beauty').createCollection('bg')
    bg_over6.getSelector().staticSelection.add(['bg_set'])
    bg_mtl6 = bg_over6.createOverride('fx_base_mtl', typeIDs.materialOverride)
    bg_mtl6.setMaterial('fx_base_mtlSG')
    rs.getRenderLayer('trajectory_bg_lit_beauty').createCollection('fx').createAbsoluteOverride('persp',
                                                                                                'visibility').setAttrValue(
        True)
    orange_lit6 = rs.getRenderLayer('trajectory_bg_lit_beauty').createCollection('orange')
    orange_lit6.getSelector().staticSelection.add(['orange_set'])
    orange_lit6.createAbsoluteOverride('light_set_litShape', 'color').setAttrValue((1, 0, 0))
    orange_lit6.createAbsoluteOverride('light_set_litShape', 'intensity').setAttrValue(5)
    orange_lit6.createAbsoluteOverride('light_set_litShape', 'aiExposure').setAttrValue(5)
    orange_lit6.createAbsoluteOverride('light_set_litShape', 'lightVisible').setAttrValue(0)
    blue_lit6 = rs.getRenderLayer('trajectory_bg_lit_beauty').createCollection('blue')
    blue_lit6.getSelector().staticSelection.add(['blue_set'])
    blue_lit6.createAbsoluteOverride('light_set_litShape', 'color').setAttrValue((0, 0, 1))
    blue_lit6.createAbsoluteOverride('light_set_litShape', 'intensity').setAttrValue(5)
    blue_lit6.createAbsoluteOverride('light_set_litShape', 'aiExposure').setAttrValue(5)
    blue_lit6.createAbsoluteOverride('light_set_litShape', 'lightVisible').setAttrValue(0)
