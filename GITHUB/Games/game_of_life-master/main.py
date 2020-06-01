import sys
from PyQt5.QtWidgets import (QApplication)
# import gui and cells class
import gui
import cells


if __name__ == '__main__':
    # set number of cells
    width = 32
    height = 32
    # init cells
    cells = cells.Cells(width, height)
    # init gui
    app = QApplication(sys.argv)
    game = gui.Game(width, height, cells)
    sys.exit(app.exec_())
