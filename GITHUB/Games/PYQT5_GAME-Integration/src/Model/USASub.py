'''
USA SUB
'''

import CustomLabel
import os
import BaseGamePiece
import Submarines

me = '[USASub]'
class USASub(Submarines.Submarines):

    def __init__(self):
        super(USASub, self).__init__()
        self.Name = 'USA_SUBMARINE'
        self.xPos = 0
        self.yPos = 0


    def isHit(self):
        print('you hit The Sub')
        return

    def FireTorpedo(self):
        print('Firing Torpedo')
        return

    def FireNuke(self):
        print('Nuke has been launched, God help us all')
        return
