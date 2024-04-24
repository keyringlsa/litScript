import os, sys
from glob import glob
from pprint import pprint



def sha_AS(sha_name, mesh_name):
    import maya.cmds as cmds

    print(sha_name, mesh_name)
    shape_name = mesh_name.replace("Shape","")
    cmds.select(mesh_name)
    cmds.hyperShade(assign=sha_name)




def ch_data():
    import maya.cmds as cmds

    mesh_grp = cmds.ls(sl=1)

    row_datas = []


    for i in mesh_grp :
        mesh_list = cmds.listRelatives(i, ad=True, type='shape')
        mesh_name = i
        detail_list = []
        for j in mesh_list :
            mesh_shape = j
            materials = cmds.listConnections(j, type='shadingEngine')
            shaders =cmds.ls(cmds.listConnections(materials), materials=True)
            shape_detail = {'name': mesh_shape,'child':[], 'shader': shaders}
            detail_list.append(shape_detail)

        row_data = [{'name': mesh_name, 'child': detail_list, 'shader':[]}]
        row_datas.append(row_data)
    print(row_datas)
    return row_datas
