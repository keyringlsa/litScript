import os, sys
from glob import glob
import re
import maya.cmds as cmds


def on_double_click(name):

    file_dir = cmds.file(q=True, sceneName=True)
    file_dir_split = file_dir.split('LGT')[0].replace("/","\\")
    file_dir_splitB = file_dir_split.split(os.sep)

    root_path = os.path.join(file_dir_splitB[0], file_dir_splitB[1], file_dir_splitB[2], file_dir_splitB[3])

    path = os.path.join(root_path,name)

    source_path = 'LGT/wip/maya/data'
    real_root = os.path.join(path, source_path).replace('\\', '/')


    os.startfile(real_root)




def datalist(name) :
    item = name

    file_dir = cmds.file(q=True, sceneName=True)
    file_dir_split = file_dir.split('LGT')[0].replace("/","\\")
    file_dir_splitB = file_dir_split.split(os.sep)

    root_path = os.path.join(file_dir_splitB[0], file_dir_splitB[1], file_dir_splitB[2], file_dir_splitB[3])

    #litlist.py에 있던 configues를 아래로 변경처리
    datas = []

    source_path = 'LGT/wip/maya/data'
    real_root = os.path.join(root_path, item, source_path).replace('\\', '/')
    if os.path.isdir(real_root) and os.listdir(real_root):

        configues = glob(real_root + "/*")  # 특정 파일이 하고 싶은 경우 f포매팅f"/{item}_LGT_*_v*.json"
        datas.append(configues)


    row_datas = list()
    pattern = re.compile(f"{item}_LGT_.*_v\d+\.json$")
    if datas:
        for data in datas[0]:
            data_name = os.path.basename(data)

            row_data = dict()
            if pattern.match(data_name):
                data_re = data.replace('\\', '/')
                data_sp_name = data_name.split('.json')[0]


                name_match = re.match(rf"({item}_LGT_.*?)_v(\d+)\.json$", data_name)
                if name_match:
                    file_name = name_match.group(1)
                    file_version = name_match.group(2)

                    # Creating dictionary with name and version
                    row_data['name'] = file_name
                    row_data['version'] = file_version
                    row_datas.append(row_data)



    return row_datas








