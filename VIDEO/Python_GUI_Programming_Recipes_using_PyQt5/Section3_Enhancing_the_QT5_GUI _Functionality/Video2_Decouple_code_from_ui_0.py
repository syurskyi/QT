'''
Created on Sep 20, 2017

@author: Burkhard A. Meier
'''

from Video2_MainWindow import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    