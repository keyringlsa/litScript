import os, sys
from glob import glob
import re
import maya.cmds as cmds


def make_file_structure(lkd_type):

    file_dir = cmds.file(q=True, sceneName=True)
    file_dir_split = file_dir.split('LKD')[0].replace("/","\\")
    file_dir_splitB = file_dir_split.split(os.sep)

    root_path = os.path.join(file_dir_splitB[0], "\\", file_dir_splitB[1], 'assets', lkd_type)

    items = os.listdir(root_path)

    row_datas = []

    for item in items:

        row_data = dict()

        source_path = 'LKD/wip/maya/data'
        real_root = os.path.join(root_path, item, source_path).replace('\\', '/')

        if not os.path.isdir(real_root):
            os.makedirs(real_root)



        if os.path.isdir(real_root) and os.listdir(real_root):

            configues = glob(real_root + "/*") #특정 파일이 하고 싶은 경우 f포매팅f"/{item}_LGT_*_v*.json"
            row_data['configues'] = configues

        row_data['name'] = item

        row_datas.append(row_data)



    return row_datas





