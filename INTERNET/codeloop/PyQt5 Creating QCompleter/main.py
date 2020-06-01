from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QCompleter, QLineEdit
import sys


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 QCompleter"
        self.top = 200
        self.left = 500
        self.width = 300
        self.height = 200


        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.Completer()



        self.show()


    def Completer(self):
        vbox = QVBoxLayout()
        names = ["Afghanistan", "India", "Pakistan", "Japan", "Indonesia", "China", "UAE", "America"]

        completer = QCompleter(names)

        self.lineedit = QLineEdit()
        self.lineedit.setCompleter(completer)

        vbox.addWidget(self.lineedit)

        self.setLayout(vbox)




App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())