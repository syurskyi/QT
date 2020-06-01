import sys
import time

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog

from voice_handler_d import Ui_Dialog
from wav_recorder import record, CHUNK, FORMAT, CHANNELS, RATE


class VoiceHandler(QDialog, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.off)
        self.pushButton_2.clicked.connect(self.recording)

    def recording(self):
        record("data/voice/voice_{}.wav".format(int(time.time())))
        self.off()

    def off(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    voice = VoiceHandler()
    voice.show()
    sys.exit(app.exec_())
