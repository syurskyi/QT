# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(801, 598)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_faren = QtGui.QPushButton(self.centralwidget)
        self.btn_faren.setGeometry(QtCore.QRect(20, 450, 371, 91))
        self.btn_faren.setObjectName(_fromUtf8("btn_faren"))
        self.btn_celcius = QtGui.QPushButton(self.centralwidget)
        self.btn_celcius.setGeometry(QtCore.QRect(410, 450, 371, 91))
        self.btn_celcius.setObjectName(_fromUtf8("btn_celcius"))
        self.input_temp = QtGui.QLineEdit(self.centralwidget)
        self.input_temp.setGeometry(QtCore.QRect(140, 170, 531, 61))
        self.input_temp.setAcceptDrops(False)
        self.input_temp.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.input_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.input_temp.setObjectName(_fromUtf8("input_temp"))
        self.label_celcius = QtGui.QLabel(self.centralwidget)
        self.label_celcius.setGeometry(QtCore.QRect(340, 140, 121, 20))
        self.label_celcius.setAlignment(QtCore.Qt.AlignCenter)
        self.label_celcius.setObjectName(_fromUtf8("label_celcius"))
        self.label_faren = QtGui.QLabel(self.centralwidget)
        self.label_faren.setGeometry(QtCore.QRect(360, 280, 81, 20))
        self.label_faren.setAlignment(QtCore.Qt.AlignCenter)
        self.label_faren.setObjectName(_fromUtf8("label_faren"))
        self.title = QtGui.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(20, 40, 781, 61))
        self.title.setObjectName(_fromUtf8("title"))
        self.text_result = QtGui.QLabel(self.centralwidget)
        self.text_result.setGeometry(QtCore.QRect(10, 310, 781, 61))
        self.text_result.setObjectName(_fromUtf8("text_result"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setCheckable(False)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.input_temp, self.btn_faren)
        MainWindow.setTabOrder(self.btn_faren, self.btn_celcius)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Temperature Converter", None))
        self.btn_faren.setText(_translate("MainWindow", "Convert to Celcius", None))
        self.btn_celcius.setText(_translate("MainWindow", "Convert to Fahrenheit", None))
        self.label_celcius.setText(_translate("MainWindow", "Temperature", None))
        self.label_faren.setText(_translate("MainWindow", "Result", None))
        self.title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">Temperature Converter</span></p></body></html>", None))
        self.text_result.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.menuFile.setTitle(_translate("MainWindow", "&File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

