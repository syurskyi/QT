'''
France SUB
'''

import CustomLabel
import os
import BaseGamePiece
import Submarines
me = '[FRANCESub]'

class FRANCESub(Submarines.Submarines):

    def __init__(self):
        super(FRANCESub, self).__init__()
        self.Name = 'USA_SUBMARINE'
        self.xPos = 0
        self.yPos = 0


    def isHit(self):
        print('you hit The French Fry!')
        return

    def FireTorpedo(self):
        print('Firing Torpedo')
        return

    def FireNuke(self):
        print('Nuke has been launched, God help us all')
        return
