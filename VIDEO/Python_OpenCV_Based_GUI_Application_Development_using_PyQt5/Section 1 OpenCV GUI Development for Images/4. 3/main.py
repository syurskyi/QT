import sys

import cv2
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class Life2Coding(QDialog):
    def __init__(self):
        super(Life2Coding,self).__init__()
        loadUi('life2coding.ui',self)




app=QApplication(sys.argv)
window=Life2Coding()
window.setWindowTitle('Hanif PyQt5 Tutorials')
window.setGeometry(100,100,400,200)
window.show()
sys.exit(app.exec_())