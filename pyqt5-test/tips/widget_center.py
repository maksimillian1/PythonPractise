def center(self):
	geom = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        geom.moveCenter(cp)
        self.move(geom.topRight())
