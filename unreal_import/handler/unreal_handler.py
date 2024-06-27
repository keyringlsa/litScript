
import unreal
import yaml
import os
from imp import reload
from unreal_import.handler import shader_importer
reload(shader_importer)





def find_fbx_folders(folder_path):
    asset_lib = unreal.EditorAssetLibrary()

    fbx_folders = []
    mtl_folders = []

    def recursive_search_folders(current_folder):
        subfolders = asset_lib.list_assets(current_folder, recursive=False, include_folder=True)
        for subfolder in subfolders:
            if asset_lib.does_directory_exist(subfolder):
                folder_name = unreal.Paths.get_base_filename(subfolder)
                folder_path = unreal.Paths.get_path(subfolder)
                if "fbx" in folder_name.lower() or "fbx" in folder_path.lower():
                    fbx_folders.append(subfolder)
                elif "mtl" in folder_name.lower() or "mtl" in folder_path.lower():
                    mtl_folders.append(subfolder)
                recursive_search_folders(subfolder)


    recursive_search_folders(folder_path)

    return {"fbx": fbx_folders, "mtl": mtl_folders}


def already_exists_files(sel):

    asset_type = sel

    if asset_type == "Character" :
        asset_type_path = "ch"
    elif asset_type == "Prop" :
        asset_type_path = "prop"
    elif asset_type == "EnvProp" :
        asset_type_path = "envprop"
    elif asset_type == "Env" :
        asset_type_path = "env"

    unreal_project_folder = os.path.join('/Game/project/asset/',asset_type_path)
    subdirs = find_fbx_folders(unreal_project_folder)

    return subdirs




def import_fbx_to_unreal(fbx_file_path, destination_path):
    # FBX 임포트 태스크 생성
    task = unreal.AssetImportTask()
    task.filename = fbx_file_path
    task.destination_path = destination_path
    task.automated = True
    task.replace_existing = True
    task.save = True

    # FBX 임포트 설정
    options = unreal.FbxImportUI()
    options.import_as_skeletal = False
    options.import_animations = False
    options.static_mesh_import_data.combine_meshes = False

    task.options = options

    # FBX 파일 임포트 실행
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])

    # 가져온 에셋 경로 반환
    imported_assets = task.get_editor_property('imported_object_paths')
    return imported_assets


def move_materials(destination_path, material_package_path):
    # 가져온 경로에서 머티리얼 파일을 찾아 mtl 폴더로 이동
    asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = asset_registry.get_assets_by_path(destination_path, recursive=True)

    # mtl 폴더 생성
    if not unreal.EditorAssetLibrary.does_directory_exist(material_package_path):
        unreal.EditorAssetLibrary.make_directory(material_package_path)

    for asset in assets:
        asset_data = asset.get_asset()
        if isinstance(asset_data, unreal.Material) or isinstance(asset_data, unreal.MaterialInstance):
            old_path = asset_data.get_path_name()
            asset_name = old_path.split('/')[-1]
            new_path = f"{material_package_path}/{asset_name}"
            unreal.EditorAssetLibrary.rename_asset(old_path, new_path)





def import_pub_item(row_data=None, type_datas=None):
    # current_version = row_data.current_version
    obj_name = row_data.name
    # task = row_data.task
    version = row_data.version
    # id = row_data.id

    asset_type = shader_importer.convert_type(type_datas)




    fbx_file_path = row_data.file_path
    destination_path = f"/Game/project/asset/{asset_type}/{obj_name}/fbx/v{version:03d}"
    imported_assets = import_fbx_to_unreal(fbx_file_path, destination_path)

    # 머티리얼을 mtl 폴더로 이동
    material_package_path = f"/Game/project/asset/{asset_type}/{obj_name}/mtl/v{version:03d}"
    move_materials(destination_path, material_package_path)



