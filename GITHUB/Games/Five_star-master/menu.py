# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuGame = QtWidgets.QMenu(self.menubar)
        self.menuGame.setObjectName("menuGame")
        self.menuChange_the_difficulty = QtWidgets.QMenu(self.menuGame)
        self.menuChange_the_difficulty.setObjectName("menuChange_the_difficulty")
        self.menuSystem = QtWidgets.QMenu(self.menubar)
        self.menuSystem.setObjectName("menuSystem")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_game = QtWidgets.QAction(MainWindow)
        self.actionNew_game.setObjectName("actionNew_game")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionEasy = QtWidgets.QAction(MainWindow)
        self.actionEasy.setObjectName("actionEasy")
        self.actionCommon = QtWidgets.QAction(MainWindow)
        self.actionCommon.setObjectName("actionCommon")
        self.actionDifficult = QtWidgets.QAction(MainWindow)
        self.actionDifficult.setObjectName("actionDifficult")
        self.menuChange_the_difficulty.addAction(self.actionEasy)
        self.menuChange_the_difficulty.addAction(self.actionCommon)
        self.menuChange_the_difficulty.addAction(self.actionDifficult)
        self.menuGame.addAction(self.actionNew_game)
        self.menuGame.addAction(self.menuChange_the_difficulty.menuAction())
        self.menuSystem.addAction(self.actionQuit)
        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menuSystem.menuAction())

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered['bool'].connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuGame.setTitle(_translate("MainWindow", "Game"))
        self.menuChange_the_difficulty.setTitle(_translate("MainWindow", "Change the difficulty"))
        self.menuSystem.setTitle(_translate("MainWindow", "System"))
        self.actionNew_game.setText(_translate("MainWindow", "New game"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionEasy.setText(_translate("MainWindow", "Easy"))
        self.actionCommon.setText(_translate("MainWindow", "Common"))
        self.actionDifficult.setText(_translate("MainWindow", "Difficult"))

