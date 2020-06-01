import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QSize
from AppKit import NSScreen
#define the question msgbox object
class end_box(QWidget):
 
    def __init__(self):
    	#title of the box window
        self.title = 'Question Box'
        #box width
        self.width = 400
        #box height
        self.height = 160
        #box position in the screen default to be at the center
        self.left = (NSScreen.mainScreen().frame().size.width-self.width)//2
        self.top = (NSScreen.mainScreen().frame().size.height-self.height)//2
        #game status: quit or restart
        self.status = None
        #game type: the returned status when game ends 
        self.types = None

    def initBox(self):

        #create the msgbox object
        msgBox = QMessageBox()
        #set the title of the msgbox window
        msgBox.setWindowTitle(self.title)
        #set the size of the msgbox
        msgBox.setBaseSize(QSize(self.width, self.height))
        #set the position of the msgbox on the screen
        msgBox.move(self.left,self.top)
        #determine which question to be asked depends on the status of the game
        if self.types == 'Game Start':
        	question_text = 'Choose Game Board Size'
        	#set the icon of the msgbox
	        msgBox.setIcon(QMessageBox.Information)
	        #define three buttons corresponding to three different board sizes
	        small_button = msgBox.addButton('5X5',QMessageBox.RejectRole)
	        medium_button = msgBox.addButton('10X10',QMessageBox.NoRole)
        	large_button = msgBox.addButton('15X15',QMessageBox.YesRole)
	        #set default button to be medium button
	        msgBox.setDefaultButton(medium_button)
	        #set the displayed TEXT in the msgbox
        	msgBox.setText(question_text)
        	#execute the msgbox
	        buttonReply = msgBox.exec_()
	        #change game status depends on the button responds
	        self.status = [(5,5),(10,10),(15,15)][buttonReply]

        else:
        	#determine which question to be asked depends on the status of the game
	        if self.types == "Normal Exit":
	        	question_text = "Restart or Quit?"
	        elif self.types == "Game Tied":
	        	question_text = 'Game Tied\nRestart or Quit?'
	        else:
	        	question_text = f"Congrates to {self.types}!!\nRestart or Quit?"
	        #set the icon of the msgbox
	        msgBox.setIcon(QMessageBox.Question)
            #define two buttons --restart/quit
	        restart_button = msgBox.addButton('Restart',QMessageBox.ResetRole)
	        quit_button = msgBox.addButton('Quit',QMessageBox.RejectRole)
	        #set default button to be QUIT button
        	msgBox.setDefaultButton(quit_button)
	        #set the displayed TEXT in the msgbox
	        msgBox.setText(question_text)
	        #execute the msgbox
	        buttonReply = msgBox.exec_()
	        #change game status depends on the button responds
	        if buttonReply == 0:
	            self.status = 'RESTART'
	        else:
	            self.status = 'QUIT'
 
    def set_end_status(self,types):
    	self.types = types


#define the question box function
def question_screen(types):
	#create QtApp parent obeject
    app = QApplication(sys.argv)
    #innitiate the msgbox object
    ex = end_box()
    #set the game neding status 
    ex.set_end_status(types)
    #display the msgbox
    ex.initBox()
    return ex.status

