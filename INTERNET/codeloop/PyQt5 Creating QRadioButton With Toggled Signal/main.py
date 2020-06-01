from PyQt5.QtWidgets import QApplication, QDialog, QRadioButton, QHBoxLayout, QGroupBox, QVBoxLayout, QLabel
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Radio Button"
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
        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif",15))
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.show()


    def CreateLayout(self):
        self.groupBox = QGroupBox("What Is Your Favorite Programming Language ?")
        self.groupBox.setFont(QtGui.QFont("Sanserif",13))
        hboxLayout = QHBoxLayout()
        self.radiobtn1 = QRadioButton("Football")
        self.radiobtn1.setChecked(True)
        self.radiobtn1.setIcon(QtGui.QIcon("football.png"))
        self.radiobtn1.setIconSize(QtCore.QSize(40,40))
        self.radiobtn1.setFont(QtGui.QFont("Sanserif", 13))
        hboxLayout.addWidget(self.radiobtn1)
        self.radiobtn1.toggled.connect(self.onRadioBtn)
        self.radiobtn2 = QRadioButton("Cricket")
        self.radiobtn2.setIcon(QtGui.QIcon("cricket.png"))
        self.radiobtn2.setIconSize(QtCore.QSize(40, 40))
        self.radiobtn2.setFont(QtGui.QFont("Sanserif", 13))
        self.radiobtn2.toggled.connect(self.onRadioBtn)
        hboxLayout.addWidget(self.radiobtn2)
        self.radiobtn3 = QRadioButton("Tennis")
        self.radiobtn3.setIcon(QtGui.QIcon("tennis.png"))
        self.radiobtn3.setIconSize(QtCore.QSize(40, 40))
        self.radiobtn3.setFont(QtGui.QFont("Sanserif", 13))
        self.radiobtn3.toggled.connect(self.onRadioBtn)
        hboxLayout.addWidget(self.radiobtn3)
        self.groupBox.setLayout(hboxLayout)


    def onRadioBtn(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.label.setText("You Have Selected " + radioBtn.text())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())