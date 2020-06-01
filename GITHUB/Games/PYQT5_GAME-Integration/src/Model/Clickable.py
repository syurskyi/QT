'''
Turns a non clickable object such as a label into a clickable object
'''
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def clickable(widget):

    class Filter(QObject):
        clicked = pyqtSignal()

        def eventFilter(self, obj, event):

            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        position = str(event.pos())
                        print(str(event.pos()))
                        self.clicked.emit()
                        position = position[position.index('(') + 1: position.index(')')]
                        xy = position.split(',')
                        print(int(xy[0]))
                        print(int(xy[1]))
                        xy = [int(xy[0]), int(xy[1])]
                        obj.curiousposition = xy
                        return True


            return False
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked
