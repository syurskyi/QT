from PyQt5 import QtGui, QtWidgets, QtCore, QtTest, uic
import random
from pathlib import Path#necessary, since the way Windows directories work a) is bugged in python and an unintended consequence of the development of Windows - it was meant to be / but uses \ instead. and b) I want it to work cross-OS, not just Linux
import sys

class Game(QtWidgets.QWidget):
    """docstring for Game."""
    #switchStates shows the **actual** states of the switches; once a switch is True, it cannot be set to False
    #switchUpdates shows the **future** states of the switches, a switch can toggle between True and False. However, buttons potentially being disabled makes this impossible to abuse.
    switchStates = {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False}#dictionary which shows whether a switch is up or down. Up == False
    switchUpdates = {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False}#dictionary which shows the changes that are about to occur, when the user confirms their turn and rolls dice again
    d1 = 0#the first die
    d2 = 0#the second die
    firstPress = True#my if statement for rolling dice necessitates this for the first roll
    def __init__(self):
        super(Game, self).__init__()
        uic.loadUi("GameMain.ui", self)
        self.rollConfirm.clicked.connect(self.rollDice)#linking rollDice button
        self.restartButton.clicked.connect(self.restart)#linking restart button
        self.switch1.clicked.connect(lambda: self.toggleSwitch(self.switch1, 1))#linking each switch to a function which changes its state in switchUpdates
        self.switch2.clicked.connect(lambda: self.toggleSwitch(self.switch2, 2))
        self.switch3.clicked.connect(lambda: self.toggleSwitch(self.switch3, 3))
        self.switch4.clicked.connect(lambda: self.toggleSwitch(self.switch4, 4))
        self.switch5.clicked.connect(lambda: self.toggleSwitch(self.switch5, 5))
        self.switch6.clicked.connect(lambda: self.toggleSwitch(self.switch6, 6))
        self.switch7.clicked.connect(lambda: self.toggleSwitch(self.switch7, 7))
        self.switch8.clicked.connect(lambda: self.toggleSwitch(self.switch8, 8))
        self.switch9.clicked.connect(lambda: self.toggleSwitch(self.switch9, 9))

    def restart(self):#just resets everything to its original values, and how it looked before
        self.switchStates = {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False}
        self.switchUpdates = {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False}
        self.firstPress = True
        self.d1 = 0
        self.d2 = 0
        self.die1Label.setPixmap(QtGui.QPixmap())
        self.die2Label.setPixmap(QtGui.QPixmap())
        self.rollConfirm.setText("Confirm and Roll")
        self.setStyleSheet("")
        switchArray = [self.switch1, self.switch2, self.switch3, self.switch4, self.switch5, self.switch6, self.switch7, self.switch8, self.switch9]#array of all switches, to make next bit shorter. Longer version can be found in past commits
        for switch in switchArray:
            switch.setStyleSheet("background-color:rgb(138, 226, 52)")#for each switch, change the background colour
        self.disableAll()

    def toggleSwitch(self, switch, switchNum):
        if self.switchUpdates[switchNum] == False:#if the switch is up
            switch.setStyleSheet("background-color:rgb(252, 233, 79)")#push it down, changing its colour
            self.switchUpdates[switchNum] = True#and set it to DOWN in switchUpdates
        else:#do the opposite if it's down already
            switch.setStyleSheet("background-color:rgb(138, 226, 52);")
            self.switchUpdates[switchNum] = False
        if all(value == True for value in self.switchUpdates.values()):#if all the switches are down (on last switch, not confirm, hence this line) then display WIN. tbh I got this line from stack overflow and only just about get how it works.
            self.rollConfirm.setText("YOU WIN!")
            self.setStyleSheet("background-color:rgb(196, 160, 0);")

    def rollDice(self):
        if self.switchUpdates != self.switchStates or self.firstPress:#if switchUpdates is different to switchStates (i.e. something will change). As at the start both are the same, firstPress is a necessary variable, declared as True, however later changed to False.
            self.switchStates.update(self.switchUpdates)#states of switches are changed to those seen in intended changes (switchUpdates)
            self.firstPress = False#so this variable can't be abused for infinite rolls without playing
            self.d1 = random.randint(1, 6)#rolling dice
            self.d2 = random.randint(1, 6)
            self.die1Label.setPixmap(QtGui.QPixmap(str(Path("DiceFaces/Dice" + str(self.d1) + ".png"))))#and changing pictures
            self.die2Label.setPixmap(QtGui.QPixmap(str(Path("DiceFaces/Dice" + str(self.d2) + ".png"))))
            self.checkLegalMoves()

    def disableAll(self):
        switchArray = [self.switch1, self.switch2, self.switch3, self.switch4, self.switch5, self.switch6, self.switch7, self.switch8, self.switch9]#array of switches to make next bit faster
        for switch in switchArray:
            switch.setEnabled(False)#for each switch, turn it off so you can't press it

    def checkLegalMoves(self):
        self.disableAll()#turn of all the switches
        ##if (self.d1 == 1 or self.d2 == 1 or self.d1 + self.d2 == 1) and self.switchUpdates[1] == False:
        ##    self.switch1.setEnabled(True)
        switchArray = [self.switch1, self.switch2, self.switch3, self.switch4, self.switch5, self.switch6, self.switch7, self.switch8, self.switch9]#array of switches to make next bit faster
        for switch in switchArray:
            if(self.d1 == switchArray.index(switch)+1 or self.d2 == switchArray.index(switch)+1 or self.d1 + self.d2 == switchArray.index(switch)+1) and self.switchUpdates[switchArray.index(switch)+1] == False:#for each switch, if its number is that of one of the dice or the dice's values added
                switch.setEnabled(True)#turn it back on


def main():
    app = QtWidgets.QApplication(sys.argv)
    gameW = Game()
    gameW.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
