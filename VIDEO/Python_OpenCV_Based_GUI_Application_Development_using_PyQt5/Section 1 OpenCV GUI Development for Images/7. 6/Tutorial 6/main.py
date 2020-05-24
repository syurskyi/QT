import sys

import cv2
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi


class Life2Coding(QDialog):
    def __init__(self):
        super(Life2Coding,self).__init__()
        loadUi('life2coding.ui',self)
        self.image=None
        self.loadButton.clicked.connect(self.loadClicked)
        self.saveButton.clicked.connect(self.saveClicked)
        self.cannyButton.clicked.connect(self.cannyClicked)

    @pyqtSlot()
    def cannyClicked(self):
        gray=cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY) if len(self.image.shape)>=3 else  self.image
        self.image=cv2.Canny(gray,100,200)
        self.displayImage(2)


    @pyqtSlot()
    def loadClicked(self):
        fname,filter =QFileDialog.getOpenFileName(self,'Open File','C:\\',"Image Files (*.jpg)")
        if fname:
            self.loadImage(fname)
        else:
            print('Invalid Image')

    @pyqtSlot()
    def saveClicked(self):
        fname, filter = QFileDialog.getSaveFileName(self, 'Save File', 'C:\\', "Image Files (*.jpg)")
        if fname:
            cv2.imwrite(fname,self.image)
        else:
            print('Error')


    def loadImage(self,fname):
        self.image=cv2.imread(fname,cv2.IMREAD_COLOR)
        self.displayImage(1)

    def displayImage(self,window=1):
        qformat=QImage.Format_Indexed8

        if len(self.image.shape)==3: #rows[0],cols[1],channels[2]
            if(self.image.shape[2])==4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888
        img=QImage(self.image,self.image.shape[1],self.image.shape[0],self.image.strides[0],qformat)
        #BGR > RGB
        img= img.rgbSwapped()
        if window==1:
            self.imgLabel.setPixmap(QPixmap.fromImage(img))
            self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        if window==2:
            self.processedLabel.setPixmap(QPixmap.fromImage(img))
            self.processedLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=Life2Coding()
    window.setWindowTitle('Hanif PyQt5 Tutorials')
    window.show()
    sys.exit(app.exec_())