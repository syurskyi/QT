# -*- coding: utf-8 -*-
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QColor, QFont, QPainter, QPen, QPixmap
from PyQt5.QtWidgets import QGroupBox, QLabel, QWidget

from include.placeobjects import placeObjects


class GameGroup(QGroupBox):
    """
    Game's interface (current state and movement of the mouse)

    Attributes:
        mainWindow (QMainWindow): Application's main window (to which this object is attached).
        level (int): Difficulty level (0: Easy, 1: Medium, 2: Hard).
        stage (int): Level's stage (0, 1 or 2).
        gameFrame (QWidget).
        cheeseList (int): Number of cheeses in the current stage (detect the end of the game).
        finish (bool): Check if game is finished (stop moving the mouse).
        gameStatusLabel (QLabel): Current status (cheeses remains, win or lose).
    """

    def __init__(self, mainWindow, level, stage):
        super().__init__(mainWindow, objectName='gameGroup')

        gamePath = mainWindow.path + 'icons/'

        self.setGeometry(QRect(360, 0, 720, 520))
        self.setTitle('Game')

        self.gameFrame = QWidget(self, objectName ='gameFrame')
        self.gameFrame.setStyleSheet('#gameFrame {border: 1px solid gray;}')
        self.gameFrame.setGeometry(QRect(5, 15, 710, 485))

        self.gameFrame.cheeseList, self.gameFrame.trapList, self.gameFrame.mouse = placeObjects(self.gameFrame, gamePath, level, stage)

        self.cheeseList = len(self.gameFrame.cheeseList)
        self.finish = False
        self.gameFrame.show()

        self.gameStatusLabel = QLabel(self, objectName='gameStatusLabel')
        self.gameStatusLabel.setEnabled(False)
        self.gameStatusLabel.setGeometry(QRect(10, 498, 701, 21))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gameStatusLabel.setFont(font)
        self.gameStatusLabel.setText('Playing (' + str(self.cheeseList) + ' / ' + str(len(self.gameFrame.cheeseList)) + ' cheese remains)')

        self.gameFrame.label = QLabel(self.gameFrame)
        canvas = QPixmap(self.gameFrame.size().width(), self.gameFrame.size().height())
        canvas.fill(QColor(0, 0, 0, 210))
        self.gameFrame.label.setPixmap(canvas)
        self.gameFrame.label.hide()

        self.show()


    def write_result(self, win=True):
        self.gameFrame.label.show()
        painter = QPainter(self.gameFrame.label.pixmap())

        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor('#0aab15' if win else '#AB0A10'))
        painter.setPen(pen)

        font = QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(50)
        painter.setFont(font)

        painter.drawText(155, 218, 'You Won !' if win else 'Game Over !')
        painter.end()


    def move(self, axisX, axisY):
        """
        Move the mouse to a specified point.

        Parameters:
            axisX (int): The X coordinate (in the reference of the screen).
            axisY (int): The Y coordinate (in the reference of the screen).

        Returns:
            None
        """

        if not (self.finish or axisX < 0 or axisY < 0 or axisY+self.gameFrame.mouse.height > 485 or axisX+self.gameFrame.mouse.width > 710): # If the game is not finished AND the mouse will not go beyond the limits of the game screen with this move
            self.gameFrame.mouse.move(axisX, axisY)

            for cheese in self.gameFrame.cheeseList:
                if self.gameFrame.mouse.isCollided(cheese): # The mouse eats a cheese: Hide this cheese and decrement the number of remaining cheeses
                    cheese.hide()
                    self.cheeseList -= 1

                self.gameStatusLabel.setText('Playing (' + str(self.cheeseList) + ' / ' + str(len(self.gameFrame.cheeseList)) + ' cheese remains)')

            if self.cheeseList == 0: # No cheese remains: The game is considered "won"
                    self.gameStatusLabel.setText('You Won !')
                    self.write_result(True)
                    self.finish = True

            for trap in self.gameFrame.trapList: # Check if there is no collision with a mousetrap
                if self.gameFrame.mouse.isCollided(trap):
                    self.gameStatusLabel.setText('Game Over !') # Collision with mousetrap detected: The game is considered "lost"
                    self.write_result(False)
                    self.finish = True
