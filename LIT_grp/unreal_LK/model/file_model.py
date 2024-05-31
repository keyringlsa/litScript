from PySide2 import QtCore

class MakeItem(object):

    def __init__(self, data_dict):
        self.name = data_dict['name']
        self.version = data_dict['version']
        self.path = data_dict['path']


    def show_info(self):

        print(self.name)
        print(self.path)



class fileModel(QtCore.QAbstractTableModel):
    HORIZONTAL_HEADERS = ['name', 'version'] #여기에 가로 정보값 추가(colum 관련)

    def __init__(self, row_data=None, parent=None): # row_data = 샷건에서 쿼리한 dict data
        QtCore.QAbstractTableModel.__init__(self, parent) #QtCore.QAbstractTableModel은 데이터 항목을 2차원 배열로 표현해주는 메서드, 해당 메서드를 실행시키면

        self.entri_data = []
        for data_dict in row_data:
            item = MakeItem(data_dict) # item 은 고유한 변수이름을 가진 클래스
            self.entri_data.append(item)


    def rowCount(self, parent):
        return len(self.entri_data)

    def columnCount(self, parent):
        return len(self.HORIZONTAL_HEADERS)

    def headerData(self, row, orientation, role): # 헤더 아이템을 생성해주는 곳

        if orientation == QtCore.Qt.Horizontal: #가로열

            if role == QtCore.Qt.DisplayRole:
                return self.HORIZONTAL_HEADERS[row] #가로열의 목록을 더 늘리고 싶을 때 'HORIZONTAL_HEADERS'확인

        if orientation == QtCore.Qt.Vertical: #세로열
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
                return item.version
          #str이므로 해당과 같이 코드를 수정해야 리스트가 아닌 str으로 받는다.


        if role == QtCore.Qt.TextAlignmentRole:
            if column == 0:
                return QtCore.Qt.AlignCenter
            elif column == 1:
                return QtCore.Qt.AlignCenter


        if role == QtCore.Qt.UserRole:
            return item



    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable


#
#
# ######################################################
# #
# from PySide2 import QtCore, QtGui
# from PySide2.QtWidgets import QComboBox, QStyledItemDelegate
#
# class MakeItem(object):
#     def __init__(self, data_dict):
#         self.name = data_dict['name']
#         self.versions = [data_dict['version']]  # Store versions in a list
#
# class fileModel(QtCore.QAbstractTableModel):
#     HORIZONTAL_HEADERS = ['name', 'version']
#
#     def __init__(self, row_data=None, parent=None):
#         QtCore.QAbstractTableModel.__init__(self, parent)
#         self.entri_data = []
#
#         for data_dict in row_data:
#             existing_item = next((item for item in self.entri_data if item.name == data_dict['name']), None)
#             if existing_item:
#                 existing_item.versions.append(data_dict['version'])
#             else:
#                 item = MakeItem(data_dict)
#                 self.entri_data.append(item)
#
#     def rowCount(self, parent):
#         return len(self.entri_data)
#
#     def columnCount(self, parent):
#         return len(self.HORIZONTAL_HEADERS)
#
#     def headerData(self, section, orientation, role):
#         if orientation == QtCore.Qt.Horizontal:
#             if role == QtCore.Qt.DisplayRole:
#                 return self.HORIZONTAL_HEADERS[section]
#
#         if orientation == QtCore.Qt.Vertical:
#             if role == QtCore.Qt.DisplayRole:
#                 return section + 1  # Return row numbers for vertical headers
#
#
#     def data(self, index, role):
#         row = index.row()
#         column = index.column()
#         item = self.entri_data[row]
#
#         if role == QtCore.Qt.DisplayRole:
#             if column == 0:
#                 return item.name
#             elif column == 1:
#                 return ', '.join(item.versions) if item.versions else ""
#
#         if role == QtCore.Qt.UserRole:  # For combo box data
#             if column == 1 and item.versions:
#                 return item.versions
#
#         return None
#
#     def flags(self, index):
#         return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
#
#
#
#
#
#
# class ComboBoxDelegate(QStyledItemDelegate):
#     def createEditor(self, parent, option, index):
#         combo_box = QComboBox(parent)
#         combo_box.addItems(index.data(QtCore.Qt.UserRole))
#         return combo_box
#
#     def setEditorData(self, editor, index):
#         value = index.data(QtCore.Qt.DisplayRole)
#         editor.setCurrentText(value)
#
#     def setModelData(self, editor, model, index):
#         value = editor.currentText()
#         model.setData(index, value, QtCore.Qt.EditRole)
#
