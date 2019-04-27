import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget
from PyQt5.QtGui import QIcon


class QTApp(QWidget):

    def __init__(self):
        super().__init__()
        self.btn = QPushButton("Exit", self)
        self.initUI()

    def initUI(self):
        self.btn.clicked.connect(QApplication.exit)
        self.btn.resize(100, 100)
        self.btn.move(250, 150)
        self.btn.setParent(self)

        self.setWindowIcon(QIcon("icon.ico"))
        self.setWindowTitle("QTApp")
        self.resize(600, 400)
        self.center()
        self.show()

    def center(self):
        geom = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        geom.moveCenter(cp)
        self.move(geom.topRight())


if __name__ == '__main__':

     qapp = QApplication(sys.argv)
     app = QTApp()
     sys.exit(qapp.exec_())