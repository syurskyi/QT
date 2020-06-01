'''
Although it is titled the Landing page it is being treated more like the initial
GameBoard.  Luckily this is just a view so it is subject to change, I can always
make a view called GameBoard which inherits the BaseView
'''

import sys, os
from PyQt5.QtWidgets import  *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

sys.path.insert(0, '../Controllers')
sys.path.insert(1, '../Model')
sys.path.insert(2, '../Views')

import BaseView
import ButtonController
from CustomLabel import *
import Submarines
import USASub
import RUSSIANSub
import FRANCESub
import NUKEController

class LandingPage(BaseView.BaseView):

    def __init__(self):
        super(LandingPage, self).__init__()
        self.ctrl = None
        self.components = []
        self.p = None
        self.p2 = None
        self.initUI()


    def initUI(self):

        checkbox = QCheckBox('Show title', self)
        checkbox.move(20, 20)
        checkbox.toggle()
        self.components.append(checkbox)
        #insertimage onto screen
        self.label = CustomLabel(self)
        self.p = QPixmap(os.getcwd() + '/images/GridMap.png')
        self.label.setPixmap(self.p)
        self.resize(self.label.width(), self.label.height())
        self.ctrl = ButtonController.ButtonController(self, self.components[0])
        self.label2 = CustomLabel(self)
        self.viewp1 = QPixmap(os.getcwd() + '/images/smallMissile.png')
        self.label2.setPixmap(self.viewp1)
        self.p2 = self.viewp1
        self.SetSubmarines()
        self.SetNukes()
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Thermonuclear War')

    def SetSubmarines(self):
        i = 0
        #Setup USA
        while i < 5:
            self.components.append(CustomLabel(self))
            label = self.components[len(self.components) -1]
            self.USASUB_P = QPixmap(os.getcwd() + '/images/SubmarineUSA.png')
            label.setPixmap(self.USASUB_P)
            submarine = USASub.USASub()
            submarine.xPos = 75*i
            submarine.yPos = 80*i
            submarine.label = label
            submarine.label.move(int(submarine.xPos)%796, int(submarine.yPos)%396)
            self.components.append(submarine)
            i += 1

        i = 0
        #Setup Russia
        while i < 4:
            self.components.append(CustomLabel(self))
            label = self.components[len(self.components) -1]
            self.USASUB_P = QPixmap(os.getcwd() + '/images/SubmarineRussian.png')
            label.setPixmap(self.USASUB_P)
            submarine = RUSSIANSub.RUSSIANSub()
            submarine.xPos = 75*i + 500
            submarine.yPos = 80*i
            submarine.label = label
            submarine.label.move(int(submarine.xPos)%796, int(submarine.yPos)%396)
            self.components.append(submarine)
            i += 1


        i = 0
        #Setup France
        while i < 2:
            self.components.append(CustomLabel(self))
            label = self.components[len(self.components) -1]
            self.USASUB_P = QPixmap(os.getcwd() + '/images/SubmarineFrench.png')
            label.setPixmap(self.USASUB_P)
            submarine = FRANCESub.FRANCESub()
            submarine.xPos = 140*i + 200
            submarine.yPos = 80*i
            submarine.label = label
            submarine.label.move(int(submarine.xPos)%796, int(submarine.yPos)%396)
            self.components.append(submarine)
            i += 1


    def SetNukes(self):
        self.components.append(CustomLabel(self))
        label = self.components[len(self.components) -1]
        label.Name = "Nuclear Football Launch"
        self.NUKE_FB_L = QPixmap(os.getcwd() + '/images/NukeFootballLaunchButton.png')
        label.setPixmap(self.NUKE_FB_L)
        label.move(int(796/2-(75/2)), int(500))
        self.NUKE_CTRL = NUKEController.NUKEController(self, label)
        return

    def SetCommanders(self):
        return

    def SetPresident(self):
        return
