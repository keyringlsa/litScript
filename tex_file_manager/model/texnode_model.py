import os
import re

from PySide2 import QtCore, QtGui

class MakeItem(object):

    def __init__(self, data_dict):
        self.name = data_dict['name']
        self.file_path = data_dict['file_path']
        self.tile_mode = data_dict['tile_mode']
        self.color_space = data_dict['color_space']
        self.tex_files = data_dict['tex_files']
        self.item = data_dict
        self.is_tx = True

        self.exist_tx_file()

    def exist_tx_file(self):

        for _file in self.tex_files:
            org_file_name, ext =  os.path.splitext(_file)
            tx_file_name = f"{org_file_name}_{self.color_space}_ACEScg{ext}.tx"

            if not os.path.isfile(tx_file_name):
                self.is_tx = False

class TexNodeTableModel(QtCore.QAbstractTableModel):
    HORIZONTAL_HEADERS = ['Name', 'File Path', 'Tile Mode', 'Color Space', 'Multi Tile Files', 'Exist Tx']

    def __init__(self, row_data=None, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)

        self.entri_data = []
        for data_dict in row_data:
            item = MakeItem(data_dict)
            self.entri_data.append(item)

    def rowCount(self, parent):
        return len(self.entri_data)

    def columnCount(self, parent):
        return len(self.HORIZONTAL_HEADERS)

    def headerData(self, row, orientation, role):
        if orientation == QtCore.Qt.Horizontal:
            if role == QtCore.Qt.DisplayRole:
                return self.HORIZONTAL_HEADERS[row]
        if orientation == QtCore.Qt.Vertical:
            if role == QtCore.Qt.DisplayRole:
                return QtCore.QAbstractTableModel.headerData(self, row, orientation, role)

    def data(self, index, role):
        row = index.row()
        column = index.column()
        item = self.entri_data[row]

        if role == QtCore.Qt.DisplayRole:
            if column == 0:
                return item.name
            elif column == 1:
                return item.file_path
            elif column == 2:
                return item.tile_mode
            elif column == 3:
                return item.color_space
            elif column == 4:
                if len(item.tex_files) > 1:
                    sequence_pattern = r'\d{4}'
                    view_data = re.findall(sequence_pattern, '/'.join(item.tex_files))
                    return ", ".join(view_data)
                else:
                    return None
            elif column == 5:
                if item.is_tx:
                    return "Exist"
                else:
                    return "None"

        elif role == QtCore.Qt.BackgroundColorRole:
            if item.is_tx:
                return QtGui.QBrush(QtGui.QColor(60,60,115))
            else:
                return QtGui.QBrush(QtGui.QColor(115,60,60))

        elif role == QtCore.Qt.UserRole:
            return item

        return None

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable