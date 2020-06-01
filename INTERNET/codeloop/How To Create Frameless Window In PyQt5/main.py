from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizeGrip
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Size Grip"
        self.top = 200
        self.left = 500
        self.width = 640
        self.height = 480
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setGeometry(self.left, self.top, self.width, self.height)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        vboxlayout = QVBoxLayout()
        sizegrip = QSizeGrip(self)
        #sizegrip.setVisible(True)
        vboxlayout.addWidget(sizegrip)
        self.setLayout(vboxlayout)
        self.show()



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())