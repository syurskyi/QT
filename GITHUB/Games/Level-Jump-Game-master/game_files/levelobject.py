class LevelObject:
    #This class is used by leveleditor to create objects

    def __init__(self,object_type):
        #object_type: 'current', 'player', 'enemy', 'visible', 'invisible', 'finish'
        self.object_type = object_type #this is used in DrawLevelObject
        self.x = 0
        self.y = 0
        self.is_active = True #if this is false, object is removed 
        self.is_added = False #This is used when objects are added to the scene
        
        
    def set_pos(self,x,y):
        #sets the levelobject position
        self.x = x
        self.y = y

    def inactivate(self):
        #This is just a small helper method called from LevelEditor class
        self.is_active = False
        
    def added(self):
        #This is a small helper method called from gui after an drawobject has been added
        self.is_added = True
