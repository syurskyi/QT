from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QPushButton, QSizePolicy, QGridLayout
from PyQt5.QtWidgets import QMainWindow

from core.utils.image_helper import get_full_image_path


class Screen(QMainWindow):
    keyPressed = QtCore.pyqtSignal(int)

    def __init__(self, screen_width: int = 1000, screen_height: int = 600, name: str = "Asteroids"):
        super().__init__()
        self.resize(screen_width, screen_height)

        # self.setGeometry(200, 200, 200 + x, 200 + y)
        self.setWindowTitle(name)

        self.BackGround = QPixmap(get_full_image_path("galaxy.jpg"))
        self.BackGroundLabel = QtWidgets.QLabel(self)
        self.BackGroundLabel.setPixmap(self.BackGround)
        self.BackGroundLabel.setGeometry(0, 0, screen_width, screen_height)

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        self.keyPressed.emit(event.key())

    def display_winner(self, winner, on_end):
        self._label = QtWidgets.QLabel(self)
        self._label.setText(f"WINNER: {winner.player_id}")
        self._label.setGeometry(400, 100, 250, 50)
        self._label.setStyleSheet("color: white; font-size: 26px; font-family: Arial Black;")
        self._label.show()

        self._btn = QtWidgets.QPushButton("OK", self)
        self._btn.clicked.connect(on_end)
        self._btn.setGeometry(400, 200, 80, 30)
        self._btn.setStyleSheet("color: black; font-size: 18px; font-family: Arial Black;")
        self._btn.show()
