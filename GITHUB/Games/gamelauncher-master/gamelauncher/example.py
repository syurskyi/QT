import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox, QHBoxLayout
from PyQt5.QtWidgets import QFileDialog
from PyQt5.uic import loadUi
import subprocess
import glob

buttons = []
dirs = ["D:\\Games\\Mega Man 11\\game.exe","D:\\Games\\Deadpool\\Binaries\\DP.exe"]
base = "D:\\Games\\"

class btn(QPushButton):
    def __init__(self, temp):
        super(btn, self).__init__()
        self.setText(str(temp))
        self.value = temp

class GameLauncher(QDialog):
    def __init__(self):
        super(GameLauncher, self).__init__()
        loadUi('anim.ui', self)
        self.setWindowTitle("Game Launcher")
        #adding two buttons with for loop
        for i in range(0,2):
            buttons.append(btn(dirs[i].split("\\")[-1]))
            #buttons[i].clicked.connect(lambda checked, arg=i: self.button_on_click(arg))
            self.container.addWidget(buttons[i])
            
        #trying out the file dialog thing in python
        fileBrowse = QFileDialog().getOpenFileName(buttons[0], 'Open File', 'C:\\')
        print(fileBrowse)

    def button_on_click(self, temp):
        temp = int(temp)
        s = dirs[temp].split("\\")
        gamename = s[-1]    
        path = ""
        for i in range(0, len(s)-1):
            path += s[i] + '\\'
        #start the game using the logic
        print(glob.glob(base+"\\*.exe"))
        subprocess.call('start ' + gamename, cwd=path, shell=True)
        
        

    
        
        
app = QApplication(sys.argv)
widget = GameLauncher()
widget.show()
sys.exit(app.exec_())