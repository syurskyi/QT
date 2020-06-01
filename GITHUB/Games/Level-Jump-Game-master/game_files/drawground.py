from drawstatic import DrawStatic
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QBrush

class DrawGround(DrawStatic):
    #inherits DrawStatic
    #tells how ground objects are drawn

    def __init__(self,owner):
        super(DrawGround,self).__init__(owner,'ground_object')

        #color could be easily changed
        dimgray = QColor(105,105,105)
        self.setBrush(QBrush(dimgray))

        self.new_height = 0 #used when ground object's position is adjusted from gui
