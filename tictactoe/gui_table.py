import sys
from PyQt5.QtWidgets import *
from tictactoe import TicTacToe


class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'Tic Tac Toe'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()
        self.game = TicTacToe()
        self.win_wind = QWidget()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createGridLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()

        self.lst = [QPushButton() for _ in range(9)]
        self.dict = {}

        index = 0
        for i in range(3):
            for j in range(3):
                layout.addWidget(self.lst[index], i, j)
                self.dict[index] = [i,j]
                index += 1

        self.lst[0].clicked.connect(lambda: self.buttonClicked(0))
        self.lst[1].clicked.connect(lambda: self.buttonClicked(1))
        self.lst[2].clicked.connect(lambda: self.buttonClicked(2))
        self.lst[3].clicked.connect(lambda: self.buttonClicked(3))
        self.lst[4].clicked.connect(lambda: self.buttonClicked(4))
        self.lst[5].clicked.connect(lambda: self.buttonClicked(5))
        self.lst[6].clicked.connect(lambda: self.buttonClicked(6))
        self.lst[7].clicked.connect(lambda: self.buttonClicked(7))
        self.lst[8].clicked.connect(lambda: self.buttonClicked(8))

        self.horizontalGroupBox.setLayout(layout)


    def buttonClicked(self,index):
        self.lst[index].setDisabled(True)
        field = self.dict[index]
        wind = None
        if self.game.current:
            self.game.board[field[0]][field[1]] = "x"
            self.lst[index].setText("x")
            self.game.current = False
        else:
            self.game.board[field[0]][field[1]] = "o"
            self.lst[index].setText("o")
            self.game.current = True
        if self.game.check(self.game) == 'x':
            wind = WinnerWindow("x")
            sys.exit(app.exec_())
        elif self.game.check(self.game) == 'o':
            wind = WinnerWindow("o")
            sys.exit(app.exec_())


class WinnerWindow(QWidget):

    def __init__(self, winner):
        super().__init__()
        self.initUI()
        self.winner = winner

    def initUI(self):
        lbl3 = QLabel("Congratulation {}!".format(self.winner), self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())