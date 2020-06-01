from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.Qt import QGraphicsRectItem, QGraphicsPixmapItem, QPixmap
from PyQt5.QtGui import QColor, QBrush
from tile import Tile

class Tile_graphitem(QGraphicsPixmapItem):
    
    def __init__(self, tile, tile_size, x, y):
        # Call init of the parent object
        super(Tile_graphitem, self).__init__()
        self.x = x
        self.y = y
        
        self.tile = tile
        self.tile_size = tile_size
        self.set_sprite()
        
        
    def set_sprite(self):
        if self.tile.get_type() == Tile.FREE:
            self.setPixmap(QPixmap('graphics/free_tile.png').scaled(self.tile_size, self.tile_size))
            self.setOffset(self.x * self.tile_size, self.y * self.tile_size)
        elif self.tile.get_type() == Tile.TREE:
            self.setPixmap(QPixmap('graphics/tree_tile.png').scaled(self.tile_size, self.tile_size))
            self.setOffset(self.x * self.tile_size, self.y * self.tile_size)
        else:
            self.setPixmap(QPixmap('graphics/rock_tile.png').scaled(self.tile_size, self.tile_size))
            self.setOffset(self.x * self.tile_size, self.y * self.tile_size)
            
    def set_on_fire(self):
        self.setPixmap(QPixmap('graphics/fire.png').scaled(self.tile_size, self.tile_size))
            

        
        
        
        
    