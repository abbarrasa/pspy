from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtCore import QObject
from gui.about import Ui_AboutDialog
from gui.edit import Ui_EditDialog
from gui.menubar import Ui_MenuBar
from gui.game_sql_model import GameSqlModel
#from game import Game
from settings import Settings
import os
import resources


class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/icons/pspy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage('Message in statusbar.', 5000)
        MainWindow.setStatusBar(self.statusbar)

        # Create menu bar
        self.setupMenuBar(MainWindow)

        # Create central widget
        centralWidget = QtWidgets.QWidget(MainWindow)
        self.refreshTablePushButton = QtWidgets.QPushButton(centralWidget)
        self.refreshTablePushButton.setObjectName("refreshTablePushButton")
        gridLayout = QtWidgets.QGridLayout(centralWidget)
        gridLayout.setObjectName("gridLayout")
        gridLayout.addWidget(self.refreshTablePushButton, 0, 0, 1, 1)

        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        settings = Settings()
        db_filename = settings.read().get('General', 'db_file')
        path_to_db = os.path.expanduser(db_filename)
        db.setDatabaseName(path_to_db)

        self.model = GameSqlModel()
#        self.model.setTable("Game")
#        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
#        self.model.select()
        self.tableView = QtWidgets.QTableView(centralWidget)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSortingEnabled(True)
        self.tableView.hideColumn(0)
#        self.tableView.hideColumn(4)
        self.tableView.setModel(self.model)
        gridLayout.addWidget(self.tableView, 1, 0, 1, 2)
        MainWindow.setCentralWidget(centralWidget)


#        games = Game.select()
#        a = list(games)
#        print(a)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PSPy"))
        self.refreshTablePushButton.setText(_translate("MainWindow", "Refresh"))
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, _translate("MainWindow", "ID"))
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, _translate("MainWindow", "Title"))
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, _translate("MainWindow", "Description"))
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, _translate("MainWindow", "Comment"))
#        self.model.setHeaderData(4, QtCore.Qt.Horizontal, _translate("MainWindow", "Cover"))
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, _translate("MainWindow", "Format"))
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, _translate("MainWindow", "Size"))
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, _translate("MainWindow", "Path"))

    def setupMenuBar(self, MainWindow):
        menubar = QtWidgets.QMenuBar(MainWindow)
        ui = Ui_MenuBar()
        ui.setupUi(menubar)
        MainWindow.setMenuBar(menubar)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWin = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWin)
    mainWin.show()
    sys.exit(app.exec_())
