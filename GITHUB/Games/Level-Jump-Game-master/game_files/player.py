from dynamicobject import DynamicObject

from dynamicobject import DynamicObject
from config import Config

class Player(DynamicObject):

    #class variables, defined in config.txt
    #speed of player
    Speed = Config.player_speed
    Jump_x = Config.player_jump_x  #how much player move sideways while jumping
    
    Jump_y = Config.player_jump_y #how much player moves up in one jump cycle
    #tells max jump height
    Jump_max_height = Config.player_jump_max_height
    Fall_y = Config.player_fall_y # how much player moves down while falling
    
    Fall_x = Config.player_fall_x #this doesn't need to be same as Jump_x (unless parabel trajectory is wanted)
    
    
    
    

    def __init__(self):
        super(Player,self).__init__(Player.Speed,'player')
        #set correct values based on the class variables
        self.jump_x = Player.Jump_x
        self.fall_y = Player.Fall_y
        self.jump_y = Player.Jump_y
        self.fall_x = Player.Fall_x
        
        self.jumping = False #tells if player is jumping
        self.jump_direction = '' #'up', 'right', 'left'
        self.jump_cycles = 0 #tells how many times jump mathod has been called during 'one' jump

    def set_jump_direction(self,direction):
        #called from gamefield,
        #a helper method to set jump_direction to 'up','right','left'
        
        if (direction == 'up' or direction == 'right' or direction == 'left'):
            self.jump_direction = direction
        
        
    
