import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QAction
from PyQt5.QtCore import QSize    
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle("PSPy")
        self.statusBar().showMessage('Message in statusbar.', 5000)

        # Create exit action
        exitAction = QAction(QIcon('application-exit'), 'E&xit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitCall)
        
        # Create exit action
        aboutAction = QAction(QIcon('help-about'), '&About', self)        
        aboutAction.setStatusTip('About PSPy')
        aboutAction.triggered.connect(self.aboutCall)
        
        # Create menu bar and add action
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu = menuBar.addMenu('&Help')
        fileMenu.addAction(exitAction)        

    def aboutCall(self):
        print('About')

    def exitCall(self):
        print('Exit app')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
