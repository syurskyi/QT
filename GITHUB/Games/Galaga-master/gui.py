from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QStackedWidget, QWidget, QPushButton, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal
import game
import config
import sys
from key_notifier import KeyNotifier


class GameWindow(QMainWindow):

    startAgain = pyqtSignal()

    def __init__(self):
        super().__init__()

        print('Started new game window')

        self.game = None
        self.centralWidget = QStackedWidget()
        self.setCentralWidget(self.centralWidget)
        self.mainMenuWidget = MainMenu()
        self.menu()

        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.do_key_press)
        self.key_notifier.start()

        self.setWindowTitle('Galaga')
        self.setWindowIcon(QIcon('images/ship.png'))
        self.show()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def menu(self):
        self.mainMenuWidget.playOnePlayerGameSignal.connect(self.playOnePlayerGame)
        self.mainMenuWidget.playTwoPlayerGameSignal.connect(self.playTwoPlayersGame)
        self.mainMenuWidget.quitGameSignal.connect(self.quit)

        self.centralWidget.addWidget(self.mainMenuWidget)
        self.centralWidget.setCurrentWidget(self.mainMenuWidget)

        self.resize(240, 250)
        self.center()

    def playOnePlayerGame(self):
        self.resize(config.BOARD_WIDTH, config.BOARD_HEIGHT)
        self.center()
        self.game = game.Game(1)
        self.game.gameOverSignal.connect(self.gameOver)
        self.setCentralWidget(self.game)

    def playTwoPlayersGame(self):
        self.resize(config.BOARD_WIDTH, config.BOARD_HEIGHT)
        self.center()
        self.game = game.Game(2)
        self.game.gameOverSignal.connect(self.gameOver)
        self.setCentralWidget(self.game)

    def gameOver(self):
        print('GAME IS OVER')

        self.startAgain.emit()

    def do_key_press(self, key):
        try:
            self.game.__update_position__(key)
        except Exception as e:
            print('Exception: {}'.format(str(e)))

    def keyPressEvent(self, event):
        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        self.key_notifier.rem_key(event.key())

    def quit(self):
        sys.exit()

    def stopThreads(self):
        try:
            print('Closing all threads from Galagaa')
            if self.game is not None:
                self.game.shootLaser.die()
                self.game.moveEnemy.die()
                self.game.enemyShoot.die()
                self.game.enemyAttack.die()
                self.game.deusExMachina.die()
            self.key_notifier.die()
        except Exception as e:
            print('Exception while trying to close threads: {}', str(e))

    def closeEvent(self, event):
        try:
            if self.game is not None:
                self.game.shootLaser.die()
                self.game.moveEnemy.die()
                self.game.enemyShoot.die()
                self.game.enemyAttack.die()
                self.game.deusExMachina.die()
            self.key_notifier.die()
        except Exception as e:
            print('Exception while trying to close threads: {}', str(e))

        sys.exit()


class MainMenu(QWidget):

    playOnePlayerGameSignal = pyqtSignal()
    playTwoPlayerGameSignal = pyqtSignal()
    quitGameSignal = pyqtSignal()

    def __init__(self):
        super(MainMenu, self).__init__()

        button_width = 190
        button_height = 50
        button_offset = 25

        play_button = QPushButton('One Player', self)
        play_button.setFixedWidth(button_width)
        play_button.setFixedHeight(button_height)
        play_button.move(button_offset, (button_offset * 1) + (button_height * 0))
        play_button.clicked.connect(self.playOnePlayer)

        play_twoplayers_button = QPushButton('Two Players', self)
        play_twoplayers_button.setFixedWidth(button_width)
        play_twoplayers_button.setFixedHeight(button_height)
        play_twoplayers_button.move(button_offset, (button_offset * 2) + (button_height * 1))
        play_twoplayers_button.clicked.connect(self.playTwoPlayers)

        quit_button = QPushButton('Quit', self)
        quit_button.setFixedWidth(button_width)
        quit_button.setFixedHeight(button_height)
        quit_button.move(button_offset, (button_offset * 3) + (button_height * 2))
        quit_button.clicked.connect(self.quit)

        self.show()

    def playOnePlayer(self):
        self.playOnePlayerGameSignal.emit()

    def playTwoPlayers(self):
        self.playTwoPlayerGameSignal.emit()

    def quit(self):
        self.quitGameSignal.emit()
