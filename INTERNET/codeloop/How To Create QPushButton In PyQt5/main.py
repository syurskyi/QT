from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        title = "PyQt5 PushButton"
        left = 500
        top = 200
        width = 300
        height = 250
        iconName = "icon.png"
        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left,  top, width, height)
        self.UiComponents()
        self.show()
    def UiComponents(self):
        button = QPushButton("Close Application", self)
        #button.move(50,50)
        button.setGeometry(QRect(100,100,150,40))
        button.setIcon(QtGui.QIcon("icon.png"))
        button.setIconSize(QtCore.QSize(40,40))
        button.setToolTip("&lt;h1&gt;This Is Click Button&lt;h1&gt;")
        button.clicked.connect(self.ButtonAction)
    def ButtonAction(self):
         print("Hello World")
         sys.exit()
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
