import sys

import cv2
import numpy as np
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
from PyQt5.uic import loadUi


class Life2Coding(QDialog):
    face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    def __init__(self):
        super(Life2Coding,self).__init__()
        loadUi('life2coding.ui',self)
        self.image=None
        self.processedImage=None
        self.loadButton.clicked.connect(self.loadClicked)
        self.saveButton.clicked.connect(self.saveClicked)
        self.detectButton.clicked.connect(self.detectClicked)
        # self.hSlider.valueChanged.connect(self.cannyDisplay)
        self.dialValue.valueChanged.connect(self.rotate_image)
        self.rotateValue.returnPressed.connect(self.updateImage)

    def updateImage(self):
        angle=int(self.rotateValue.text())
        self.loadButton.setDefault(False)
        self.loadButton.setAutoDefault(False)
        if angle >=0 and angle <=360:
            self.rotate_image(angle)
            self.dialValue.setValue(angle)
        else:
            QMessageBox.information(self,'Error','Please Enter Between 0 to 360')

    def rotate_image(self, angle, scale=1.):
        w = self.image.shape[1]
        h = self.image.shape[0]
        rangle = np.deg2rad(int(angle))  # angle in radians

        # now calculate new image width and height

        nw = (abs(np.sin(rangle) * h) + abs(np.cos(rangle) * w)) * scale
        nh = (abs(np.cos(rangle) * h) + abs(np.sin(rangle) * w)) * scale

        # ask OpenCV for the rotation matrix


        rot_mat = cv2.getRotationMatrix2D((nw * 0.5, nh * 0.5), angle, scale)

        # calculate the move from the old center to the new center combined
        # with the rotation
        rot_move = np.dot(rot_mat, np.array([(nw - w) * 0.5, (nh - h) * 0.5, 0]))

        # the move only affects the translation, so update the translation
        # part of the transform
        rot_mat[0, 2] += rot_move[0]
        rot_mat[1, 2] += rot_move[1]

        self.processedImage = cv2.warpAffine(self.image, rot_mat, (int(np.math.ceil(nw)), int(np.math.ceil(nh))))
        self.rotateValue.setText(str(angle))
        self.displayImage(2)


    @pyqtSlot()
    def cannyDisplay(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) if len(self.image.shape) >= 3 else self.image
        self.processedImage = cv2.Canny(gray, self.hSlider.value(), self.hSlider.value()*3)
        self.displayImage(2)

    @pyqtSlot()
    def detectClicked(self):
        gray=cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY) if len(self.image.shape)>=3 else  self.image
        faces=self.face_cascade.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            if self.chkFace.isChecked():
                cv2.rectangle(self.processedImage,(x,y),(x+w,y+h),(255,0,0),2)
            else:
                self.processedImage=self.image.copy()
            roi_gray=gray[y:y+h,x:x+w]
            roi_color=self.processedImage[y:y+h,x:x+w]
            if self.chkEye.isChecked():
                eyes=self.eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            else:
                self.processedImage[y:y+h,x:x+w]=self.image[y:y+h,x:x+w].copy()

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
            cv2.imwrite(fname,self.processedImage)
        else:
            print('Error')


    def loadImage(self,fname):
        self.image=cv2.imread(fname,cv2.IMREAD_COLOR)
        self.processedImage=self.image.copy()
        self.displayImage(1)

    def displayImage(self,window=1):
        qformat=QImage.Format_Indexed8

        if len(self.processedImage.shape)==3: #rows[0],cols[1],channels[2]
            if(self.processedImage.shape[2])==4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888
        img=QImage(self.processedImage,self.processedImage.shape[1],self.processedImage.shape[0],self.processedImage.strides[0],qformat)
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