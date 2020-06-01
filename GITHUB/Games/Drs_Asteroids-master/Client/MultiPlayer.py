import sys
from datetime import datetime
from multiprocessing import Process

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QComboBox, QMessageBox

from AsteroidsGame import AsteroidsGame
from ClientGame import ClientAsteroidsGame
from core.utils.image_helper import get_full_image_path
from entities.PlayerInput import PlayerInput
from Communication.Server import Server


def _start_game_process(player1_input, player2_input, title="Multi Player") -> str:
    process = Process(target=_start_game, args=(player1_input.player_id, player1_input.color,
                                                player2_input.player_id, player2_input.color,
                                                title))
    process.daemon = True
    process.start()


def _start_game(player1_id, player1_color, player2_id, player2_color, title="Multi Player"):
    app = QApplication(sys.argv)
    game = AsteroidsGame(
        player_inputs=[
            PlayerInput(player_id=player1_id, color=player1_color),
            PlayerInput(player_id=player2_id, color=player2_color)
        ], title=title)
    game.start()
    sys.exit(app.exec_())


class MultiPlayerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 1000, 600)
        self.setWindowTitle("MultiPlayer")
        self.initUI()

    def initUI(self):
        self.initWindow()
        self.username()
        self.chooseShip()
        self.labels()
        self.buttonPlay()
        self.buttonCreateOnline()
        self.buttonConnect()

    def initWindow(self):
        self.BackGround = QPixmap(get_full_image_path("galaxy.jpg"))
        self.BackGroundLabel = QtWidgets.QLabel(self)
        self.BackGroundLabel.setPixmap(self.BackGround)
        self.BackGroundLabel.setGeometry(0, 0, 1000, 600)

    def username(self):
        self.lbl2 = QtWidgets.QLabel(self)
        self.lbl2.setText("Enter name")
        self.lbl2.setGeometry(200, 150, 200, 50)
        self.lbl2.setStyleSheet(" color: white;font-size: 26px; font-family: Arial Black;");

        self.player1NameLineEdit = QLineEdit(self)
        self.player1NameLineEdit.setGeometry(200, 200, 200, 50)
        self.player2NameLineEdit = QLineEdit(self)
        self.player2NameLineEdit.setGeometry(200, 300, 200, 50)

    def chooseShip(self):
        self.lbl2 = QLabel(self)
        self.lbl2.setText("Choose ship")
        self.lbl2.setGeometry(410, 150, 200, 50)
        self.lbl2.setStyleSheet(" color: white;font-size: 26px; font-family: Arial Black;");

        self.player1Cb = QComboBox(self)
        self.player1Cb.setStyleSheet(
            "border:1px solid rgb(220, 20, 60);font-size: 20px; color: red; font-family: Helvetica;");
        self.player1Cb.addItem("")
        self.player1Cb.addItem("red")
        self.player1Cb.addItem("green")
        self.player1Cb.addItem("yellow")
        self.player1Cb.addItem("blue")
        self.player1Cb.model().item(0).setEnabled(False)
        self.player1Cb.setGeometry(410, 200, 200, 50)

        self.player2Cb = QComboBox(self)
        self.player2Cb.setStyleSheet(
            "border:1px solid rgb(220, 20, 60);font-size: 20px; color: red; font-family: Helvetica;");
        self.player2Cb.addItem("")
        self.player2Cb.addItem("red")
        self.player2Cb.addItem("green")
        self.player2Cb.addItem("yellow")
        self.player2Cb.addItem("blue")
        self.player2Cb.model().item(0).setEnabled(False)
        self.player2Cb.setGeometry(410, 300, 200, 50)

    def labels(self):
        self.lbl3 = QtWidgets.QLabel(self)
        self.lbl3.setText("First player")
        self.lbl3.setGeometry(10, 200, 200, 50)
        self.lbl3.setStyleSheet(" color: red;font-size: 20px; font-family: Arial ;");

        self.lbl4 = QtWidgets.QLabel(self)
        self.lbl4.setText("Second player")
        self.lbl4.setGeometry(10, 300, 200, 50)
        self.lbl4.setStyleSheet(" color: red;font-size: 20px; font-family: Arial ;");

    def buttonPlay(self):
        self.playButton = QtWidgets.QPushButton(self)
        self.playButton.setText("PLAY LOCAL")
        self.playButton.setGeometry(750, 400, 200, 50)
        self.playButton.setStyleSheet(
            "border:2px solid rgb(120, 20, 60); color: blue;font-size: 26px; font-family: Arial Black;");
        self.playButton.clicked.connect(self.onPlayButtonClicked)

    def buttonCreateOnline(self):
        self.onlineButton = QtWidgets.QPushButton(self)
        self.onlineButton.setText("CREATE GAME")
        self.onlineButton.setGeometry(750, 300, 200, 50)
        self.onlineButton.setStyleSheet(
            "border:2px solid rgb(120, 20, 60); color: blue;font-size: 22px; font-family: Arial Black;");
        self.onlineButton.clicked.connect(self.onCreateButtonClicked)

    def buttonConnect(self):
        self.connectButton = QtWidgets.QPushButton(self)
        self.connectButton.setText("JOIN GAME")
        self.connectButton.setGeometry(750, 350, 200, 50)
        self.connectButton.setStyleSheet(
            "border:2px solid rgb(120, 20, 60); color: blue;font-size: 26px; font-family: Arial Black;");

    def onPlayButtonClicked(self):
        if self.player1NameLineEdit.text() == "" or self.player2NameLineEdit.text() == "" or str(
                self.player1Cb.currentText()) == "" or str(self.player2Cb.currentText()) == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.NoIcon)
            msg.setText("Enter your username and choose ship")
            msg.setWindowTitle("Error")
            msg.exec_()

        elif self.player1NameLineEdit.text() == self.player2NameLineEdit.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.NoIcon)
            msg.setText("Username must be unique")
            msg.setWindowTitle("Error")
            msg.exec_()

        else:

            player1_input = PlayerInput(player_id=self.player1NameLineEdit.text(), color=self.player1Cb.currentText())
            player2_input = PlayerInput(player_id=self.player2NameLineEdit.text(), color=self.player2Cb.currentText())

            _start_game_process(player1_input, player2_input, title="Asteroids - Multi Player")
            self.hide()
            self.player1NameLineEdit.setText("")
            self.player2NameLineEdit.setText("")


    def onCreateButtonClicked(self):
        if self.player1NameLineEdit.text() == "" or str(self.player1Cb.currentText()) == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.NoIcon)
            msg.setText("Enter your username and choose ship")
            msg.setWindowTitle("Error")
            msg.exec_()

        else:
            player1_input = PlayerInput(player_id=self.player1NameLineEdit.text(), color=self.player1Cb.currentText())

            self.server = Server(5)

            self.game = ClientAsteroidsGame('seed', player_inputs=[player1_input], title="Asteroids - Client")
            self.game.start()


def wi():
    app = QApplication(sys.argv)
    win = MultiPlayerWindow()

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    wi()
