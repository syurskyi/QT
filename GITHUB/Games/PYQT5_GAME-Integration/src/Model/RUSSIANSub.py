'''
Russian SUB
'''

import CustomLabel
import os
import BaseGamePiece
import Submarines

me = '[RUSSIANSub]'

class RUSSIANSub(Submarines.Submarines):

    def __init__(self):
        super(RUSSIANSub, self).__init__()
        self.Name = 'RUSSIAN_SUBMARINE'
        self.xPos = 0
        self.yPos = 0


    def isHit(self):
        print('The sub is gonna sink')
        return

    def FireTorpedo(self):
        print('Firing Torpedo')
        return

    def FireNuke(self):
        print('Nuke has been launched, God help us all')
        return
