'''
Created on Sep 29, 2017

@author: Burkhard A. Meier
'''

import sys
from time import sleep
from pprint import pprint
import sqlite3
from PyQt5 import QtSql
from PyQt5 import QtCore, QtWidgets
from Section4_Advanced_Qt5_Programming.Video1_OpenGL_Rotation import PyQtOpenGL
from Section4_Advanced_Qt5_Programming.Video2_Networking_TCPServer_TCPClient import TcpServer, TcpClient
from Section4_Advanced_Qt5_Programming.Video5_MainWindow_Complex_UI_slot import Ui_MainWindow
from PyQt5.QtGui import QColor


class MoveToolButton(QtWidgets.QToolButton):
    
    def __init__(self, parent):
        super().__init__(parent)  
        self.change_palette()
    
    def change_palette(self, back=QColor("#bd0000"), fore=QColor("#bd125c")):    
        palette = self.palette()
        palette.setColor(self.backgroundRole(), back)
        palette.setColor(self.foregroundRole(), fore)
        self.setPalette(palette)     
    
    def position_button(self, new_position):    
        self.move(new_position.x(), new_position.y())
        
    new_position = QtCore.pyqtProperty(QtCore.QPoint, fset=position_button)   # define a new property       


class MainWindow_EXEC():
            
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        
        def slot1():
            print('hi from slot1')
            self.ui.button_slot.setText('Slot1')
            
            
        self.MainWindow.slot1 = slot1
        
        self.ui.setupUi(self.MainWindow)   
        #-------------------------- 

        #-------------------------- 
        self.init_tabs()
        
        self.MainWindow.show()
        sys.exit(app.exec_()) 

    #----------------------------------------------------------
    
    
    
    
    #----------------------------------------------------------
    def stop_animation(self):
        try:
            self.animated_frame.stop()
            self.animated_lcd.stop()
            self.animated_toolbutton.stop()
        except: pass
        
    #----------------------------------------------------------
    def animate(self):
        self.animated_frame = QtCore.QPropertyAnimation(self.ui.frame, b'geometry')
        self.animated_frame.setDuration(10000)
        self.animated_frame.setStartValue(QtCore.QRect(10, 10, 100, 100))
        self.animated_frame.setEndValue(QtCore.QRect(10, 10, 200, 200))
        self.animated_frame.start()
        self.animated_frame.finished.connect(lambda: self.ui.frame.setFrameStyle(QtWidgets.QFrame.Box))
        
        self.animated_lcd = QtCore.QPropertyAnimation(self.ui.lcdNumber_animation, b'value')
        self.animated_lcd.setDuration(9000)
        self.animated_lcd.setStartValue(0)
        self.animated_lcd.setEndValue(999)
        self.animated_lcd.start()
        self.animated_lcd.finished.connect(lambda: self.ui.lcdNumber_animation.setFrameStyle(QtWidgets.QFrame.StyledPanel))
        
        self.move_toolbutton.change_palette()   # reset to default colors  
        self.animated_toolbutton = QtCore.QPropertyAnimation(self.move_toolbutton, b'new_position')
        self.animated_toolbutton.setDuration(9000)
        self.animated_toolbutton.setStartValue(QtCore.QPoint(330, 20))
        self.animated_toolbutton.setKeyValueAt(0.2, QtCore.QPoint(398, 50))
        self.animated_toolbutton.setKeyValueAt(0.5, QtCore.QPoint(152, 120))
        self.animated_toolbutton.setKeyValueAt(0.6, QtCore.QPoint(420, 240))
        self.animated_toolbutton.setKeyValueAt(0.7, QtCore.QPoint(420, 260))
        self.animated_toolbutton.setKeyValueAt(0.9, QtCore.QPoint(330, 330))
        self.animated_toolbutton.setKeyValueAt(0.99, QtCore.QPoint(330, 310))
        self.animated_toolbutton.setEndValue(QtCore.QPoint(490, 300))
        self.animated_toolbutton.start()

        self.animated_toolbutton.finished.connect(lambda: self.move_toolbutton.change_palette(QColor('#00aa00'), QColor('#00aa00')))

                              
    #----------------------------------------------------------
    def sql_delete_row(self):
        if self.model:
            self.model.removeRow(self.ui.tableView.currentIndex().row())
        else:
            self.sql_tableview_model()       
                
    #----------------------------------------------------------
    def sql_add_row(self):
        if self.model:
            self.model.insertRows(self.model.rowCount(), 1)
        else:
            self.sql_tableview_model()

    #----------------------------------------------------------
    def sql_tableview_model(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('PEOPLE.db')
        
        tableview = self.ui.tableView
        self.model = QtSql.QSqlTableModel()
        tableview.setModel(self.model)
        
        self.model.setTable('PERSON')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)   # All changes to the model will be applied immediately to the database
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Last name")


    #----------------------------------------------------------
    def print_data(self):
        sqlite_file = 'PEOPLE.db'
        conn = sqlite3.connect(sqlite_file)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM 'PERSON' ORDER BY ID")
        all_rows = cursor.fetchall()
        pprint(all_rows)
        
        conn.commit()       # not needed when only selecting data
        conn.close()        
        
    #----------------------------------------------------------
    def create_DB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('PEOPLE.db')
        db.open()
        
        query = QtSql.QSqlQuery()
          
        query.exec_("create table PERSON(ID int primary key, "
                    "FIRST_NAME varchar(20), LAST_NAME varchar(20))")
        query.exec_("insert into PERSON values(1000, 'Albert', 'Einstein')")
        query.exec_("insert into PERSON values(1001, 'Guido', 'van Rossum')")
        query.exec_("insert into PERSON values(1002, 'Steve', 'Jobs')")
        query.exec_("insert into PERSON values(1003, 'Bill', 'Gates')")

   
    #----------------------------------------------------------
    def connect_to_server_1(self):
        # create a client, passing in UI widget references
        self.tcp_client_1 = TcpClient(line_edit_widget=self.ui.lineEdit_client_1, text_widget=self.ui.textEdit_client_1)
        self.tcp_client_1.connect_server()              
        self.ui.button_client_1.setEnabled(False)
        
        # Signals and slots for networking
        self.tcp_client_1.socket.readyRead.connect(self.tcp_client_1.read_data)
        self.tcp_client_1.socket.disconnected.connect(self.server_disconnect_1)        
        self.tcp_client_1.socket.error.connect(self.server_error_1)

    def server_disconnect_1(self):
        self.tcp_client_1.socket.close()
        self.ui.button_client_1.setEnabled(True)
        
    def server_error_1(self):
        error = "Error: {}".format(self.tcp_client_1.socket.errorString())
        self.display_text_1(error)
        self.tcp_client_1.socket.close()
        self.ui.button_client_1.setEnabled(True)    

    def display_text_1(self, text):
        self.ui.textEdit_client_1.append(text) 

    def send_data_1(self):
        try: self.tcp_client_1.write_data()
        except: pass 
                
    #----------------------------------------------------------
    def connect_to_server_2(self):
        # create a client, passing in UI widget references
        self.tcp_client_2 = TcpClient(line_edit_widget=self.ui.lineEdit_client_2, text_widget=self.ui.textEdit_client_2)
        self.tcp_client_2.connect_server()              
        self.ui.button_client_2.setEnabled(False)
        
        # Signals and slots for networking
        self.tcp_client_2.socket.readyRead.connect(self.tcp_client_2.read_data)
        self.tcp_client_2.socket.disconnected.connect(self.server_disconnect_2)        
        self.tcp_client_2.socket.error.connect(self.server_error_2)

    def server_disconnect_2(self):
        self.tcp_client_2.socket.close()
        self.ui.button_client_2.setEnabled(True)
        
    def server_error_2(self):
        error = "Error: {}".format(self.tcp_client_2.socket.errorString())
        self.display_text_2(error)
        self.tcp_client_2.socket.close()
        self.ui.button_client_2.setEnabled(True)    

    def display_text_2(self, text):
        self.ui.textEdit_client_2.append(text) 

    def send_data_2(self):
        try: self.tcp_client_2.write_data() 
        except: pass  
               
    #----------------------------------------------------------
    def start_server(self):
        self.tcp_server = TcpServer()
                
    #----------------------------------------------------------
    def init_tabs(self):
        
        #--------------------------
        self.ui.button_stop_animation.clicked.connect(self.stop_animation)
        self.ui.button_start_animation.clicked.connect(self.animate)

        self.ui.toolButton.hide()
#         self.toolButton = QtWidgets.QToolButton(self.tab_animation)
#         self.move_toolbutton.setObjectName("toolButton")
        self.move_toolbutton = MoveToolButton(self.ui.tab_animation)
        self.move_toolbutton.setGeometry(QtCore.QRect(330, 20, 25, 19))
        self.move_toolbutton.setAutoFillBackground(True)
        self.move_toolbutton.setText("***")
        
        #--------------------------
#         self.create_DB()
        self.ui.button_SQL_view_data.clicked.connect(self.print_data)
        self.model = None
        self.ui.button_SQL_view_data.clicked.connect(self.sql_tableview_model)
        self.ui.button_SQL_add.clicked.connect(self.sql_add_row)
        self.ui.button_SQL_delete.clicked.connect(self.sql_delete_row)

        #--------------------------
        self.ui.button_start_server.clicked.connect(self.start_server)
        # Signals and slots for clients
        self.ui.button_client_1.clicked.connect(self.connect_to_server_1)   
        self.ui.lineEdit_client_1.returnPressed.connect(self.send_data_1)    
        self.ui.button_client_2.clicked.connect(self.connect_to_server_2)   
        self.ui.lineEdit_client_2.returnPressed.connect(self.send_data_2)             
        
        #--------------------------
        open_gl = PyQtOpenGL(parent=self.ui.frame_gl)   # create class instance, passing in the tab as parent
        open_gl.setMinimumSize(300, 300)                # keep proportions, set to same size as frame
        open_gl.paint_0 = False
        open_gl.paint_1 = False
        open_gl.paint_2 = False
        open_gl.resize_lines = False 
        open_gl.paint_rotation = False

        #-------------------------- 
        self.ui.comboBox.hide()
        self.drop_combo = DragDropCombo(self.MainWindow)
        self.drop_combo.setMinimumSize(QtCore.QSize(141, 0))
        self.ui.horizontalLayout_2.addWidget(self.drop_combo)
        
        #--------------------------
        self.ui.pushButton.hide()
#         self.ui.pushButton.setParent(None)  # deleting parent deletes the button        
        self.drop_button = DragDropButton('DropButton', self.MainWindow)
        self.drop_button.setMinimumSize(QtCore.QSize(161, 0))
        self.ui.horizontalLayout_2.addWidget(self.drop_button)

        #--------------------------
        self.update_tree()
        self.update_calendar()
        self.update_progressbar()
        
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
        
         
        
if __name__ == "__main__":
    MainWindow_EXEC()
