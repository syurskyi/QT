# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\serge\Dropbox\nuke\.nuke\example\PYTHON_EXAMPLE\Python_Example_All_Tutorials\VIDEO\Advanced_Python_Scripting\009_Project_Manager\projectManagerMy\widgets\settingsDialog.ui'
#
# Created: Sat Nov 11 12:48:30 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        settingsDialog.setObjectName("settingsDialog")
        settingsDialog.resize(567, 189)
        self.verticalLayout = QtGui.QVBoxLayout(settingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table = QtGui.QTableWidget(settingsDialog)
        self.table.setObjectName("table")
        self.verticalLayout.addWidget(self.table)
        self.buttonBox = QtGui.QDialogButtonBox(settingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(settingsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), settingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), settingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(settingsDialog)

    def retranslateUi(self, settingsDialog):
        settingsDialog.setWindowTitle(QtGui.QApplication.translate("settingsDialog", "Settings Dialog", None, QtGui.QApplication.UnicodeUTF8))

