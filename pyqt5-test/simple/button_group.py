import sys
from PyQt5.QtWidgets import QWidget, QButtonGroup, QPushButton, QApplication, QDesktopWidget, QGridLayout
from random import randint

class ButtonGroup(QWidget):

    def __init__(self):
        super().__init__()

        self.grid = QGridLayout()
        self.btn_group = QButtonGroup()
        self.initUI()


    def initUI(self):
        pos = [(x, y) for x in range(3) for y in range(3)]
        btn_list  = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for pos, num in zip(pos, btn_list):
            btn = QPushButton(num)
            self.grid.addWidget(btn, *pos)
            self.btn_group.addButton(btn, int(num))

        self.btn_group.buttonClicked[int].connect(self.button_group_clicked)
        self.setLayout(self.grid)
        self.setWindowTitle("Button Group")
        self.resize(400,250)
        self.center()
        self.show()

    def button_group_clicked(self, id):
        btn = self.btn_group.button(id)
        btn.setText(str(randint(1, 100)))

    def center(self):
        geom = self.frameGeometry()
        cnt = QDesktopWidget().availableGeometry().center()
        geom.moveCenter(cnt)
        self.move(geom.topLeft())


if __name__ == "__main__":
    app =  QApplication(sys.argv)
    btn = ButtonGroup()
    sys.exit(app.exec__())