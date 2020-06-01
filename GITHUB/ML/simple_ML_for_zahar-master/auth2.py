import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog
from auth2_d import Ui_Dialog
from PyQt5.QtCore import QTimer
from frame_editor import FrameEditor
import cv2


class Auth2(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.running = True
        self.auth_state = False
        self.timer = QTimer(self)
        self.image = None
        self.exitButton.clicked.connect(self.off)
        self.camera = cv2.VideoCapture(0)
        self.start_camera()

    def start_camera(self):
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1)

    def stop_camera(self):
        self.timer.stop()

    def update_frame(self):
        _, self.image = self.camera.read()
        result = FrameEditor(self.image, "acc").returnframe()
        if result:
            self.auth_state = True
            self.stop_camera()
            self.off()
        self.display_image()

    def display_image(self):
        qformat = QImage.Format_Indexed8
        if self.image is not None:
            if len(self.image.shape) == 3:
                if self.image.shape[2] == 4:
                    qformat = QImage.Format_RGBA8888
                else:
                    qformat = QImage.Format_RGB888
            out_image = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat)
            out_image = out_image.rgbSwapped()
            self.label_2.setPixmap(QPixmap.fromImage(out_image))
            self.label_2.setScaledContents(True)

    def off(self):
        self.camera.release()
        self.close()

    def closeEvent(self, event):
        if self.sender() == self.exitButton or self.auth_state:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    auth = Auth2()
    auth.show()
    sys.exit(app.exec_())
