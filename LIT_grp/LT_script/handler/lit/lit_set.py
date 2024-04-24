def lit_base():
    import mtoa.utils as mutils
    import maya.cmds as cmds



    mutils.createLocator("aiSkyDomeLight", asLight=True)
    cmds.rename('aiSkyDomeLight1', 'dome_lit')
    cmds.directionalLight(rotation=(-130, -30, 0))
    cmds.rename('directionalLight1', 'bg_key_lit')
    cmds.directionalLight(rotation=(-130, -30, 0))
    cmds.rename("directionalLight1", "ch_key_lit")
    cmds.group(em=True, name='lit_grp')
    cmds.group(em=True, name='bg_lit_grp')
    cmds.group(em=True, name='ch_lit_grp')
    cmds.parent('bg_key_lit', 'bg_lit_grp')
    cmds.parent('ch_key_lit', 'ch_lit_grp')
    cmds.parent('bg_lit_grp', 'lit_grp')
    cmds.parent('ch_lit_grp', 'lit_grp')
    cmds.parent('dome_lit', 'lit_grp')


def lit_ch():
    import mtoa.utils as mutils
    import maya.cmds as cmds
    import maya.mel as mel
    selected_object = cmds.ls(selection=True)

    if len(selected_object) == 1:
        object_name = selected_object[0]
        object_bounding_box = cmds.exactWorldBoundingBox(object_name)
        object_center = [(object_bounding_box[0] + object_bounding_box[3]) / 2,
                         (object_bounding_box[1] + object_bounding_box[4]) / 2,
                         (object_bounding_box[2] + object_bounding_box[5]) / 2]
        cmds.spaceLocator(name="lit_back_a_loc")[0]
        cmds.setAttr("lit_back_a_loc.localScaleX", 50)
        cmds.setAttr("lit_back_a_loc.localScaleY", 50)
        cmds.setAttr("lit_back_a_loc.localScaleZ", 50)
        mutils.createLocator('aiAreaLight', asLight=True)
        cmds.rename('aiAreaLight1', 'lit_back_a')
        cmds.setAttr("lit_back_a.translateZ", 100)
        cmds.setAttr("lit_back_a.scaleY", 50)
        cmds.setAttr("lit_back_a.scaleX", 50)
        cmds.setAttr("lit_back_a.scaleZ", 50)
        cmds.setAttr("lit_back_aShape.normalize",0)
        cmds.parent('lit_back_a', "lit_back_a_loc")
        cmds.setAttr("lit_back_a_loc.rotateY", -180)
        cmds.spaceLocator(name="lit_rim_a_loc")[0]
        cmds.setAttr("lit_rim_a_loc.localScaleX", 50)
        cmds.setAttr("lit_rim_a_loc.localScaleY", 50)
        cmds.setAttr("lit_rim_a_loc.localScaleZ", 50)
        mutils.createLocator('aiAreaLight', asLight=True)
        cmds.rename('aiAreaLight1', 'lit_rim_a')
        cmds.setAttr("lit_rim_a.translateZ", 100)
        cmds.setAttr("lit_rim_a.scaleY", 50)
        cmds.setAttr("lit_rim_a.scaleX", 50)
        cmds.setAttr("lit_rim_a.scaleZ", 50)
        cmds.setAttr("lit_rim_aShape.normalize",0)
        cmds.parent('lit_rim_a', "lit_rim_a_loc")
        cmds.spaceLocator(name="lit_fill_a_loc")[0]
        cmds.setAttr("lit_fill_a_loc.localScaleX", 50)
        cmds.setAttr("lit_fill_a_loc.localScaleY", 50)
        cmds.setAttr("lit_fill_a_loc.localScaleZ", 50)
        mutils.createLocator('aiAreaLight', asLight=True)
        cmds.rename('aiAreaLight1', 'lit_fill_a')
        cmds.setAttr("lit_fill_a.translateZ", 100)
        cmds.setAttr("lit_fill_a.scaleY", 50)
        cmds.setAttr("lit_fill_a.scaleX", 50)
        cmds.setAttr("lit_fill_a.scaleX", 50)
        cmds.setAttr("lit_fill_a.scaleZ", 50)
        cmds.setAttr("lit_fill_aShape.normalize",0)
        cmds.parent('lit_fill_a', "lit_fill_a_loc")
        cmds.setAttr("lit_fill_a_loc.rotateY", 90)
        cmds.xform("lit_back_a_loc", t=object_center, ws=True)
        cmds.xform("lit_rim_a_loc", t=object_center, ws=True)
        cmds.xform("lit_fill_a_loc", t=object_center, ws=True)


def rivet():

    import maya.cmds as cmds


    nameObject = ""
    namePOSI = ""

    parts = []
    list = cmds.ls(selection=True, flatten=True)
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

    else:
        list = cmds.ls(selection=True, flatten=True, type="nurbsSurface")
        size = len(list)

        if size > 0:
            if size != 1:
                cmds.error("No one point selected")
                return ""

            parts = list[0].split(".")
            nameObject = parts[0]
            parts = list[0].split("[")
            u = float(parts[1].strip("]"))
            v = float(parts[2].strip("]"))

            namePOSI = cmds.createNode("pointOnSurfaceInfo", name="rivetPointOnSurfaceInfo1")
            cmds.setAttr(namePOSI + ".turnOnPercentage", 0)
            cmds.setAttr(namePOSI + ".parameterU", u)
            cmds.setAttr(namePOSI + ".parameterV", v)
            cmds.connectAttr(nameObject + ".ws", namePOSI + ".is", force=True)

        else:
            cmds.error("No edges or point selected")
            return ""

    nameLocator = cmds.createNode("transform", name="rivet1")
    cmds.createNode("locator", name=nameLocator + "Shape", parent=nameLocator)

    nameAC = cmds.createNode("aimConstraint", name=nameLocator + "_rivetAimConstraint1", parent=nameLocator)
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
    cmds.connectAttr(nameAC + ".crx", nameLocator + ".rx")
    cmds.connectAttr(nameAC + ".cry", nameLocator + ".ry")
    cmds.connectAttr(nameAC + ".crz", nameLocator + ".rz")

    cmds.select(nameLocator, replace=True)
    return nameLocator


def lit_make(lit_type, lit_name):


    import mtoa.utils as mutils
    import maya.cmds as cmds

    new_name = lit_name
    selected_object = cmds.ls(selection=True)


    if len(selected_object) == 1:
        object_name = selected_object[0]
        object_bounding_box = cmds.exactWorldBoundingBox(object_name)
        object_center = [(object_bounding_box[0] + object_bounding_box[3]) / 2,
                         (object_bounding_box[1] + object_bounding_box[4]) / 2,
                         (object_bounding_box[2] + object_bounding_box[5]) / 2]
        
        


        if lit_type == "area" :
            loc_ = cmds.spaceLocator(p=('0', '0', '0'), name="loc")
            cmds.rename("loc", new_name + "_loc")
            cmds.setAttr(new_name + "_loc.localScaleX", 20)
            cmds.setAttr(new_name + "_loc.localScaleY", 20)
            cmds.setAttr(new_name + "_loc.localScaleZ", 20)
            mutils.createLocator('aiAreaLight', asLight=True)
            cmds.rename('aiAreaLight1', new_name)
            cmds.setAttr(new_name + ".translateZ", 50)
            cmds.setAttr(new_name + ".scaleY", 20)
            cmds.setAttr(new_name + ".scaleX", 20)
            cmds.setAttr(new_name + ".scaleZ", 20)
            cmds.parent(new_name, new_name + "_loc")
            cmds.xform(new_name + "_loc", t=object_center, ws=True)
            cmds.setAttr(new_name + "Shape.normalize", 0)

        elif lit_type == "point" :
            loc_ = cmds.spaceLocator(p=('0', '0', '0'), name="loc")
            cmds.rename("loc", new_name + "_loc")
            cmds.setAttr(new_name + "_loc.localScaleX", 20)
            cmds.setAttr(new_name + "_loc.localScaleY", 20)
            cmds.setAttr(new_name + "_loc.localScaleZ", 20)
            cmds.CreatePointLight(1, 1,1,1, 0, 0, 0,0,0, 1)
            cmds.rename('pointLight1', new_name)
            cmds.setAttr(new_name + ".translateZ", 50)
            cmds.setAttr(new_name + ".scaleY", 20)
            cmds.setAttr(new_name + ".scaleX", 20)
            cmds.setAttr(new_name + ".scaleZ", 20)
            cmds.parent(new_name, new_name + "_loc")
            cmds.xform(new_name + "_loc", t=object_center, ws=True)
            cmds.setAttr(new_name + "Shape.aiNormalize", 0)


        elif lit_type == "spot" :
            loc_ = cmds.spaceLocator(p=('0', '0', '0'), name="loc")
            cmds.rename("loc", new_name + "_loc")
            cmds.setAttr(new_name + "_loc.localScaleX", 20)
            cmds.setAttr(new_name + "_loc.localScaleY", 20)
            cmds.setAttr(new_name + "_loc.localScaleZ", 20)
            cmds.CreateSpotLight(1, 1,1,1, 0, 40, 0, 0, 0, 0,0,0, 1, 0)
            cmds.rename('spotLight1', new_name)
            cmds.setAttr(new_name + ".translateZ", 50)
            cmds.setAttr(new_name + ".scaleY", 20)
            cmds.setAttr(new_name + ".scaleX", 20)
            cmds.setAttr(new_name + ".scaleZ", 20)
            cmds.parent(new_name, new_name + "_loc")
            cmds.xform(new_name + "_loc", t=object_center, ws=True)
            cmds.setAttr(new_name + "Shape.aiNormalize", 0)

        elif lit_type == "direftional" :
            cmds.CreateDirectionalLight(1, 1,1,1, "0", 0,0,0, 0)
            cmds.rename('directionalLight1', new_name)
            cmds.xform(new_name, t=object_center, ws=True)

        elif lit_type == "dome" :
            mutils.createLocator("aiSkyDomeLight", asLight=True)
            cmds.rename('aiSkyDomeLight1', new_name)
            cmds.setAttr(new_name+"Shape.camera",0)
            cmds.xform(new_name, t=object_center, ws=True)





    else:

        if lit_type == "area" :
            loc_ = cmds.spaceLocator(p=('0', '0', '0'), name="loc")
            cmds.rename("loc", new_name + "_loc")
            cmds.setAttr(new_name + "_loc.localScaleX", 20)
            cmds.setAttr(new_name + "_loc.localScaleY", 20)
            cmds.setAttr(new_name + "_loc.localScaleZ", 20)
            mutils.createLocator('aiAreaLight', asLight=True)
            cmds.rename('aiAreaLight1', new_name)
            cmds.setAttr(new_name + ".translateZ", 50)
            cmds.setAttr(new_name + ".scaleY", 20)
            cmds.setAttr(new_name + ".scaleX", 20)
            cmds.setAttr(new_name + ".scaleZ", 20)
            cmds.parent(new_name, new_name + "_loc")
            cmds.setAttr(new_name + "Shape.normalize", 0)


        elif lit_type == "point" :
            loc_ = cmds.spaceLocator(p=('0', '0', '0'), name="loc")
            cmds.rename("loc", new_name + "_loc")
            cmds.setAttr(new_name + "_loc.localScaleX", 20)
            cmds.setAttr(new_name + "_loc.localScaleY", 20)
            cmds.setAttr(new_name + "_loc.localScaleZ", 20)
            cmds.CreatePointLight(1, 1,1,1, 0, 0, 0,0,0, 1)
            cmds.rename('pointLight1', new_name)
            cmds.setAttr(new_name + ".translateZ", 50)
            cmds.setAttr(new_name + ".scaleY", 20)
            cmds.setAttr(new_name + ".scaleX", 20)
            cmds.setAttr(new_name + ".scaleZ", 20)
            cmds.parent(new_name, new_name + "_loc")
            cmds.setAttr(new_name + "Shape.aiNormalize", 0)


        elif lit_type == "spot" :
            loc_ = cmds.spaceLocator(p=('0', '0', '0'), name="loc")
            cmds.rename("loc", new_name + "_loc")
            cmds.setAttr(new_name + "_loc.localScaleX", 20)
            cmds.setAttr(new_name + "_loc.localScaleY", 20)
            cmds.setAttr(new_name + "_loc.localScaleZ", 20)
            cmds.CreateSpotLight(1, 1,1,1, 0, 40, 0, 0, 0, 0,0,0, 1, 0)
            cmds.rename('spotLight1', new_name)
            cmds.setAttr(new_name + ".translateZ", 50)
            cmds.setAttr(new_name + ".scaleY", 20)
            cmds.setAttr(new_name + ".scaleX", 20)
            cmds.setAttr(new_name + ".scaleZ", 20)
            cmds.parent(new_name, new_name + "_loc")
            cmds.setAttr(new_name + "Shape.aiNormalize", 0)

        elif lit_type == "direftional" :
            cmds.CreateDirectionalLight(1, 1,1,1, "0", 0,0,0, 0)
            cmds.rename('directionalLight1', new_name)


        elif lit_type == "dome" :
            mutils.createLocator("aiSkyDomeLight", asLight=True)
            cmds.rename('aiSkyDomeLight1', new_name)
            cmds.setAttr(new_name+"Shape.camera",0)



def Lit_grp(LG_type) :
    import maya.cmds as cmds

    lit_sl = cmds.ls(sl=1)

    for i in lit_sl:
        if LG_type == "dome":
            cmds.setAttr(i + '.aiAov', "dome", type='string')
        elif LG_type == "key":
            cmds.setAttr(i + '.aiAov', "key", type='string')
        elif LG_type == "keyadd":
            cmds.setAttr(i + '.aiAov', "keyadd", type='string')
        elif LG_type == "fill":
            cmds.setAttr(i + '.aiAov', "fill", type='string')
        elif LG_type == "rim":
            cmds.setAttr(i + '.aiAov', "rim", type='string')
        elif LG_type == "back":
            cmds.setAttr(i + '.aiAov', "back", type='string')
        elif LG_type == "bounce":
            cmds.setAttr(i + '.aiAov', "bounce", type='string')
        else :
            cmds.setAttr(i+'.aiAov', LG_type,  type='string')




def LIT_AT(Lit_AT_type, Lit_AT_value) :
    import maya.cmds as cmds

    lit_sel = cmds.ls(sl=1)

    for i in lit_sel :
        cmds.setAttr(i+f".{Lit_AT_type}", float(Lit_AT_value))



def Lit_normal(Normal_ON):
    import maya.cmds as cmds
    lit_sel = cmds.ls(sl=1)

    if Normal_ON == 1:
        for i in lit_sel:
            cmds.setAttr(i + ".aiNormalize", 1)  # 선택한 라이트들 노말라이즈 켜줍니다.
    elif Normal_ON == 0:
        for i in lit_sel:
            cmds.setAttr(i + ".aiNormalize", 0)  # 선택한 라이트들 노말라이즈 꺼줍니다.






