from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox, QMenuBar
from PyQt5.QtWidgets import QMenu
import subprocess #for starting the game

def createWindow():
    #create the applicaton first
    app = QApplication([])
    app.setApplicationDisplayName("Game Launcher")

    #creating menu bar
    m1 = QMenu('File')
    m2 = QMenu('Edit')

    bar = QMenuBar()
    bar.addMenu(m1)
    bar.addMenu(m2)


    #creating window
    window = QWidget()

    layout = QVBoxLayout()

    #create a button for starting the game
    button = QPushButton("Open Megaman")

    #click method i.e. to start the game
    def button_on_click():
        subprocess.call('start game.exe', cwd="D:\\Games\\Mega Man 11", shell=True)

    #setting up the event listener
    button.clicked.connect(button_on_click)
    layout.addWidget(bar)
    layout.addWidget(button)

    #setting the layout and then starting the application
    window.setLayout(layout)
    window.show()
    app.exec_()

if __name__ == '__main__':
    createWindow()


#subprocess.call('start game.exe', cwd="D:\Games\Mega Man 11", shell=True)