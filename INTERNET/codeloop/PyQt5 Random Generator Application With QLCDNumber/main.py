from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber, QPushButton
import sys
from random import randint


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 QLCD Number"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.InitUi()
        self.show()

    def InitUi(self):
        vbox = QVBoxLayout()
        self.lcd = QLCDNumber()
        self.lcd.display(60)
        vbox.addWidget(self.lcd)
        self.lcd.setStyleSheet('background-color:green')
        self.button = QPushButton("Radom Number Gererator")
        self.button.setStyleSheet('background-color:yellow')
        self.button.clicked.connect(self.lcdHanlder)
        vbox.addWidget(self.button)
        self.setLayout(vbox)

    def lcdHanlder(self):
        random = randint(1,200)
        self.lcd.display(random)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())