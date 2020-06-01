"""
-*- coding: utf-8 -*-
----------------------------------------------
--- Author         : Mayank Ashokkumar Lad
--- Mail           : mayanklad12@gmail.com
--- Github         : https://github.com/mayanklad
--- LinkedIn       : https://www.linkedin.com/in/mayank-lad-602568151
----------------------------------------------
"""
#Imports
from PyQt5 import QtCore, QtGui, QtWidgets
from orbits_main import Orbits

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(Orbits)
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.lb_app = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lb_app.setFont(font)
        self.lb_app.setTextFormat(QtCore.Qt.AutoText)
        self.lb_app.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_app.setObjectName("lb_app")
        self.gridLayout.addWidget(self.lb_app, 0, 0, 1, 1)
        self.lb_about = QtWidgets.QLabel(self.centralwidget)
        self.lb_about.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_about.setObjectName("lb_about")
        self.gridLayout.addWidget(self.lb_about, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Orbits"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.lb_app.setText(_translate("MainWindow", "Orbits"))
        self.lb_about.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">About</span></p><p align=\"center\">A simple Black Hole Simulator</p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Developer</span></p><p align=\"center\">Mayank Lad</p><p align=\"center\"><a href=\"https://github.com/mayanklad?tab=repositories\"><span style=\" text-decoration: underline; color:#0000ff;\">GitHub</span></a></p><p align=\"center\"><a href=\"https://www.linkedin.com/in/mayank-lad-602568151\"><span style=\" text-decoration: underline; color:#0000ff;\">LinkedIn</span></a><br/></p><p align=\"center\"><br/></p></body></html>"))


if __name__ == "__main__":
    import sys

    if getattr(sys, 'frozen', False):
        os.chdir(os.path.dirname(sys.executable))
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

