from drawstatic import DrawStatic
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QBrush

class DrawFinish(DrawStatic):
    #inherits DrawStatic
    #tells how finish objects are drawn

    #NOTICE: This class could be easily implemented to be part of DrawStatic
    #(this is an unnecessary class) but the implementation is not changed (at this state of project)
    #because then also gui requires many modifications

    def __init__(self,owner):
        super(DrawFinish,self).__init__(owner,'finish_object')

        #color could be easily changed
        springgreen = QColor(0,255,127)
        self.setBrush(QBrush(springgreen))
        
        
        
