'''
Created on Sep 21, 2017

@author: Burkhard A. Meier
'''

import sys
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from Video4_MainWindow_Complex_UI import Ui_MainWindow

class MainWindow_EXEC():
    
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)    
        
        self.update_tree()
        self.update_calendar()
        self.update_progressbar()
            
        MainWindow.show()
        sys.exit(app.exec_())        

    #----------------------------------------------------------
    def update_tree(self): 
        self.ui.treeWidget.headerItem().setText(1, 'Header 2')
        self.ui.treeWidget.topLevelItem(0).setText(1, "Item 2")
        self.ui.treeWidget.topLevelItem(0).addChild(QtWidgets.QTreeWidgetItem())
        self.ui.treeWidget.topLevelItem(0).child(0).setText(1, "Subitem 2")
        
    def print_tree(self):
        header0 = self.ui.treeWidget.headerItem().text(0)
        header1 = self.ui.treeWidget.headerItem().text(1)
        print(header0 + '\n' + header1 + '\n')        
        
    #----------------------------------------------------------
    def update_calendar(self):
        self.ui.calendarWidget.selectionChanged.connect(self.update_date)

    def update_date(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())      
    
    #----------------------------------------------------------
    def update_progressbar(self):
        self.ui.radioButton_start.clicked.connect(self.start_progressbar)
        self.ui.radioButton_stop.clicked.connect(self.stop_progressbar)
        self.ui.radioButton_reset.clicked.connect(self.reset_progressbar)
        self.progress_value = 0
        self.stop_progress = False

    def start_progressbar(self):
        self.stop_progress = False
        self.progress_value = self.ui.progressBar.value()
        
        while (self.progress_value <= 101) and not (self.stop_progress):
            self.ui.progressBar.setValue(self.progress_value)
#             self.progress_value += 0.0001
            self.progress_value += 1
            sleep(0.1)
            QtWidgets.QApplication.processEvents()
        
    def stop_progressbar(self):
        self.stop_progress = True
    
    def reset_progressbar(self):
        self.progress_value = 0
        self.ui.progressBar.reset()
        self.stop_progress = False
        
    
if __name__ == "__main__":
    MainWindow_EXEC()
