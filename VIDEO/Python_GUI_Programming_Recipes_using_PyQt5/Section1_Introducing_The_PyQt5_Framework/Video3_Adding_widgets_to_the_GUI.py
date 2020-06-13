'''
Created on Aug 25, 2017

@author: Burkhard A. Meier
'''


# #--------------------------------------------------


# # Structure of PyQt5 GUIs
#  
# # Imports
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget     
#   
# # Create Application  
# app = QApplication(sys.argv)
#  
# # Create Window
# win = QWidget()
#    
# # Add widgets and change properties 
# win.setWindowTitle('PyQt5 GUI')
#   
# # show the constructed PyQt window
# win.show()
#   
# # execute the application
# sys.exit(app.exec_())

# #--------------------------------------------------

# # code reorganized using a class
#  
# # Imports
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget 
#  
#  
# class GUI():
#     def __init__(self): 
#                     
#         self.initUI()
#  
#          
#     def initUI(self):   
#         self.win = QWidget()                    # create Window
#         self.win.setWindowTitle('PyQt5 GUI')    # add widgets and change properties
#  
#  
# if __name__ == '__main__':     
#     app = QApplication(sys.argv)        # create Application     
#     gui = GUI()                         # create instance of class
#     gui.win.show()                      # show the constructed PyQt window
#     sys.exit(app.exec_())               # execute the application

#--------------------------------------------------

# # class inheriting from QWidget
#  
#  
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget 
#   
#   
# class GUI(QWidget):                 # inherit from QWidget
#     def __init__(self): 
#         super().__init__()          # initialize super class, which creates the Window
#           
#         self.initUI()               # refer to Window as self
#   
#           
#     def initUI(self):   
#         self.setWindowTitle('PyQt5 GUI')    # add widgets and change properties
#   
#   
# if __name__ == '__main__':     
#     app = QApplication(sys.argv)        # create Application     
#     gui = GUI()                         # create instance of class
#     gui.show()                          # show the constructed PyQt window
#     sys.exit(app.exec_())               # execute the application
    

# #--------------------------------------------------

# # class inheriting from QMainWindow
#  
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow 
#   
#   
# class GUI(QMainWindow):             # inherit from QMainWindow
#     def __init__(self): 
#         super().__init__()          # initialize super class, which creates the Window
#           
#         self.initUI()               # refer to Window as self
#   
#           
#     def initUI(self):   
#         self.setWindowTitle('PyQt5 GUI')    # add widgets and change properties
#   
#   
# if __name__ == '__main__':     
#     app = QApplication(sys.argv)        # create Application     
#     gui = GUI()                         # create instance of class
#     gui.show()                          # show the constructed PyQt window
#     sys.exit(app.exec_())               # execute the application

# #--------------------------------------------------
 
# class inheriting from QMainWindow
# resize window
 
 
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow 
#   
#  
# class GUI(QMainWindow):             # inherit from QMainWindow
#     def __init__(self): 
#         super().__init__()          # initialize super class, which creates the Window
#           
#         self.initUI()                           
#   
#           
#     def initUI(self):                       # set properties and add widgets        
#         self.setWindowTitle('PyQt5 GUI')    # refer to Window as self
#           
#         self.resize(400,300)                # resize window (width, height)         
#   
#   
# if __name__ == '__main__':     
#     app = QApplication(sys.argv)        # create Application     
#     gui = GUI()                         # create instance of class
#     gui.show()                          # show the constructed PyQt window
#     sys.exit(app.exec_())               # execute the application

# #--------------------------------------------------
  
# class inheriting from QMainWindow
# add status bar
#    
#    
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow 
#   
#       
# class GUI(QMainWindow):             # inherit from QMainWindow
#     def __init__(self): 
#         super().__init__()          # initialize super class, which creates the Window
#             
#         self.initUI()                           
#     
#             
#     def initUI(self):                       # set properties and add widgets        
#         self.setWindowTitle('PyQt5 GUI')    # refer to Window as self
#           
#         self.resize(400,300)                    # resize window (width, height) 
#             
#         self.statusBar().showMessage('Text in statusbar')
#     
#     
# if __name__ == '__main__':     
#     app = QApplication(sys.argv)        # create Application     
#     gui = GUI()                         # create instance of class
#     gui.show()                          # show the constructed PyQt window
#     sys.exit(app.exec_())               # execute the application    
    

#--------------------------------------------------
  

# class inheriting from QMainWindow
# add menu bar

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction 
#   
# class GUI(QMainWindow):             # inherit from QMainWindow
#     def __init__(self): 
#         super().__init__()          # initialize super class, which creates the Window
#            
#         self.initUI()                           
#               
#     def initUI(self):                       # set properties and add widgets        
#         self.setWindowTitle('PyQt5 GUI')    # refer to Window as self
#           
#         self.statusBar().showMessage('Text in statusbar')
#           
#         menubar = self.menuBar()                # create menu bar
#         file_menu = menubar.addMenu('File')     # add menu to menu bar
#           
#         new_action = QAction('New', self)       # create an Action      
#         file_menu.addAction(new_action)         # add Action to menu
#           
#         new_action.setStatusTip('New File')     # statusBar updated
#           
#         self.resize(400,300)                    # resize window (width, height) 
#             
# if __name__ == '__main__':     
#     app = QApplication(sys.argv)        # create Application     
#     gui = GUI()                         # create instance of class
#     gui.show()                          # show the constructed PyQt window
#     sys.exit(app.exec_())               # execute the application    

# #--------------------------------------------------
#  
# # class inheriting from QMainWindow
# # add menu bar with two menus
#  
#  
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction 
#   
#  
# class GUI(QMainWindow):             # inherit from QMainWindow
#     def __init__(self): 
#         super().__init__()          # initialize super class, which creates the Window
#            
#         self.initUI()                           
#    
#            
#     def initUI(self):                       # set properties and add widgets        
#         self.setWindowTitle('PyQt5 GUI')    # refer to Window as self
#           
#         self.statusBar().showMessage('Text in statusbar')
#           
#         menubar = self.menuBar()                # create menu bar
#           
#         file_menu = menubar.addMenu('File')     # add menu to menu bar
#         new_action = QAction('New', self)       # create an Action      
#         file_menu.addAction(new_action)         # add Action to menu
#         new_action.setStatusTip('New File')     # statusBar updated
#           
#         edit_menu = menubar.addMenu('Edit')     # add a second menu
#   
#  
#         self.resize(400,300)                    # resize window (width, height) 
#            
#   
#    
# if __name__ == '__main__':     
#     app = QApplication(sys.argv)        # create Application     
#     gui = GUI()                         # create instance of class
#     gui.show()                          # show the constructed PyQt window
#     sys.exit(app.exec_())               # execute the application    


# #--------------------------------------------------
#  
# # class inheriting from QMainWindow
# # add icon to new menu

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction 
#   
# from PyQt5.QtGui import QIcon
#    
#    
# class GUI(QMainWindow):             # inherit from QMainWindow
#     def __init__(self): 
#         super().__init__()          # initialize super class, which creates the Window
#            
#         self.initUI()                           
#    
#            
#     def initUI(self):                       # set properties and add widgets        
#         self.setWindowTitle('PyQt5 GUI')    # refer to Window as self
#           
#         self.statusBar().showMessage('Text in statusbar')
#           
#         menubar = self.menuBar()                # create menu bar
#           
#         file_menu = menubar.addMenu('File')     
#         new_icon = QIcon('icons/new_icon.png')          # create icon
#         new_action = QAction(new_icon, 'New', self)     # add icon to menu 
#                
#         file_menu.addAction(new_action)         # add Action to menu
#         new_action.setStatusTip('New File')     # statusBar updated
#           
#         edit_menu = menubar.addMenu('Edit')     # add a second menu
#   
#         self.resize(400,300)                    # resize window (width, height) 
#  
#    
# if __name__ == '__main__':     
#     app = QApplication(sys.argv)        # create Application     
#     gui = GUI()                         # create instance of class
#     gui.show()                          # show the constructed PyQt window
#     sys.exit(app.exec_())               # execute the application 


## NOT SHOWN IN VIDEO - COMBINED
# 
# #--------------------------------------------------
#  
# # class inheriting from QMainWindow
# # add Exit menu item
  
  
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction 
# from PyQt5.QtGui import QIcon
#   
#   
# class GUI(QMainWindow):             # inherit from QMainWindow
#     def __init__(self): 
#         super().__init__()          # initialize super class, which creates the Window
#           
#         self.initUI()                           
#   
#           
#     def initUI(self):                       # set properties and add widgets        
#         self.setWindowTitle('PyQt5 GUI')    # refer to Window as self
#          
#         self.statusBar().showMessage('Text in statusbar')
#          
#         menubar = self.menuBar()                # create menu bar
#          
#         file_menu = menubar.addMenu('File')     
#         new_icon = QIcon('icons/new_icon.png')          # create icon
#         new_action = QAction(new_icon, 'New', self)     # add icon to menu 
#               
#         file_menu.addAction(new_action)         # add Action to menu
#         new_action.setStatusTip('New File')     # statusBar updated
# 
#         exit_action = QAction('Exit', self)     # create Exit Action
#         file_menu.addAction(exit_action)
#          
#         edit_menu = menubar.addMenu('Edit')     # add a second menu
#  
# 
#         self.resize(400,300)                    # resize window (width, height) 
#           
#  
#   
# if __name__ == '__main__':     
#     app = QApplication(sys.argv)        # create Application     
#     gui = GUI()                         # create instance of class
#     gui.show()                          # show the constructed PyQt window
#     sys.exit(app.exec_())               # execute the application 



# #--------------------------------------------------
#  
# # class inheriting from QMainWindow
# # add separator and Exit menu item
  
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction 
# from PyQt5.QtGui import QIcon
#    
#    
# class GUI(QMainWindow):             # inherit from QMainWindow
#     def __init__(self): 
#         super().__init__()          # initialize super class, which creates the Window
#            
#         self.initUI()                           
#    
#            
#     def initUI(self):                       # set properties and add widgets        
#         self.setWindowTitle('PyQt5 GUI')    # refer to Window as self
#           
#         self.statusBar().showMessage('Text in statusbar')
#           
#         menubar = self.menuBar()                # create menu bar
#           
#         file_menu = menubar.addMenu('File')     
#         new_icon = QIcon('icons/new_icon.png')          # create icon
#         new_action = QAction(new_icon, 'New', self)     # add icon to menu 
#                
#         file_menu.addAction(new_action)         # add Action to menu
#         new_action.setStatusTip('New File')     # statusBar updated
#   
#         file_menu.addSeparator()                # add separator line between menu items
#           
#         exit_icon = QIcon('icons/exit_icon.png')          # create icon 
#         exit_action = QAction(exit_icon, 'Exit', self)    # create Exit Action
#         exit_action.setStatusTip('Click to exit the application')
#         file_menu.addAction(exit_action)
#           
#         edit_menu = menubar.addMenu('Edit')     # add a second menu
#   
#  
#         self.resize(400,300)                    # resize window (width, height) 
#            
#   
#    
# if __name__ == '__main__':     
#     app = QApplication(sys.argv)        # create Application     
#     gui = GUI()                         # create instance of class
#     gui.show()                          # show the constructed PyQt window
#     sys.exit(app.exec_())               # execute the application 
 
 
# #--------------------------------------------------
#  
# # class inheriting from QMainWindow
# # make Exit menu item quit the app
  
  
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction 
# from PyQt5.QtGui import QIcon
#    
#    
# class GUI(QMainWindow):             # inherit from QMainWindow
#     def __init__(self): 
#         super().__init__()          # initialize super class, which creates the Window
#            
#         self.initUI()                           
#    
#            
#     def initUI(self):                       # set properties and add widgets        
#         self.setWindowTitle('PyQt5 GUI')    # refer to Window as self
#           
#         self.statusBar().showMessage('Text in statusbar')
#           
#         menubar = self.menuBar()                # create menu bar
#           
#         file_menu = menubar.addMenu('File')     
#         new_icon = QIcon('icons/new_icon.png')          # create icon
#         new_action = QAction(new_icon, 'New', self)     # add icon to menu 
#                
#         file_menu.addAction(new_action)         # add Action to menu
#         new_action.setStatusTip('New File')     # statusBar updated
#   
#         file_menu.addSeparator()                # add separator line between menu items
#           
#         exit_icon = QIcon('icons/exit_icon.png')          # create icon 
#         exit_action = QAction(exit_icon, 'Exit', self)    # create Exit Action
#         exit_action.setStatusTip('Click to exit the application')
#           
#         exit_action.triggered.connect(self.close)   # close application when clicked
#           
#         file_menu.addAction(exit_action)
#           
#         # ---------------------------------
#         edit_menu = menubar.addMenu('Edit')     # add a second menu
#   
#  
#         self.resize(400,300)                    # resize window (width, height) 
#            
#   
#    
# if __name__ == '__main__':     
#     app = QApplication(sys.argv)        # create Application     
#     gui = GUI()                         # create instance of class
#     gui.show()                          # show the constructed PyQt window
#     sys.exit(app.exec_())               # execute the application    

# 
# #--------------------------------------------------
#  
# # class inheriting from QMainWindow
# # add keyboard shortcut to quit the app
  
  
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction 
#   
# from PyQt5.QtGui import QIcon
#    
#    
# class GUI(QMainWindow):             # inherit from QMainWindow
#     def __init__(self): 
#         super().__init__()          # initialize super class, which creates the Window
#            
#         self.initUI()                           
#    
#            
#     def initUI(self):                       # set properties and add widgets        
#         self.setWindowTitle('PyQt5 GUI')    # refer to Window as self
#           
#         self.statusBar().showMessage('Text in statusbar')
#           
#         menubar = self.menuBar()                # create menu bar
#           
#         file_menu = menubar.addMenu('File')     
#         new_icon = QIcon('icons/new_icon.png')          # create icon
#         new_action = QAction(new_icon, 'New', self)     # add icon to menu 
#                
#         file_menu.addAction(new_action)         # add Action to menu
#         new_action.setStatusTip('New File')     # statusBar updated
#   
#         file_menu.addSeparator()                # add separator line between menu items
#           
#         exit_icon = QIcon('icons/exit_icon.png')          # create icon 
#         exit_action = QAction(exit_icon, 'Exit', self)    # create Exit Action
#         exit_action.setStatusTip('Click to exit the application')
#           
#         exit_action.triggered.connect(self.close)   # close application when clicked
#         exit_action.setShortcut('Ctrl+Q')           # keyboard shortcut to close application      
#                                                     # main window has focus
#           
#         file_menu.addAction(exit_action)
#           
#         # ---------------------------------
#         edit_menu = menubar.addMenu('Edit')     # add a second menu
#   
#  
#         self.resize(400,300)                    # resize window (width, height) 
#            
#   
#    
# if __name__ == '__main__':     
#     app = QApplication(sys.argv)        # create Application     
#     gui = GUI()                         # create instance of class
#     gui.show()                          # show the constructed PyQt window
#     sys.exit(app.exec_())               # execute the application    





#--------------------------------------------------
 
# class inheriting from QMainWindow
# Refactored code for better readability
 
  
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction 
from PyQt5.QtGui import QIcon

class GUI(QMainWindow):             # inherit from QMainWindow
    def __init__(self): 
        super().__init__()          # initialize super class, which creates the Window
           
        self.initUI()                           
   
           
    def initUI(self):                       # set properties and add widgets        
        self.setWindowTitle('PyQt5 GUI')    # refer to Window as self
        self.resize(400,300)                # resize window (width, height) 
          
        self.add_menus_and_status()
          
          
    def add_menus_and_status(self):        
        self.statusBar().showMessage('Text in statusbar')
          
        menubar = self.menuBar()                # create menu bar
          
        file_menu = menubar.addMenu('File')     # add first menu  
             
        new_icon = QIcon('icons/new_icon.png')          # create icon
        new_action = QAction(new_icon, 'New', self)     # add icon to menu 
        new_action.setStatusTip('New File')             # update statusBar     
        file_menu.addAction(new_action)                 # add Action to menu
          
        file_menu.addSeparator()                # add separator line between menu items
          
        exit_icon = QIcon('icons/exit_icon.png')          # create icon 
        exit_action = QAction(exit_icon, 'Exit', self)    # create Exit Action
        exit_action.setStatusTip('Click to exit the application')
        exit_action.triggered.connect(self.close)         # close application when clicked
        exit_action.setShortcut('Ctrl+Q')                 # keyboard shortcut, window has focus     
        file_menu.addAction(exit_action)
          
        # ---------------------------------
        edit_menu = menubar.addMenu('Edit')     # add a second menu
  
  
if __name__ == '__main__':     
    app = QApplication(sys.argv)        # create Application     
    gui = GUI()                         # create instance of class
    gui.show()                          # show the constructed PyQt window
    sys.exit(app.exec_())               # execute the application  