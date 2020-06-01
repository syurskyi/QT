""" 
    Batteships game. Basics of IT semester project.
    Author: Piotr Kucharski 
"""

from PyQt5.QtGui import QPixmap, QPainter

class Field:
    """Defines the field of battleships


    Have list shot where coordinates are marked as shot
    Have list ships where all Ship objects are stored
    fieldUI uses field.png pixmap"""

    def __init__(self):
        """shot value list:
         True - hit
         False - miss
         number diffrent to -1 - there is a ship in this position"""
        self.shot = []

        emptyList = []          # Temporary variable for fulfilling the shot list

        # Fulfilling shot list as empty
        for i in range(0, 10):
            emptyList = []
            for j in range(0, 10):
                emptyList.append(-1)
            self.shot.append(emptyList)

        del emptyList           # We won't need this list anymore

        self.ships = []
        self.fieldUI = QPixmap("res/pictures/field.png")

    def change_field(self, filename, x, y):
        """Method changes graphic on field - adds new image

        x, y - coordinates where new graphic should be
        filename - path to image"""

        new_image = QPixmap(filename)
        merge = self.fieldUI.copy()
        painter = QPainter(merge)

        painter.drawPixmap(x, y, new_image)
        painter.end()
        self.fieldUI = QPixmap(merge)

    def __str__(self):
        for i in range (0, 10):
            for j in range (0, 10):
                print("%5d (%d %d)" % (self.shot[j][i], j, i), " ", end="")
            print()
        return ""