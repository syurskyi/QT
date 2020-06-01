# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\framecoins.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(1143, 651)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dice = QtWidgets.QFrame(Frame)
        self.frame_dice.setGeometry(QtCore.QRect(0, 0, 570, 651))
        self.frame_dice.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dice.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dice.setObjectName("frame_dice")
        self.bt_dice = QtWidgets.QPushButton(self.frame_dice)
        self.bt_dice.setGeometry(QtCore.QRect(90, 0, 371, 121))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        self.bt_dice.setFont(font)
        self.bt_dice.setFlat(True)
        self.bt_dice.setObjectName("bt_dice")
        self.lb_numeroi = QtWidgets.QPushButton(self.frame_dice)
        self.lb_numeroi.setGeometry(QtCore.QRect(90, 170, 371, 121))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(18)
        self.lb_numeroi.setFont(font)
        self.lb_numeroi.setFlat(True)
        self.lb_numeroi.setObjectName("lb_numeroi")
        self.bt_over = QtWidgets.QPushButton(self.frame_dice)
        self.bt_over.setGeometry(QtCore.QRect(90, 290, 185, 121))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(18)
        self.bt_over.setFont(font)
        self.bt_over.setFlat(True)
        self.bt_over.setObjectName("bt_over")
        self.bt_under = QtWidgets.QPushButton(self.frame_dice)
        self.bt_under.setGeometry(QtCore.QRect(275, 290, 185, 121))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(18)
        self.bt_under.setFont(font)
        self.bt_under.setFlat(True)
        self.bt_under.setObjectName("bt_under")
        self.bt_roll = QtWidgets.QPushButton(self.frame_dice)
        self.bt_roll.setGeometry(QtCore.QRect(90, 440, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(18)
        self.bt_roll.setFont(font)
        self.bt_roll.setFlat(True)
        self.bt_roll.setObjectName("bt_roll")
        self.te_aposta = QtWidgets.QTextEdit(self.frame_dice)
        self.te_aposta.setGeometry(QtCore.QRect(90, 410, 371, 31))
        self.te_aposta.setObjectName("te_aposta")
        self.frame_rou = QtWidgets.QFrame(Frame)
        self.frame_rou.setGeometry(QtCore.QRect(570, 0, 570, 651))
        self.frame_rou.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_rou.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_rou.setObjectName("frame_rou")
        self.bt_roulette = QtWidgets.QPushButton(self.frame_rou)
        self.bt_roulette.setGeometry(QtCore.QRect(100, 0, 371, 121))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        self.bt_roulette.setFont(font)
        self.bt_roulette.setFlat(True)
        self.bt_roulette.setObjectName("bt_roulette")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.bt_dice.setText(_translate("Frame", "Dice"))
        self.lb_numeroi.setText(_translate("Frame", "1000"))
        self.bt_over.setText(_translate("Frame", "Over 25000"))
        self.bt_under.setText(_translate("Frame", "Under 25000"))
        self.bt_roll.setText(_translate("Frame", "Roll"))
        self.bt_roulette.setText(_translate("Frame", "Roulette"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

