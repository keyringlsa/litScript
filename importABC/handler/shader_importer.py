import maya.cmds as cmds
import maya.mel as mel
import yaml

from pprint import pprint

def str_convert_pattern(shape_name):

    if '|' in shape_name:

        return "|".join(list(map(lambda x: f"*:{x}", shape_name.split("|"))))
    else:

        return f"*:{shape_name}"


def import_shader(row_data=None, target_geos=None):

    asset_name = row_data.current_version.get("entity").get("name")
    version = row_data.version
    shd_namespace = f"{asset_name}_shd_v{version:03d}"
    yaml_file_path = row_data.file_path

    with open(yaml_file_path, 'r') as file:
        shader_dict = yaml.full_load(file)

    # if that project is older project, shader yaml format is different
    # ex: RFO, ALS20
    try:
        shader_scene = shader_dict['shader_scene']

        if not cmds.objExists(f"{shd_namespace}*:*"):
            imported_file = cmds.file(shader_scene, type="mayaBinary", reference=True,
                                      namespace=shd_namespace, rnn=True)

        ## assign
        cmds.select(cl=True)
        target_geo_group = cmds.ls(target_geos, type='transform')
        target_shapes = cmds.ls(cmds.listRelatives(target_geo_group, ad=True, type='mesh'))

        for SG_dict in shader_dict["shading_engines"]:
            for SG, mat_dict in SG_dict.items():
                preview_mtl = mat_dict["mat"]
                # arnold_mtl = mat_dict["arnold_mat"]
                dis_mtl = mat_dict["dis_mat"]
                assign_shapes = mat_dict["meshes"]

                convert_shapes = cmds.ls(list(map(lambda x: str_convert_pattern(x), assign_shapes)))


                filtered_shapes = [i for i in convert_shapes if i in target_shapes]
                print("filtered_shapes",filtered_shapes)

                # assign shader
                print("preview_mtl",preview_mtl)
                mtl = f"{shd_namespace}:{preview_mtl[0]}"

                cmds.select(filtered_shapes, r=True)
                cmds.hyperShade(assign=mtl)
                b = cmds.listConnections(mtl, type='shadingEngine')

                shadingEngine = cmds.listConnections(mtl, type='shadingEngine')[0]

                if dis_mtl:
                    dis_mtl_name = f"{shd_namespace}:{dis_mtl[0]}"
                    cmds.connectAttr(f"{dis_mtl_name}.displacement", f"{shadingEngine}.displacementShader")
                # if arnold_mtl:
                #     arnold_mtl_name = f"{shd_namespace}:{arnold_mtl[0]}"
                #     cmds.connectAttr(f"{arnold_mtl_name}.outColor", f"{shadingEngine}.aiSurfaceShader")

    except:



        regular_shaders = shader_dict['materials']['regular_shader']
        dis_shaders = shader_dict['materials']['displacement_shader']

        target_geo_group = cmds.ls(target_geos, type='transform')
        asset_shapes = cmds.ls(cmds.listRelatives(target_geo_group, ad=True, type='mesh'))

        for shader in regular_shaders:
            for shader_name, assign_shapes in shader.items():

                shapes = cmds.ls(list(map(lambda x: f"*:{x}", assign_shapes)))
                filtered_shapes = [i for i in shapes if i in asset_shapes]

                if filtered_shapes:

                    cmds.select(filtered_shapes, r=True)
                    cmds.hyperShade(assign=f"{shd_namespace}:{shader_name}")
                    cmds.select(cl=True)

                else:
                    print(f'씬 안에 {shader_name}에 필요한 메쉬가 없습니다.')

                    print("필요한 메쉬 리스트")
                    pprint(assign_shapes)
                    print('\n' * 3)

        for dis_shader in dis_shaders:
            for dis_shader_name, target_shapes in dis_shader.items():
                _shapes = cmds.ls(list(map(lambda x: f"*:{x}", target_shapes)))
                filtered_shapes = [i for i in _shapes if i in asset_shapes]

                if filtered_shapes:

                    SGs = list(set(cmds.listConnections(filtered_shapes, type='shadingEngine')))

                    for SG in SGs:
                        try:
                            cmds.connectAttr(f"{shd_namespace}:{dis_shader_name}.displacement", f"{SG}.displacementShader")
                        except Exception as e:
                            print("dis shader connect Failed - !!")
                            print(e)
                else:
                    print(f'씬 안에 {dis_shader_name}에 필요한 메쉬가 없습니다.')

                    print("필요한 메쉬 리스트")
                    pprint(target_shapes)
                    print('\n' * 3)










