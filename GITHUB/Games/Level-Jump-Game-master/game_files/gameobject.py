from position import Position

class GameObject:
    #This is the upper class for all gamefiled's objects

    def __init__(self,object_type):
        self.position = None # position object handle
        self.type = object_type # defined in lower classes
        level = 0 #object level, is not really used in the current implementation

    def set_object_level(self,level):
        self.level = level #called from gamefield


    def set_position_object(self,pos_object):
        #this method is just used to set the position object
        self.position = pos_object
        
    
