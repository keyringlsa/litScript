
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




def import_fbx_to_unreal(fbx_file_path, destination_path, asset_type):
    task = unreal.AssetImportTask()
    task.filename = fbx_file_path
    task.destination_path = destination_path
    task.automated = True
    task.replace_existing = True
    task.save = True

    # FBX 임포트 설정
    options = unreal.FbxImportUI()

    # 스켈레톤 메쉬 설정인데 추후 리깅 껄로 테스트해봐야함 아직 베타
    skeletal_list = ["ch", "prop"]
    if asset_type in skeletal_list:
        options = buildSkeletalMeshImportOptions(options)  # buildSkeletalMeshImportOptions 함수의 반환 값을 할당

    else:
        options = buildStaticMeshImportOptions(options)  # buildStaticMeshImportOptions 함수의 반환 값을 할당


    task.options = options

    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])

    imported_assets = task.get_editor_property('imported_object_paths')
    return imported_assets

def buildStaticMeshImportOptions(options):
    options.set_editor_property('import_mesh', True)
    options.set_editor_property('import_textures', False)
    options.set_editor_property('import_materials', False)
    options.set_editor_property('import_as_skeletal', False)  # Static Mesh
    options.static_mesh_import_data.set_editor_property('import_translation', unreal.Vector(0.0, 0.0, 0.0))
    options.static_mesh_import_data.set_editor_property('import_rotation', unreal.Rotator(0.0, 0.0, 0.0))
    options.static_mesh_import_data.set_editor_property('import_uniform_scale', 1.0)
    options.static_mesh_import_data.set_editor_property('combine_meshes', False)
    options.static_mesh_import_data.set_editor_property('generate_lightmap_u_vs', True)
    options.static_mesh_import_data.set_editor_property('auto_generate_collision', True)
    return options

def buildSkeletalMeshImportOptions(options):
    options.set_editor_property('import_mesh', True)
    options.set_editor_property('import_textures', True)
    options.set_editor_property('import_materials', True)
    options.set_editor_property('import_as_skeletal', True)  # Skeletal Mesh
    options.skeletal_mesh_import_data.set_editor_property('import_translation', unreal.Vector(0.0, 0.0, 0.0))
    options.skeletal_mesh_import_data.set_editor_property('import_rotation', unreal.Rotator(0.0, 0.0, 0.0))
    options.skeletal_mesh_import_data.set_editor_property('import_uniform_scale', 1.0)
    options.skeletal_mesh_import_data.set_editor_property('import_morph_targets', True)
    options.skeletal_mesh_import_data.set_editor_property('update_skeleton_reference_pose', False)
    return options





def move_materials(destination_path, material_package_path):

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

    obj_name = row_data.name
    version = row_data.version

    asset_type = shader_importer.convert_type(type_datas)




    fbx_file_path = row_data.file_path
    destination_path = f"/Game/project/asset/{asset_type}/{obj_name}/fbx/v{version:03d}"
    imported_assets = import_fbx_to_unreal(fbx_file_path, destination_path, asset_type)

    # 머티리얼을 mtl 폴더로 이동
    material_package_path = f"/Game/project/asset/{asset_type}/{obj_name}/mtl/v{version:03d}"
    move_materials(destination_path, material_package_path)

