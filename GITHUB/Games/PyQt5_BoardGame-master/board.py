from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import pyqtSlot
from random import randint
from PyQt5 import QtTest
import sys

class Ui(QMainWindow):
    def __init__(self):
        super(Ui,self).__init__()
        uic.loadUi('board1.ui', self)

        self.Step_1 = 0
        self.Step_2 = 0

        self.updateStep(1, self.Step_1)
        self.updateStep(2, self.Step_2)

        self.DICE_2.hide()
        self.newGame.hide()

        self.playerWins.hide()
        self.Wins.hide()
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Board Game")
        self.setWindowIcon(QtGui.QIcon('icon.jpg'))

        self.step_1.setText("STEP_1: " + str(self.Step_1))
        self.step_2.setText("STEP_2: " + str(self.Step_2))

        self.bonusLabel.hide()
        
        self.DICE_1.clicked.connect(self.button_clicked_1)
        self.DICE_2.clicked.connect(self.button_clicked_2)

        self.newGame.clicked.connect(self.NewGame)

    def updateStep(self, flag, step):
        player_1 = [self.b1_0,self.b1_1,self.b1_2,self.b1_3,self.b1_4,self.b1_5,
                    self.b1_6,self.b1_7,self.b1_8,self.b1_9,self.b1_10,self.b1_11,
                    self.b1_12,self.b1_13,self.b1_14,self.b1_15,self.b1_16,self.b1_17,
                    self.b1_18,self.b1_19,self.b1_20,self.b1_21]
        player_2 = [self.b2_0,self.b2_1,self.b2_2,self.b2_3,self.b2_4,self.b2_5,
                    self.b2_6,self.b2_7,self.b2_8,self.b2_9,self.b2_10,self.b2_11,
                    self.b2_12,self.b2_13,self.b2_14,self.b2_15,self.b2_16,self.b2_17,
                    self.b2_18,self.b2_19,self.b2_20,self.b2_21]
        
        if flag == 1:
            for button in player_1:
                button.hide()
            player_1[step].show()
        else:
            for button in player_2:
                button.hide()
            player_2[step].show()
        
    @pyqtSlot()
    def button_clicked_1(self):
        random = randint(1, 6)
        QtTest.QTest.qWait(150)

        self.DICE_1.setStyleSheet( "QPushButton {border-image: url(Resources/Dice/d1_" + str(random) + ".png); border-radius: 15px;}" )
  
        while random != 0:
            self.Step_1 += 1
            random -= 1

            if self.Step_1 > 21:
                self.Step_1 = 21
            
            self.updateStep(1, self.Step_1)
            QtTest.QTest.qWait(500)

        if self.Step_1 == 4:
            QtTest.QTest.qWait(666)
            self.Step_1 = 8
            self.updateStep(1, self.Step_1)
        if self.Step_1 == 12:
            QtTest.QTest.qWait(666)
            self.Step_1 = 16
            self.updateStep(1, self.Step_1)

        self.step_1.setText("STEP_1: " + str(self.Step_1))

        if self.Step_1 == 21:
            self.newGame.show()
            self.DICE_1.hide()

            self.playerWins.setText("GREEN")
            self.playerWins.setStyleSheet( "QLabel {color: green;}" )

            self.playerWins.show()
            self.Wins.show()
        else:
            self.DICE_1.hide()
            self.DICE_2.show()

        self.DICE_1.setStyleSheet( "QPushButton {border-image: url(Resources/Dice/d1_0.png); border-radius: 15px;}" )

        QtTest.QTest.qWait(666)

        if self.Step_1 == 9 or self.Step_1 == 20:
            self.Step_1 = self.red(1, self.Step_1)
        elif self.Step_1 == 5 or self.Step_1 == 13:
            self.Step_1 = self.green(1, self.Step_1)
        elif self.Step_1 == 10:
            self.Step_1 = self.purple(1, self.Step_1)
            

    @pyqtSlot()
    def button_clicked_2(self):
        random = randint(1,6)
        QtTest.QTest.qWait(150)

        self.DICE_2.setStyleSheet( "QPushButton {border-image: url(Resources/Dice/d2_" + str(random) + ".png); border-radius: 15px;}" )

        while random != 0:
            self.Step_2 += 1
            random -= 1

            if self.Step_2 > 21:
                self.Step_2 = 21
            
            self.updateStep(2, self.Step_2)
            QtTest.QTest.qWait(500)

        if self.Step_2 == 4:
            QtTest.QTest.qWait(666)
            self.Step_2 = 8
            self.updateStep(2, self.Step_2)
        if self.Step_2 == 12:
            QtTest.QTest.qWait(666)
            self.Step_2 = 16
            self.updateStep(2, self.Step_2)

        self.step_2.setText("STEP_2: " + str(self.Step_2))

        if self.Step_2 == 21:
            self.newGame.show()
            self.DICE_2.hide()

            self.playerWins.setText("RED")
            self.playerWins.setStyleSheet( "QLabel {color: red;}" )

            self.playerWins.show()
            self.Wins.show()
        else:
            self.DICE_2.hide()
            self.DICE_1.show()

        self.DICE_2.setStyleSheet( "QPushButton {border-image: url(Resources/Dice/d2_0.png); border-radius: 15px;}" )

        QtTest.QTest.qWait(666)

        if self.Step_2 == 9 or self.Step_2 == 20:
            self.Step_2 = self.red(2, self.Step_2)
        elif self.Step_2 == 5 or self.Step_2 == 13:
            self.Step_2 = self.green(2, self.Step_2)
        elif self.Step_2 == 10:
            self.Step_2 = self.purple(2, self.Step_2)

    def red(self, player, Step):
        randomRed = randint(-3, -1)
        rand = randomRed

        self.bonusLabel.setText("BACK: " + str(-rand) + " steps")
        self.bonusLabel.setStyleSheet( "QLabel {color: red;}" )
        self.bonusLabel.show()
        
        QtTest.QTest.qWait(150)

        if player == 1:
            while randomRed != 0:
                Step -= 1
                randomRed += 1

                if Step > 21:
                    Step = 21
                if Step <= 0:
                    Step = 0
                
                self.updateStep(player, Step)
                QtTest.QTest.qWait(500)
            
        if player == 2:
            while randomRed != 0:
                Step += -1
                randomRed += 1

                if Step > 21:
                    Step = 21
                if Step < 0:
                    Step = 0

                self.updateStep(player, Step)
                QtTest.QTest.qWait(500)
        
        self.bonusLabel.hide()

        return Step 

    def green(self, player, Step):
        randomGreen = randint(1, 3)
        rand = randomGreen

        self.bonusLabel.setText("NEXT: " + str(rand) + " steps")
        self.bonusLabel.setStyleSheet( "QLabel {color: green;}" )
        self.bonusLabel.show()
        
        QtTest.QTest.qWait(150)

        if player == 1:
            while randomGreen != 0:
                Step += 1
                randomGreen -= 1

                if Step > 21:
                    Step = 21
                if Step <= 0:
                    Step = 0
                
                self.updateStep(player, Step)
                QtTest.QTest.qWait(500)
            
        if player == 2:
            while randomGreen != 0:
                Step += 1
                randomGreen -= 1

                if Step > 21:
                    Step = 21
                if Step < 0:
                    Step = 0

                self.updateStep(player, Step)
                QtTest.QTest.qWait(500)
        
        self.bonusLabel.hide()

        return Step

    def purple(self, player, Step):
        randomPurple = randint(1, 2)
        if randomPurple == 1:
            Step = self.red(player, Step)
        else:
            Step = self.green(player, Step)

        return Step

    @pyqtSlot()
    def NewGame(self):
        self.Step_1 = 0
        self.Step_2 = 0

        self.step_1.setText("STEP_1: " + str(self.Step_1))
        self.step_2.setText("STEP_2: " + str(self.Step_2))

        self.bonusLabel.setText("")
        
        self.updateStep(1, self.Step_1)
        self.updateStep(2, self.Step_2)

        self.newGame.hide()

        self.DICE_1.show()

        self.Wins.hide()
        self.playerWins.hide()

def window():
    app = QApplication(sys.argv)
    win = Ui()
    win.show()
    sys.exit(app.exec_())

window()
