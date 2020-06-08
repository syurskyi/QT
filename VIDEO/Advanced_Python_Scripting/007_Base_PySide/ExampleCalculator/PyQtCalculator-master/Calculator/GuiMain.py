__author__ = 'joel'
from Calculator import Gui
from PySide import QtGui
import sys

app = QtGui.QApplication(sys.argv)  # app for qt
main_window = Gui.MainWindow()  # my mainWindow class
main_window.show()
app.exec_()