# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Sergej\Dropbox\nuke\.nuke\example\PYTHON_EXAMPLE\Python_Example_All_Tutorials\VIDEO\Advanced_Python_Scripting\007_Base_PySide\ExampleCalculator\PYQT-Calculator-master\calc.ui'
#
# Created: Mon Nov 21 23:56:02 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 369)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lcd = QtGui.QLCDNumber(self.centralwidget)
        self.lcd.setMinimumSize(QtCore.QSize(358, 87))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.lcd.setFont(font)
        self.lcd.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcd.setFrameShadow(QtGui.QFrame.Plain)
        self.lcd.setNumDigits(8)
        self.lcd.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd.setObjectName("lcd")
        self.verticalLayout.addWidget(self.lcd)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.b1 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setWeight(75)
        font.setBold(True)
        self.b1.setFont(font)
        self.b1.setAutoFillBackground(False)
        self.b1.setAutoDefault(False)
        self.b1.setDefault(False)
        self.b1.setFlat(False)
        self.b1.setObjectName("b1")
        self.gridLayout_2.addWidget(self.b1, 0, 0, 1, 1)
        self.b2 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setWeight(75)
        font.setBold(True)
        self.b2.setFont(font)
        self.b2.setAutoFillBackground(False)
        self.b2.setAutoDefault(False)
        self.b2.setDefault(False)
        self.b2.setFlat(False)
        self.b2.setObjectName("b2")
        self.gridLayout_2.addWidget(self.b2, 0, 1, 1, 1)
        self.b3 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setWeight(75)
        font.setBold(True)
        self.b3.setFont(font)
        self.b3.setAutoFillBackground(False)
        self.b3.setAutoDefault(False)
        self.b3.setDefault(False)
        self.b3.setFlat(False)
        self.b3.setObjectName("b3")
        self.gridLayout_2.addWidget(self.b3, 0, 2, 1, 1)
        self.plus = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setWeight(75)
        font.setBold(True)
        self.plus.setFont(font)
        self.plus.setAutoFillBackground(False)
        self.plus.setAutoDefault(False)
        self.plus.setDefault(False)
        self.plus.setFlat(False)
        self.plus.setObjectName("plus")
        self.gridLayout_2.addWidget(self.plus, 0, 3, 1, 1)
        self.b4 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setWeight(75)
        font.setBold(True)
        self.b4.setFont(font)
        self.b4.setAutoFillBackground(False)
        self.b4.setAutoDefault(False)
        self.b4.setDefault(False)
        self.b4.setFlat(False)
        self.b4.setObjectName("b4")
        self.gridLayout_2.addWidget(self.b4, 1, 0, 1, 1)
        self.b5 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setWeight(75)
        font.setBold(True)
        self.b5.setFont(font)
        self.b5.setAutoFillBackground(False)
        self.b5.setAutoDefault(False)
        self.b5.setDefault(False)
        self.b5.setFlat(False)
        self.b5.setObjectName("b5")
        self.gridLayout_2.addWidget(self.b5, 1, 1, 1, 1)
        self.b6 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setWeight(75)
        font.setBold(True)
        self.b6.setFont(font)
        self.b6.setAutoFillBackground(False)
        self.b6.setAutoDefault(False)
        self.b6.setDefault(False)
        self.b6.setFlat(False)
        self.b6.setObjectName("b6")
        self.gridLayout_2.addWidget(self.b6, 1, 2, 1, 1)
        self.minus = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setWeight(75)
        font.setBold(True)
        self.minus.setFont(font)
        self.minus.setAutoFillBackground(False)
        self.minus.setAutoDefault(False)
        self.minus.setDefault(False)
        self.minus.setFlat(False)
        self.minus.setObjectName("minus")
        self.gridLayout_2.addWidget(self.minus, 1, 3, 1, 1)
        self.b7 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setWeight(75)
        font.setBold(True)
        self.b7.setFont(font)
        self.b7.setAutoFillBackground(False)
        self.b7.setAutoDefault(False)
        self.b7.setDefault(False)
        self.b7.setFlat(False)
        self.b7.setObjectName("b7")
        self.gridLayout_2.addWidget(self.b7, 2, 0, 1, 1)
        self.b8 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setWeight(75)
        font.setBold(True)
        self.b8.setFont(font)
        self.b8.setAutoFillBackground(False)
        self.b8.setAutoDefault(False)
        self.b8.setDefault(False)
        self.b8.setFlat(False)
        self.b8.setObjectName("b8")
        self.gridLayout_2.addWidget(self.b8, 2, 1, 1, 1)
        self.b9 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setWeight(75)
        font.setBold(True)
        self.b9.setFont(font)
        self.b9.setAutoFillBackground(False)
        self.b9.setAutoDefault(False)
        self.b9.setDefault(False)
        self.b9.setFlat(False)
        self.b9.setObjectName("b9")
        self.gridLayout_2.addWidget(self.b9, 2, 2, 1, 1)
        self.multiply = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setWeight(75)
        font.setBold(True)
        self.multiply.setFont(font)
        self.multiply.setAutoFillBackground(False)
        self.multiply.setObjectName("multiply")
        self.gridLayout_2.addWidget(self.multiply, 2, 3, 1, 1)
        self.clr = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setWeight(75)
        font.setBold(True)
        self.clr.setFont(font)
        self.clr.setAutoFillBackground(False)
        self.clr.setObjectName("clr")
        self.gridLayout_2.addWidget(self.clr, 3, 0, 1, 1)
        self.b0 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setWeight(75)
        font.setBold(True)
        self.b0.setFont(font)
        self.b0.setAutoFillBackground(False)
        self.b0.setAutoDefault(False)
        self.b0.setDefault(False)
        self.b0.setFlat(False)
        self.b0.setObjectName("b0")
        self.gridLayout_2.addWidget(self.b0, 3, 1, 1, 1)
        self.period = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setWeight(75)
        font.setBold(True)
        self.period.setFont(font)
        self.period.setAutoFillBackground(False)
        self.period.setAutoDefault(False)
        self.period.setDefault(False)
        self.period.setFlat(False)
        self.period.setObjectName("period")
        self.gridLayout_2.addWidget(self.period, 3, 2, 1, 1)
        self.divide = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setWeight(75)
        font.setBold(True)
        self.divide.setFont(font)
        self.divide.setAutoFillBackground(False)
        self.divide.setObjectName("divide")
        self.gridLayout_2.addWidget(self.divide, 3, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.enter = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setWeight(75)
        font.setBold(True)
        self.enter.setFont(font)
        self.enter.setAutoFillBackground(False)
        self.enter.setAutoDefault(False)
        self.enter.setDefault(False)
        self.enter.setFlat(False)
        self.enter.setObjectName("enter")
        self.verticalLayout.addWidget(self.enter)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.b1.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.b1.setShortcut(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.b2.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.b2.setShortcut(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.b3.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.b3.setShortcut(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.plus.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.plus.setShortcut(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.b4.setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.b4.setShortcut(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.b5.setText(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.b5.setShortcut(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.b6.setText(QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.b6.setShortcut(QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.minus.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.minus.setShortcut(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.b7.setText(QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.b7.setShortcut(QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.b8.setText(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.b8.setShortcut(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.b9.setText(QtGui.QApplication.translate("MainWindow", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.b9.setShortcut(QtGui.QApplication.translate("MainWindow", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.multiply.setText(QtGui.QApplication.translate("MainWindow", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.multiply.setShortcut(QtGui.QApplication.translate("MainWindow", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.clr.setText(QtGui.QApplication.translate("MainWindow", "Clr", None, QtGui.QApplication.UnicodeUTF8))
        self.clr.setShortcut(QtGui.QApplication.translate("MainWindow", "Backspace", None, QtGui.QApplication.UnicodeUTF8))
        self.b0.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.b0.setShortcut(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.period.setText(QtGui.QApplication.translate("MainWindow", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.period.setShortcut(QtGui.QApplication.translate("MainWindow", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.divide.setText(QtGui.QApplication.translate("MainWindow", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.divide.setShortcut(QtGui.QApplication.translate("MainWindow", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.enter.setText(QtGui.QApplication.translate("MainWindow", "Enter", None, QtGui.QApplication.UnicodeUTF8))
        self.enter.setShortcut(QtGui.QApplication.translate("MainWindow", "Return", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))

