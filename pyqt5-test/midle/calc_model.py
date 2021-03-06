import sys, re
from PyQt5.QtWidgets import QPushButton, QGridLayout, \
    QDesktopWidget, QApplication, QWidget, QButtonGroup, QLabel, QErrorMessage


class Calc(QWidget):

    OPERATIONS = ['+', '-', '*', '/']

    def __init__(self):
        super().__init__()

        self.grid = QGridLayout()
        self.btn_group_nums = QButtonGroup()
        self.calc_field = QLabel()
        self.result_field = QLabel()
        self.initUI()

    def initUI(self):
        self.move_center()
        self.button_group()
        self.grid.addWidget(self.calc_field, 4, 0)
        self.grid.addWidget(self.result_field, 4, 2)

        self.setLayout(self.grid)
        self.setWindowTitle("Calculator")
        self.show()

    def bntclicked(self, id):
        btn = self.btn_group_nums.buttons()[id]
        if btn.text() == '=':
            try:
                res = Calc.calc(Calc.to_operand_list(self.calc_field.text()))
                self.result_field.setText(str(res))
                self.calc_field.setText('')
            except Exception as E:
                error_dialog = QErrorMessage()
                error_dialog.showMessage('Invalid input!')
                error_dialog.exec_()
                self.calc_field.setText('')
        else:
            if self.calc_field.text() == '':
                self.calc_field.setText(btn.text())
            else:
                self.calc_field.setText(self.calc_field.text() + btn.text())

    @staticmethod
    def to_operand_list(to_render):
        regex = r'\+|-|\/|\*'
        nums = re.split(regex, to_render)
        nums.remove('')

        for i in range(len(to_render)):
            if to_render[i] in Calc.OPERATIONS and to_render[i] != nums[i]:
                nums.insert(i, to_render[i])
        return nums

    @staticmethod
    def calc(lst):
        Calc.basic_validate(lst)
        res = float(lst[0])
        for i in range(len(lst[1:])):
            if lst[i] in Calc.OPERATIONS:
                if lst[i] == '+':
                    res += float(lst[i + 1])
                elif lst[i] == '-':
                    res -= float(lst[i + 1])
                elif lst[i] == '*':
                    res *= float(lst[i + 1])
                else:
                    res /= float(lst[i + 1])
        return res

    @staticmethod
    def basic_validate(lst):
        if lst[0] == '-' or '+':
            lst[1] = str(lst[0]+lst[1])
            lst.pop(0)

    def button_group(self):
        BTN_LST = ['7', '8', '9', '/',
                   '4', '5', '6', '*',
                   '1', '2', '3', '-',
                   '.', '0', '=', '+']
        pos = [(i, j) for i in range(4) for j in range(4)]

        for i in range(len(BTN_LST)):
            btn = QPushButton(BTN_LST[i], self)
            self.grid.addWidget(btn, *pos[i])
            self.btn_group_nums.addButton(btn, i)

        self.btn_group_nums.setExclusive(True)
        self.btn_group_nums.buttonClicked[int].connect(self.bntclicked)

    def move_center(self):
        geom = self.frameGeometry()
        cnt = QDesktopWidget().availableGeometry().center()
        geom.moveCenter(cnt)
        self.move(geom.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calc()
    sys.exit(app.exec_())