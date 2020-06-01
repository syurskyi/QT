from PyQt5.QtWidgets import QGraphicsPixmapItem

class DrawDynamic(QGraphicsPixmapItem):
    #inherits QGraphicsPixmapItem
    #tells how player and enemy objects are drawn

    def __init__(self,owner,pixmap):
        
        super(DrawDynamic,self).__init__(pixmap)
        self.owner_object = owner #this is the connection to gamefield's object
        #which this drawdynamic object draws
        
        self.type = owner.type #this line may be unnecessary
        self.removed = False #This tells if object is removed from the drawing scene

    def move_item(self):
        x = self.owner_object.position.x_min #left corner
        y = self.owner_object.position.y_max #upper corner

       
        self.setPos(x,y)#setPos is defined in QGraphicsPixmapItem
        
