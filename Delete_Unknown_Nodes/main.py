from pprint import pprint

import maya.cmds as cmds

def run():
    plugins = cmds.unknownPlugin(query=True, list=True) or ['None data']

    for plugin in plugins:
        if plugin == 'None data':
            print(f'{plugin} is None data')
        else:
            try:
                cmds.unknownPlugin(plugin, remove=True)
                print(f'{plugin} --> succes remove')
            except:
                print(f'{plugin} --> failed remove')

    unknownNodes = cmds.ls(type="unknown")
    unknownNodes += cmds.ls(type="unknownDag")

    for un_node in unknownNodes:

        try:
            cmds.delete(un_node)
            print(f'{un_node} --> succes remove')
        except:
            try:
                cmds.lockNode(un_node, lock=False)
                cmds.delete(un_node)
                print(f'{un_node} --> succes remove')
            except Exception as e:
                print(e)

    graphInfo = cmds.ls(type='nodeGraphEditorInfo')
    if len(graphInfo) > 0:
        pprint(graphInfo)
        cmds.delete(graphInfo)


"""
from imp import reload
from Delete_Unknown_Nodes import main
reload(main)
main.run()
"""