import sys

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QByteArray
from PyQt5.QtGui import QMovie

from character_modul import Postac, Parowka, Benek, Laser


class Ui_MainWindow(object):
    okno = None

    def __init__(self):
        self.tlo = QtWidgets.QLabel()       # atrapy elementów tak aby nie powstawały błędy
        self.player = QtWidgets.QLabel()
        self.enemy = QtWidgets.QLabel()
        self.score = QtWidgets.QLabel()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.centralwidget.setObjectName("centralwidget")

        self.make_background()
        self.make_score()
        self.player = Benek(self.centralwidget)
        self.centralwidget.close()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.score.setText(_translate("MainWindow", "Score: 0"))

    def make_background(self):
        self.tlo = QtWidgets.QLabel(self.centralwidget)
        self.tlo.setGeometry(QtCore.QRect(0, 0, self.okno.width(), self.okno.height()))
        self.tlo.setText("")
        self.tlo.setPixmap(QtGui.QPixmap("images/stars_background.gif"))
        self.tlo.setScaledContents(True)
        self.tlo.setObjectName("label")

        self.movie = QMovie("images/stars_background.gif", QByteArray(), self.tlo)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.tlo.setMovie(self.movie)
        self.movie.start()
        self.movie.loopCount()

    def make_score(self):
        Postac.score = 0
        self.score = QtWidgets.QLabel(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(0, 100, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.score.setFont(font)
        self.score.setText("Score: 0")
        self.score.setObjectName("label_4")
        self.score.setStyleSheet("QLabel#label_4 {color: #aaffff}")
