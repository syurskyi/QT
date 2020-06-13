'''
Created on Sep 21, 2017

@author: Burkhard A. Meier
'''

import sys
from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from Video4_MainWindow_Complex_UI import Ui_MainWindow


class MainWindow_EXEC():
    
    def __init__(self):
        self.threadpool = QtCore.QThreadPool()
        
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
        self.ui.radioButton_start.clicked.connect(self.oh_no)
#         self.ui.radioButton_start.clicked.connect(self.start_progressbar)
        self.ui.radioButton_stop.clicked.connect(self.stop_progressbar)
        self.ui.radioButton_reset.clicked.connect(self.reset_progressbar)
        self.progress_value = 0
        self.stop_progress = False

    def test(self, progress_value):
        while progress_value < 10:
            print('hi')
            sleep(0.1)
            
                   
    def oh_no(self):
        # Pass the function to execute
#         worker = Worker(self.start_progressbar) # Any other args, kwargs are passed to the run function
# WORKS!        worker = Worker(self.test, self.progress_value) # Any other args, kwargs are passed to the run function
#         worker = Worker(self.start_progressbar_run, self.stop_progress, self.progress_value, self.ui.progressBar)

        worker = Worker(self.start_progressbar_run, self.stop_progress, self.ui.progressBar)

        
        # Execute
        self.threadpool.start(worker)
        
    
    def start_progressbar_run(self, stop_progress, progressBar):
#     def start_progressbar_run(self, stop_progress, progress_value, progressBar):
        print('inside run')
        print(progressBar)
        stop_progress = False
        progress_value = progressBar.value()
        print(progress_value)
        
        while progress_value <= 101 and not stop_progress:
            print(progress_value)
            progress_value += 1
            sleep(0.1)
  
#         while (progress_value <= 101) and not (stop_progress):
#             progressBar.setValue(progress_value)
#             progress_value += 1
#             sleep(0.1)
                    
        
    def start_progressbar(self):
        self.stop_progress = False
        self.progress_value = self.ui.progressBar.value()
 
        while (self.progress_value <= 101) and not (self.stop_progress):
            self.ui.progressBar.setValue(self.progress_value)
            self.progress_value += 1
            sleep(0.1)

#             QtWidgets.QApplication.processEvents()
   
        
    def stop_progressbar(self):
        self.stop_progress = True
    
    def reset_progressbar(self):
        self.progress_value = 0
        self.ui.progressBar.reset()
        self.stop_progress = False
        


class Worker(QtCore.QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and 
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        self.fn(*self.args, **self.kwargs)
        
        
if __name__ == "__main__":
    MainWindow_EXEC()
