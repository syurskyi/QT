from PyQt5.QtWidgets import QGraphicsRectItem
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QColor

class DrawLevelObject(QGraphicsRectItem):
    #This class is used by gui to draw leveleditor object to a scene
    #It inherits QGraphicsRectItem to draw squares
    
    square_size = 20 #This tells square size for leveleditor objects
    #(it could be easily implemented to be read from config.txt but it hasn't been done)
    
    distance_x = 0 #distance from scene left corner, for aesthetic reasons should be kept at 0
    distance_y = 50 #distance from scene upper corner (this tells how much space there is for text objects)


    def __init__(self,owner):
        #owner is the levelobject this draw object represents

        x = owner.x * DrawLevelObject.square_size + DrawLevelObject.distance_x #owner.x is a relative pos and x is an absolute pos
        y = owner.y * DrawLevelObject.square_size + DrawLevelObject.distance_y
        super(DrawLevelObject, self).__init__(x, y, DrawLevelObject.square_size, DrawLevelObject.square_size) #init the upper class
        self.owner = owner #This is used to remove deleted object from scene
        self.set_color()

        self.is_deleted = False #This is used in gui when removing items from the scene


    def set_color(self):
        #This is called when an object is initialized
        #It sets correct color to the object based on the owner object type
        
        if self.owner.object_type == 'current':
            #creates an almost clear square
            color = QColor(255,255,255,5)
            #Notice that the 4th number is the alpha channel value

        elif self.owner.object_type == 'player':
            #creates a blue square
            color = QColor(0,0,255,255)

        elif self.owner.object_type == 'enemy':
            #creates a red squre
            color = QColor(255,0,0,255)

        elif self.owner.object_type == 'visible':
            #creates a brown square
            color = QColor(110,60,10,255)

        elif self.owner.object_type == 'finish':
            #creates a green square
            color = QColor(0,255,0,255)

        elif self.owner.object_type == 'invisible':
            #creates a black square
            color = QColor(0,0,0,255)

        self.setBrush(QBrush(color))

    def move(self):
        #This method is called from gui to move objects
        #This method was used to update current position, old method
        x = self.owner.x *DrawLevelObject.square_size + DrawLevelObject.distance_x
        y = self.owner.y *DrawLevelObject.square_size + DrawLevelObject.distance_y
        self.setRect(x,y,DrawLevelObject.square_size,DrawLevelObject.square_size)


    def adjust_position(self,editor_screen,win_width, x):
        #This method is called from gui move_level_objects
        #It updates drawlevel objects position
        #If 'current' object (see leveleditor and gui) has moved outside the screen x coordinates need to be shifted win_width left
        #x is a adjustment term for window size
        x = self.owner.x * DrawLevelObject.square_size + DrawLevelObject.distance_x - editor_screen *(win_width - x)
        y = self.owner.y *DrawLevelObject.square_size + DrawLevelObject.distance_y

        #update the object position
        self.setRect(x,y,DrawLevelObject.square_size, DrawLevelObject.square_size)
