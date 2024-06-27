#테스트 코드
#이건 안의 파일까지 검색하는 함수
# def list_all_subfolders(folder_path):
#
#     asset_lib = unreal.EditorAssetLibrary()
#
#
#     folders = asset_lib.list_assets(folder_path, recursive=False, include_folder=True)
#
#
#     all_subfolders = []
#
#
#     def recursive_subfolder_search(folder):
#
#         subfolders = asset_lib.list_assets(folder, recursive=False, include_folder=True)
#         for subfolder in subfolders:
#             all_subfolders.append(subfolder)
#
#             recursive_subfolder_search(subfolder)
#
#
#     for folder in folders:
#         all_subfolders.append(folder)
#         recursive_subfolder_search(folder)
#
#     return all_subfolders

# 이건 폴더 전체 탐색
# def find_all_folders(folder_path):
#
#     asset_lib = unreal.EditorAssetLibrary()
#
#
#     folders = asset_lib.list_assets(folder_path, recursive=True, include_folder=True)
#
#
#     all_folders = []
#
#
#     for item in folders:
#         if asset_lib.does_directory_exist(item):
#             all_folders.append(item)
#
#     return all_folders

