'''
GameEngine for Thermonuclear War, an open source production.
All coded by yours truly, Blake.
'''
import threading
import time
import USASub
import RUSSIANSub
import FRANCESub

me = '[GameEngine]'

class GameEngine(threading.Thread):

    def __init__(self, GameBoard):
        super(GameEngine,self).__init__()
        self.name = 'GameEngineThread'
        self.gameboard = GameBoard

    def run(self):
        while(True):
            time.sleep(1)
            #check for positions of missiles
            for component in self.gameboard.components:
                if isinstance(component, USASub.USASub):
                    component.xPos += 10
                    component.label.move(int(component.xPos)%(796 - 75) , int(component.yPos)%(396 -75))

                if isinstance(component, RUSSIANSub.RUSSIANSub):
                    component.xPos += 10
                    component.label.move(int(component.xPos)%(796 - 75), int(component.yPos)%(396 - 75))

                if isinstance(component, FRANCESub.FRANCESub):
                    component.yPos += 10
                    component.label.move(int(component.xPos)%(796 - 75), int(component.yPos)%(396 - 75))

            #check for positions of submarines

            #Check For Collisions
