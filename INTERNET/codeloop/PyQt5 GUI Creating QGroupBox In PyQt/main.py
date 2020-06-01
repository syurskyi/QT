from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QRadioButton, QGroupBox, QVBoxLayout
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 QGroup Box"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setGeometry(self.left, self.top, self.width, self.height)
        hbox = QHBoxLayout()
        groupbox = QGroupBox("Select Your Favorite Fruit ")
        groupbox.setFont(QtGui.QFont("Sanserif", 15))
        hbox.addWidget(groupbox)
        vbox = QVBoxLayout()
        rad1 = QRadioButton("Apple")
        vbox.addWidget(rad1)
        rad2 = QRadioButton("Banana")
        vbox.addWidget(rad2)
        rad3 = QRadioButton("Melon")
        vbox.addWidget(rad3)
        groupbox.setLayout(vbox)
        self.setLayout(hbox)
        self.show()



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())