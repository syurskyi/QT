""" 
    Batteships game. Basics of IT semester project.
    Author: Piotr Kucharski 
"""

from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap, QFont
from PyQt5.QtMultimedia import QSound

from random import randint, seed

import label

class Window(QMainWindow):
    """Defines main window of the game."""

    def __init__(self):
        super().__init__()
        self.__init_ui()

        # Show new window
        self.show()

        # Play background music
        self.music = QSound("res/sound/setting_field2.wav")
        self.music.play()

        # Prevent from resizing
        self.setFixedSize(self.size())

        # Variable determinates if all things are done to be rady to play
        self.canStart = False

        # Set up random generator
        seed()

    def __init_ui(self):
        """Sets an ui for a game.

        size = 800x600
        position = 200, 200
        background = backgroundPE.png
        music while setting field: setting_field1.wav
        music while playing: gameplay.wav
        """

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle("Battleships")
        self.setWindowIcon(QIcon("res/pictures/icon.png"))

        # Setting background
        background = QPalette()
        background.setBrush(QPalette.Background, QBrush(QPixmap("res/pictures/backgroundPE.png")))
        self.setPalette(background)

        # Setting player's field
        self.playerFieldLabel = label.Label(self, "Player")
        self.playerFieldLabel.setGeometry(50, 50, 295, 295)

        # Set player's target field
        self.targetFieldLabel = label.Label(self, "Enemy")
        self.targetFieldLabel.setGeometry(455, 50, 295, 295)

        # Add a label which shows information to player
        self.informativeLabel = QLabel(self)
        self.informativeLabel.setFont(QFont("MutantAcademyBB", 30))    # 54
        self.informativeLabel.setStyleSheet('color: white')
        self.informativeLabel.setText("Click on your field to place the ship")
        self.informativeLabel.setGeometry(20, 500, 800, 90)

        # Add a label which tells in-game informations
        self.inGameLabel = QLabel(self)
        self.inGameLabel.setFont(QFont("Capture It", 25))
        self.inGameLabel.setStyleSheet('color: pink')
        self.inGameLabel.setText("Ships to be placed: 10")
        self.inGameLabel.setGeometry(37, 400, 600, 90)

        # Add 'ready' button - it starts the game with ToolTip
        self.readyButton = QPushButton("Ready", self)
        self.readyButton.setToolTip("Click this button once you set up the ships")
        self.readyButton.resize(self.readyButton.sizeHint())
        self.readyButton.move(360, 2)
        self.readyButton.clicked.connect(self.startGame)

        # Add which ship is being placed
        self.whichShipLabel = QLabel(self)
        self.whichShipLabel.setFont(QFont("Tahoma", 25))
        self.whichShipLabel.setGeometry(520, 400, 300, 90)
        self.whichShipLabel.setStyleSheet('color: red')
        self.whichShipLabel.setText("%d-mast ship" % self.playerFieldLabel.hp)

    def startGame(self):
        if len(self.playerFieldLabel.gameField.ships) == 10:
            self.playerFieldLabel.isGame = True
            self.playerFieldLabel.canUserClick = False
            self.targetFieldLabel.isGame = True
            self.informativeLabel.setText("Shoot to opponent's field\nShips left: %d" % len(self.playerFieldLabel.gameField.ships))
            self.music.stop()
            self.music = QSound("res/sound/gameplay_lel.wav")
            self.music.setLoops(100)
            self.music.play()
            self.readyButton.setText("Playing...")
            self.readyButton.setToolTip("The game is in progress.")
            self.readyButton.setDisabled(True)
            self.inGameLabel.setText("")

    def ai_shoot(self):
        """Method defined for automatic shooting for ai - uses self.playerFieldLabel"""

        self.shoot_x = randint(0, 9)
        self.shoot_y = randint(0, 9)
        self.isHit = False

        result = self.playerFieldLabel.shoot_to_field(self.shoot_x, self.shoot_y)
        # if ai hits - shoot around that place
        if result == True:
            self.isHit = True
            direction = randint(0, 3)

            if direction == 0:
                while self.isHit != False:
                    self.shoot_x += 1
                    self.isHit = self.playerFieldLabel.shoot_to_field(self.shoot_x, self.shoot_y)

            elif direction == 1:
                while self.isHit != False:
                    self.shoot_x -= 1
                    self.isHit = self.playerFieldLabel.shoot_to_field(self.shoot_x, self.shoot_y)

            elif direction == 2:
                while self.isHit != False:
                    self.shoot_y += 1
                    self.isHit = self.playerFieldLabel.shoot_to_field(self.shoot_x, self.shoot_y)

            elif direction == 3:
                while self.isHit != False:
                    self.shoot_y -= 1
                    self.isHit = self.playerFieldLabel.shoot_to_field(self.shoot_x, self.shoot_y)

            del direction

        elif result == None:
            self.ai_shoot()

    def end_game(self, winner):
        if winner == "Player":
            self.music.stop()
            self.music = QSound("res/sound/victory.wav")
            self.music.play()

            self.informativeLabel.setStyleSheet("color: yellow")
            self.informativeLabel.setFont(QFont("MutantAcademyBB", 41))
            self.informativeLabel.setText("Congratulations! Victory!")
            self.informativeLabel.setDisabled(True)
            self.targetFieldLabel.canUserClick = False
            self.targetFieldLabel.setDisabled(True)


        elif winner == "Enemy":
            self.music.stop()
            self.music = QSound("res/sound/loss.wav")
            self.music.play()

            self.targetFieldLabel.canUserClick = False
            self.informativeLabel.setStyleSheet('color: red')
            self.informativeLabel.setFont(QFont("MutantAcademyBB", 53))
            self.informativeLabel.setText("You lose. Game over.")
            self.informativeLabel.setDisabled(True)
            self.playerFieldLabel.setDisabled(True)

        self.readyButton.setText("Exit")
        self.readyButton.setToolTip("Click this button to exit the game.")
        self.readyButton.clicked.connect(self.close)
        self.readyButton.setDisabled(False)
        self.targetFieldLabel.canTextEdit = False
        self.playerFieldLabel.canTextEdit = False