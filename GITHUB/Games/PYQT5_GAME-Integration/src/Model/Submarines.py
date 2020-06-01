'''
Submarine class gives a general submarine
'''
import CustomLabel
import os
import BaseGamePiece

me = '[Submarines]'

class Submarines(BaseGamePiece.BaseGamePiece):

    def __init__(self):
        super(Submarines, self).__init__()
        self.Name = 'SUBMARINE'
        self.xPos = 0
        self.yPos = 0


    def isHit(self):
        return

    def FireTorpedo(self):
        return

    def FireNuke(self):
        return
