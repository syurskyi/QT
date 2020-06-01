# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'solver.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Solver(object):
    def setupUi(self, Solver):
        Solver.setObjectName("Solver")
        Solver.resize(296, 344)
        Solver.setMinimumSize(QtCore.QSize(296, 344))
        Solver.setMaximumSize(QtCore.QSize(296, 344))
        self.verticalLayout = QtWidgets.QVBoxLayout(Solver)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Solver)
        self.label.setStyleSheet("QTableWidget::item { \n"
"border-left: 2px solid white; \n"
"border-top: 2px solid white; \n"
"} \n"
"QTableWidget{ \n"
"border-bottom: 2px solid white; \n"
"border-right: 2px solid white; \n"
"}")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(Solver)
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(9)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(30)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(23)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_btn = QtWidgets.QPushButton(Solver)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.solve_btn = QtWidgets.QPushButton(Solver)
        self.solve_btn.setDefault(True)
        self.solve_btn.setObjectName("solve_btn")
        self.horizontalLayout.addWidget(self.solve_btn)
        self.reset_btn = QtWidgets.QPushButton(Solver)
        self.reset_btn.setObjectName("reset_btn")
        self.horizontalLayout.addWidget(self.reset_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Solver)
        QtCore.QMetaObject.connectSlotsByName(Solver)

    def retranslateUi(self, Solver):
        _translate = QtCore.QCoreApplication.translate
        Solver.setWindowTitle(_translate("Solver", "PyDoku Solver"))
        self.label.setText(_translate("Solver", "Enter the puzzle below, then hit \'Solve\' to show solution."))
        self.cancel_btn.setText(_translate("Solver", "Cancel"))
        self.solve_btn.setText(_translate("Solver", "Solve"))
        self.reset_btn.setText(_translate("Solver", "Reset"))

