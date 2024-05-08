

from PySide2 import QtCore, QtGui


class RenderLayerItem(object):
    '''
    set get data
    '''
    def __init__(self, item):
        self._checked = item['render']
        self.name = item['name']

    @property
    def checked(self):
        return self._checked

    def setChecked(self, checked=True):
        self._checked = bool(checked)


class RenderLayerModel(QtCore.QAbstractListModel):
    '''
    display
    '''
    def __init__(self, entries=[], project_home=None, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self._entries = [RenderLayerItem(item) for item in entries]
        self.project_home = project_home

    def rowCount(self, parent):
        return len(self._entries)

    def data(self, index, role):
        row = index.row()
        if role == QtCore.Qt.DisplayRole:
            name = self._entries[row].name

            if name.startswith('rs_'):
                name = name.split('rs_', 1)[1]
            if name is "defaultRenderLayer":
                name = "masterLayer"
            return name

        elif role == QtCore.Qt.CheckStateRole:
            if self._entries[row].checked is True:
                return QtCore.Qt.Checked
            else:
                return QtCore.Qt.Unchecked
        elif role == QtCore.Qt.DecorationRole:
            if self._entries[row].checked is True:
                return QtGui.QPixmap("{0}/img/render_layer_enable.png".format(self.project_home))
            else:
                return QtGui.QPixmap("{0}/img/render_layer_disable.png".format(self.project_home))
        elif role == QtCore.Qt.UserRole:
            return self._entries[index.row()]
        return None

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if index.isValid():
            if role == QtCore.Qt.CheckStateRole:
                row_data = self._entries[index.row()]
                row_data.setChecked(not row_data.checked)
                return True
        return False

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable

