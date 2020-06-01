
from PyQt5.QtWidgets import QGraphicsRectItem
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QColor


#from gamefield import GameField
#from position import Position


class DrawGame(QGraphicsRectItem):
    
    #THIS IS AN OLD CLASS, not used anymore
    
    #gamefield is created prior creating drawgame objects
    #drawgame object is created in gui and it's lower classes represent
    #how playfield object are drawn
    #DrawGame lower class objects are appended to  drawing scene in gui as items
    #if there is bug in this class or lower classes whole gui freezes

    #this class has not been fully implementet yet
    
    def __init__(self,owner,object_type):

        x = owner.position.x_min #left corner
        
        y = owner.position.y_max #upper corner
        
        #print('objektin alku x: {},y:{}'.format(x,y))
        width = owner.position.x_max - x
        heigth =owner.position.y_min - y #y_min is lowest point of object
        
        super(DrawGame, self).__init__(x,y,width,heigth)
        self.owner_object = owner #this is the playfield object which this object represents, set in gui
        self.type = object_type #defined in lower classes
        #self.size = 10 #for testing only
        brush = QBrush(1) # fill evenly
        self.setBrush(brush)

    '''def set_size(self):
        #called after init set object size for drawing
        pass
        
    '''    



    '''   


    def draw_mainframe(self,window_width,window_heigth):
        #this method is called from Gui update_game -method
        #window_width and window_heigth tell game window size
        #it draws playfield's 'ground' and static objects
        
        #Drawing the ground from bottom of the window to lowest objects lower limit
        #Checking that y dimensional positions of the objects are appropriate is done elsewhere 
        #ie. lowest objects aren't outside of the screen

        static_heigth = Position.static_object_heigth
        static_width = Position.static_object_width  #assigned for ease of use
        
        y_max = window_heigth
        y_min = self.gamefield.max_level * static_heigth + self.gamefield.distance_y * static_heigth

        #draw ground which is rectangular, x coordinates that have invisble
        #don't have ground underside of them
        



        
        
    def get_invisible_object_locations(self):
        locations = []
        for i in range(self.gamefield.static_objects):
            #locations are always in pairs x_min, x_max 
            if self.gamefield.static_objects[i].type == 'invisible_object':
                locations.append(self.gamefield.static_objects[i].position.x_min)
                locations.append(self.gamefield.static_objects[i].position.x_max)

        return locations  
          
          
        
'''
        
    
