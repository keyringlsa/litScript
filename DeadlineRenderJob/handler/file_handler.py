import os, sys, shutil
import re

from glob import glob

def is_latest_version(path, version):

    pattern = r'v\d{3}'
    matches = re.findall(pattern, path)[0]
    latest_version = version - 1
    latest_dir = None

    while(latest_version > 0):
        if os.path.isdir(path.replace(matches, f"v{latest_version:03d}")):
            latest_dir = path.replace(matches, f"v{latest_version:03d}")
            break
        latest_version -= 1

    return latest_dir

def copy_from_latest_version_file(item_dict):

    render_path = item_dict["render_dir"] + '/' + item_dict["version_name"] + '/' + item_dict["render_layer"]
    latest_dir = is_latest_version(render_path, item_dict['version_num'])

    if not os.path.isdir(render_path):
        os.makedirs(render_path)

    if latest_dir:
        img_files = glob(f"{latest_dir}/*")

        for _img_file in img_files:

            new_file = _img_file.replace(latest_dir, render_path)
            shutil.copy2(_img_file, new_file)


