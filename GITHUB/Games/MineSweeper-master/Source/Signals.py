from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtCore


class Signals(QObject):
    set_buttons = QtCore.pyqtSignal()
    cloud_bombs = QtCore.pyqtSignal()
    uncloud_bombs = QtCore.pyqtSignal()
    update_bombs_display = QtCore.pyqtSignal()
    update_time_display = QtCore.pyqtSignal()
    pause = QtCore.pyqtSignal()
    loose = QtCore.pyqtSignal()
    win = QtCore.pyqtSignal()
    stop_music = QtCore.pyqtSignal()
    play_music = QtCore.pyqtSignal()
    add_music = QtCore.pyqtSignal()
    delete_music = QtCore.pyqtSignal()
    hide_question_marks = QtCore.pyqtSignal()

    def __init__(self):
        QObject.__init__(self)

    @staticmethod
    def reconnect(signal, signal_call):
        while True:
            try:
                if signal_call is not None:
                    signal.disconnect(signal_call)
                else:
                    signal.disconnect()
            except TypeError:
                break
