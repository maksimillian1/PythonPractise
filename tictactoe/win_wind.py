from PyQt5.QtWidgets import QWidget, QLabel


class WinnerWindow(QWidget):

    def __init__(self, winner):
        super().__init__()
        self.initUI(winner)

    def initUI(self, winner):
        lbl3 = QLabel("Congratulation {}!".format(winner))
        lbl3.setParent(self)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
