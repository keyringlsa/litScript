from PySide2 import QtCore
from pprint import pprint

class MakeItem(object):

    def __init__(self, data_dict):
        self.name = data_dict['name']
        self.configues = None
        if data_dict.get('configues'):
            self.configues = data_dict['configues']





    def show_info(self):

        #print(self.name)

        if self.configues:
            print(self.configues)




class lkdModel(QtCore.QAbstractItemModel):
    HORIZONTAL_HEADERS = ['name', 'configues']


    def __init__(self, row_datas=None, parent=None):
        QtCore.QAbstractItemModel.__init__(self, parent)

        self.entri_data = []
        self.filtered_indices = []  # 검색 결과를 담을 리스트

        for data_dict in row_datas:
            item = MakeItem(data_dict)
            self.entri_data.append(item)

        # 모델 내부에 데이터가 변경될 때마다 뷰를 업데이트할 수 있도록 시그널 설정
        #self.dataChanged.connect(self.update_view)

    def update_view(self, topLeft, bottomRight):
        # 모델 내부의 데이터가 변경되면 뷰를 업데이트
        self.layoutChanged.emit()




    def rowCount(self, parent):
        return len(self.filtered_indices) if self.filtered_indices else len(self.entri_data)
        #return len(self.entri_data)


    def columnCount(self, parent):
        return len(self.HORIZONTAL_HEADERS)

    def headerData(self, row, orientation, role): # 헤더 아이템을 생성해주는 곳

        if orientation == QtCore.Qt.Horizontal: #가로열

            if role == QtCore.Qt.DisplayRole:
                return self.HORIZONTAL_HEADERS[row] #가로열의 목록을 더 늘리고 싶을 때 'HORIZONTAL_HEADERS'확인

        if orientation == QtCore.Qt.Vertical: #세로열
            if role == QtCore.Qt.DisplayRole:

                return QtCore.QAbstractTableModel.headerData(self, row, orientation, role)

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def parent(self, index): #AbstractItemModel로 만들 시 해당 함수 꼭 포함
        if not index.isValid():
            return QtCore.QModelIndex()

        item = index.internalPointer()
        return QtCore.QModelIndex()

    def index(self, row, column, parent): #AbstractItemModel로 만들 시 해당 함수 꼭 포함
        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()

        if not parent.isValid():
            parentItem = self.entri_data[row]
            return self.createIndex(row, column, parentItem)

        return QtCore.QModelIndex()

    def data(self, index, role):

        if not self.filtered_indices:  # 필터링된 결과가 없으면 기존 로직 그대로 수행
            row = index.row()
            item = self.entri_data[row]
        else:  # 필터링된 결과가 있으면 해당 결과를 바탕으로 항목 가져오기
            row = self.filtered_indices[index.row()]
            item = self.entri_data[row]



        # row = index.row()
        # # column = index.column()
        # item = self.entri_data[row]

        if role == QtCore.Qt.DisplayRole:
            return item.name

        if role == QtCore.Qt.DecorationRole:
            return None

        if role == QtCore.Qt.TextAlignmentRole:
            return None

        if role == QtCore.Qt.BackgroundColorRole:
            return None

        if role == QtCore.Qt.UserRole:
            return item



