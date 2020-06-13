# Using the final GUI created in Video 1.3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtGui import QIcon


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()                           

    def initUI(self):
        self.setWindowTitle('PyQt5 GUI')
        self.resize(400,300)
        self.add_menus_and_status()

    def add_menus_and_status(self):
        self.statusBar().showMessage('Text in statusbar')

        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        new_icon = QIcon('icons/new_icon.png')
        new_action = QAction(new_icon, 'New', self)
        new_action.setStatusTip('New File')
        file_menu.addAction(new_action)

        file_menu.addSeparator()

        exit_icon = QIcon('icons/exit_icon.png')
        exit_action = QAction(exit_icon, 'Exit', self)
        exit_action.setStatusTip('Click to exit the application')
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut('Ctrl+Q')
        file_menu.addAction(exit_action)

        menubar.addMenu('Edit')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())
