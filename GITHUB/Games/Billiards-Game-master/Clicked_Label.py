from PyQt5.QtWidgets import QLabel,QWidget,QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import QMouseEvent,QPixmap,QPainter,QPaintEvent
#自定义控件：Clickable_QLabel
class Clickable_QLabel(QLabel):
    clicked=pyqtSignal()
    def __init__(self) -> object:

        super().__init__()
        # self.setScaledContents(True)
        # self.setGeometry(QRect(300,600,300,600))
        # self.setAcceptDrops(True)
        # self.dragstart=None
        # self.x1=600
        # self.y1=350
        self.Pos=None
    def mousePressEvent(self, ev:QMouseEvent):
        # self.clicked.emit()#signal emit
        self.dragstart=ev.pos()
        self.clicked.emit()#signal emit

    def mouseReleaseEvent(self, ev:QMouseEvent):
        self.clicked.emit()  # signal emit
        self.Pos=ev.pos()
        print('Pos:', ev.pos())
        # return ev.pos()