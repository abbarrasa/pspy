from PyQt5 import QtCore, QtSql
from util import Util


class GameSqlModel(QtSql.QSqlTableModel):
    def __init__(self, parent=None):
        QtSql.QSqlTableModel.__init__(self, parent=parent)
        self.setTable("Game")
        self.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.select()

    def data(self, item, role):
        val = QtSql.QSqlTableModel.data(self, item, role)
        if role == QtCore.Qt.DisplayRole:
            if item.column() == 4:
                return ""
                #try:
                #    return '{:.4f}'.format(round(float(val), 4))
                #except ValueError:
                #    pass
            if item.column() == 6:
                return Util.humanReadableSize(val)
        if role == QtCore.Qt.EditRole:
            if item.column() == 4:
                return ""
                #try:
                #    return float(val)
                #except ValueError:
                #    pass
            if item.column() == 6:
                return Util.humanReadableSize(val)

        return val
