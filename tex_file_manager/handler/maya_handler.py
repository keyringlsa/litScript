import os, sys, re

import maya.cmds as cmds
import maya.mel as mel

from pprint import pprint
from glob import glob


def get_tex_multi_tile_files(file_path):

    udim_pattern = r'\d{4}\.'
    result = re.search(udim_pattern, file_path)
    sequence_code = None

    if '<UDIM>' in file_path:
        sequence_code = '<UDIM>'
    elif result:
        sequence_code = result.group()[:-1]

    if sequence_code:
        search_files = glob(file_path.replace(sequence_code, '*'))
    else:
        search_files = [file_path]

    return search_files



def get_file_nodes_from_current_scene():

    all_file_node = cmds.ls(type='file')

    cmds.select(cl=True)

    file_list = list()

    for _file in all_file_node:
        file_path = cmds.getAttr(f"{_file}.ftn")
        tile_mode = cmds.getAttr(f"{_file}.uvTilingMode")
        color_space = cmds.getAttr(f"{_file}.colorSpace")

        if ' ' in color_space:
            color_space = ''.join(color_space.split(' '))

        tex_files = get_tex_multi_tile_files(file_path)

        file_node_dict = {
            "name": _file,
            "file_path": file_path,
            "tile_mode": tile_mode,
            "color_space": color_space,
            "tex_files": tex_files
        }

        file_list.append(file_node_dict)

    return file_list
