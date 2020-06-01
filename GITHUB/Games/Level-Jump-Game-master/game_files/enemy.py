from dynamicobject import DynamicObject
from config import Config 

class Enemy(DynamicObject):
    #inherits DynamicObject
    #these are defined in config.txt
    Enemy_speed = Config.enemy_speed
    Fall_y = Config.enemy_fall_y #tells how fast enemies fall
    
    def __init__(self):
        super(Enemy,self).__init__(Enemy.Enemy_speed,'enemy')
        self.destroyed = False #tells if enemy is destroyed
        self.direction = False #False = enemy moves left, True = enemy moves right
        self.fall_y = Enemy.Fall_y
        
        
    def set_destroyed(self):
        #called from gamefield sets enemy destroyed
        self.destroyed = True

    def turn_direction(self):
        #this is a help method used to turn an enemy object direction
        if self.direction:
            self.direction = False

        else:
            self.direction = True


    
        
