import os, sys
import gui_table
from PyQt5.QtWidgets import *


class TicTacToe:
	
	def __init__(self):
		self.board = [['_']*3 for i in range(3)]
		self.current = True
		self.wins = TicTacToe.winlist()

	def __repr__(self):
		res = "\n"
		for i in self.board:
			res += "|{} {} {}|\n".format(i[0], i[1], i[2])
		return res

	@staticmethod
	def proptolist(string):
		indx = string.index('=') + 1
		return [num for num in string[indx:-1].split(',')]

	@staticmethod
	def center(self):
		geom = self.frameGeometry()
		cnt = QDesktopWidget().availableGeometry().center()
		geom.moveCenter(cnt)
		self.move(geom.topLeft())

	@staticmethod
	def winlist():
		my_path = os.path.abspath(os.path.dirname(__file__))
		path = os.path.join(my_path, "templates/wins.properties")
		with open(path, 'r') as fl:
			return [TicTacToe.proptolist(x) for x in fl]

	@staticmethod
	def check(self):
		matr = self.winlist()
		test = []
		for lst in matr:
			for item in lst:
				test.append(self.board[int(item[0])][int(item[1])])
			if test.count('x') == 3:
				return 'x'
			elif test.count('o') == 3:
				return 'o'
			test = []
		return None


if __name__ == '__main__':
	app = QApplication(sys.argv)
	game = gui_table.App()
	sys.exit(app.exec_())