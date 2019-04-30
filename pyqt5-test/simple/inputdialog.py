import sys
from PyQt5.QtWidgets import QPushButton, QLabel, QApplication, QWidget, QDesktopWidget, QHBoxLayout, QVBoxLayout
from simple.gridlayout import GridLayout


class Dialog(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dial = None


    def initUI(self):
        butt = QPushButton("Kek" , self)
        butt.setGeometry(100, 100, 50, 50)
        butt.clicked.connect(self.button_clicked)
        butt.setParent(self)

        self.center()
        self.resize(500,350)
        self.show()

    def button_clicked(self):
        self.dial = GridLayout()
        self.dial.show()
        self.close()
        

    def center(self):
        geom  = self.frameGeometry()
        cnt = QDesktopWidget().availableGeometry().center()
        geom.moveCenter(cnt)
        self.move(geom.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dial = Dialog()
    sys.exit(app.exec_())



