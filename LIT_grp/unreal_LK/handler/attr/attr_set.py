

def custom_at_set(at_name,at_type):
    import maya.cmds as cmds
    sel = cmds.ls(sl=1)

    for i in sel :
        if at_type == "float":
            cmds.addAttr(i, ln=at_name, at=at_type, keyable=True)
        elif at_type == "string":
            cmds.addAttr(i, ln=at_name, dt=at_type)



def exp_set(ex_input):
    import maya.cmds as cmds

    if ex_input["ex_inputA"] :
        cmds.expression(s=ex_input["ex_inputA"] + "=" + ex_input["ex_inputB"] + ";")
    if ex_input["ex_inputC"] :
        cmds.expression(s=ex_input["ex_inputC"] + "=" + ex_input["ex_inputD"] + ";")
    if ex_input["ex_inputE"] :
        cmds.expression(s=ex_input["ex_inputE"] + "=" + ex_input["ex_inputF"] + ";")
