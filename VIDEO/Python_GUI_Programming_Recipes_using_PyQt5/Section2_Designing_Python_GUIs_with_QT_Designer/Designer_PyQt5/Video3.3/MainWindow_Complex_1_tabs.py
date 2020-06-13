# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainWindow_Complex_1_tabs.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(577, 559)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget_1 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_1.setObjectName("tabWidget_1")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_1)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_1_1 = QtWidgets.QWidget()
        self.tab_1_1.setObjectName("tab_1_1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_1_1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget_2.addTab(self.tab_1_1, "")
        self.tab_1_2 = QtWidgets.QWidget()
        self.tab_1_2.setObjectName("tab_1_2")
        self.tabWidget_2.addTab(self.tab_1_2, "")
        self.verticalLayout_3.addWidget(self.tabWidget_2)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.tabWidget_1.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(30, 30, 188, 48))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.tabWidget_1.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget_1, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 577, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_1.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget_1, self.tabWidget_2)
        MainWindow.setTabOrder(self.tabWidget_2, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_1_1), _translate("MainWindow", "Tab 1"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_1_2), _translate("MainWindow", "Tab 2"))
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.tab_1), _translate("MainWindow", "Tab 1"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

