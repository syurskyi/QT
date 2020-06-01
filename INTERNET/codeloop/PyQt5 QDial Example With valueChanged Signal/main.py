from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QDial, QVBoxLayout, QLabel
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Scroll Bar"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        self.dial = QDial()
        self.dial.setMaximum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(30)
        self.dial.valueChanged.connect(self.dialer_changed)
        vbox.addWidget(self.dial)
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.show()

    def dialer_changed(self):
        getValue = self.dial.value()
        self.label.setText(" Dialer Value : " + str(getValue))


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())