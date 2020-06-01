from drawstatic import DrawStatic
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QBrush



class DrawVisible(DrawStatic):
    #tells how visible objects are drawn
    #inherits DrawStatic

    #NOTICE: This class could be easily implemented to be part of DrawStatic
    #(this is an unnecessary class) but the implementation is not changed (at this state of project)
    #because then also gui requires many modifications

    def __init__(self,owner):
        super(DrawVisible,self).__init__(owner,'visible_object')

        #color could be easily changed
        saddlebrown = QColor(139,69,19)
        self.setBrush(QBrush(saddlebrown))
