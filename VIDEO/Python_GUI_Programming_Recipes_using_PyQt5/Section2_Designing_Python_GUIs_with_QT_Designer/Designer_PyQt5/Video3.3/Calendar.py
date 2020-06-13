# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Calendar.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(408, 265)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout.addWidget(self.dateEdit)

        self.retranslateUi(Dialog)
        self.calendarWidget.selectionChanged.connect(self.dateEdit.selectAll)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

