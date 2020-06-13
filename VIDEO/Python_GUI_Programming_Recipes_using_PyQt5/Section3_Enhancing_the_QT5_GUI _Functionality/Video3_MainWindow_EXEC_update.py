'''
Created on Sep 21, 2017

@author: Burkhard A. Meier
'''

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Video3_MainWindow_Complex_7_FINAL_UI import Ui_MainWindow

class MainWindow_EXEC():
    
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)        
        MainWindow.show()
        
        sys.exit(app.exec_())        

    def update_tree(self):
        pass
    
    def update_calendar(self):
        pass
    
    def update_progressbar(self):
        pass

if __name__ == "__main__":
    MainWindow_EXEC()
