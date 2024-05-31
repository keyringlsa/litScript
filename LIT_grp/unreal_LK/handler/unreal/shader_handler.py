import unreal
import yaml
import os



def unreal_txt_import(sel, file_path, lkd_type) :
        yaml_file_path = file_path

        sel_low = sel.lower()
        if lkd_type == "Character":
                lkd_type_low = "ch"
        else:
                lkd_type_low = lkd_type.lower()

        with open(yaml_file_path, 'r') as file:
                shader_dict = yaml.full_load(file)

                for shader_list in shader_dict['shading_engines']:
                        for sh_name, row_data in shader_list.items():
                                mat_name = row_data['mat']
                                txt_path = row_data['textures']

                                if txt_path:
                                        txt_re = txt_path[0].replace("<UDIM>", "{}")
                                        print(txt_re)

                                        # Example usage
                                        udim_range = range(1001, 1050)  # UDIM의 범위
                                        for udim in udim_range:
                                                texture_path = txt_re.format(udim)
                                                if os.path.exists(texture_path):
                                                        destination_path = f"/Game/project/asset/{lkd_type_low}/{sel_low}/tex"  # 프로젝트 내에서 텍스처를 저장할 경로
                                                        print(destination_path)
                                                        import_texture(texture_path, destination_path)
                                                        break  # 파일을 찾았으면 반복문을 종료합니다.

                                # if txt_path:
                                #
                                #
                                #         txt_re = txt_path[0].replace("<UDIM>", "1001")
                                #         print(txt_re)
                                #
                                #         # Example usage
                                #         texture_path = txt_re  # 경로를 실제 텍스처 파일 경로로 변경하세요
                                #         destination_path = f"/Game/{lkd_type}/{sel}/TEX"  # 프로젝트 내에서 텍스처를 저장할 경로
                                #         print(destination_path)
                                #         import_texture(texture_path, destination_path)


def import_texture(file_path, destination_path):

        AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
        AssetImportTask = unreal.AssetImportTask()
        AssetImportTask.set_editor_property('filename', file_path)
        AssetImportTask.set_editor_property('destination_path', destination_path)
        AssetTools.import_asset_tasks([AssetImportTask])


def mtl_connect(sel, file_path, lkd_type):
        yaml_file_path = file_path
        sel_low = sel.lower()
        if lkd_type == "Character" :
                lkd_type_low = "ch"
        else :
                lkd_type_low = lkd_type.lower()


        material_package_path = f"/Game/project/asset/{lkd_type_low}/{sel_low}/mtl"
        text_package_path = f"/Game/project/asset/{lkd_type_low}/{sel_low}/tex"
        with open(yaml_file_path, 'r') as file:
                shader_dict = yaml.full_load(file)

                for shader_list in shader_dict['shading_engines']:
                        for sh_name, row_data in shader_list.items():
                                mat_name = row_data['mat'][0]
                                txt_path = row_data['textures']
                                if txt_path :
                                        txt_base_name = os.path.basename(txt_path[0])
                                        txt_name = txt_base_name.split('.')[0]
                                        file_ext = txt_base_name.split('.')[-1]

                                        txt_real_path = f"{text_package_path}/{txt_name}"

                                        material_path = f"{material_package_path}/{mat_name}"

                                        material = unreal.EditorAssetLibrary.load_asset(material_path)
                                        if not material:
                                                print(f"Material not found at: {material_path}")
                                                return

                                        color_texture = unreal.EditorAssetLibrary.load_asset(
                                                txt_real_path)
                                        if color_texture:
                                                txt_expression = unreal.MaterialEditingLibrary.create_material_expression(
                                                        material, unreal.MaterialExpressionTextureSample, -384, 200)
                                                txt_expression.texture = color_texture

                                                if txt_name.split('_')[-1] == "baseColor" or "dif" or "diffuse" :
                                                        if file_ext == "exr" :
                                                                # 버츄얼 샘플러 타입으로 변경
                                                                txt_expression.set_editor_property("sampler_type",
                                                                                                   unreal.MaterialSamplerType.SAMPLERTYPE_VIRTUAL_LINEAR_COLOR)
                                                                unreal.MaterialEditingLibrary.connect_material_property(
                                                                        txt_expression, "",
                                                                        unreal.MaterialProperty.MP_BASE_COLOR)
                                                                pass

                                                        else:
                                                                # Base Color 텍스처 설정

                                                                # 버츄얼 샘플러 타입으로 변경
                                                                txt_expression.set_editor_property("sampler_type",
                                                                                                   unreal.MaterialSamplerType.SAMPLERTYPE_VIRTUAL_COLOR)
                                                                unreal.MaterialEditingLibrary.connect_material_property(
                                                                        txt_expression, "",
                                                                        unreal.MaterialProperty.MP_BASE_COLOR)


                                                elif txt_name.split('_')[-1] == "emi":

                                                        # emissive 텍스처 설정

                                                        txt_expression.set_editor_property("sampler_type",
                                                                                                unreal.MaterialSamplerType.SAMPLERTYPE_VIRTUAL_COLOR)
                                                        unreal.MaterialEditingLibrary.connect_material_property(
                                                                txt_expression, "",
                                                                unreal.MaterialProperty.MP_EMISSIVE_COLOR)






                                                elif txt_name.split('_')[-1] == "nor":

                                                        # noraml 텍스처 설정

                                                        # 버츄얼 샘플러 타입으로 변경
                                                        txt_expression.set_editor_property("sampler_type",
                                                                                              unreal.MaterialSamplerType.SAMPLERTYPE_VIRTUAL_NORMAL)
                                                        unreal.MaterialEditingLibrary.connect_material_property(
                                                                txt_expression, "",
                                                                unreal.MaterialProperty.MP_NORMAL)

                                                else :
                                                        continue

                                unreal.EditorAssetLibrary.save_asset(material.get_path_name())
                                print(f"Textures applied to material at: {material_path}")





# def get_materials_in_folder(folder_path):
#         # 에디터 애셋 라이브러리를 사용하여 모든 애셋을 가져옵니다.
#         asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()
#
#         # 폴더 내의 모든 애셋 정보를 가져옵니다.
#         asset_data_list = asset_registry.get_assets_by_path(folder_path, recursive=True)
#
#         # Material 애셋만 필터링합니다.
#         material_list = []
#         for asset_data in asset_data_list:
#                 # Name 객체를 문자열로 변환
#                 asset_name_str = str(asset_data.asset_name)
#                 material_list.append(asset_name_str)
#
#         return material_list
#

def create_folder_in_unreal(sel, lkd_type):
        sel_low = sel.lower()
        if lkd_type == "Character":
                lkd_type_low = "ch"
        else:
                lkd_type_low = lkd_type.lower()
        bg_package_path = f"/Game/project/asset/{lkd_type_low}/{sel_low}/bp"
        fbx_package_path = f"/Game/project/asset/{lkd_type_low}/{sel_low}/fbx"
        material_package_path = f"/Game/project/asset/{lkd_type_low}/{sel_low}/mtl"
        text_package_path = f"/Game/project/asset/{lkd_type_low}/{sel_low}/tex"

        asset_tools = unreal.AssetToolsHelpers.get_asset_tools()


        paths_to_create = [
                bg_package_path,
                fbx_package_path,
                material_package_path,
                text_package_path
        ]


        for path in paths_to_create:
                result = unreal.EditorAssetLibrary.make_directory(path)
                if result:
                        unreal.log('Successfully created folder: {}'.format(path))
                else:
                        unreal.log_error('Failed to create folder: {}'.format(path))