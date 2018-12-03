from PyQt5 import QtCore, QtSql, QtWidgets
from util import Util


# class GameSqlModel(QtSql.QSqlTableModel):
class GameSqlModel(QtSql.QSqlRelationalTableModel):
    def __init__(self, parent=None):
#        QtSql.QSqlTableModel.__init__(self, parent=parent)
        QtSql.QSqlRelationalTableModel.__init__(self, parent=parent)
        self.setTable("Game")
        self.setRelation(4, QtSql.QSqlRelation("format", "id", "name"));
        #self.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.setEditStrategy(QtSql.QSqlTableModel.OnRowChange)
        self.select()

    def data(self, item, role):
        val = QtSql.QSqlTableModel.data(self, item, role)
        if role == QtCore.Qt.DisplayRole:
            if item.column() == 5:
                return Util.humanReadableSize(val)
        if role == QtCore.Qt.EditRole:
            if item.column() == 5:
                return Util.humanReadableSize(val)

        return val

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if index.column() == 4:
            if not value or value not in ['ISO', 'CSO', 'Eboot']:
                raise ValueError('{0} is not a valid format'.format(value))

        return QtSql.QSqlQueryModel.setData(self, index, value, role)

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
