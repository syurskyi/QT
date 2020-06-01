from PyQt5.QtWidgets import QApplication, QDialog, QCheckBox, QHBoxLayout, QGroupBox, QVBoxLayout, QLabel
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore




class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 CheckBox"
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


        self.check1 = QCheckBox("Python")
        self.check1.setIcon(QtGui.QIcon("pythonicon.png"))
        self.check1.setIconSize(QtCore.QSize(40,40))
        self.check1.setFont(QtGui.QFont("Sanserif", 13))
        self.check1.toggled.connect(self.onCheckbox_toggled)
        hboxLayout.addWidget(self.check1)


        self.check2 = QCheckBox("Java")
        self.check2.setIcon(QtGui.QIcon("java.png"))
        self.check2.setIconSize(QtCore.QSize(40, 40))
        self.check2.setFont(QtGui.QFont("Sanserif", 13))
        self.check2.toggled.connect(self.onCheckbox_toggled)
        hboxLayout.addWidget(self.check2)

        self.check3 = QCheckBox("C++")
        self.check3.setIcon(QtGui.QIcon("cpp.png"))
        self.check3.setIconSize(QtCore.QSize(40, 40))
        self.check3.setFont(QtGui.QFont("Sanserif", 13))
        self.check3.toggled.connect(self.onCheckbox_toggled)
        hboxLayout.addWidget(self.check3)

        self.groupBox.setLayout(hboxLayout)




    def onCheckbox_toggled(self):
        if self.check1.isChecked():
            self.label.setText(" You Have Selected: " + self.check1.text())


        if self.check2.isChecked():
            self.label.setText("You Have Selected : " + self.check2.text())


        if self.check3.isChecked():
            self.label.setText("You Have Selected : " + self.check3.text())





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())