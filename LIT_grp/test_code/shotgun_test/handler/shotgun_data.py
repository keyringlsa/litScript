import shotgun_api3



class Shotgun_login(object):
    def __init__(self):
        self.sg = shotgun_api3.Shotgun("https://keyring-studio.shotgrid.autodesk.com",
                                       script_name='keyring_api',
                                       api_key="hodYi4uinv!wylfnssnsrchwv"
                                       )

    def default_script_auth(self):
        print("훌쩍")
        return self.sg




# def shotgun_toolkit() :
#     import sgtk
#     toolkit = sgtk.platform.current_engine()
#     tk_contxt = toolkit.context
#     tk_project = tk_contxt.project
#     tk_shot = tk_contxt.entity