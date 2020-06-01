from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QSlider, QLabel
import sys
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Slider"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        hbox = QHBoxLayout()
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.changedValue)
        self.label = QLabel("0")
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)
        self.setLayout(hbox)
        self.show()


    def changedValue(self):
        size = self.slider.value()
        self.label.setText(str(size))


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())