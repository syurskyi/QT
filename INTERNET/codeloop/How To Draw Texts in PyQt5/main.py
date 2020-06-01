from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QTextDocument
from PyQt5.QtCore import QRect, Qt, QRectF
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Drawing Text"
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


        painter.drawText(100,100, "Hello PyQt5 App Development")

        rect = QRect(100,150, 250,25)
        painter.drawRect(rect)
        painter.drawText(rect, Qt.AlignCenter, "Hello World")


        document = QTextDocument()
        rect2 = QRectF(0,0,250,250)
        document.setTextWidth(rect2.width())
        document.setHtml("<b>Python GUI </b> <i> Development </i> <font size = '10' color='red'>Complete Series</font>")
        document.drawContents( painter, rect2)



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())