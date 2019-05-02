from tictactoe import *
import gui_table
from PyQt5.QtWidgets import QWidget, QLabel, QDesktopWidget, QGridLayout, QPushButton


class WinnerWindow(QWidget):

    def __init__(self, winner):
        super().__init__()
        self.initUI(winner)
        self.retry = None

    def initUI(self, winner):
        label = QLabel("Congratulation {}!".format(winner))
        button = QPushButton("Retry?", self)
        grid = QGridLayout()
        grid.addWidget(label, 0, 1)
        grid.addWidget(button, 1, 1)

        button.clicked.connect(self.clicked)
        TicTacToe.center(self)
        self.setLayout(grid)
        self.setWindowTitle('Winner')

    def clicked(self):
        self.retry = gui_table.App()
        self.close()