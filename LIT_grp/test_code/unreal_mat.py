# def mtl_connect(asset_name, version, yaml_file_path, asset_type, imported_data):
#
#
#
#     with open(yaml_file_path, 'r') as file:
#         shader_dict = yaml.full_load(file)
#
#     material_package_path = f"/Game/project/asset/{asset_type}/{asset_name}/mtl/v{imported_data:03d}"
#     text_package_path = f"/Game/project/asset/{asset_type}/{asset_name}/tex/v{version:03d}"
#
#     tex_filter = {"basecolor":["baseColor", "diff", "dif", "diffuse"], "normal":["normal", "nor"],
#                   "roughness":["roughness","rou"], "specular":["spec"], "emission":["emi","Emissive"], "transparency": [],
#                     "opacity":["opac","opacity"], "bump":[], "metallic":[], "OCC":[]}
#
#
#
#     for shader_list in shader_dict['shading_engines']:
#         for sh_name, row_data in shader_list.items():
#             mat_name = row_data['mat'][0]
#             txt_path = row_data['textures']
#             if txt_path:
#                 txt_base_name = os.path.basename(txt_path[0])
#                 txt_name = txt_base_name.split('.')[0]
#                 file_ext = txt_base_name.split('.')[-1]
#
#                 txt_real_path = f"{text_package_path}/{txt_name}"
#
#                 material_path = f"{material_package_path}/{mat_name}"
#
#                 material = unreal.EditorAssetLibrary.load_asset(material_path)
#                 if not material:
#                     print(f"Material not found at: {material_path}")
#                     return
#
#                 color_texture = unreal.EditorAssetLibrary.load_asset(
#                     txt_real_path)
#                 if color_texture:
#
#                     txt_expression = unreal.MaterialEditingLibrary.create_material_expression(
#                         material, unreal.MaterialExpressionTextureSample, -384, 200)
#                     txt_expression.texture = color_texture
#
#                     if txt_name.split('_')[-1] in tex_filter["basecolor"]:
#                         if file_ext == "exr":
#                             # 버츄얼 샘플러 타입으로 변경
#                             txt_expression.set_editor_property("sampler_type",
#                                                                unreal.MaterialSamplerType.SAMPLERTYPE_VIRTUAL_LINEAR_COLOR)
#                             unreal.MaterialEditingLibrary.connect_material_property(
#                                 txt_expression, "",
#                                 unreal.MaterialProperty.MP_BASE_COLOR)
#                             unreal.EditorAssetLibrary.save_asset(
#                                 material.get_path_name())
#
#                         else:
#                             # Base Color 텍스처 설정
#
#                             # 버츄얼 샘플러 타입으로 변경
#                             txt_expression.set_editor_property("sampler_type",
#                                                                unreal.MaterialSamplerType.SAMPLERTYPE_VIRTUAL_COLOR)
#                             unreal.MaterialEditingLibrary.connect_material_property(
#                                 txt_expression, "",
#                                 unreal.MaterialProperty.MP_BASE_COLOR)
#                             unreal.EditorAssetLibrary.save_asset(
#                                 material.get_path_name())
#
#                     elif txt_name.split('_')[-1] in tex_filter["emission"]:
#
#                         # emissive 텍스처 설정
#
#                         txt_expression.set_editor_property("sampler_type",
#                                                            unreal.MaterialSamplerType.SAMPLERTYPE_VIRTUAL_COLOR)
#                         unreal.MaterialEditingLibrary.connect_material_property(
#                             txt_expression, "",
#                             unreal.MaterialProperty.MP_EMISSIVE_COLOR)
#                         unreal.EditorAssetLibrary.save_asset(material.get_path_name())
#
#
#
#
#
#                     elif txt_name.split('_')[-1] in tex_filter["normal"]:
#
#                         # noraml 텍스처 설정
#
#                         # 버츄얼 샘플러 타입으로 변경
#                         txt_expression.set_editor_property("sampler_type",
#                                                            unreal.MaterialSamplerType.SAMPLERTYPE_VIRTUAL_NORMAL)
#                         unreal.MaterialEditingLibrary.connect_material_property(
#                             txt_expression, "",
#                             unreal.MaterialProperty.MP_NORMAL)
#                         unreal.EditorAssetLibrary.save_asset(material.get_path_name())
#                     else:
#                         continue
#
#                     unreal.EditorAssetLibrary.save_asset(material.get_path_name())
#
#             # unreal.EditorAssetLibrary.save_asset(material.get_path_name())
#             print(f"Textures applied to material at: {material_path}")






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