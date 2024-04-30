# Author lt_hyunyong_ki in 2023 12 13

import os, re
from CoreModules.constant import *
from util.email_handler import main as email_handler
from pprint import pprint

class ShotgunPublisher():

    def __init__(self, sg=None, context=None, description=None, version_file=None, publish_files=None,
                 work_name=None, work_version=None):
        """
        parameters:
            sg: shotgun api object
            context: sgtk context object
            description: publish description
            version_file: file for upload, like jpg or mov
            publish_files: file for publish on shotgun website
            work_name: your work scene file name without path, file ext like ASSETNAME_MDL_main
            work_version: version number
        """

        self.context = context
        self.description = description
        self.version_file = version_file
        self.publish_files = publish_files
        self.work_name = work_name
        self.work_version = work_version

        if sg:
            self.sg = sg
        else:
            import connect_sg
            self.sg = connect_sg.Shotgun_Connect().sg

        self.version_id = None
        self.published_items = list()


    def create_version(self):

        item = {
            'cached_display_name': self.work_name,
            'code': self.work_name,
            'project': self.context.project,
            'entity': self.context.entity,
            'sg_task': self.context.task,
            'created_by': self.context.user,
            'description': self.description,
            'user': self.context.user,
        }

        self.version_id = self.sg.create("Version", item)

        if self.version_id:
            self.sg.upload('Version', self.version_id["id"], self.version_file, field_name="sg_uploaded_movie")
            self.sg.update("Version", self.version_id['id'],
                           {"sg_status_list": "pub"})
            self.sg.update("Task", self.context.task['id'],
                           {"sg_status_list": "pub"})

    def publish(self):

        if self.version_file:
            self.create_version()

        for _file in self.publish_files:

            file_path, file_name_ext = os.path.split(_file)
            file_name, _ext = os.path.splitext(file_name_ext)
            file_path = _file.replace("/", "\\")

            version_name = file_name
            matches = re.findall(r'_v\d{3}', version_name)
            if matches: version_name = version_name.replace(matches[0], "")

            item = {
                "code": file_name,
                "name": version_name,
                "path": {
                    'link_type': 'local',
                    'content_type': None,
                    'local_path': file_path
                },
                "image": None,
                "description": self.description,
                "created_by": self.context.user,
                "entity": self.context.entity,
                "project": self.context.project,
                "task": self.context.task,
                "version_number": self.work_version
            }
            item.update(PUBLISHEDTYPES[_ext])

            if self.version_id:
                item.update({"version": self.version_id})

            pub = self.sg.create('PublishedFile', item)

            if self.version_file:
                self.sg.upload('PublishedFile', pub['id'], self.version_file, field_name="image")
            self.published_items.append(pub)

    def execute_email_dialog(self):
        email_dialog = email_handler.EmailDialogMain(sg=self.sg,
                                                     context=self.context,
                                                     version=self.version_id,
                                                     publishes=self.published_items,
                                                     description=self.description)
        email_dialog.exec_()
