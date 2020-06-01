import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

from Client.MultiPlayer import MultiPlayerWindow
from Client.SinglePlayer import SinglePlayerWindow
from Client.Tournament import TournamentWindow
from Client.Scores import ScoreWindow
from core.utils.image_helper import get_full_image_path


class MyWindow(QMainWindow):
    def __init__(self,scoreFilePath):
        super().__init__()
        self.setGeometry(200, 200, 1000, 600)
        self.setWindowTitle("Menu")
        self.scoreFilePath =scoreFilePath
        self.initUI()

    def initUI(self):
        self.initWindow()
        self.Buttons()

    def Buttons(self):
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("START GAME")
        self.b1.setGeometry(400, 100, 250, 50)
        self.b1.setStyleSheet(
            "border:2px solid rgb(120, 20, 60); color: blue;font-size: 26px; font-family: Arial Black;");
        self.b1.clicked.connect(self.on_push_button)
        self.dialog = SinglePlayerWindow()

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("MULTIPLAYER")
        self.b2.setGeometry(400, 200, 250, 50)
        self.b2.setStyleSheet(
            "border:2px solid rgb(120, 20, 60); color: blue;font-size: 26px; font-family: Arial Black;");
        self.b2.clicked.connect(self.on_push_button2)
        self.dialog2 = MultiPlayerWindow()

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("TOURNAMENT")
        self.b2.setGeometry(400, 300, 250, 50)
        self.b2.setStyleSheet(
            "border:2px solid rgb(120, 20, 60); color: blue;font-size: 26px; font-family: Arial Black;");
        self.b2.clicked.connect(self.on_push_button3)
        self.dialog3 = TournamentWindow()

        self.b23 = QtWidgets.QPushButton(self)
        self.b23.setText("SCORE")
        self.b23.setGeometry(400, 400, 250, 50)
        self.b23.setStyleSheet(
            "border:2px solid rgb(120, 20, 60); color: blue;font-size: 26px; font-family: Arial Black;");
        self.b23.clicked.connect(self.on_push_button4)
        self.dialog4 = ScoreWindow(scoreFilePath=self.scoreFilePath)

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("EXIT")
        self.b3.setGeometry(400, 500, 250, 50)
        self.b3.setStyleSheet(
            "border:2px solid rgb(120, 20, 60); color: blue;font-size: 26px; font-family: Arial Black;");
        self.b3.clicked.connect(self.quit)

    def on_push_button(self):
        self.dialog.show()

    def on_push_button2(self):
        self.dialog2.show()

    def on_push_button3(self):
        self.dialog3.show()

    def on_push_button4(self):
        self.dialog4.show()

    def initWindow(self):
        self.BackGround = QPixmap(get_full_image_path("galaxy.jpg"))
        self.BackGroundLabel = QtWidgets.QLabel(self)
        self.BackGroundLabel.setPixmap(self.BackGround)
        self.BackGroundLabel.setGeometry(0, 0, 1000, 600)

    def quit(self):
        app = QApplication.instance()
        app.closeAllWindows()


def display_menu(scoreFilePath):
    app = QApplication(sys.argv)
    win = MyWindow(scoreFilePath)

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    display_menu("../test.txt")
