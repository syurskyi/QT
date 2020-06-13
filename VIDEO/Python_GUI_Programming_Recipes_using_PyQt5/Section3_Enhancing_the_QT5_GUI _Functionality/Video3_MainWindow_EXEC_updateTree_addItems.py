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
        
        self.update_tree()
            
        MainWindow.show()
        sys.exit(app.exec_())        

    def update_tree(self):
#         self.print_tree() 
        self.ui.treeWidget.headerItem().setText(1, 'Header 2')
#         self.print_tree() 

        print(self.ui.treeWidget.topLevelItem(0).text(0))
        print(self.ui.treeWidget.topLevelItem(0).child(0).text(0))
              
        self.ui.treeWidget.topLevelItem(0).setText(1, "Item 2")
        print(self.ui.treeWidget.topLevelItem(0).text(1))
        
        self.ui.treeWidget.topLevelItem(0).addChild(QtWidgets.QTreeWidgetItem())
        self.ui.treeWidget.topLevelItem(0).child(0).setText(1, "Subitem 2")
        print(self.ui.treeWidget.topLevelItem(0).child(0).text(1))

    def print_tree(self):
        header0 = self.ui.treeWidget.headerItem().text(0)
        header1 = self.ui.treeWidget.headerItem().text(1)
        print(header0 + '\n' + header1 + '\n')        
        

    def update_calendar(self):
        pass
    
    def update_progressbar(self):
        pass

if __name__ == "__main__":
    MainWindow_EXEC()
