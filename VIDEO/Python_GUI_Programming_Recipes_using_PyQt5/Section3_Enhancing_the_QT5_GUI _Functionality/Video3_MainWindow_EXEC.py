'''
Created on Sep 21, 2017

@author: Burkhard A. Meier
'''

from PyQt5 import QtCore, QtGui, QtWidgets

from Video3_MainWindow_Complex_7_FINAL_UI import Ui_MainWindow


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())