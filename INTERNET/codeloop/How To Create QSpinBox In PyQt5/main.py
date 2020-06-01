from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QLabel
import sys
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 QSpingBox"
        self.top = 200
        self.left = 500
        self.width = 200
        self.height = 100
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox= QVBoxLayout()
        self.spinbox = QSpinBox(self)
        self.spinbox.valueChanged.connect(self.spin_changed)
        vbox.addWidget(self.spinbox)
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.show()

    def spin_changed(self):
        spinValue = self.spinbox.value()
        self.label.setText("Current Value Is : " + str(spinValue))



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())