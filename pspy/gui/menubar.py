from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot


class Ui_MenuBar(QtWidgets.QMenuBar):
    def __init__(self, parent=None):
        QtWidgets.QMenuBar.__init__(self, parent=parent)
        self.setObjectName("menubar")
        self.setupUi()
        
    def setupUi(self):
        _translate = QtCore.QCoreApplication.translate
        
        # Create new action
        newAction = QtWidgets.QAction(QtGui.QIcon.fromTheme('document-new'), _translate('MenuBar', '&New'))
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip(_translate('MenuBar', 'New game'))
        newAction.triggered.connect(self.newCall)

        # Create exit action
        exitAction = QtWidgets.QAction(QtGui.QIcon.fromTheme('application-exit'), _translate('MenuBar', 'E&xit'))
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip(_translate('MenuBar', 'Exit application'))
        exitAction.triggered.connect(self.exitCall)

        # Create find action
        findAction = QtWidgets.QAction(QtGui.QIcon.fromTheme('edit-find'), _translate('MenuBar', '&Find'))
        findAction.setShortcut('Ctrl+F')
        findAction.setStatusTip(_translate('MenuBar', 'Find'))
        findAction.triggered.connect(self.findCall)

        # Create about action
        aboutAction = QtWidgets.QAction(QtGui.QIcon.fromTheme('help-about'), _translate('MenuBar', 'About'))
        aboutAction.setStatusTip(_translate('MenuBar', 'About PSPy'))
        aboutAction.triggered.connect(self.aboutCall)

        # Create menu bar and add action
        fileMenu = self.menubar.addMenu(_translate('MenuBar', '&File'))
        fileMenu.addAction(newAction)
        fileMenu.addAction(exitAction)
        editMenu = self.menubar.addMenu(_translate('MenuBar', '&Edit'))
        editMenu.addAction(findAction)
        helpMenu = self.menubar.addMenu(_translate('MenuBar', '&Help'))
        helpMenu.addAction(aboutAction)
            
    @pyqtSlot()
    def newCall(self):
        dialog = QtWidgets.QDialog(self.parent)
        Ui_EditDialog().setupUi(dialog)
        dialog.show()
        print('New')

    @pyqtSlot()
    def findCall(self):
        print('Find')

    @pyqtSlot()
    def aboutCall(self):
        dialog = QtWidgets.QDialog(self.parent)
        Ui_AboutDialog().setupUi(dialog)
        dialog.show()
        print('About')

    @pyqtSlot()
    def exitCall(self):
        QtWidgets.QApplication.exit()
        print('Exit app')
