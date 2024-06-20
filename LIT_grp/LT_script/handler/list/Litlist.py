import os, sys
from glob import glob
import re
import maya.cmds as cmds


def make_file_structure(seq_path):



    items = os.listdir(seq_path)

    row_datas = list()

    for item in items:

        row_data = dict()

        source_path = 'LGT/wip/maya/data'
        real_root = os.path.join(seq_path, item, source_path).replace('\\', '/')

        if not os.path.isdir(real_root):
            os.makedirs(real_root)

        # configues = []
        # if os.path.isdir(real_root):
        #     files = os.listdir(real_root)
        #     pattern = re.compile(f"{item}_LGT_.*_v\d+\.json$")
        #     for file in files:
        #         if pattern.match(file):
        #             file_path = os.path.join(real_root, file)
        #             configues.append(file_path)
        #
        # row_data['name'] = item
        # row_data['configues'] = configues

        if os.path.isdir(real_root) and os.listdir(real_root):

            configues = glob(real_root + "/*") #특정 파일이 하고 싶은 경우 f포매팅f"/{item}_LGT_*_v*.json"
            row_data['configues'] = configues

        row_data['name'] = item

        row_datas.append(row_data)



    return row_datas





