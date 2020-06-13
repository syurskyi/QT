'''
Created on Aug 25, 2017

@author: Burkhard A. Meier
'''



#====================================================
# LAYOUT USING HORIZONTAL AND VERTICAL BOXES
#====================================================  
# #--------------------------------------------------
#
# add labels and buttons to layouts
# can't directly assign to QMainWindow
# have to create a QWidget, assign layout to it and 
# make it the central widget of the QMainWindow
 
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QWidget 
# from PyQt5.Qt import QLabel, QPushButton, QHBoxLayout, QVBoxLayout
# from PyQt5.QtGui import QIcon
#     
# class GUI(QMainWindow):             
#     def __init__(self): 
#         super().__init__()          
#         self.initUI()                           
#     
#     def initUI(self):                              
#         self.setWindowTitle('PyQt5 GUI')    
#         self.resize(400,300)                  
#         self.add_menus_and_status()
#       
#         self.horizontal_vertical_box_layout()
#           
#       
#     def horizontal_vertical_box_layout(self):
#         label_1 = QLabel('First label')
#         label_2 = QLabel('Another label')
#           
#         button_1 = QPushButton('Click 1')
#         button_2 = QPushButton('Click 2')
#           
#         hbox_1 = QHBoxLayout()
#         hbox_2 = QHBoxLayout()
#           
#         hbox_1.addWidget(label_1)
#         hbox_1.addWidget(button_1)
#   
#         hbox_2.addWidget(label_2)
#         hbox_2.addWidget(button_2)
#                   
#         vbox = QVBoxLayout()
#         vbox.addLayout(hbox_1)
#         vbox.addLayout(hbox_2)
#           
#         layout_widget = QWidget()       # create QWidget object
#         layout_widget.setLayout(vbox)   # set layout
#           
#         self.setCentralWidget(layout_widget)    # make QWidget the central widget
#           
#           
#                      
#     def add_menus_and_status(self):        
#         self.statusBar().showMessage('Text in statusbar')
#            
#         menubar = self.menuBar()                
#         file_menu = menubar.addMenu('File')          
#         new_icon = QIcon('icons/new_icon.png')          
#         new_action = QAction(new_icon, 'New', self)      
#         new_action.setStatusTip('New File')                 
#         file_menu.addAction(new_action)                 
#            
#         file_menu.addSeparator()               
#            
#         exit_icon = QIcon('icons/exit_icon.png')          
#         exit_action = QAction(exit_icon, 'Exit', self)    
#         exit_action.setStatusTip('Click to exit the application')
#         exit_action.triggered.connect(self.close)       
#         exit_action.setShortcut('Ctrl+Q')                     
#         file_menu.addAction(exit_action)
#            
#         menubar.addMenu('Edit')     
#    
# if __name__ == '__main__':     
#     app = QApplication(sys.argv)            
#     gui = GUI()                         
#     gui.show()                          
#     sys.exit(app.exec_())  
      

# # #--------------------------------------------------
# #
# # stretch the layout - hbox_1
 
 
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QWidget 
# from PyQt5.Qt import QLabel, QPushButton, QHBoxLayout, QVBoxLayout
# from PyQt5.QtGui import QIcon
#    
# class GUI(QMainWindow):             
#     def __init__(self): 
#         super().__init__()          
#         self.initUI()                           
#    
#     def initUI(self):                              
#         self.setWindowTitle('PyQt5 GUI')    
#         self.resize(400,300)                   
#         self.add_menus_and_status()
#      
#         self.horizontal_vertical_box_layout()
#          
#      
#     def horizontal_vertical_box_layout(self):
#         label_1 = QLabel('First label')
#         label_2 = QLabel('Another label')
#          
#         button_1 = QPushButton('Click 1')
#         button_2 = QPushButton('Click 2')
#          
#         hbox_1 = QHBoxLayout()
#         hbox_1.addStretch()                # push/stretch to right
#         hbox_2 = QHBoxLayout()
#          
#         hbox_1.addWidget(label_1)
#         hbox_1.addWidget(button_1)
#  
#         hbox_2.addWidget(label_2)
#         hbox_2.addWidget(button_2)
#                  
#         vbox = QVBoxLayout()
#         vbox.addLayout(hbox_1)
#         vbox.addLayout(hbox_2)
#          
#         layout_widget = QWidget()       # create QWidget object
#         layout_widget.setLayout(vbox)   # set layout
#          
#         self.setCentralWidget(layout_widget)    # make QWidget the central widget
#          
#          
#                     
#     def add_menus_and_status(self):        
#         self.statusBar().showMessage('Text in statusbar')
#           
#         menubar = self.menuBar()                
#         file_menu = menubar.addMenu('File')          
#         new_icon = QIcon('icons/new_icon.png')          
#         new_action = QAction(new_icon, 'New', self)      
#         new_action.setStatusTip('New File')                 
#         file_menu.addAction(new_action)                 
#           
#         file_menu.addSeparator()               
#           
#         exit_icon = QIcon('icons/exit_icon.png')          
#         exit_action = QAction(exit_icon, 'Exit', self)    
#         exit_action.setStatusTip('Click to exit the application')
#         exit_action.triggered.connect(self.close)       
#         exit_action.setShortcut('Ctrl+Q')                     
#         file_menu.addAction(exit_action)
#           
#         menubar.addMenu('Edit')     
#   
# if __name__ == '__main__':     
#     app = QApplication(sys.argv)            
#     gui = GUI()                         
#     gui.show()                          
#     sys.exit(app.exec_())  

# 
# # #--------------------------------------------------
# #
# # stretch the layout - hbox_1, hbox_2 and vbox
 
 
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QWidget 
from PyQt5.Qt import QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
    
class GUI(QMainWindow):             
    def __init__(self): 
        super().__init__()          
        self.initUI()                           
    
    def initUI(self):                              
        self.setWindowTitle('PyQt5 GUI')    
        self.resize(400,300)                   
        self.add_menus_and_status()
      
        self.horizontal_vertical_box_layout()
          
      
    def horizontal_vertical_box_layout(self):
        label_1 = QLabel('First label')
        label_2 = QLabel('Another label')
          
        button_1 = QPushButton('Click 1')
        button_2 = QPushButton('Click 2')
          
        hbox_1 = QHBoxLayout()
        hbox_1.addStretch()         # push/stretch to right
        hbox_2 = QHBoxLayout()
        hbox_2.addStretch()         # push/stretch to right
          
        hbox_1.addWidget(label_1)
        hbox_1.addWidget(button_1)
  
        hbox_2.addWidget(label_2)
        hbox_2.addWidget(button_2)
                  
        vbox = QVBoxLayout()
        vbox.addStretch()           # push/stretch down
          
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)
          
        layout_widget = QWidget()       # create QWidget object
        layout_widget.setLayout(vbox)   # set layout
          
        self.setCentralWidget(layout_widget)    # make QWidget the central widget
          
          
                     
    def add_menus_and_status(self):        
        self.statusBar().showMessage('Text in statusbar')
           
        menubar = self.menuBar()                
        file_menu = menubar.addMenu('File')          
        new_icon = QIcon('icons/new_icon.png')          
        new_action = QAction(new_icon, 'New', self)      
        new_action.setStatusTip('New File')                 
        file_menu.addAction(new_action)                 
           
        file_menu.addSeparator()               
           
        exit_icon = QIcon('icons/exit_icon.png')          
        exit_action = QAction(exit_icon, 'Exit', self)    
        exit_action.setStatusTip('Click to exit the application')
        exit_action.triggered.connect(self.close)       
        exit_action.setShortcut('Ctrl+Q')                     
        file_menu.addAction(exit_action)
           
        menubar.addMenu('Edit')     
   
if __name__ == '__main__':     
    app = QApplication(sys.argv)            
    gui = GUI()                         
    gui.show()                          
    sys.exit(app.exec_())  


