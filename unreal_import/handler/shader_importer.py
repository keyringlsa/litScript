import unreal, os, re, yaml



def convert_type(target_type):
    asset_type = target_type

    if asset_type == "Character":
        asset_type_path = "ch"
    elif asset_type == "Prop":
        asset_type_path = "prop"
    elif asset_type == "EnvProp":
        asset_type_path = "envprop"
    elif asset_type == "Env":
        asset_type_path = "env"

    return asset_type_path




def import_shader(row_data=None, target_type=None, imported_ver=None):
    asset_name = row_data.current_version.get("entity").get("name")
    version = row_data.version
    yaml_file_path = row_data.file_path
    asset_type = convert_type(target_type)


    imp_mtl = imported_ver["mtl"]

    imported_data = get_latest_version(imp_mtl, asset_name)

    import_tex(asset_name, version, yaml_file_path, asset_type)
    mtl_connect(asset_name, version, yaml_file_path, asset_type, imported_data)







def get_latest_version(paths, asset_name):

    folders = [path for path in paths if f'{asset_name}/mtl/' in path]

    # 숫자가 포함된 폴더의 버전 번호 추출 및 최대 버전 찾기
    max_version = -1
    for path in folders:
        match = re.search(r'v(\d+)', path)
        if match:
            version = int(match.group(1))
            if version > max_version:
                max_version = version

    return max_version if max_version != -1 else None









def import_tex(asset_name, version, yaml_file_path, asset_type):

    with open(yaml_file_path, 'r') as file:
        shader_dict = yaml.full_load(file)

        for shader_list in shader_dict['shading_engines']:
            for sh_name, row_data in shader_list.items():
                mat_name = row_data['mat']
                txt_paths = row_data['textures']

                if txt_paths:
                    for txt_path in txt_paths:
                        txt_re = txt_path.replace("<UDIM>", "{}")


                        # Example usage
                        udim_range = range(1001, 1050)  # UDIM의 범위
                        for udim in udim_range:
                            texture_path = txt_re.format(udim)
                            if os.path.exists(texture_path):
                                destination_path = f"/Game/project/asset/{asset_type}/{asset_name}/tex/v{version:03d}"  # 프로젝트 내에서 텍스처를 저장할 경로
                                print(destination_path)
                                import_texture(texture_path, destination_path)
                                break  # 파일을 찾았으면 반복문을 종료합니다.




def import_texture(file_path, destination_path):

        AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
        AssetImportTask = unreal.AssetImportTask()
        AssetImportTask.set_editor_property('filename', file_path)
        AssetImportTask.set_editor_property('destination_path', destination_path)
        AssetTools.import_asset_tasks([AssetImportTask])


def mtl_connect(asset_name, version, yaml_file_path, asset_type, imported_data):



    with open(yaml_file_path, 'r') as file:
        shader_dict = yaml.full_load(file)

    material_package_path = f"/Game/project/asset/{asset_type}/{asset_name}/mtl/v{imported_data:03d}"
    text_package_path = f"/Game/project/asset/{asset_type}/{asset_name}/tex/v{version:03d}"

    tex_filter = {"basecolor": ["baseColor", "diff", "dif", "diffuse"],
                  "normal": ["normal", "nor"],
                  "roughness": ["roughness", "rou"],
                  "specular": ["spec"],
                  "emission": ["emi", "Emissive"],
                  "transparency": [],
                  "opacity": ["opac", "opacity"],
                  "bump": [],
                  "metallic": [],
                  "OCC": []}



    for shader_list in shader_dict['shading_engines']:
        for sh_name, row_data in shader_list.items():
            mat_name = row_data['mat'][0]


            txt_paths = row_data['textures']
            if txt_paths:
                for txt_path in txt_paths:
                    txt_base_name = os.path.basename(txt_path)

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

                        if txt_name.split('_')[-1] in tex_filter["basecolor"]:
                            if file_ext == "exr":
                                # 버츄얼 샘플러 타입으로 변경
                                txt_expression.set_editor_property("sampler_type",
                                                                   unreal.MaterialSamplerType.SAMPLERTYPE_VIRTUAL_LINEAR_COLOR)
                                unreal.MaterialEditingLibrary.connect_material_property(
                                    txt_expression, "",
                                    unreal.MaterialProperty.MP_BASE_COLOR)


                            else:
                                # Base Color 텍스처 설정

                                # 버츄얼 샘플러 타입으로 변경
                                txt_expression.set_editor_property("sampler_type",
                                                                   unreal.MaterialSamplerType.SAMPLERTYPE_VIRTUAL_COLOR)
                                unreal.MaterialEditingLibrary.connect_material_property(
                                    txt_expression, "",
                                    unreal.MaterialProperty.MP_BASE_COLOR)


                        elif txt_name.split('_')[-1] in tex_filter["emission"]:

                            # emissive 텍스처 설정

                            txt_expression.set_editor_property("sampler_type",
                                                               unreal.MaterialSamplerType.SAMPLERTYPE_VIRTUAL_COLOR)
                            unreal.MaterialEditingLibrary.connect_material_property(
                                txt_expression, "",
                                unreal.MaterialProperty.MP_EMISSIVE_COLOR)






                        elif txt_name.split('_')[-1] in tex_filter["normal"]:

                            # noraml 텍스처 설정

                            # 버츄얼 샘플러 타입으로 변경
                            txt_expression.set_editor_property("sampler_type",
                                                               unreal.MaterialSamplerType.SAMPLERTYPE_VIRTUAL_NORMAL)
                            unreal.MaterialEditingLibrary.connect_material_property(
                                txt_expression, "",
                                unreal.MaterialProperty.MP_NORMAL)

                        else:
                            continue


                        unreal.EditorAssetLibrary.save_asset(material_path)




            print(f"Textures applied to material at: {material_path}")







def create_folder_in_unreal(row_datas=None, target_type=None) :

    for type, datas in row_datas.items():
        if target_type == datas['type']:
            asset_type = convert_type(target_type)
            asset_list = datas["name"]
            for data in asset_list:
                asset_name = data

                bg_package_path = f"/Game/project/asset/{asset_type}/{asset_name}/bp"
                fbx_package_path = f"/Game/project/asset/{asset_type}/{asset_name}/fbx"
                material_package_path = f"/Game/project/asset/{asset_type}/{asset_name}/mtl"
                text_package_path = f"/Game/project/asset/{asset_type}/{asset_name}/tex"

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