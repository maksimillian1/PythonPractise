import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setMenu()
        self.statusBar()

        self.setWindowTitle("Main")
        self.resize(400, 300)
        self.setGeometry(300,300,250,150)
        self.show()

    def setMenu(self):
        menu = self.menuBar()
        fileMenu = menu.addMenu('File')
        fileMenu.addAction(self.exitAction())
        emptyMenu = menu.addMenu('Empty')

    def exitAction(self):
        exitAct = QAction(QIcon('icon.ico'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit Application')
        exitAct.triggered.connect(qApp.quit)
        return exitAct

if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    app = MainWindow()
    sys.exit(qapp.exec_())


