from gameobject import GameObject
from config import Config

class InvisibleObject(GameObject):

    #This class is now implemented to GameObject straighly
    
    #class variables 
    Invisible_Object_Height = Config.invisible_object_height #normally set in config

    def __init__(self):
        self.type = 'invisible_object'
        
