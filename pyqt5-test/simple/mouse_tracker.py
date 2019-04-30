import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QDesktopWidget, QGridLayout
from PyQt5.QtCore import Qt


class MouseTracker(QWidget):

    def __init__(self):
        super().__init__()
        self.grid = QGridLayout()
        self.indicator = QLabel()
        self.initUI()

    def initUI(self):
        x, y = 0, 0
        dot = "x:{0}, y:{1}".format(x, y)
        self.indicator.setText(self.dot)
        self.grid.addWidget(self.indicator, 0 ,0, Qt.AlignTop)

        self.setMouseTracking(True)
        self.setLayout(self.grid)
        self.center()
        self.resize(300, 200)
        self.show()

    def center(self):
        geom = self.frameGeometry()
        cnt = QDesktopWidget().availableGeometry().center()
        geom.moveCenter(cnt)
        self.move(geom.topLeft())

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        dot = "x:{}, y:{}".format(x, y)
        self.indicator.setText(dot)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mouse = MouseTracker()
    sys.exit(app.exec_())