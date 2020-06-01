from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton, QWhatsThis
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Whatisthis"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setGeometry(self.left, self.top, self.width, self.height)
        hbox = QHBoxLayout()
        label = QLabel("Focus And Press SHIFT + F1")
        hbox.addWidget(label)
        button = QPushButton("Click Me", self)
        button.setWhatsThis("This is a button that you can click on this button")
        hbox.addWidget(button)
        self.setLayout(hbox)
        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())