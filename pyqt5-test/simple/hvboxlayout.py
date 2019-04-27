import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class HVBox(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        label1 = QLabel("First", self)
        label2 = QLabel("Second", self)

        hlayout = QHBoxLayout()
        hlayout.addStretch(1)
        hlayout.addWidget(label1)
        hlayout.addWidget(label2)

        vlayout = QVBoxLayout()
        vlayout.addStretch(1)
        vlayout.addLayout(hlayout)

        self.setLayout(vlayout)
        self.setGeometry(300, 300, 250, 150)
        self.center()
        self.show()

    def center(self):
        geom = self.frameGeometry()
        cnt = QDesktopWidget().availableGeometry().center()
        geom.moveCenter(cnt)
        self.move(geom.topLeft())


if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    app = HVBox()
    sys.exit(qapp.exec_())