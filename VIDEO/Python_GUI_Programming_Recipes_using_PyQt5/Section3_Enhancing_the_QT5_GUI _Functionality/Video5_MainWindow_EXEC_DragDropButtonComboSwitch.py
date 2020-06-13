'''
Created on Sep 21, 2017

@author: Burkhard A. Meier
'''

import sys
from time import sleep

from PyQt5 import QtCore, QtWidgets
from Video5_MainWindow_Complex_UI import Ui_MainWindow


class DragDropButton(QtWidgets.QPushButton):
    
    def __init__(self, text, parent):
        super().__init__(text, parent)       
        self.setAcceptDrops(True)
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()
            
    def dropEvent(self, event):
        self.setText(event.mimeData().text())
    

class DragDropCombo(QtWidgets.QComboBox):    

    def __init__(self, parent):
        super().__init__(parent)        
        self.setAcceptDrops(True)
                            
    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()                            

    def dropEvent(self, event):
        self.addItem(event.mimeData().text())
        
                                     

class MainWindow_EXEC():
   
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)   
        #-------------------------- 
        
        self.ui.comboBox.hide()
        self.drop_combo = DragDropCombo(MainWindow)
        self.drop_combo.setMinimumSize(QtCore.QSize(141, 0))
        self.ui.horizontalLayout_2.addWidget(self.drop_combo)
        
        #--------------------------
        self.ui.pushButton.hide()
#         self.ui.pushButton.setParent(None)  # deleting parent deletes the button        
        self.drop_button = DragDropButton('DropButton', MainWindow)
        self.drop_button.setMinimumSize(QtCore.QSize(161, 0))
        self.ui.horizontalLayout_2.addWidget(self.drop_button)

        #--------------------------
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

    def progressbar_counter(self, start_value=0):
        self.run_thread = RunThread(parent=None, counter_start=start_value)
        self.run_thread.start()
        self.run_thread.counter_value.connect(self.set_progressbar)
                
    def set_progressbar(self, counter):
        if not self.stop_progress:
            self.ui.progressBar.setValue(counter)        
                   
    def start_progressbar(self):
        self.stop_progress = False
        self.progress_value = self.ui.progressBar.value()        
        self.progressbar_counter(self.progress_value)
           
    def stop_progressbar(self):
        self.stop_progress = True
        try: self.run_thread.stop()
        except: pass
           
    def reset_progressbar(self):
        self.stop_progressbar()
        self.progress_value = 0
        self.stop_progress = False
        self.ui.progressBar.reset()
        

class RunThread(QtCore.QThread):   
    counter_value = QtCore.pyqtSignal(int)            # define new Signal    
    def __init__(self, parent=None, counter_start=0):
        super(RunThread, self).__init__(parent)
        self.counter = counter_start
        self.is_running = True
        
    def run(self):
        while self.counter < 100 and self.is_running == True:
            sleep(0.1)
            self.counter += 1
            print(self.counter)
            self.counter_value.emit(self.counter)     # emit new Signal with value
            
    def stop(self):
        self.is_running = False
        print('stopping thread...')
        self.terminate()
        
        
if __name__ == "__main__":
    MainWindow_EXEC()
