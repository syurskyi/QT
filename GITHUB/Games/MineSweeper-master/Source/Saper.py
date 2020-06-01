from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist
from PyQt5 import QtGui
from Source.Logic import Logic
from Source.Menu import Menu
from Source import globals
from Source.Signals import Signals
from Source.Music import Music
import sys


class Window(QMainWindow):
    def __init__(self, signals):
        super().__init__()
        __menu = Menu(self, signals)
        __central_widget = QWidget()

        self.__signals = signals
        self.keys_order = 0  # I need that to notice a keyboard sequences(xyzzy)
        self.__game = Logic(__central_widget, self.__signals)
        self.setCentralWidget(__central_widget)
        self.properties()

    def properties(self):
        self.setWindowTitle('MineSweeper')
        self.setWindowIcon(QtGui.QIcon('../Images/window_icon.jpg'))
        self.setMaximumSize(540, 440)
        self.show()

    def closeEvent(self, event):
        self.__signals.stop_music.emit()
        answer = QMessageBox.question(QMessageBox(), "Message", "Do you really close the program?")
        if answer == QMessageBox.Yes:
            globals.save_values()
            # here in future can be a function to save game and sb can return to old game,
            # its will be great idea but that idea need work and new function in Board()
            event.accept()
        else:
            self.__signals.play_music.emit()
            event.ignore()

    def keyPressEvent(self, e):     # if user pass in right order 'xyzzy' bomb fields will cloud, 'r' return color
        if not globals.game_pause:
            if e.key() == Qt.Key_X:
                self.keys_order = 1
            elif e.key() == Qt.Key_Y and self.keys_order == 1:
                self.keys_order += 1
            elif e.key() == Qt.Key_Z and (self.keys_order == 2 or self.keys_order == 3):
                self.keys_order += 1
            elif e.key() == Qt.Key_Y and self.keys_order == 4:
                self.keys_order = 0
                self.__signals.cloud_bombs.emit()
            elif e.key() == Qt.Key_R and not globals.game_over:
                self.__signals.uncloud_bombs.emit()
            else:
                self.keys_order = 0


if __name__ == '__main__':
    globals.initialize()
    __signals = Signals()
    app = QApplication(sys.argv)
    window = Window(__signals)
    playlist = QMediaPlaylist()
    player = QMediaPlayer()
    playlist.currentIndex()
    music = Music(playlist, player, __signals)
    music.play_music()
    sys.exit(app.exec())
