from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QVBoxLayout
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Window"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300


        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()



        self.btn = QPushButton("Open Second Dialog")
        self.btn.setFont(QtGui.QFont("Sanserif", 15))
        self.btn.clicked.connect(self.openSecondDialog)

        vbox.addWidget(self.btn)

        self.setLayout(vbox)



        self.show()


    def openSecondDialog(self):
        mydialog = QDialog(self)
        #mydialog.setModal(True)
        #mydialog.exec()

        mydialog.show()



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())