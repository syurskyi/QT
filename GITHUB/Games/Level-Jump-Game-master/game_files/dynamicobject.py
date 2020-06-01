from gameobject import GameObject

class DynamicObject(GameObject):
    #This class inherts GameObject

    def __init__(self, speed,object_type):
        self.speed_x = speed #is defined in lower classes
        self.type = object_type
        self.falling = False #tells if object is falling
        self.fall_direction = 'down' #This tell object fall direction ('left', 'right' 'down')
        self.fallen = False #This is probably used only by enemies but just in case added here in upper class

    def set_new_position(self,x_min,x_max,y_min,y_max):
          #this is a helper method to set new position
          #called from gamefield fall, jump and move methods
          #this method does not check if position is ok to move into

          self.position.x_min = x_min
          self.position.x_max = x_max
          self.position.y_min = y_min
          self.position.y_max = y_max


    def set_fallen(self):
        #This is just a helper method called from gamefield to set object (an enemy) fallen
        self.fallen = True
        
