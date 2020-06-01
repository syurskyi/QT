import random

from PyQt5.QtGui import QIntValidator
from PyQt5.uic.properties import QtGui

from CoreGame import Settings
from CoreGame.Menus.FrameCoins import Ui_Frame

class CoinsGui(Ui_Frame):
    def __init__(self,frame,coins):
        Ui_Frame.__init__(self)

        self.setupUi(frame)
        self.frame = frame
        self.diceou = -1
        self.coins = coins

        self.styleleft = """

                                        QPushButton{
                                            background-image:url('roullete.png');
                                            margin: 1px;
                                            border-style: outset;
                                            background-repeat:no-repeat;
                                            background-position: center;

                                            padding-top:120px;
                                            background-color:transparent;
                                        color:transparent;
                                        }
                                        QPushButton:hover{
                                            background-color:white;
                                            color:#2b5259;

                                        }

                                        """
        self.styleright = """

                                QPushButton{
                                    background-image:url('dice.png');
                                    margin: 1px;
                                    border-style: outset;
                                    background-repeat:no-repeat;
                                    background-position: center;
                                    padding-top:120px;
                                    background-color:transparent;
                                color:transparent;
                                }
                                

                                """
        self.i = 0

        self.bt_dice.setStyleSheet(self.styleright)
        self.bt_roll.setStyleSheet("QPushButton{color:#2b5259;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:#478db7;color:white;};")
        self.bt_over.setStyleSheet("QPushButton{color:#2b5259;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:#478db7;color:white;};")

        self.bt_under.setStyleSheet("QPushButton{color:#2b5259;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:#478db7;color:white;};")
        self.bt_over.clicked.connect(self.handlerbtover)
        self.bt_under.clicked.connect(self.handlerbtunder)
        self.bt_roll.clicked.connect(self.handlerbtroll)



    def handlerbtover(self):
        self.diceou = 0
        self.bt_over.setStyleSheet(
            "QPushButton{background-repeat:no-repeat;background-color:#478db7;color:white;background-position: center;margin: 1px;border-style: outset;}")
        self.bt_under.setStyleSheet(
            "QPushButton{color:#2b5259;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:#478db7;color:white;};")

    def handlerbtunder(self):
        self.diceou = 1
        self.bt_under.setStyleSheet(
            "QPushButton{background-repeat:no-repeat;background-color:#478db7;color:white;background-position: center;margin: 1px;border-style: outset;}")
        self.bt_over.setStyleSheet(
            "QPushButton{color:#2b5259;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:#478db7;color:white;};")

    def handlerbtroll(self):


        if self.te_aposta.toPlainText() != "" and self.diceou != -1 and Settings.COINS >= int(
                self.te_aposta.toPlainText()):
            numero = random.randrange(50000)

            Settings.COINS -= int(self.te_aposta.toPlainText())
            self.coins.setText(str(Settings.COINS))

            if numero < 25000 and self.diceou == 1:
                self.lb_numeroi.setStyleSheet(
                    "QPushButton{color:#2b5259;background-repeat:no-repeat;background-color:#47b7a1;background-position: center;margin: 1px;border-style: outset;}")

                Settings.COINS += (int(self.te_aposta.toPlainText()) * 2)
                self.coins.setText(str(Settings.COINS))

            elif numero >= 25000 and self.diceou == 0:
                self.lb_numeroi.setStyleSheet(
                    "QPushButton{color:#2b5259;background-repeat:no-repeat;background-color:#47b7a1;background-position: center;margin: 1px;border-style: outset;}")
                Settings.COINS += (int(self.te_aposta.toPlainText()) * 2)
                self.coins.setText(str(Settings.COINS))
            else:
                self.lb_numeroi.setStyleSheet(
                    "QPushButton{color:#2b5259;background-repeat:no-repeat;background-color:#b74759;background-position: center;margin: 1px;border-style: outset;}")

            self.lb_numeroi.setText(str(numero))



    def getframe(self):
        return self.frame