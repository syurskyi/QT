
import sys, os
sys.path.insert(0, '../Model')
sys.path.insert(1, '../Views')

import BaseController
from Clickable import clickable
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *

class ButtonController(BaseController.BaseController):

    def __init__(self, view, component):
        super(ButtonController,self).__init__(view)
        self.checkbox = component
        self.checkbox.clicked.connect(self.changeTitle)
        clickable(self.view.label).connect(self.ClickedTheMap)
        self.view = view
        self.clicks = 0

    def changeTitle(self, state):

        if self.checkbox.isChecked():
            self.view.setWindowTitle('QCheckBox')
        else:
            self.view.setWindowTitle(' ')

    def ClickedTheMap(self):
        self.clicks += 1
        print(self.view.label.curiousposition)
        self.view.label2.rotation += 15
        self.view.label2.rotate_pixmap(self.view.label2.rotation)
        self.view.label2.move(int(self.view.label.curiousposition[0]), int(self.view.label.curiousposition[1]))
        if self.clicks == 10:
            self.viewp1 = QPixmap(os.getcwd() + '/images/Nuke2.png')
            self.view.label2.setPixmap(self.viewp1)
            self.view.label2.resize(75,75)
        self.view.show()
