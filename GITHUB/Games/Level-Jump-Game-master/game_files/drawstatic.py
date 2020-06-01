from PyQt5.QtWidgets import QGraphicsRectItem
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QColor

class DrawStatic(QGraphicsRectItem):
    
    #gamefield is created prior creating draw objects
    #drawstatic object is created in gui and it's lower classes represent
    #how static playfield object are drawn
    #DrawStatic lower class objects are appended to  drawing scene in gui as items

    # This class inherits QGraphicsRectItem
    
    def __init__(self,owner,object_type):

        self.x = owner.position.x_min #left corner
        
        self.y = owner.position.y_max #upper corner, these are stored for reuse
        
        self.width = owner.position.x_max - self.x
        self.height = owner.position.y_min - self.y #y_min is the lowest point of this object
        
        super(DrawStatic, self).__init__(self.x,self.y,self.width,self.height)
        self.owner_object = owner #this is the playfield object which this object represents, set in gui
        self.type = object_type #defined in lower classes
        
    
