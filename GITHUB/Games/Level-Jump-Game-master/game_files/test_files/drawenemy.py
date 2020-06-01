from drawgame import DrawGame

class DrawEnemy(DrawGame):
    #inherits DrawGame
    #tells how enemies are drawn
    
    def __init__(self,owner):
        super(DrawEnemy,self).__init__(owner,'enemy')
      
