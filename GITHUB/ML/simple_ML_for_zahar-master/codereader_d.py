# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'codereader.ui'
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
        icon.addPixmap(QtGui.QPixmap("../recognitionwithbarcodes/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(25, 239, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 461, 211))
        self.label_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(0, 290, 161, 30))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Корзина"))
        self.label.setText(_translate("Dialog", "Наведите на камеру штрих-код продукта"))
        self.pushButton.setText(_translate("Dialog", "Вернуться обратно"))

