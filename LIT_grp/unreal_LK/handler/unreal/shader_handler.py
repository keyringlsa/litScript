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
                                        txt_re = txt_path[0].replace("<UDIM>", "{}")
                                        print(txt_re)

                                        # Example usage
                                        udim_range = range(1001, 1050)  # UDIM의 범위
                                        for udim in udim_range:
                                                texture_path = txt_re.format(udim)
                                                if os.path.exists(texture_path):
                                                        destination_path = f"/Game/{lkd_type}/{sel}/TEX"  # 프로젝트 내에서 텍스처를 저장할 경로
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


