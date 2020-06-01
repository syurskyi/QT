# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(225, 111)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Menu)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Menu)
        self.label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.play_btn = QtWidgets.QPushButton(Menu)
        self.play_btn.setObjectName("play_btn")
        self.verticalLayout.addWidget(self.play_btn)
        self.solve_btn = QtWidgets.QPushButton(Menu)
        self.solve_btn.setObjectName("solve_btn")
        self.verticalLayout.addWidget(self.solve_btn)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "PyDoku"))
        self.label.setText(_translate("Menu", "PyDoku"))
        self.play_btn.setText(_translate("Menu", "Play Sudoku"))
        self.solve_btn.setText(_translate("Menu", "Sudoku Solver"))

