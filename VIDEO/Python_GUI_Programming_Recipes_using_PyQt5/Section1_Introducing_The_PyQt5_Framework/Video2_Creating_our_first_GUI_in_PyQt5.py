'''
Created on Aug 31, 2017

@author: Burkhard A. Meier
'''



# import sys 
# from PyQt5.QtWidgets import *
# 
# app = QApplication(sys.argv)
# win = QWidget()
# win.show()
# 
# app.exec_()

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget       # avoid wild imports
#       
# app = QApplication(sys.argv)
# win = QWidget()
# win.show()
#       
# app.exec_()         # Qt exec_ ends with an underscore
# app.exec()          # exec is a Python keyword
  

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget     
#        
# app = QApplication(sys.argv)
# win = QWidget()
# win.show()
#      
# sys.exit(app.exec_())       # cleanly exit on exceptions
  

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget     
#    
# app = QApplication(sys.argv)
# win = QWidget()
#  
# win.setWindowTitle('PyQt5 GUI')
#    
# win.show()
# sys.exit(app.exec_()) 

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget     
#     
# app = QApplication(sys.argv)
# win = QWidget()
#     
# win.setWindowTitle('PyQt5 GUI')
# win.resize(400, 300)            # set window size: width, height
#     
# win.show()
# sys.exit(app.exec_())

# Structure of Qt5 GUIs
 
# Imports
import sys
from PyQt5.QtWidgets import QApplication, QWidget     
   
# Create Application  
app = QApplication(sys.argv)
  
# Create Window
win = QWidget()
    
# Add widgets and change properties 
win.setWindowTitle('PyQt5 GUI')
   
# show the constructed Qt window
win.show()
   
# execute the application
sys.exit(app.exec_())





