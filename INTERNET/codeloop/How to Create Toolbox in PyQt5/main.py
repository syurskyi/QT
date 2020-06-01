from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QToolBox, QLabel, QVBoxLayout
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 ToolBox"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color:yellow")
        vbox = QVBoxLayout()
        toolbox = QToolBox()
        vbox.addWidget(toolbox)
        label = QLabel()
        toolbox.addItem(label, "Python")
        toolbox.setFont(QtGui.QFont("Sanserif", 15))
        label = QLabel()
        toolbox.addItem(label, "Java")
        label = QLabel()
        toolbox.addItem(label, "C++")
        self.setLayout(vbox)
        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())