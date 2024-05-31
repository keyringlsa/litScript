import unreal
import yaml
import os



def unreal_txt_import(sel, file_path, lkd_type) :
        yaml_file_path = file_path


        with open(yaml_file_path, 'r') as file:
                shader_dict = yaml.full_load(file)

                for shader_list in shader_dict['shading_engines']:
                        for sh_name, row_data in shader_list.items():
                                mat_name = row_data['mat']
                                txt_path = row_data['textures']

                                if txt_path:
                                        txt_re = txt_path[0].replace("<UDIM>", "1001")
                                        print(txt_re)

                                        # Example usage
                                        texture_path = txt_re  # 경로를 실제 텍스처 파일 경로로 변경하세요
                                        destination_path = f"/Game/{lkd_type}/{sel}/TEX"  # 프로젝트 내에서 텍스처를 저장할 경로
                                        import_texture_as_virtual_texture(texture_path, destination_path)





def import_texture_as_virtual_texture(texture_path, destination_path):
        # Create a new AssetTools helper
        asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

        # Specify the import task with the texture path
        import_task = unreal.AssetImportTask()
        import_task.filename = texture_path
        import_task.destination_path = destination_path
        import_task.automated = True
        import_task.save = True

        # Import the texture
        asset_tools.import_asset_tasks([import_task])

        # Get the imported asset
        imported_asset_path = destination_path + "/" + unreal.Paths.get_base_filename(
                texture_path)
        texture = unreal.EditorAssetLibrary.load_asset(imported_asset_path)

        if texture:
                # Convert texture to virtual texture
                convert_to_virtual_texture(texture)
        else:
                print(f"Failed to load the imported texture: {imported_asset_path}")


def convert_to_virtual_texture(texture):
        # Ensure the asset is of type Texture
        if isinstance(texture, unreal.Texture):
                texture.virtual_texture_streaming = True
                texture.save_package()

                print(f"Texture {texture.get_name()} converted to Virtual Texture.")
        else:
                print(f"The asset {texture.get_name()} is not a texture.")