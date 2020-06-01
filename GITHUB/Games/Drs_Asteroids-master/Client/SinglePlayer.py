import sys
from multiprocessing import Process

from AsteroidsGame import AsteroidsGame
from entities.PlayerInput import PlayerInput

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QComboBox, QMessageBox

from core.utils.image_helper import get_full_image_path


def _start_game_process(player1_input, title="Single Player") -> str:
    process = Process(target=_start_game, args=(player1_input.player_id, player1_input.color,
                                                title))
    process.daemon = True
    process.start()


def _start_game(player1_id, player1_color, title="Single Player"):
    app = QApplication(sys.argv)
    game = AsteroidsGame(
        player_inputs=[
            PlayerInput(player_id=player1_id, color=player1_color)
        ], title=title)
    game.start()
    sys.exit(app.exec_())


class SinglePlayerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 1000, 600)
        self.setWindowTitle("OnePlayer")
        self.initUI()

    def initUI(self):
        self.initWindow()
        self.username()
        self.chooseShip()
        self.buttonPlay()

    def initWindow(self):
        self.BackGround = QPixmap(get_full_image_path("galaxy.jpg"))
        self.BackGroundLabel = QtWidgets.QLabel(self)
        self.BackGroundLabel.setPixmap(self.BackGround)
        self.BackGroundLabel.setGeometry(0, 0, 1000, 600)

    def username(self):
        self.enterNameLabel = QtWidgets.QLabel(self)
        self.enterNameLabel.setText("Enter name")
        self.enterNameLabel.setGeometry(200, 150, 200, 50)
        self.enterNameLabel.setStyleSheet(" color: white;font-size: 26px; font-family: Arial Black;");

        self.player1NameLineEdit = QLineEdit(self)
        self.player1NameLineEdit.setGeometry(200, 200, 200, 50)

    def chooseShip(self):
        self.choseShipLabel = QLabel(self)
        self.choseShipLabel.setText("Choose ship")
        self.choseShipLabel.setGeometry(410, 150, 200, 50)
        self.choseShipLabel.setStyleSheet(" color: white;font-size: 26px; font-family: Arial Black;");

        self.player1Cb = QComboBox(self)
        self.player1Cb.setStyleSheet("border:1px solid rgb(220, 20, 60); color: red; font-family: Helvetica;");
        self.player1Cb.addItem("")
        self.player1Cb.addItem("red")
        self.player1Cb.addItem("green")
        self.player1Cb.addItem("yellow")
        self.player1Cb.addItem("blue")

        self.player1Cb.model().item(0).setEnabled(False)
        self.player1Cb.setGeometry(410, 200, 200, 50)

    def buttonPlay(self):
        self.playButton = QtWidgets.QPushButton(self)
        self.playButton.setText("PLAY")
        self.playButton.setGeometry(750, 400, 200, 50)
        self.playButton.setStyleSheet(
            "border:2px solid rgb(120, 20, 60); color: blue;font-size: 26px; font-family: Arial Black;")
        self.playButton.clicked.connect(self.onPlayButtonClicked)

    def onPlayButtonClicked(self):
        if self.player1NameLineEdit.text() == "" or str(self.player1Cb.currentText()) == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.NoIcon)
            msg.setText("Enter your username and choose ship")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:

            player1_input = PlayerInput(player_id=self.player1NameLineEdit.text(), color=self.player1Cb.currentText())

            _start_game_process(player1_input, title="Asteroids - SinglePlayer")
            self.hide()
            self.player1NameLineEdit.setText("")


def wi():
    app = QApplication(sys.argv)
    win = SinglePlayerWindow()

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    wi()
