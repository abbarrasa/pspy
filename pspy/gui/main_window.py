from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from gui.about import Ui_AboutDialog
from gui.edit import Ui_EditDialog
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
        
        # Create new action
        newAction = QtWidgets.QAction(QtGui.QIcon.fromTheme('new'), '&New', MainWindow)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('New game')
        newAction.triggered.connect(
            lambda checked, window=MainWindow: self.newCall(window))

        # Create exit action
        exitAction = QtWidgets.QAction(QtGui.QIcon.fromTheme('application-exit'), 'E&xit', MainWindow)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitCall)

        # Create find action
        findAction = QtWidgets.QAction(QtGui.QIcon.fromTheme('edit-find'), '&Find', MainWindow)
        findAction.setShortcut('Ctrl+F')
        findAction.setStatusTip('Find')
        findAction.triggered.connect(self.findCall)

        # Create about action
        aboutAction = QtWidgets.QAction(QtGui.QIcon.fromTheme('help-about'), 'About', MainWindow)
        aboutAction.setStatusTip('About PSPy')
        aboutAction.triggered.connect(
            lambda checked, window=MainWindow: self.aboutCall(window))

        # Create menu bar and add action
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        fileMenu = self.menubar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(exitAction)
        editMenu = self.menubar.addMenu('&Edit')
        editMenu.addAction(findAction)
        helpMenu = self.menubar.addMenu('&Help')
        helpMenu.addAction(aboutAction)
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PSPy"))

    @pyqtSlot()
    def newCall(self, window):
        dialog = QtWidgets.QDialog(window)
        Ui_EditDialog().setupUi(dialog)
        dialog.show()
        print('New')
        
    @pyqtSlot()
    def findCall(self):
        print('Find')

    @pyqtSlot()
    def aboutCall(self, window):
        dialog = QtWidgets.QDialog(window)
        Ui_AboutDialog().setupUi(dialog)
        dialog.show()
        print('About')

    @pyqtSlot()
    def exitCall(self):
        import sys
        sys.exit(0)
        print('Exit app')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWin = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWin)
    mainWin.show()
    sys.exit(app.exec_())
