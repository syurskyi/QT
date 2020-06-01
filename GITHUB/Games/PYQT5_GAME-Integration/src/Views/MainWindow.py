import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

sys.path.insert(0, '../Controllers')
sys.path.insert(1, '../Model')
sys.path.insert(2, '../Views')

import BaseView
import ButtonController
import LandingPage

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()
        self.ctrl = None
        self.components = []
        self.view = None
        self.initUI()


    def initUI(self):
        self.view = LandingPage.LandingPage()
        self.view.initUI()
        self.statusBar().showMessage('PlayerOne: GO')
        self.setCentralWidget(self.view)

        self.setGeometry(300, 300, 796, 650)
        #self.resize(self.view.label.width(),self.view.label.height())
        self.setWindowTitle('Thermonuclear War')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
