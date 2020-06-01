# -*- coding: utf-8 -*-
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


class GameIcon(QLabel):
     """
     Location of objects and collision detection between them.
     """

     def __init__(self, parent, path, InitPosition, changePos=False):
         super().__init__(parent)

         pixmap = QPixmap(path)
         initX, initY = InitPosition[0], InitPosition[1]

         self.height = pixmap.size().height()
         self.width = pixmap.size().width()

         super().setGeometry(QRect(initX, initY, self.height, self.width))
         super().setPixmap(pixmap)

         self.changePos = changePos
         self.visiblePixList = []

         iconImage = pixmap.toImage()
         for i in range(0, self.height):
             for j in range(0, self.width):
                 if iconImage.pixel(i, j) != 0:
                     self.visiblePixList.append((i+initX, j+initY))


     def isCollided(self, gameIcon):
        """
        Real 2D collision detection between two objects (mouse-cheese or mouse-mousetrap) in the game.

        Parameters:
            self (GameIcon): First object (the mouse).
            gameIcon (GameIcon): Second object (a cheese or mousetrap).

        Returns:
            (bool).
        """

        if self.isHidden() or gameIcon.isHidden(): # If one of the two objects is hidden, there are surely no collision
            return False

        icon1Pos, icon2Pos = super().pos(), gameIcon.pos()
        icon1X, icon1Y = icon1Pos.x(), icon1Pos.y()
        icon2X, icon2Y = icon2Pos.x(), icon2Pos.y()

        if (icon1X + self.width >= icon2X and icon1X <= icon2X + gameIcon.width
                and icon1Y + self.height >= icon2Y and icon1Y <= icon2Y + gameIcon.height): # Large phase: check the collision of the "minimum container rectangle" of the two objects

            # Check if there is a real collision (pixel-perfect collision detection)
            icon1visPix = ([(icon1X+i, icon1Y+j) for (i, j) in self.visiblePixList] if self.changePos
                            else self.visiblePixList) # If the first object is moving, update its pixel's positions
            icon2visPix = ([(icon2X+i, icon2Y+j) for (i, j) in gameIcon.visiblePixList] if gameIcon.changePos
                            else gameIcon.visiblePixList) # If the second object is moving, update its pixel's positions

            return True if len(set(icon1visPix) & set(icon2visPix)) != 0 else False # Check if there is at least one common pixel between the two objects

        return False
