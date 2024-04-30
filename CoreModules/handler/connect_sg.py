import shotgun_api3


class Shotgun_Connect(object):

    def __init__(self):

        self.sg = shotgun_api3.Shotgun("https://keyring-studio.shotgrid.autodesk.com",
                                       script_name='keyring_api',
                                       api_key="hodYi4uinv!wylfnssnsrchwv"
                                       )

    def default_script_auth(self):
        print('connect shotgun api')
        return self.sg