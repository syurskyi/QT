import sys

import cv2
from PyQt5.QtCore import QSize, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class Life2Coding(QDialog):
    def __init__(self):
        super(Life2Coding,self).__init__()
        loadUi('life2coding.ui',self)
        self.video_size=QSize(640,480)
        self.image=None
        self.processedImage=None
        self.startButton.clicked.connect(self.start_webcam)
        self.stopButton.clicked.connect(self.stop_webcam)

    def start_webcam(self):
        self.capture=cv2.VideoCapture(0) #0 =default #1,2,3 =Extra Webcam
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,self.video_size.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,self.video_size.height())

        self.timer =QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(5)

    def update_frame(self):
        ret,frame=self.capture.read()
        frame=cv2.cvtColor(frame,1)
        self.image=cv2.flip(frame,1)
        self.processedImage=self.image
        self.displayImage(1)



    def stop_webcam(self):
        self.timer.stop()


    def displayImage(self, window=1):
        qformat = QImage.Format_Indexed8

        if len(self.processedImage.shape) == 3:  # rows[0],cols[1],channels[2]
            if (self.processedImage.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(self.processedImage, self.processedImage.shape[1], self.processedImage.shape[0],
                     self.processedImage.strides[0], qformat)
        # BGR > RGB
        img = img.rgbSwapped()
        if window == 1:
            self.imgLabel.setPixmap(QPixmap.fromImage(img))
            self.imgLabel.setScaledContents(True)
        if window == 2:
            self.processedLabel.setPixmap(QPixmap.fromImage(img))
            self.processedLabel.setScaledContents(True)


if __name__=='__main__':
    app=QApplication(sys.argv)
    window=Life2Coding()
    window.setWindowTitle('Hanif Life2Coding PyQt5 Tutorials')
    window.show()
    sys.exit(app.exec_())