from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QHBoxLayout, QGroupBox, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "HBox Layout"
        self.top = 200
        self.left = 400
        self.width = 400
        self.height = 100
        self.iconName = "icon.png"

        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        self.CreateLayout()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        self.show()


    def CreateLayout(self):
        self.groupBox = QGroupBox("What Is Your Favorite Programming Language ?")
        hboxLayout = QHBoxLayout()

        self.button = QPushButton("Football", self)
        self.button.setIcon(QtGui.QIcon("football.png"))
        self.button.setIconSize(QtCore.QSize(40, 40))
        self.button.setMinimumHeight(40)
        hboxLayout.addWidget(self.button)

        self.button2 = QPushButton("Cricket", self)
        self.button2.setIcon(QtGui.QIcon("cricket.png"))
        self.button2.setIconSize(QtCore.QSize(40, 40))
        self.button2.setMinimumHeight(40)
        hboxLayout.addWidget(self.button2)

        self.button3 = QPushButton("Tennis", self)
        self.button3.setIcon(QtGui.QIcon("tennis.png"))
        self.button3.setIconSize(QtCore.QSize(40, 40))
        self.button3.setMinimumHeight(40)
        hboxLayout.addWidget(self.button3)


        self.groupBox.setLayout(hboxLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())