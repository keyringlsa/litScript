import maya.cmds as cmds
import yaml


def work_area_info(context=None):

    project = context.project.get("name")
    entity = context.entity.get("name")

    return project, entity

def import_alembic_file(row_data=None, context=None):
    project, entity = work_area_info(context)

    name = row_data.name
    task = row_data.task
    version = row_data.version
    id = row_data.id
    namespace = name.split('_', 1)[0]
    asset_name = name.split('_', 1)[-1].split('__')[0]
    end_name = name.split('__')[-1]
    if end_name == "FX.abc" or "CFX.abc"  :
        namespace = name.split('_', 1)[0]+"FX"

    else :
        namespace = name.split('_', 1)[0]
    root_node = f"{namespace}:{asset_name}"

    if not cmds.objExists(root_node):
        root_node = cmds.group(name=root_node, em=True)

    file_path = row_data.file_path

    imported_file = cmds.file(file_path, type="Alembic",
                              reference=False, namespace=namespace,
                              rnn=True, i=True)

    tf_nodes = cmds.ls(imported_file, tr=True)
    top_nodes = [i for i in tf_nodes if not cmds.listRelatives(i, p=True)]

    for top_node in top_nodes:
        cmds.select(top_node, r=True)
        cmds.addAttr(top_node, ln='published_file_name', dt="string")
        cmds.addAttr(top_node, ln='asset_name', dt="string")
        cmds.addAttr(top_node, ln='task_name', dt="string")
        cmds.addAttr(top_node, ln='publish_version', attributeType='long')
        cmds.addAttr(top_node, ln='publish_id', attributeType='long')

        cmds.setAttr(f"{top_node}.published_file_name", name, type='string')
        cmds.setAttr(f"{top_node}.asset_name", asset_name, type='string')
        cmds.setAttr(f"{top_node}.task_name", task, type='string')
        cmds.setAttr(f"{top_node}.publish_version", version)
        cmds.setAttr(f"{top_node}.publish_id", id)

        cmds.setAttr(f"{top_node}.published_file_name", lock=True)
        cmds.setAttr(f"{top_node}.asset_name", lock=True)
        cmds.setAttr(f"{top_node}.task_name", lock=True)
        cmds.setAttr(f"{top_node}.publish_version", lock=True)
        cmds.setAttr(f"{top_node}.publish_id", lock=True)

        cmds.parent(top_node, root_node)

def import_camera_file(row_data=None, context=None):
    project, entity = work_area_info(context)

    name = row_data.name
    task = row_data.task
    version = row_data.version
    id = row_data.id
    namespace = "CAMERA"
    asset_name = "CAMERA"

    file_path = row_data.file_path

    with open(row_data.file_path, 'r') as f:
        camera_yaml_file = yaml.full_load(f)

    if camera_yaml_file.get("version_name"):
        namespace = camera_yaml_file.get("version_name")

    # import 2s keyframe locator

    # if camera_yaml_file.get("2s_keyframe"):
    #     keyframe_locator_info = camera_yaml_file['2s_keyframe']
    #     locator_name = keyframe_locator_info["name"]
    #     keyframes = keyframe_locator_info["key_frames"]
    #
    #     if not cmds.objExists(locator_name):
    #         locator = cmds.spaceLocator()
    #         cmds.rename(locator[0], locator_name)
    #     else:
    #         cmds.cutKey(locator_name, animation="keys")
    #
    #     for _time in keyframes:
    #         cmds.setKeyframe(locator_name, attribute='translateX', value=0, time=_time)


    # import cam abc

    cam_alembic_path = camera_yaml_file['abc']

    imported_file = cmds.file(cam_alembic_path, type="Alembic", reference=False,
                              i=True, namespace=namespace, rnn=True)

    tf_nodes = cmds.ls(imported_file, tr=True)
    top_nodes = [i for i in tf_nodes if not cmds.listRelatives(i, p=True)]

    for top_node in top_nodes:
        cmds.select(top_node, r=True)
        cmds.addAttr(top_node, ln='published_file_name', dt="string")
        cmds.addAttr(top_node, ln='asset_name', dt="string")
        cmds.addAttr(top_node, ln='task_name', dt="string")
        cmds.addAttr(top_node, ln='publish_version', attributeType='long')
        cmds.addAttr(top_node, ln='publish_id', attributeType='long')

        cmds.setAttr(f"{top_node}.published_file_name", name, type='string')
        cmds.setAttr(f"{top_node}.asset_name", asset_name, type='string')
        cmds.setAttr(f"{top_node}.task_name", task, type='string')
        cmds.setAttr(f"{top_node}.publish_version", version)
        cmds.setAttr(f"{top_node}.publish_id", id)

        cmds.setAttr(f"{top_node}.published_file_name", lock=True)
        cmds.setAttr(f"{top_node}.asset_name", lock=True)
        cmds.setAttr(f"{top_node}.task_name", lock=True)
        cmds.setAttr(f"{top_node}.publish_version", lock=True)
        cmds.setAttr(f"{top_node}.publish_id", lock=True)

def import_atom_file(row_data=None, context=None):
    project, entity = work_area_info(context)
    file_path = row_data.file_path

    cmds.file(file_path, type="atomImport", ra=True, i=True)

def import_pub_item(row_data=None, context=None):

    data_type = row_data.file_type

    if data_type == "Alembic Cache":
        import_alembic_file(row_data=row_data, context=context)
    elif data_type == "Yml File":
        import_camera_file(row_data=row_data, context=context)
    elif data_type == "Atom File":
        import_atom_file(row_data=row_data, context=context)


def get_imported_item_model():

    items = list()
    get_items = [i.split('.')[0] for i in cmds.ls("*:*.published_file_name")]

    for item in get_items:
        item_dict = dict()

        item_dict['name'] = item
        item_dict['entity'] = cmds.getAttr(f"{item}.asset_name")
        item_dict['task'] = cmds.getAttr(f"{item}.task_name")
        item_dict['version'] = cmds.getAttr(f"{item}.publish_version")
        item_dict['id'] = cmds.getAttr(f"{item}.publish_id")

        items.append(item_dict)

    return items

def already_exists_files():

    return [cmds.getAttr(i) for i in cmds.ls("*:*.published_file_name")]

def replace_alembic_reference(row_data=None):

    current_version = row_data.current_version
    obj_name = row_data.name
    task = row_data.task
    version = row_data.version
    id = row_data.id

    # reference_node = cmds.referenceQuery(obj_name, referenceNode=True)
    # cmds.file(row_data.file_path, loadReference=reference_node)
    cmds.select(obj_name, r=True)
    mesh_parent = cmds.listRelatives(obj_name, p=True, f=True, type='transform')[0]
    cmds.AbcImport(row_data.file_path, connect=mesh_parent, mode='replace', fitTimeRange=True)

    cmds.setAttr(f"{obj_name}.task_name", lock=False)
    cmds.setAttr(f"{obj_name}.publish_version", lock=False)
    cmds.setAttr(f"{obj_name}.publish_id", lock=False)

    cmds.setAttr(f"{obj_name}.task_name", task, type='string')
    cmds.setAttr(f"{obj_name}.publish_version", version)
    cmds.setAttr(f"{obj_name}.publish_id", id)

    cmds.setAttr(f"{obj_name}.task_name", lock=True)
    cmds.setAttr(f"{obj_name}.publish_version", lock=True)
    cmds.setAttr(f"{obj_name}.publish_id", lock=True)


    return True

def set_plugin_info():

    abc_plugin_list = ["AbcExport", "AbcImport"]

    for _plugin in abc_plugin_list:

        if not cmds.pluginInfo(_plugin, query=True, loaded=True):
            cmds.loadPlugin(_plugin)

def select_imported_item(item):

    cmds.select(item.name, r=True)