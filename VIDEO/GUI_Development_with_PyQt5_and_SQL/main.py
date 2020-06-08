import sys

from PyQt5 import QtWidgets, QtCore
from ui.ui_mainmenu import MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())