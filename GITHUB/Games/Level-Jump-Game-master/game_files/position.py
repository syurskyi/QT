
from config import Config

class Position:
    # class variables, set in config.txt 
    #distance from start of drawing area in x-dimension
    Distance_x = Config.distance_x
    
    #notice the typo in height (GameField depends on this value)
    Empty_line_heigth = Config.empty_line_height #tells how many pixels are not draw/empty line in the top of screen

    #RESTRICTIONS: static object w and h can be set freely but if objects are too tall
    #and Empty_line_height too big, objects don't fit in the screen
    #player and enemy h and w can be set freely but both figures must be less (w also equal works)
    
    #to static object's counterparts
    #these restriction are created to make map designing easier
    
    #Notice also the mispelling of height (these were mispelled at the beginning and also other classes depend on these values
    #so the spelling has not been corrected because it can break the whole code)

    static_object_heigth = Config.static_object_height
    static_object_width = Config.static_object_width
    
    enemy_heigth = Config.enemy_height
    enemy_width = Config.enemy_width
    
    player_heigth = Config.player_height
    player_width = Config.player_width
    

    #a position object belongs to one gameobject, positions are drawable and in pixels
    
    def __init__(self):
        self.x_min = 0 #relative pos. of the most left point of the object
        self.x_max = 0 #relative pos. of the most right point of the object
        self.y_min = 0 #relative pos. of the lowest point of the object
        self.y_max = 0 #relative pos. of the tallest point of the object
        self.level = 0 
        
    def set_position(self,x,level,object_type, Distance_y):
        # x tells how many static/empty objects are on the left side of the object
        # level tells relative level of the object
        # object_type and location are assumed to be correct, error handling elsewhere
        # valid object_types: 'player', 'enemy', 'static'
        # Distance_y tells distance from drawing window upperlimit

        self.level = level

        self.x_min = Position.Distance_x + x*Position.static_object_width #x is the relative position (tells how many objects are left of the object)
        self.y_max = Position.static_object_heigth * level + Distance_y*Position.Empty_line_heigth #level tells how many objects there are above the object
        self.y_min = self.y_max + Position.static_object_heigth
        #this is implemented a way that y_min and x_min are correct but x_max and y_max depend on the object's type
        
        if object_type == 'player':
            
            self.x_max = self.x_min + Position.player_width #assign x_max so it suits for a player
         
            self.y_max = self.y_min - Position.player_heigth #rewrite y_max so it suits for player model
            
            
        elif object_type == 'enemy':
            self.x_max = self.x_min + Position.enemy_width #assign x_max so it suits for an enemy
            
            self.y_max = self.y_min - Position.enemy_heigth #rewrite y_max so it suits for enemy model

        else:
            self.x_max = self.x_min + Position.static_object_width #assign x_max so it suits for a static object
      
            


    


    
    
