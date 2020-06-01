# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\framenivel.ui'
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
        self.bt_left = QtWidgets.QPushButton(Frame)
        self.bt_left.setGeometry(QtCore.QRect(0, 0, 141, 651))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.bt_left.setFont(font)
        self.bt_left.setStyleSheet("")
        self.bt_left.setIconSize(QtCore.QSize(26, 16))
        self.bt_left.setDefault(False)
        self.bt_left.setFlat(True)
        self.bt_left.setObjectName("bt_left")
        self.bt_right = QtWidgets.QPushButton(Frame)
        self.bt_right.setGeometry(QtCore.QRect(986, 0, 141, 651))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.bt_right.setFont(font)
        self.bt_right.setStyleSheet("")
        self.bt_right.setIconSize(QtCore.QSize(26, 16))
        self.bt_right.setDefault(False)
        self.bt_right.setFlat(True)
        self.bt_right.setObjectName("bt_right")
        self.bt_unlock = QtWidgets.QPushButton(Frame)
        self.bt_unlock.setGeometry(QtCore.QRect(142, 0, 141, 651))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.bt_unlock.setFont(font)
        self.bt_unlock.setFlat(True)
        self.bt_unlock.setObjectName("bt_unlock")
        self.bt_right_2 = QtWidgets.QPushButton(Frame)
        self.bt_right_2.setGeometry(QtCore.QRect(845, 0, 141, 651))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.bt_right_2.setFont(font)
        self.bt_right_2.setStyleSheet("")
        self.bt_right_2.setIconSize(QtCore.QSize(26, 16))
        self.bt_right_2.setDefault(False)
        self.bt_right_2.setFlat(True)
        self.bt_right_2.setObjectName("bt_right_2")
        self.label = QtWidgets.QPushButton(Frame)
        self.label.setGeometry(QtCore.QRect(280, 200, 561, 251))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setFlat(True)
        self.label.setObjectName("label")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.bt_left.setText(_translate("Frame", "Anterior"))
        self.bt_right.setText(_translate("Frame", "Seguinte"))
        self.bt_unlock.setText(_translate("Frame", "Desbloquear"))
        self.bt_right_2.setText(_translate("Frame", "Nivel 1"))
        self.label.setText(_translate("Frame", "Bloqueado"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

