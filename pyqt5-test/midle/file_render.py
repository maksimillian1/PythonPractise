import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QDesktopWidget


class FileRender(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    file = FileRender()
    sys.exit(app.exec_())