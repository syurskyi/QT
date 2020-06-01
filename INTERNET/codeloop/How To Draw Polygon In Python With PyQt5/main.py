from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtGui import QBrush, QPen,QPainter, QPolygon
from PyQt5.QtCore import QPoint, Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Drawing Polygon"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300


        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        #painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        painter.setBrush(QBrush(Qt.red, Qt.VerPattern))


        points = QPolygon([
            QPoint(10,10),
            QPoint(10,100),
            QPoint(100,10),
            QPoint(100,100)



        ])

        painter.drawPolygon(points)



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())