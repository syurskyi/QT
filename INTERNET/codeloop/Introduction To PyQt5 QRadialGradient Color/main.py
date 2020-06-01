from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import sys
from PyQt5.QtGui import QPainter, QBrush, QPen, QRadialGradient
from PyQt5.QtCore import Qt, QPoint


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Radial Gradient"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500


        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))

        radialGradient = QRadialGradient(QPoint(100,100), 100)

        # center point and radious

        radialGradient.setColorAt(0.4, Qt.white)
        radialGradient.setColorAt(0.8, Qt.green)
        radialGradient.setColorAt(1.0, Qt.black)
        painter.setBrush(QBrush(radialGradient))

        painter.drawRect(10,10, 200,200)





App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())