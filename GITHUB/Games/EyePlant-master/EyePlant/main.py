import sys

from PyQt5.QtWidgets import QApplication

from my import ui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ui.mainWindow()
    win.show()
    exit(app.exec_())
