# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/andrew/Documents/recognitionwithbarcodes/auth2.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 320)
        Dialog.setMinimumSize(QtCore.QSize(480, 320))
        Dialog.setMaximumSize(QtCore.QSize(480, 320))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(25, 239, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 461, 211))
        self.label_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.exitButton = QtWidgets.QPushButton(Dialog)
        self.exitButton.setGeometry(QtCore.QRect(0, 290, 161, 30))
        self.exitButton.setObjectName("exitButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Вход"))
        self.label.setText(_translate("Dialog", "Наведите на камеру уникальный qr-код на Вашей карте"))
        self.exitButton.setText(_translate("Dialog", "Вернуться обратно"))

