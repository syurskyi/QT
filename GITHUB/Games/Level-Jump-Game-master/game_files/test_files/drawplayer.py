from drawgame import DrawGame
#from PyQt5.QtWidgets import QGraphicsItem

class DrawPlayer(DrawGame):
    #inherits DrawGame
    #tells how player object is drawn

    def __init__(self,owner):
        
        super(DrawPlayer,self).__init__(owner,'player')
       
        
      
        
