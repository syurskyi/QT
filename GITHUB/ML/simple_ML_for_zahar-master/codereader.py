import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog
from codereader_d import Ui_Dialog
from PyQt5.QtCore import QTimer
from frame_editor import FrameEditor
import cv2


class CodeReader(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.running = True
        self.info_product = None
        self.timer = QTimer(self)
        self.image = None
        self.pushButton.clicked.connect(self.off)
        self.camera = cv2.VideoCapture(0)
        self.start_camera()

    def start_camera(self):
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1)

    def stop_camera(self):
        self.timer.stop()

    def update_frame(self):
        _, self.image = self.camera.read()
        result = FrameEditor(self.image, "product").returnframe()
        if result:
            self.info_product = result
            self.stop_camera()
            self.off()
        self.display_image()

    def display_image(self):
        if self.image is not None:
            qformat = QImage.Format_Indexed8
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
        if self.sender() == self.pushButton or self.info_product:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    reader = CodeReader()
    reader.show()
    sys.exit(app.exec_())
