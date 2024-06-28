import os

from PySide2 import QtCore, QtGui, QtWidgets


HORIZONTAL_HEADERS = ['name', 'artist', 'created_date', 'description', 'version', 'versions', 'import']
VERSION_CHANGE_ROLE = QtCore.Qt.UserRole + 1
VERSION_CHECK_ROLE = QtCore.Qt.UserRole + 2

ICON_PATH = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0] + '/icons'
CAM_ICON = os.path.join(ICON_PATH, 'camera.svg')
MESH_ICON = os.path.join(ICON_PATH, 'mesh.svg')
SHADER_ICON = os.path.join(ICON_PATH, 'shader_ball.png')


class PubItem(object):
    def __init__(self, name=None, current_version=None, all_versions=None, data_type=None, file_type=None, parent=None, p_row=None):
        self.name = name
        self.current_version = current_version
        self.all_versions = all_versions
        self.parent = parent
        self.children = []
        self.file_type = file_type # for import action
        self.data_type = data_type # for item delegate
        self.p_row = p_row # for background color role
        self.prefix = None

        if self.current_version is not None:
            self.user = self.current_version.get('created_by').get('name')
            self.created = self.current_version.get('created_at').strftime('%Y-%m-%d %H:%M:%S')
            self.description = self.current_version.get('description')
            self.version = self.current_version.get('version_number')
            self.version_str = f"{self.current_version['task']['name']}_v{self.version:03d}"
            self.file_path = self.current_version.get('path').get("local_path")
            self.task = self.current_version.get('task').get('name')
            self.id = self.current_version.get('id')

            if self.name.endswith('__GEO'):
                self.prefix = '__GEO'

            elif self.name.endswith('__MAT'):
                self.prefix = '__MAT'


            self.need_update = False
            self.check_latest_version()

    def set_version(self, version_str: str):

        for pub in self.all_versions:
            pub_version = pub['version_number']
            pub_version_str = f"{pub['task'].get('name')}_v{pub_version:03d}"

            if version_str == pub_version_str:
                print(f"{self.name} version change")
                print(f"{self.version_str} --> {version_str}")

                self.current_version = pub
                self.user = pub.get('created_by').get('name')
                self.created = pub.get('created_at').strftime('%Y-%m-%d %H:%M:%S')
                self.description = pub.get('description')
                self.version = pub.get('version_number')
                self.version_str = pub_version_str
                self.file_path = pub.get('path').get("local_path")
                self.task = pub.get('task').get('name')
                self.id = pub.get('id')



    def check_latest_version(self):

        current_created = self.current_version.get("created_at")
        self.need_update = False

        for version in self.all_versions:
            version_created = version.get("created_at")

            if version_created > current_created:
                self.need_update = True


    def appendChild(self, item):
        self.children.append(item)

    def child(self, row):
        return self.children[row]

    def childCount(self):
        return len(self.children)

    def columnCount(self):
        return len(HORIZONTAL_HEADERS)

    def data(self, column):

        if column == 0:
            return self.name
        else:
            return None


    def parentItem(self):
        return self.parent

    def row(self):
        if self.parent:
            return self.parent.children.index(self)
        return 0


class PubItemTreeModel(QtCore.QAbstractItemModel):
    def __init__(self, row_datas=None, parent=None,head_items=None, asset_type=None):
        super(PubItemTreeModel, self).__init__(parent)

        self.entri_datas = row_datas
        self.rootItem = PubItem()
        self.asset_type = asset_type
        self.head_items = head_items

        self.organize_rowdatas()


    def organize_rowdatas(self):

        for asset_name, imported_datas in self.entri_datas.items():
            head_type = None
            for h_type, h_data in self.head_items.items():
                if asset_name in h_data['name']:
                    head_type = h_type
                    break

            if head_type == self.asset_type:
                asset_item = PubItem(name=asset_name, parent=self.rootItem, p_row=1)
                self.rootItem.appendChild(asset_item)

                ## GEO

                geo_parent = PubItem(name="Geometry", parent=asset_item, p_row=2)
                asset_item.appendChild(geo_parent)

                for imported_geo in imported_datas['geometry']:
                    for geo_name, row_data in imported_geo.items():
                        data_type = row_data['type'].get("name")

                        current_version = row_data['current_version']
                        all_versions = row_data['all_versions']

                        geo_item = PubItem(name=geo_name, current_version=current_version,
                                           all_versions=all_versions, data_type="GEO", file_type=data_type,
                                           parent=geo_parent, p_row=3)
                        geo_parent.appendChild(geo_item)

                ## MATERIAL

                if len(imported_datas['shader']) > 0:
                    shader_parent = PubItem(name="Material", parent=asset_item, p_row=4)
                    asset_item.appendChild(shader_parent)

                    shader_item = PubItem(name=f"{asset_name}__MAT", current_version=imported_datas['shader'][-1],
                                          all_versions=imported_datas['shader'], data_type="YML", parent=shader_parent,
                                          p_row=5)
                    shader_parent.appendChild(shader_item)




    def index(self, row, column, parent=QtCore.QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        return QtCore.QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QtCore.QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parentItem()

        if parentItem == self.rootItem:
            return QtCore.QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent=QtCore.QModelIndex()):
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()

    def columnCount(self, parent=QtCore.QModelIndex()):
        return self.rootItem.columnCount()

    def data(self, index, role=QtCore.Qt.DisplayRole):

        row = index.row()
        column = index.column()
        item = index.internalPointer()

        if not index.isValid():
            return None

        if role == QtCore.Qt.DisplayRole:
            if item.current_version is None:
                if column == 0:
                    return item.name
            else:
                if column == 0:
                    return item.name
                elif column == 1:
                    return item.user
                elif column == 2:
                    return item.created
                elif column == 3:
                    return item.description
                elif column == 4:
                    return item.version
                elif column == 7:
                    return item.prefix

        elif role == QtCore.Qt.TextAlignmentRole:
            if column in [0, 1, 2, 3, 4]:
                return QtCore.Qt.AlignCenter

        elif role == QtCore.Qt.BackgroundColorRole:
            if item.p_row == 1:
                if column == 0:
                    dark_blue = QtGui.QColor(22, 51, 84)
                    dark_gray = QtGui.QColor(44, 44, 44)

                    gradient = QtGui.QLinearGradient(QtCore.QPointF(0, 0), QtCore.QPointF(1, 0))
                    gradient.setColorAt(0, dark_blue)
                    gradient.setColorAt(0.65, dark_gray)
                    gradient.setColorAt(1, dark_gray)
                    gradient.setCoordinateMode(QtGui.QLinearGradient.ObjectMode)
                    return QtGui.QBrush(gradient)

            elif item.p_row == 2:
                if column == 0:
                    dark_cyan = QtGui.QColor(88, 100, 100)
                    dark_gray = QtGui.QColor(44, 44, 44)

                    gradient = QtGui.QLinearGradient(QtCore.QPointF(0, 0), QtCore.QPointF(1, 0))
                    gradient.setColorAt(0, dark_cyan)
                    gradient.setColorAt(0.65, dark_gray)
                    gradient.setColorAt(1, dark_gray)
                    gradient.setCoordinateMode(QtGui.QLinearGradient.ObjectMode)
                    return QtGui.QBrush(gradient)

            elif item.p_row == 4:
                if column == 0:
                    dark_cyan = QtGui.QColor(130, 40, 40)
                    dark_gray = QtGui.QColor(44, 44, 44)



                    gradient = QtGui.QLinearGradient(QtCore.QPointF(0, 0), QtCore.QPointF(1, 0))
                    gradient.setColorAt(0, dark_cyan)
                    gradient.setColorAt(0.65, dark_gray)
                    gradient.setColorAt(1, dark_gray)
                    gradient.setCoordinateMode(QtGui.QLinearGradient.ObjectMode)
                    return QtGui.QBrush(gradient)

            else:
                if item.current_version is not None:
                    if item.need_update:
                        red_color = QtGui.QColor(100, 25, 25)
                        return QtGui.QBrush(red_color)

        elif role == QtCore.Qt.DecorationRole:
            if column == 0:
                if item.prefix == '__MAT':
                    return QtGui.QPixmap(SHADER_ICON).scaled(QtCore.QSize(50, 50), QtCore.Qt.KeepAspectRatio)
                elif item.prefix == '__CAM':
                    return QtGui.QPixmap(CAM_ICON).scaled(
                        QtCore.QSize(50, 50), QtCore.Qt.KeepAspectRatio)
                elif item.data_type == 'GEO':
                    return QtGui.QPixmap(MESH_ICON).scaled(
                        QtCore.QSize(50, 50), QtCore.Qt.KeepAspectRatio)

        elif role == QtCore.Qt.SizeHintRole:
            if column == 0:
                if item.p_row == 3:
                    return QtCore.QSize(200, 60)
                elif item.p_row == 5:
                    return QtCore.QSize(200, 60)
                else:
                    return QtCore.QSize(200, 25)


        elif role == QtCore.Qt.UserRole:
            return item

        return None

    def setData(self, index, value, role):
        if index.isValid():
            row_data = self.data(index, role=QtCore.Qt.UserRole)

            if role == VERSION_CHANGE_ROLE:
                row_data.set_version(value)
                return True
            elif role == VERSION_CHECK_ROLE:
                row_data.check_latest_version()
                return True

    def headerData(self, column, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            try:
                return HORIZONTAL_HEADERS[column]
            except IndexError:
                pass
        return None

class ImportedItemDelegate(QtWidgets.QItemDelegate):

    cmb_index_changed = QtCore.Signal(str, object)
    button_clicked = QtCore.Signal(object)
    shader_assign_clicked = QtCore.Signal(object)

    def __init__(self, parent=None):
        QtWidgets.QItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        column = index.column()
        item = index.data(QtCore.Qt.UserRole)

        editor = QtWidgets.QWidget(parent)
        layout = QtWidgets.QVBoxLayout(editor)
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(10)

        if column == 5:
            combo = QtWidgets.QComboBox(editor)

            layout.addWidget(combo)
            for pub_file in reversed(item.all_versions):
                if pub_file['version_number'] and pub_file['task']:
                    version_num = pub_file['version_number']
                    version_str = f"{pub_file['task'].get('name')}_v{version_num:03d}"
                    combo.addItem(version_str, userData=pub_file)

            current_version = item.current_version['version_number']
            current_version_str = f"{pub_file['task'].get('name')}_v{current_version:03d}"
            combo.setCurrentText(current_version_str)

            slot_changedComboIndex = lambda: self.changedComboIndex(version=combo.currentText(), row_index=index)
            combo.currentIndexChanged.connect(slot_changedComboIndex)

        elif column == 6:
            if item.data_type == "GEO":
                button = QtWidgets.QPushButton(editor)
                layout.addWidget(button)
                button.setText("import")
                button.setFixedSize(80, 40)
                labda_button_clicked = lambda : self.buttonFunction(index=index)
                button.clicked.connect(labda_button_clicked)

            elif item.data_type == "YML":

                styleSheet = """
                    QPushButton {
                        background-color: rgb(125, 50, 50);
                    }
                """

                button = QtWidgets.QPushButton(editor)
                button.setStyleSheet(styleSheet)
                layout.addWidget(button)
                button.setText("assign")
                button.setFixedSize(80, 40)
                labda_button_clicked = lambda: self.shader_buttonFunction(index=index)
                button.clicked.connect(labda_button_clicked)

        return editor

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    @QtCore.Slot()
    def buttonFunction(self, index):
        self.button_clicked.emit(index)

    @QtCore.Slot()
    def shader_buttonFunction(self, index):
        self.shader_assign_clicked.emit(index)

    @QtCore.Slot()
    def changedComboIndex(self, version=None, row_index=None):
        self.cmb_index_changed.emit(version, row_index)