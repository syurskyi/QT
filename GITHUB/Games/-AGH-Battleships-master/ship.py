""" 
    Batteships game. Basics of IT semester project.
    Author: Piotr Kucharski 
"""

from PyQt5.QtGui import QPixmap

class Ship:
    """This class defines a ship object.

    It has coordiantes field which stores x and y on init
    Contains graphic pixmap of ship and size"""

    def __init__(self, x, y, size, init_id):
        self.coordinates = (x, y)
        self.typeOfShip = size      # Ships can be 4, 3, 2, 1 size
        self.shipUI = QPixmap("res/pictures/" + str(size) + ".png")
        self.hp = size
        self.id = init_id