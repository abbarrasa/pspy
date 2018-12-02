from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from gui.about import Ui_AboutDialog
from gui.edit import Ui_EditDialog



class Ui_MenuBar(QObject):
    def setupUi(self, MenuBar):
        MenuBar.setObjectName("menubar")
        _translate = QtCore.QCoreApplication.translate
        # Create new action
        newAction = QtWidgets.QAction(QtGui.QIcon.fromTheme('document-new'), _translate('MenuBar', '&New'), MenuBar)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip(_translate('MenuBar', 'New game'))
        newAction.triggered.connect(
            lambda checked, menubar=MenuBar: self.newCall(menubar))

        # Create exit action
        exitAction = QtWidgets.QAction(QtGui.QIcon.fromTheme('application-exit'), _translate('MenuBar', 'E&xit'), MenuBar)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip(_translate('MenuBar', 'Exit application'))
        exitAction.triggered.connect(self.exitCall)

        # Create find action
        findAction = QtWidgets.QAction(QtGui.QIcon.fromTheme('edit-find'), _translate('MenuBar', '&Find'), MenuBar)
        findAction.setShortcut('Ctrl+F')
        findAction.setStatusTip(_translate('MenuBar', 'Find'))
        findAction.triggered.connect(self.findCall)

        # Create about action
        aboutAction = QtWidgets.QAction(QtGui.QIcon.fromTheme('help-about'), 'About', MenuBar)
        aboutAction.setStatusTip(_translate('MenuBar', 'About PSPy'))
        aboutAction.triggered.connect(
            lambda checked, menubar=MenuBar: self.aboutCall(menubar))

        # Create menu bar and add action
        fileMenu = MenuBar.addMenu(_translate('MenuBar', '&File'))
        fileMenu.addAction(newAction)
        fileMenu.addAction(exitAction)
        editMenu = MenuBar.addMenu(_translate('MenuBar', '&Edit'))
        editMenu.addAction(findAction)
        helpMenu = MenuBar.addMenu(_translate('MenuBar', '&Help'))
        helpMenu.addAction(aboutAction)

    @pyqtSlot()
    def newCall(self, menubar):
        dialog = QtWidgets.QDialog(menubar)
        Ui_EditDialog().setupUi(dialog)
        dialog.show()
        print('New')

    @pyqtSlot()
    def findCall(self):
        print('Find')

    @pyqtSlot()
    def aboutCall(self, menubar):
        dialog = QtWidgets.QDialog(menubar)
        Ui_AboutDialog().setupUi(dialog)
        dialog.show()
        print('About')

    @pyqtSlot()
    def exitCall(self):
        QtWidgets.QApplication.exit()
        print('Exit app')
