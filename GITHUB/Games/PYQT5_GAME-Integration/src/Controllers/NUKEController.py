'''
NUKE Controller.py
Handles when the Nuke has been Pressed
'''
import sys, os
sys.path.insert(0, '../Model')
sys.path.insert(1, '../Views')

import BaseController
import GameEngine
from Clickable import clickable
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *

me = '[NUKEController]'

class NUKEController(BaseController.BaseController):

    def __init__(self, view, component):
        super(NUKEController,self).__init__(view)
        self.checkbox = component
        clickable(component).connect(self.ClickedTheLaunch)
        self.view = view
        self.clicks = 0

    def ClickedTheLaunch(self):
        self.beginWar = GameEngine.GameEngine(self.view)
        print (me + 'NUCLEAR WAR HAS BEEN DECLARED')
        self.beginWar.start()
