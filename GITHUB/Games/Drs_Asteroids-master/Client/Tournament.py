import sys
from threading import Thread

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QComboBox, QMessageBox

from AsteroidTournament import start_tournament
from core.utils.image_helper import get_full_image_path
from entities.PlayerInput import PlayerInput


class TournamentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.winner = None
        self.setGeometry(200, 200, 1000, 600)
        self.setWindowTitle("Tournament")
        self.initUI()

    def initUI(self):
        self.initWindow()
        self.username()
        self.chooseShip()
        self.labels()
        self.buttonPlay()

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
        self.player3NameLineEdit = QLineEdit(self)
        self.player3NameLineEdit.setGeometry(200, 400, 200, 50)
        self.player4NameLineEdit = QLineEdit(self)
        self.player4NameLineEdit.setGeometry(200, 500, 200, 50)

    def chooseShip(self):
        self.lbl2 = QLabel(self)
        self.lbl2.setText("Choose ship")
        self.lbl2.setGeometry(410, 150, 200, 50)
        self.lbl2.setStyleSheet(" color: white;font-size: 26px; font-family: Arial Black;") ;

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

        self.player3Cb = QComboBox(self)
        self.player3Cb.setStyleSheet(
            "border:1px solid rgb(220, 20, 60);font-size: 20px; color: red; font-family: Helvetica;");
        self.player3Cb.addItem("")
        self.player3Cb.addItem("red")
        self.player3Cb.addItem("green")
        self.player3Cb.addItem("yellow")
        self.player3Cb.addItem("blue")
        self.player3Cb.model().item(0).setEnabled(False)
        self.player3Cb.setGeometry(410, 400, 200, 50)

        self.player4Cb = QComboBox(self)
        self.player4Cb.setStyleSheet(
            "border:1px solid rgb(220, 20, 60);font-size: 20px; color: red; font-family: Helvetica;");
        self.player4Cb.addItem("")
        self.player4Cb.addItem("red")
        self.player4Cb.addItem("green")
        self.player4Cb.addItem("yellow")
        self.player4Cb.addItem("blue")
        self.player4Cb.model().item(0).setEnabled(False)
        self.player4Cb.setGeometry(410, 500, 200, 50)

    def labels(self):
        self.lbl3 = QtWidgets.QLabel(self)
        self.lbl3.setText("First player")
        self.lbl3.setGeometry(10, 200, 200, 50)
        self.lbl3.setStyleSheet(" color: red;font-size: 20px; font-family: Arial ;");

        self.lbl4 = QtWidgets.QLabel(self)
        self.lbl4.setText("Second player")
        self.lbl4.setGeometry(10, 300, 200, 50)
        self.lbl4.setStyleSheet(" color: red;font-size: 20px; font-family: Arial ;");

        self.lbl5 = QtWidgets.QLabel(self)
        self.lbl5.setText("Third player")
        self.lbl5.setGeometry(10, 400, 200, 50)
        self.lbl5.setStyleSheet(" color: red;font-size: 20px; font-family: Arial ;");

        self.lbl6 = QtWidgets.QLabel(self)
        self.lbl6.setText("Fourth player")
        self.lbl6.setGeometry(10, 500, 200, 50)
        self.lbl6.setStyleSheet(" color: red;font-size: 20px; font-family: Arial ;");

    def buttonPlay(self):
        self.playButton = QtWidgets.QPushButton(self)
        self.playButton.setText("PLAY")
        self.playButton.setGeometry(750, 400, 200, 50)
        self.playButton.setStyleSheet(
            "border:2px solid rgb(120, 20, 60); color: blue;font-size: 26px; font-family: Arial Black;");
        self.playButton.clicked.connect(self.onPlayButtonClicked)

    def onPlayButtonClicked(self):
        if self.player1NameLineEdit.text() == "" or self.player2NameLineEdit.text() == "" \
                or self.player3NameLineEdit.text() == "" or self.player4NameLineEdit.text() == "" \
                or str(self.player1Cb.currentText()) == "" or str(self.player2Cb.currentText()) == "" \
                or str(self.player3Cb.currentText()) == "" or str(self.player4Cb.currentText()) == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.NoIcon)
            msg.setText("Enter your username and choose ship")
            msg.setWindowTitle("Error")
            msg.exec_()

        elif self.player1NameLineEdit.text() == self.player2NameLineEdit.text() \
                or self.player1NameLineEdit.text() == self.player3NameLineEdit.text() \
                or self.player1NameLineEdit.text() == self.player4NameLineEdit.text() \
                or self.player2NameLineEdit.text() == self.player3NameLineEdit.text() \
                or self.player2NameLineEdit.text() == self.player4NameLineEdit.text() \
                or self.player3NameLineEdit.text() == self.player4NameLineEdit.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.NoIcon)
            msg.setText("Username must be unique")
            msg.setWindowTitle("Error")
            msg.exec_()

        else:
            player1_input = PlayerInput(player_id=self.player1NameLineEdit.text(), color=self.player1Cb.currentText())
            player2_input = PlayerInput(player_id=self.player2NameLineEdit.text(), color=self.player2Cb.currentText())
            player3_input = PlayerInput(player_id=self.player3NameLineEdit.text(), color=self.player3Cb.currentText())
            player4_input = PlayerInput(player_id=self.player4NameLineEdit.text(), color=self.player4Cb.currentText())

            thread = Thread(target=start_tournament, args=(player1_input, player2_input, player3_input, player4_input))
            thread.daemon = True
            thread.start()
            self.hide()
            self.player1NameLineEdit.setText("")
            self.player2NameLineEdit.setText("")
            self.player3NameLineEdit.setText("")
            self.player4NameLineEdit.setText("")


def wi():
    app = QApplication(sys.argv)
    win = TournamentWindow()

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    wi()
