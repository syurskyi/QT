from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QPointF, QPixmap, QGraphicsPixmapItem, QLabel
from PyQt5.QtGui import QColor, QBrush
from creature import Creature
from player import Player
from pip._vendor.distlib._backport.shutil import move

class Creature_graphitem(QGraphicsPixmapItem):
   

    def __init__(self, creature, tile_size):
        # Call init of the parent object
        super(Creature_graphitem, self).__init__()

        self.creature = creature
        self.tile_size = tile_size
    
        
        self.set_sprite()
        self.updateAll()
        
    

    def set_sprite(self):
        
        if self.creature.type == Creature.TANK:
            if self.creature.player.side == 1:
                self.setPixmap(QPixmap('graphics/tank2_p1.png').scaled(self.tile_size, self.tile_size))
            else:
                self.setPixmap(QPixmap('graphics/tank2_p2.png').scaled(self.tile_size, self.tile_size))
        elif self.creature.type == Creature.MAGE:
            if self.creature.player.side == 1:
                self.setPixmap(QPixmap('graphics/mage2_p1.png').scaled(self.tile_size, self.tile_size))
            else:
                self.setPixmap(QPixmap('graphics/mage2_p2.png').scaled(self.tile_size, self.tile_size))
        elif self.creature.type == Creature.NINJA:
            if self.creature.player.side == 1:
                self.setPixmap(QPixmap('graphics/ninja2_p1.png').scaled(self.tile_size, self.tile_size))
            else:
                self.setPixmap(QPixmap('graphics/ninja2_p2.png').scaled(self.tile_size, self.tile_size))
        elif self.creature.type == Creature.SNIPER:
            if self.creature.player.side == 1:
                self.setPixmap(QPixmap('graphics/sniper2_p1.png').scaled(self.tile_size, self.tile_size))
            else:
                self.setPixmap(QPixmap('graphics/sniper2_p2.png').scaled(self.tile_size, self.tile_size))
        
    def update_tooltip(self):
        self.setToolTip("Name: {}\nHP: {}".format(self.creature.get_name(), self.creature.get_hp()))
    
    def updateAll(self):
        self.updatePosition()
        self.update_tooltip()

    def updatePosition(self):
        self.setPos(QPointF(self.creature.get_location().get_x()*self.tile_size, (self.creature.get_location().get_y())*self.tile_size))
        

        
    
        
            
        
