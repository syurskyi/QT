from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot, QTimer, Qt

import time
import config


class KeyNotifier(QObject):

    key_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()

        self.keys = []
        self.is_done = False

        self.canPlayerOneShoot = False
        self.canPlayerTwoShoot = False
        self.cooldownTimer = QTimer()
        self.cooldownTimer.setInterval(config.PLAYER_LASER_COOLDOWN)
        self.cooldownTimer.timeout.connect(self.alert_cooldown)
        self.cooldownTimer.start()

        self.thread = QThread()
        # move the Worker object to the Thread object
        # "push" self from the current thread to this thread
        self.moveToThread(self.thread)
        # Connect Thread started signal to Worker operational slot method
        self.thread.started.connect(self.__work__)

    def start(self):
        """
        Start notifications.
        """
        self.thread.start()

    def add_key(self, key):
        self.keys.append(key)

    def rem_key(self, key):
        self.keys.remove(key)

    def die(self):
        """
        End notifications.
        """
        self.is_done = True
        self.thread.quit()

    def alert_cooldown(self):
        if not self.canPlayerOneShoot:
            self.canPlayerOneShoot = True
        if not self.canPlayerTwoShoot:
            self.canPlayerTwoShoot = True

    @pyqtSlot()
    def __work__(self):
        """
        A slot with no params.
        """
        while not self.is_done:

            for k in self.keys:

                if k == Qt.Key_Space:
                    if self.canPlayerOneShoot:
                        self.key_signal.emit(k)
                        self.canPlayerOneShoot = False

                elif k == Qt.Key_0:
                    if self.canPlayerTwoShoot:
                        self.key_signal.emit(k)
                        self.canPlayerTwoShoot = False
                else:
                    self.key_signal.emit(k)
            time.sleep(0.05)
