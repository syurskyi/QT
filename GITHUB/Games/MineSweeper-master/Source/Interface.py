from PyQt5.QtWidgets import QWidget, QMessageBox, QVBoxLayout
from Source.SettingsInterface import SettingsInterface
from Source.BoardInterface import BoardInterface
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl
from Source import globals
import time


class Interface:
    def __init__(self, variable, central_widget, signals):
        self.central_widget = central_widget
        self.variable = variable
        self.signals = signals
        self.signals.loose.connect(self.loose)
        self.signals.win.connect(self.win)
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(10)
        self.create_settings_layout(variable)
        central_widget.setLayout(self.main_layout)

    def create_settings_layout(self, variable):
        self.__settings = SettingsInterface(variable, self.signals)
        self.main_layout.addLayout(self.__settings.layout())

    def create_board_layout(self, variable):
        self.__board = BoardInterface(variable)
        self.__board_layout = self.__board.layout()

        self.main_layout.addLayout(self.__board_layout)
        self.main_layout.addStretch()

    def get_board_layout(self):
        return self.__board_layout

    def clear_board_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clear_board_layout(item.layout())

    def win(self):
        # In future I can create win() in Logic() and save result to data base.
        # Important: 2 rankings!(with users who used pause and others users who play without pause
         __win_statement = QMessageBox.question(QMessageBox(), "You win!!", "You win!!!\nYour time: {}".format(globals.time), QMessageBox.Ok)

    def loose(self):
        if globals.loose_animation:
            video = QVideoWidget()
            video.resize(500, 400)
            video.setWindowTitle("GAME OVER")
            player = QMediaPlayer()
            player.setVideoOutput(video)
            player.setMedia(QMediaContent(QUrl.fromLocalFile("../Video/bum.gif")))
            video.show()
            player.play()
            self.signals.add_music.emit()
            time.sleep(5.5)
            self.signals.delete_music.emit()
            player.stop()
            video.close()
        else:
            __loose_statement = QMessageBox.question(QMessageBox(), "GAME OVER!!", "You loose!!!\nYour time: {}".format(globals.time), QMessageBox.Ok)
