'''
Created on Sep 20, 2017

@author: Burkhard A. Meier
'''


from Video2_MainWindow import Ui_MainWindow

from PyQt5 import QtWidgets


def set_table_items(item1="item1", item2="item2", item3="item3"): 
    row = 0
    ui.tableWidget.setItem(row , 0, QtWidgets.QTableWidgetItem(item1))
    ui.tableWidget.setItem(1 , 1, QtWidgets.QTableWidgetItem(item2))
    ui.tableWidget.setItem(2 , 2, QtWidgets.QTableWidgetItem(item3))

def button_clicked():
#     ui.pushButton.setText('Button was clicked!')
    set_table_items(item2="item2-changed")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    # call function
    set_table_items()
    
    ui.pushButton.clicked.connect(button_clicked)
    # lambda works to call function directly w/out creating separate function
    ui.pushButton.clicked.connect(lambda: ui.pushButton.setText('Button was clicked!'))
    
    MainWindow.show()
    sys.exit(app.exec_())
    
    