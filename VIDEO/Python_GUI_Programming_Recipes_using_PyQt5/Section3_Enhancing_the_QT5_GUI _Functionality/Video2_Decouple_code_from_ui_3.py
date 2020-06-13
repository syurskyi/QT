'''
Created on Sep 20, 2017

@author: Burkhard A. Meier
'''

from Video2_MainWindow import Ui_MainWindow

from PyQt5 import QtWidgets


def set_table_items(): 
    row = 0
    ui.tableWidget.setItem(row , 0, QtWidgets.QTableWidgetItem("item1"))
    ui.tableWidget.setItem(1 , 1, QtWidgets.QTableWidgetItem("item2"))
    ui.tableWidget.setItem(2 , 2, QtWidgets.QTableWidgetItem("item3"))

def button_clicked():
    ui.pushButton.setText('Button was clicked!')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    # call function
    set_table_items()
    
    ui.pushButton.clicked.connect(button_clicked)
    
    MainWindow.show()
    sys.exit(app.exec_())
    
    