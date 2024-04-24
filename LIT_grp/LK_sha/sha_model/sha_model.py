# Author lt_hyunyong_ki in 2024 02 19
from PySide2 import QtCore, QtGui, QtWidgets

HORIZONTAL_HEADERS = ['name', 'shader']


class ItemModel(object):

    def __init__(self, name=None, shader=None, parent=None):
        # 여기에 부모와 자식 설정
        self.name = name
        self.parent = parent
        self.shader = shader
        self.children = []

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
    def __init__(self, row_datas=None, parent=None):
        super(ItemTreeModel, self).__init__(parent)

        self.rootItem = ItemModel()  # 부모 선언

        # 로우 데이터 받은거 for문으로 돌리기
        for row_data in row_datas:
            self.make_item(dic=row_data, parent=self.rootItem)

    def make_item(self, dic=None, parent=None):
        name = dic["name"]
        shader = dic.get("shader") #dic["shader"]도 상관없음
        childs = dic.get("child", []) #dic["child"]도 상관없음

        item = ItemModel(name=name, shader=shader, parent=parent)
        parent.appendChild(item)

        for child in childs:
            self.make_item(dic=child, parent=item)

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
            if column == 0:
                return item.name
            elif column == 1:
                return item.shader

        elif role == QtCore.Qt.BackgroundRole:
            parent_index = index.parent()  # 인덱스의 부모를 가져옴
            parent_item = parent_index.internalPointer() if parent_index.isValid() else None  # 부모 아이템 가져옴
            if column == 0 and parent_item is None:  # 부모 아이템이 없는 경우에만 백그라운드 적용
                dark_blue = QtGui.QColor(22, 51, 84)
                dark_gray = QtGui.QColor(44, 44, 44)

                gradient = QtGui.QLinearGradient(QtCore.QPointF(0, 0), QtCore.QPointF(1, 0))
                gradient.setColorAt(0, dark_blue)
                gradient.setColorAt(0.65, dark_gray)
                gradient.setColorAt(1, dark_gray)
                gradient.setCoordinateMode(QtGui.QLinearGradient.ObjectMode)
                return QtGui.QBrush(gradient)

            return QtGui.QColor(QtCore.Qt.transparent)

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
