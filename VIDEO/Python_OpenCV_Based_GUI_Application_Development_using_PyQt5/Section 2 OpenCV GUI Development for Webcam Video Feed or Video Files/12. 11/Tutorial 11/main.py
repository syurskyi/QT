import sys

import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class Life2Coding(QDialog):
    def __init__(self):
        super(Life2Coding,self).__init__()
        loadUi('life2coding.ui',self)
        self.image=None
        self.processedImage=None
        self.startButton.clicked.connect(self.start_webcam)
        self.stopButton.clicked.connect(self.stop_webcam)
        self.cannyButton.toggled.connect(self.canny_webcam)
        self.cannyButton.setCheckable(True)
        self.canny_Enabled=False

    def canny_webcam(self,status):
        if status:
            self.canny_Enabled=True
            self.cannyButton.setText('Canny Stop')
        else:
            self.canny_Enabled=False
            self.cannyButton.setText('Canny')


    def start_webcam(self):
        self.capture=cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)

        self.timer=QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)

    def update_frame(self):
        ret,self.image=self.capture.read()
        self.image=cv2.flip(self.image,1)
        self.displayImage(self.image,1)

        if(self.canny_Enabled):
            gray=cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY) if len(self.image.shape)>=3 else self.image
            self.processedImage=cv2.Canny(gray,100,200)
            self.displayImage(self.processedImage,2)


    def stop_webcam(self):
        self.timer.stop()


    def displayImage(self,img,window=1):
        qformat=QImage.Format_Indexed8
        if len(img.shape)==3 : #[0]=rows , [1]=cols [2]=channels
            if img.shape[2]==4 :
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888

        outImage=QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)
        #BGR>>RGB
        outImage=outImage.rgbSwapped()

        if window==1:
            self.imgLabel.setPixmap(QPixmap.fromImage(outImage))
            self.imgLabel.setScaledContents(True)
        if window==2:
            self.processedLabel.setPixmap(QPixmap.fromImage(outImage))
            self.processedLabel.setScaledContents(True)


if __name__=='__main__':
    app=QApplication(sys.argv)
    window=Life2Coding()
    window.setWindowTitle('Hanif Life2Coding PyQt5 Tutorials')
    window.show()
    sys.exit(app.exec_())