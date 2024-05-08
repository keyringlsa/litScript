# Author lt_hyunyong_ki in 2024 02 19
from PySide2 import QtCore, QtGui, QtWidgets



HORIZONTAL_HEADERS = ['name', 'artist', 'created_date', 'description', 'version', 'versions', 'import']
VERSION_CHANGE_ROLE = QtCore.Qt.UserRole + 1

class ItemModel(object):

    def __init__(self, name=None, row_data=None, file_type=None, parent=None):
        # 여기에 부모와 자식 설정
        self.name = name
        self.row_data = row_data
        self.parent = parent
        self.children = []
        #self.head_item = head_item
        self.file_type = file_type

        if row_data is not None:
            self.user = self.row_data[-1].get('created_by').get('name')
            self.created = self.row_data[-1].get('created_at').strftime('%Y-%m-%d %H:%M:%S')
            self.description = self.row_data[-1].get('description')
            self.version = self.row_data[-1].get('version_number')
            self.file_path = self.row_data[-1].get('path').get("local_path")
            if self.row_data[-1].get('task') is not None:
                self.task = self.row_data[-1].get('task').get('name')
            else:
                self.task = "None"
            self.id = self.row_data[-1].get('id')

    def set_version(self, version_num: int):

        for pub in self.row_data:
            pub_version = pub['version_number']

            if version_num == pub_version:
                print(f"{self.name} version change")
                print(f"{self.version} --> {version_num}")

                self.user = pub.get('created_by').get('name')
                self.created = pub.get('created_at').strftime('%Y-%m-%d %H:%M:%S')
                self.description = pub.get('description')
                self.version = pub.get('version_number')
                self.file_path = pub.get('path').get("local_path")
                self.task = pub.get('task').get('name')
                self.id = pub.get('id')

    def appendChild(self, item):
        self.children.append(item)

    def child(self, row):
        return self.children[row]

    def childCount(self):
        return len(self.children)

    def columnCount(self):
        return len(HORIZONTAL_HEADERS)

    def parentItem(self):
        return self.parent

    def row(self):
        if self.parent:
            return self.parent.children.index(self)
        return 0


class ItemTreeModel(QtCore.QAbstractItemModel):
    def __init__(self, row_datas=None, parent=None, head_items=None):
        super(ItemTreeModel, self).__init__(parent)

        self.rootItem = ItemModel()  # 부모 선언
        self.entri_datas = row_datas

        self.head_items = head_items


        self.make_item()
        # 로우 데이터 받은거 for문으로 돌리기
        # for row_data in row_datas:
        #     self.make_item(dic=row_data, parent=self.rootItem)

    def make_item(self):
        camera_parent = ItemModel(name="CAMERA", parent=self.rootItem)
        alembic_parent = ItemModel(name="ALEMBIC", parent=self.rootItem)
        atom_parent = ItemModel(name="ATOM", parent=self.rootItem)
        self.rootItem.appendChild(camera_parent)
        self.rootItem.appendChild(alembic_parent)
        self.rootItem.appendChild(atom_parent)

        created_items = []  # 이미 생성된 아이템들을 저장할 리스트

        for item_name, datas in self.entri_datas.items():
            data_type = datas['type'].get("name")
            version_data_list = datas['items']
            data_name = item_name.split('_')[1]
            data_task = datas['task'].get("name")



            if data_type == "Alembic Cache":
                # 알엠빅 아래에 카테고리 나누기
                for head in self.head_items:
                    head_type = self.head_items[head]['type']
                    head_names = self.head_items[head]['name']
                    if data_name in head_names:
                        parent_item = None
                        for child in alembic_parent.children:
                            if child.name == head_type:
                                parent_item = child
                                break
                        if not parent_item:
                            parent_item = ItemModel(name=head_type, parent=alembic_parent)
                            alembic_parent.appendChild(parent_item)
                        if item_name not in created_items:  # 이미 생성된 아이템인지 확인
                            item = ItemModel(name=item_name, row_data=version_data_list, file_type=data_type,
                                             parent=parent_item)
                            parent_item.appendChild(item)
                            created_items.append(item_name)  # 생성된 아이템 추가
                        break
            elif data_type == "Atom File":
                parent_item = atom_parent
            elif data_type == "Yml File":
                parent_item = camera_parent
            else:
                parent_item = self.rootItem

            if item_name not in created_items:  # 이미 생성된 아이템인지 확인
                item = ItemModel(name=item_name, row_data=version_data_list, file_type=data_type, parent=parent_item)
                parent_item.appendChild(item)
                created_items.append(item_name)  # 생성된 아이템 추가



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
            if item.row_data is None:
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

        elif role == QtCore.Qt.TextAlignmentRole:
            if column in [0, 1, 2, 3, 4]:
                return QtCore.Qt.AlignCenter

        elif role == QtCore.Qt.BackgroundColorRole:
            if item.row_data is None:
                if column == 0:
                    dark_blue = QtGui.QColor(22, 51, 84)
                    dark_gray = QtGui.QColor(44, 44, 44)

                    gradient = QtGui.QLinearGradient(QtCore.QPointF(0, 0), QtCore.QPointF(1, 0))
                    gradient.setColorAt(0, dark_blue)
                    gradient.setColorAt(0.65, dark_gray)
                    gradient.setColorAt(1, dark_gray)
                    gradient.setCoordinateMode(QtGui.QLinearGradient.ObjectMode)
                    return QtGui.QBrush(gradient)

        elif role == QtCore.Qt.FontRole:
            font = QtGui.QFont()
            parent_index = index.parent()  # 인덱스의 부모를 가져옴
            parent_item = parent_index.internalPointer() if parent_index.isValid() else None  # 부모 아이템 가져옴
            if column == 0 and parent_item is None:  # 부모 아이템이 없는 경우에만 백그라운드 적용
                font.setPointSize(12)

            elif column == 0 :
                font.setPointSize(12)

            return font



        elif role == QtCore.Qt.UserRole:
            return item

        return None




    def headerData(self, column, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            try:
                return HORIZONTAL_HEADERS[column]
                # return None
            except IndexError:
                pass

        return None



class ImportButtonDelegate(QtWidgets.QItemDelegate):
    cmb_index_changed = QtCore.Signal(int, object)
    button_clicked = QtCore.Signal(object)

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
            for pub_file in reversed(item.row_data):
                version_num = pub_file['version_number']
                combo.addItem(str(version_num), userData=pub_file)

            slot_changedComboIndex = lambda: self.changedComboIndex(version=combo.currentText(), row_index=index)
            combo.currentIndexChanged.connect(slot_changedComboIndex)

        elif column == 6:
            button = QtWidgets.QPushButton(editor)
            layout.addWidget(button)
            button.setText(f"import")
            button.setFixedSize(80, 40)
            labda_button_clicked = lambda: self.buttonFunction(index=index)
            button.clicked.connect(labda_button_clicked)

        return editor

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    @QtCore.Slot()
    def buttonFunction(self, index):
        self.button_clicked.emit(index)

    @QtCore.Slot()
    def changedComboIndex(self, version=None, row_index=None):
        self.cmb_index_changed.emit(int(version), row_index)