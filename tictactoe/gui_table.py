from tictactoe import *
from win_wind import *


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.game = TicTacToe()
        self.wind = None

    def initUI(self):
        self.setWindowTitle('Tic Tac Toe')
        self.createGridLayout()
        TicTacToe.center(self)
        self.resize(400, 100)
        self.show()


    def createGridLayout(self):
        layout = QGridLayout()
        self.setLayout(layout)
        self.pos = [(i, j) for i in range(3) for j in range(3)]
        self.button_group = QButtonGroup()

        for ps, num in zip(self.pos, range(9)):
            b = QPushButton("")
            self.button_group.addButton(b, num)
            layout.addWidget(b, *ps)

        self.button_group.buttonClicked[int].connect(self.clicked)

    def clicked(self, index):
        btn = self.button_group.button(index)
        btn.setDisabled(True)
        field = self.pos[index]
        if self.game.current:
            self.game.board[field[0]][field[1]] = "x"
            btn.setText("x")
            self.check_win(self.game.check(self.game))
            self.game.current = False
        else:
            self.game.board[field[0]][field[1]] = "o"
            btn.setText("o")
            self.check_win(self.game.check(self.game))
            self.game.current = True

    def check_win(self, res):
        if res == 'x' or res == 'o':
            self.wind = WinnerWindow(res)
            self.wind.show()
            self.close()
