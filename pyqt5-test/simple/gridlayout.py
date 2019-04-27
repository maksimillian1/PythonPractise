import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QDesktopWidget


class GridLayout(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        layout = QGridLayout()
        self.setLayout(layout)

        ints = (1,2,3,4,5,6,7,8,9)

        pos = [(i, j) for i in range(3) for j in range(3)]

        for ps, number in zip(pos, ints):
            btn = QPushButton(str(number))
            layout.addWidget(btn, *ps)

        self.setWindowTitle("Digits")
        self.center()
        self.show()

    def center(self):
        geom = self.frameGeometry()
        cnt = QDesktopWidget().availableGeometry().center()
        geom.moveCenter(cnt)
        self.move(geom.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    grid = GridLayout()
    sys.exit(app.exec())
