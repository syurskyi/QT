""" 
    Batteships game. Basics of IT semester project.
    Author: Piotr Kucharski 
"""

from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QSound
from random import randint

import ship
import field


class Label(QLabel):
    """Class overwrites QLabel and adds mousePressEvent for adding ships"""

    def __init__(self, window, player):
        super().__init__(window)
        self.iterator = 0
        self.gameField = field.Field()
        self.hp = 4
        self.isSettingDirection = False
        self.newImage = []
        self.iteratorForSettingDirection = 0
        self.isGame = False
        self.sound = QSound("res/sound/shot2.wav", self)
        self.miss_label = []
        self.iteratorForShooting = 0
        self.who = player
        self.Xpos = 0
        self.Ypos = 0
        self.canUserClick = True
        self.canTextEdit = True

        for i in range (0, 10):
            self.newImage.append(QLabel(self))

        for i in range (0, 101):
            self.miss_label.append(QLabel(self))

        self.setPixmap(self.gameField.fieldUI)

        self.ships = []
        for i in range(0, 10):
            self.ships.append(QLabel(self))

        if player == "Enemy":
            self.automatic_setting_field()

    def mousePressEvent(self, event):
        if self.canUserClick != False:
            self.decide_what_to_do(event.x() // 30, event.y() // 30)

        if self.isGame == False:
            if 10 - len(self.gameField.ships) == 0:
                self.window().inGameLabel.setText("Click Ready button to play")
                self.window().whichShipLabel.setText("")
                self.window().informativeLabel.setText("Prepare to battle!")
                return
            else:
                self.window().inGameLabel.setText("Ships to be placed: %d" % (10 - len(self.gameField.ships)))


        if self.isGame == False and self.isSettingDirection == True:
            self.window().informativeLabel.setText("Click in direction of the ship")

        elif self.isGame == False and self.isSettingDirection == False:
            self.window().informativeLabel.setText("Click on your field to place the ship")
            if self.iterator == 1 or self.iterator == 2:
                self.window().whichShipLabel.setText("3-mast ship")
            elif self.iterator >= 3 and self.iterator <= 5:
                self.window().whichShipLabel.setText("2-mast ship")
            else:
                self.window().whichShipLabel.setText("1-mast ship")


        if len(self.gameField.ships) != 0 and self.isGame == True and self.canTextEdit == True:
            self.window().informativeLabel.setText("Shoot to opponent's field\nShips left: %d" % len(self.gameField.ships))


    def add_ship_ui(self, x, y):
        """Meaning of ifs with iterator
        if iterator == 0 - add ship of 4 hp
        if iterator == 1 or iterator == 2 - add ship of 3 hp
        if iterator >= 3 and iterator <= 5 - add ship of 2 hp
        if iterator >= 6 and iterator <= 9 - add ship of 1 hp
         """
        if self.iterator >= 10:
            return 1

        if self.is_ship_placed_correctly(x, y):
            self.Xpos = x * 30
            self.Ypos = y * 30
            self.ships[self.iterator].setGeometry(self.Xpos, self.Ypos, 25, 25)

            if self.gameField.shot[x][y] > -1:
                return -1

            if self.iterator == 0:
                self.hp = 4
                self.isSettingDirection = True

            elif self.iterator == 1 or self.iterator == 2:
                self.hp = 3
                self.isSettingDirection = True

            elif self.iterator >= 3 and self.iterator <= 5:
                self.hp = 2
                self.isSettingDirection = True

            elif self.iterator >= 6 and self.iterator <= 9:
                self.hp = 1

            self.gameField.ships.append(ship.Ship(x, y, self.hp, self.iterator))
            if self.who == "Player":
                self.ships[self.iterator].setPixmap(self.gameField.ships[self.iterator].shipUI)

            self.gameField.shot[x][y] = self.iterator
            self.lastXY = (x, y)
            self.iterator += 1

        elif self.who == "Enemy":
            self.add_ship_ui(randint(0, 9), randint(0, 9))

    def set_direction(self, x, y):
        self.iterator -= 1

        # Ship's direction is left
        if x < self.lastXY[0]:
            if self.is_ship_placed_correctly(self.lastXY[0] - self.hp + 1, self.lastXY[1]):
                for i in range (1, self.hp):
                    self.gameField.shot[self.lastXY[0] - i][self.lastXY[1]] = self.iterator
                    self.newImage[self.iteratorForSettingDirection].setGeometry(self.Xpos - (30 * i), self.Ypos, 25, 25)
                    if self.who == "Player":
                        self.newImage[self.iteratorForSettingDirection].setPixmap(self.gameField.ships[self.iterator].shipUI)
                    self.iteratorForSettingDirection += 1
                self.isSettingDirection = False
                self.iterator += 1


            elif self.who == "Enemy":
                self.iterator += 1
                self.set_direction(randint(0, 9), randint(0, 9))

            else:
                self.iterator += 1
                if self.who == "Player":
                    self.window().inGameLabel.setText("Cannot place ship like this")

        # Ship's direction is up
        elif y < self.lastXY[1]:
            if self.is_ship_placed_correctly(self.lastXY[0], self.lastXY[1] - self.hp + 1):
                for i in range(1, self.hp):
                    self.gameField.shot[self.lastXY[0]][self.lastXY[1] - i] = self.iterator
                    self.newImage[self.iteratorForSettingDirection].setGeometry(self.Xpos, self.Ypos - (30 * i), 25, 25)
                    if self.who == "Player":
                        self.newImage[self.iteratorForSettingDirection].setPixmap(
                            self.gameField.ships[self.iterator].shipUI)
                    self.iteratorForSettingDirection += 1
                self.isSettingDirection = False
                self.iterator += 1


            elif self.who == "Enemy":
                self.iterator += 1
                self.set_direction(randint(0, 9), randint(0, 9))

            else:
                self.iterator += 1
                if self.who == "Player":
                    self.window().inGameLabel.setText("Cannot place ship like this")

        # Ship's direction is right
        elif x > self.lastXY[0]:
            if self.is_ship_placed_correctly(self.lastXY[0] + self.hp - 1, self.lastXY[1]):
                for i in range(1, self.hp):
                    self.gameField.shot[self.lastXY[0] + i][self.lastXY[1]] = self.iterator
                    self.newImage[self.iteratorForSettingDirection].setGeometry(self.Xpos + (30 * i), self.Ypos, 25, 25)
                    if self.who == "Player":
                        self.newImage[self.iteratorForSettingDirection].setPixmap(self.gameField.ships[self.iterator].shipUI)
                    self.iteratorForSettingDirection += 1
                self.isSettingDirection = False
                self.iterator += 1


            elif self.who == "Enemy":
                self.iterator += 1
                self.set_direction(randint(0, 9), randint(0, 9))

            else:
                self.iterator += 1
                if self.who == "Player":
                    self.window().inGameLabel.setText("Cannot place ship like this")

        # Ship's direction is down
        elif y > self.lastXY[1]:
            if self.is_ship_placed_correctly(self.lastXY[0], self.lastXY[1] + self.hp - 1):
                for i in range(1, self.hp):
                    self.gameField.shot[self.lastXY[0]][self.lastXY[1] + i] = self.iterator
                    self.newImage[self.iteratorForSettingDirection].setGeometry(self.Xpos, self.Ypos + (30 * i), 25, 25)
                    if self.who == "Player":
                        self.newImage[self.iteratorForSettingDirection].setPixmap(self.gameField.ships[self.iterator].shipUI)
                    self.iteratorForSettingDirection += 1
                self.isSettingDirection = False
                self.iterator += 1


            elif self.who == "Enemy":
                self.iterator += 1
                self.set_direction(randint(0, 9), randint(0, 9))

            else:
                self.iterator += 1
                if self.who == "Player":
                    self.window().inGameLabel.setText("Cannot place ship like this")

        else:
            self.iterator += 1

    def automatic_setting_field(self):
        for i in range (0, 20):
            x = randint(0, 9)
            y = randint(0, 9)

            if self.gameField.shot[x][y] == -1:
                self.decide_what_to_do(x, y)

            else:
                i -= 1

    def shoot_to_field(self, x, y):
        if x >= 0 and x <= 9 and y >= 0 and y <= 9:
            if self.gameField.shot[x][y] == 666 or self.gameField.shot[x][y] == 69:
                return None

            if self.gameField.shot[x][y] != -1:
                if self.who == "Enemy":
                    self.window().inGameLabel.setText("")
                self.sound2 = QSound("res/sound/explosion2.wav", self)
                self.sound2.play()

                # Find the ship that was attacked
                i = 0
                for i in range (0, 10):
                    if self.gameField.ships[i].id == self.gameField.shot[x][y]:
                        break

                # Set it's UI to fire
                self.gameField.ships[i].shipUI = QPixmap("res/pictures/fire.png")

                # Change the pixmap (decide if it's root of ship or just part of newImage
                for j in range (0, self.iteratorForSettingDirection):
                    if self.newImage[j].x() == x * 30 and self.newImage[j].y() == y * 30:
                        self.newImage[j].setPixmap(self.gameField.ships[i].shipUI)
                        break
                else:
                    self.ships[self.gameField.shot[x][y]].setPixmap(self.gameField.ships[i].shipUI)

                # Change the hp of the ship
                self.gameField.ships[i].hp -= 1

                # Check if the ship is sink
                if self.gameField.ships[i].hp == 0:
                    self.sound = QSound("res/sound/splash2.wav")
                    self.sound.play()

                    if self.who == "Enemy":
                        self.window().inGameLabel.setText("Enemy's ship destroyed!")
                    else:
                        self.window().inGameLabel.setText("Your ship destroyed!")

                    del self.gameField.ships[i]

                # Mark field as shot and hit
                self.gameField.shot[x][y] = 666

                if self.is_game_finished():
                    if self.who == "Player":
                        self.window().end_game("Enemy")
                    else:
                        self.window().end_game("Player")

                #Return Hit - True
                return True

            else:
                self.sound = QSound("res/sound/shot2.wav", self)
                self.sound.play()

                # There is no ship - miss!
                self.gameField.shot[x][y] = 69
                self.miss_label[self.iteratorForShooting].setGeometry(x * 30, y * 30, 25, 25)
                self.miss_label[self.iteratorForShooting].setPixmap(QPixmap("res/pictures/miss.png"))
                self.iteratorForShooting += 1
                if self.who == "Enemy":
                    self.window().inGameLabel.setText("")

                if self.who == "Enemy":
                    self.window().ai_shoot()

                return False
        else:
            return False

    def decide_what_to_do(self, x, y):
        """Function decides what to do in case of each flag"""

        if self.isGame:
            self.shoot_to_field(x, y)
        elif self.isSettingDirection:
            self.set_direction(x, y)
        else:
            self.add_ship_ui(x, y)


    def is_ship_placed_correctly(self, x, y):
        """This function tells if ship that is about to place is set correctly"""

        if x > 9 or x < 0 or y < 0 or y > 9:
            return False

        for i in range (-1, 2, 1):
            for j in range (-1, 2, 1):
                # Index out of list
                if x+j < 0 or x+j > 9 or y+i < 0 or y+i > 9:
                    continue

                # If there is another ship around - break
                if self.gameField.shot[x + j][y + i] != -1 and self.gameField.shot[x + j][y + i] != self.iterator:
                    return False
        # If nothing happened - return True - ship can be set
        return True

    def is_game_finished(self):
        if len(self.gameField.ships) == 0:
            return True
        else:
            return False
