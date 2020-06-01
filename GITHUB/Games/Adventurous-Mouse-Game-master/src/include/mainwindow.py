# -*- coding: utf-8 -*-
from cv2 import CAP_DSHOW, VideoCapture, waitKey
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QGroupBox, QLabel, QMainWindow, QWidget

from include.detect import detect
from include.paramsgroup import ParamsGroup


class MainWindow(QMainWindow):
    def __init__(self, path):
        super().__init__()

        self.setWindowIcon(QIcon(path+'icons/mouse_icon.png'))

        self.path = path
        self.setWindowTitle('Adventurous Mouse Game')
        self.setFixedSize(1091, 526)

        self.centralwidget = QWidget(self, objectName='centralwidget')
        self.setCentralWidget(self.centralwidget)

        self.gameGroup = None

        self.cameraGroup = QGroupBox(self.centralwidget, objectName='cameraGroup')
        self.cameraGroup.setGeometry(QRect(10, 190, 341, 331))
        self.cameraGroup.setTitle('Camera')

        self.label = QLabel(self.cameraGroup)
        self.label.setGeometry(QRect(5, 15, 331, 311))

        self.paramsGroup = ParamsGroup(self, self.centralwidget)

        self.closeEvent = self.close_mainWindow

        self.speed = 1
        self.show()

        self.capture = VideoCapture(0, CAP_DSHOW)

        while True:
            src, direction = detect(self.capture, self.paramsGroup.getBeginColor(), self.paramsGroup.getEndColor())

            h, w, ch = src.shape
            bytesPerLine = ch * w
            image = QImage(src.data, w, h, bytesPerLine, QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(image))

            if waitKey(1) and self.gameGroup:
                currPos = self.gameGroup.gameFrame.mouse.pos()
                currX, currY = currPos.x(), currPos.y()

                speed = self.speed

                if direction != -1:
                    if direction == 0:
                        currX, currY = currX+speed, currY
                    elif direction == 1:
                        currX, currY = currX+speed, currY-speed
                    elif direction == 2:
                        currX, currY = currX, currY-speed
                    elif direction == 3:
                        currX, currY = currX-speed, currY-speed
                    elif direction == 4:
                        currX, currY = currX-speed, currY
                    elif direction == 5:
                        currX, currY = currX-speed, currY+speed
                    elif direction == 6:
                        currX, currY = currX, currY+speed
                    else:
                        currX, currY = currX+speed, currY+speed

                    self.gameGroup.move(currX, currY)


    def close_mainWindow(self, e):
        self.capture.release()
        exit()
