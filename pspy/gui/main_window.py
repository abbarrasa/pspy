import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QAction
from PyQt5.QtCore import QSize    
from PyQt5.QtGui import QIcon


class UiMainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle("PSPy")
        self.statusBar().showMessage('Message in statusbar.', 5000)

        # Create exit action
        exitAction = QAction(QIcon.fromTheme('application-exit'), 'E&xit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')                
        exitAction.triggered.connect(self.exitCall)
        
        # Create find action
        findAction = QAction(QIcon.fromTheme('edit-find'), '&Find', self)
        findAction.setShortcut('Ctrl+F')
        findAction.setStatusTip('Find')        
        findAction.triggered.connect(self.findCall)        
        
        # Create about action
        aboutAction = QAction(QIcon.fromTheme('help-about'), 'About', self)        
        aboutAction.setStatusTip('About PSPy')
        aboutAction.triggered.connect(self.aboutCall)
        
        # Create menu bar and add action
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAction)
        editMenu = menuBar.addMenu('&Edit')
        editMenu.addAction(findAction)        
        helpMenu = menuBar.addMenu('&Help')
        helpMenu.addAction(aboutAction)
    
    def findCall(self):        
        print('Find')

    def aboutCall(self):
        about = QtWidgets.QDialog()
        ui = UiAbout()
        ui.setupUi(about)
        about.show()   
        print('About')

    def exitCall(self):
        print('Exit app')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = UiMainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
