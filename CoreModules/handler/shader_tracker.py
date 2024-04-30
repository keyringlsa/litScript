import os, re, yaml, shutil
import maya.cmds as cmds

from pprint import pprint
from imp import reload
from glob import glob
from Lookdev_Publisher.handler import file_handler
from CoreModules.USD_Contractor import usd_material_make
from CoreModules.handler import query_data

reload(file_handler)
reload(usd_material_make)
reload(query_data)

class ShaderHandler(object):

    def __init__(self, context=None,
                 sg=None,
                 usd_contractor=None,
                 copy_tex=True,
                 to_unreal=False):

        self.context = context
        self.sg = sg
        self.entity = query_data.get_entity(context.entity, sg)
        self.usd_contractor = usd_contractor
        self.project_name = context.project.get("name")
        self.asset_name = context.entity.get("name")
        self.task_name = context.task.get("name")
        self.version = None
        self.shaders = None
        self.lookdev_info_dict = {"data_type": "maya_shade"}
        self.copy_tex = copy_tex
        self.to_unreal = to_unreal

        self.target = cmds.ls("*__GEO", "*__BLUR")

        # file

        self.shade_scene = None  # pub shade scene
        self.shade_yaml = None  # pub yml file
        self.tex_pub_path = None
        self.wip_maya_scene = cmds.file(q=True, sn=True)
        self.pub_maya_scene = self.wip_maya_scene.replace("wip", "pub") # pub maya scene
        self.pub_area = self.pub_maya_scene.rsplit('/', 2)[0]
        self.version_name = cmds.file(q=True, sn=True, shn=True)
        self.version_str = self.version_name.split('_')[2]


        # check current scene

        cmds.file(type='mayaBinary', save=True, force=True)



    def get_current_version(self):

        pattern = r'v\d{3}'
        matches = re.findall(pattern, self.version_name)[0]
        self.version = int(matches[1:])

    def get_assign_shaders(self):

        sel_shapes = cmds.ls(cmds.listRelatives(self.target, f=True, ad=True))
        shading_grp = cmds.listConnections(sel_shapes, type='shadingEngine')
        shaders = cmds.ls(cmds.listConnections(shading_grp), materials=1)
        if not shaders:
            for sg in shading_grp:
                shader = cmds.connectionInfo(f"{sg}.surfaceShader", sfd=True).split(".")[0]
                shaders.append(shader)
        self.shaders = list(set(shaders))

    def get_assign_mesh_dict(self):

        sel_shapes = cmds.ls(cmds.listRelatives(self.target, f=True, ad=True))
        shading_grp = list(set(cmds.listConnections(sel_shapes, type='shadingEngine')))
        SG_list = list()

        for SG in shading_grp:
            meshes = cmds.sets(SG, q=True)
            mat = cmds.listConnections(f"{SG}.surfaceShader")
            dis_mat = cmds.listConnections(f"{SG}.displacementShader")
            # arnold_mat = cmds.listConnections(f"{SG}.aiSurfaceShader")

            SG_dict = dict()
            SG_dict[SG] = {"meshes": meshes,
                           "mat": mat,
                           "dis_mat": dis_mat}

            tex_list = list()
            get_tex_files = cmds.listConnections(cmds.listHistory(mat), type='file')
            if get_tex_files:
                file_nodes = list(set(get_tex_files))
                for _file in file_nodes:
                    ftn = cmds.getAttr(f"{_file}.ftn")
                    tex = file_handler.get_tex_files(ftn)
                    if tex not in tex_list:
                        tex_list.append(tex)
                SG_dict[SG].update({"textures": tex_list})
            else:
                SG_dict[SG].update({"textures": []})
            SG_list.append(SG_dict)

        self.lookdev_info_dict.update({"shading_engines": SG_list})
        self.lookdev_info_dict.update({"shader_scene": self.shade_scene})

    def set_export_path(self):

        pub_shade_path = self.pub_area + f"/data/shade/{self.version_str}_v{self.version:03d}"
        pub_tex_path = self.pub_area + f"/sourceimages/{self.version_str}_v{self.version:03d}"

        path_list = [pub_shade_path, pub_tex_path]

        for _path in path_list:
            if not os.path.isdir(_path):
                os.makedirs(_path)

        self.shade_scene = pub_shade_path + f"/{self.asset_name}_Shade_v{self.version:03d}.mb"
        self.shade_yaml = pub_shade_path + f"/{self.asset_name}_Shade_v{self.version:03d}.yml"
        self.tex_pub_path = pub_tex_path



    def copy_to_texture_pub_path(self):

        require_pattern = self.wip_maya_scene.rsplit("/", 2)[0]

        all_file_nodes = cmds.ls(type='file')

        for _file in all_file_nodes:
            tex = cmds.getAttr(f"{_file}.ftn")

            if require_pattern in tex:
                link_tex_files, uv_type = file_handler.get_link_tex_files(tex_pattern=tex, paste_path=self.tex_pub_path)

                if link_tex_files:
                    cmds.setAttr(f"{_file}.ftn", link_tex_files[0], type='string')
                    if uv_type == "UDIM":
                        cmds.setAttr(f"{_file}.uvTilingMode", 3)


                    pprint(link_tex_files)
                    print(uv_type)

    def copy_to_texture_unreal(self):

        asset_type = self.entity["sg_asset_type"]
        unreal_path = f"P:/{self.project_name}/UNREAL/Resources/Assets/{asset_type}/" \
                      f"{self.asset_name}/{self.asset_name}_textures"

        ShadingGroups = self.lookdev_info_dict["shading_engines"]

        for SG_dict in ShadingGroups:
            for SG in SG_dict:
                textures = SG_dict[SG]["textures"]
                file_list = []

                for tex in textures:

                    if "<UDIM>" in tex:
                        files = glob(tex.replace("<UDIM>", "*"))
                        file_list.extend(files)
                    else:
                        file_list.append(tex)

                for file in file_list:

                    unreal_dir = os.path.join(unreal_path, SG)
                    if not os.path.isdir(unreal_dir):os.makedirs(unreal_dir)

                    org_path, file_ext = os.path.split(file)
                    new_file = os.path.join(unreal_dir, file_ext)

                    shutil.copy2(file, new_file)



    def export_data(self):

        cmds.select(self.shaders, r=True)

        cmds.file(self.shade_scene,
                  force=True,
                  typ="mayaBinary",
                  exportSelected=True,
                  preserveReferences=True,
                  shader=True,
                  expressions=False,
                  constructionHistory=True)

        with open(self.shade_yaml, 'w') as f:
            yaml.dump(self.lookdev_info_dict, f)

    def export_usd(self):

        # export usd shader

        SG_list = self.lookdev_info_dict["shading_engines"]
        combine_usd = self.usd_contractor.combine_usd
        usd_path = f"{combine_usd.dir_path}" \
                   f"/MATERIAL/{self.usd_contractor.entity['name']}_preview_material.usda"

        for SG_dict in SG_list:
            for SG_name, SG_info in SG_dict.items():
                textures = SG_info["textures"]
                shader = SG_info["mat"][0]
                meshes = cmds.listRelatives(SG_info["meshes"], p=True, f=True)

                usd_shader = usd_material_make.UsdShaderMaker(
                    asset_name=self.asset_name,
                    usd_path=usd_path,
                    shader_name=shader,
                    textures=textures,
                    meshes=meshes
                )

                usd_shader.create_shader()

        # self.usd_contractor.make_combine(usd_path)
        combine_usd.open_stage()
        combine_usd.is_root = self.asset_name
        combine_usd.is_variant = "Shader"
        combine_usd.append_variant("Preview", usd_path)
        # combine_usd.combine_sublayer(usd_path)
        combine_usd.save_stage()

    def upgrade_wip_version(self):
        up_version_scene = self.wip_maya_scene.replace(f"v{self.version:03d}", f"v{self.version+1:03d}")
        shutil.copy2(self.wip_maya_scene, up_version_scene)

        cmds.file(up_version_scene, type="mayaBinary", open=True, force=True)

    # config setting
    def main(self):

        self.get_current_version()
        self.get_assign_shaders()
        self.set_export_path()
        self.get_assign_mesh_dict()

    # run export file
    def run_main(self):

        # copy tex file to pub path
        if self.copy_tex:
            self.copy_to_texture_pub_path()

        if self.to_unreal:
            self.copy_to_texture_unreal()

        # export shade scene, yaml, maya scene to pub path
        self.export_data()

        if self.usd_contractor:
            self.export_usd()

        return self.shade_yaml




