'''
Base Game piece is the primitive of all game pieces on the board
'''

me = '[BaseGamePiece]'

class BaseGamePiece(object):

    def __init__(self):
        self.damage = 0
        self.Name = None
        self.label = None
        self.Animation = None
        self.xPos = None
        self.yPos = None
        self.Location = None
        self.country = None
        self.PieceLevel = 1

    def moveLeft(self):
        self.xPos -= 1

    def moveRight(self):
        self.xPos += 1

    def moveUp(self):
        self.yPos += 1

    def MoveDown(self):
        self.yPos -= 1
