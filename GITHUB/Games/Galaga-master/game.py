from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
import config
from player_actions import ShootLaser
from player import Player
from enemy_actions import MoveEnemy, EnemyShoot, EnemyAttack
from multiprocessing import Process, Queue, current_process
from random import randint
from deus_ex_machina import DeusExMachina


class Game(QWidget):

    gameOverSignal = pyqtSignal()

    def __init__(self, players):
        super().__init__()

        print('Players to play: ', players)

        # PowerUp process
        self.powerUpQueue = Queue()
        print('Regular process id: ', current_process().pid)
        powerUpProcess = Process(target=powerup_process, args=[self.powerUpQueue])
        powerUpProcess.start()
        self.powerUpLabels = []

        # ShootLaser thread
        self.shootLaser = ShootLaser()
        self.shootLaser.calc_done.connect(self.move_laser_up)
        self.shootLaser.collision_detected.connect(self.player_laser_enemy_collide)
        self.shootLaser.moving_collision_detected.connect(self.player_laser_moving_enemy_collide)
        self.shootLaser.start()

        # MoveEnemy thread
        self.moveEnemy = MoveEnemy()
        self.moveEnemy.calc_done.connect(self.move_enemy)
        self.moveEnemy.start()

        # EnemyShoot thread
        self.enemyShoot = EnemyShoot()
        self.enemyShoot.can_shoot.connect(self.enemy_shoot_laser)
        self.enemyShoot.move_down.connect(self.move_enemy_laser)
        self.enemyShoot.collision_detected.connect(self.enemy_hit_player)
        self.enemyShoot.next_level.connect(self.next_level)
        self.enemyShoot.start()

        # EnemyAttack thread
        self.enemyAttack = EnemyAttack()
        self.enemyAttack.can_attack.connect(self.enemy_attack_player)
        self.enemyAttack.move_down.connect(self.move_enemy_down)
        self.enemyAttack.player_collision.connect(self.enemy_attack_player_hit)
        self.enemyAttack.start()

        # PowerUp thread
        self.deusExMachina = DeusExMachina()
        self.deusExMachina.collision_detected.connect(self.powerup_collision)
        self.deusExMachina.powerup_timeout.connect(self.powerup_timeout)
        self.deusExMachina.start()

        # Power up timer
        self.powerUpTimer = QTimer()
        self.powerUpTimer.setInterval(config.POWERUP_TIMEOUT)
        self.powerUpTimer.timeout.connect(self.show_powerup)
        self.powerUpTimer.start()

        # Gameplay options
        self.activePlayers = players
        self.startPlayers = players
        self.playerOneSpeed = config.PLAYER_SPEED
        self.playerTwoSpeed = config.PLAYER_SPEED
        self.playerOneCanShoot = True
        self.playerTwoCanShoot = True

        # Add background pixmap
        self.backgroundPixmap = QPixmap('images/background.png')

        # Add player one
        self.playerPixmap = QPixmap('images/ship.png')

        # add second player
        if self.startPlayers == 2:
            self.playerTwoPixmap = QPixmap('images/ship_two.png')

        # Set enemy pixmaps
        self.enemyPixmaps = []
        enemyPixmap = QPixmap('images/enemy_1.png')
        enemyPixmap = enemyPixmap.scaledToWidth(config.IMAGE_WIDTH - 20)
        enemyPixmap = enemyPixmap.scaledToHeight(config.IMAGE_HEIGHT - 20)
        self.enemyPixmaps.append(enemyPixmap)
        enemyPixmap = QPixmap('images/enemy_2.png')
        enemyPixmap = enemyPixmap.scaledToWidth(config.IMAGE_WIDTH - 20)
        enemyPixmap = enemyPixmap.scaledToHeight(config.IMAGE_HEIGHT - 20)
        self.enemyPixmaps.append(enemyPixmap)
        enemyPixmap = QPixmap('images/enemy_3.png')
        enemyPixmap = enemyPixmap.scaledToWidth(config.IMAGE_WIDTH - 20)
        enemyPixmap = enemyPixmap.scaledToHeight(config.IMAGE_HEIGHT - 20)
        self.enemyPixmaps.append(enemyPixmap)
        enemyPixmap = QPixmap('images/enemy_4.png')
        enemyPixmap = enemyPixmap.scaledToWidth(config.IMAGE_WIDTH - 20)
        enemyPixmap = enemyPixmap.scaledToHeight(config.IMAGE_HEIGHT - 20)
        self.enemyPixmaps.append(enemyPixmap)

        self.__init_ui__()

    def __init_ui__(self):

        # Set background
        numOfLabelsX = config.BOARD_WIDTH // config.IMAGE_WIDTH
        numOfLabelsY = config.BOARD_HEIGHT // config.IMAGE_HEIGHT

        for x in range(numOfLabelsX):
            for y in range(numOfLabelsY):
                backgroundLabel = QLabel(self)
                backgroundLabel.setPixmap(self.backgroundPixmap)
                backgroundLabelX = config.IMAGE_WIDTH * x
                backgroundLabelY = config.IMAGE_HEIGHT * y
                backgroundLabel.setGeometry(backgroundLabelX, backgroundLabelY, config.IMAGE_WIDTH, config.IMAGE_HEIGHT)

        # Set lives label
        self.playerLivesLabel = QLabel(self)
        self.playerLivesLabelText = "<font color='white'>Lives: 3</font>"
        self.playerLivesLabel.setText(self.playerLivesLabelText)
        self.playerLivesLabel.setFont(QFont('Times', 16, QFont.Bold))

        # Set second player lives label
        if self.startPlayers == 2:
            self.playerTwoLivesLabel = QLabel(self)
            self.playerTwoLivesLabelText = "<font color='white'>Lives: 3</font>"
            self.playerTwoLivesLabel.setText(self.playerTwoLivesLabelText)
            self.playerTwoLivesLabel.setFont(QFont('Times', 16, QFont.Bold))
            self.playerTwoLivesLabel.setGeometry(config.BOARD_WIDTH - 100, 0, 100, 30)

        #Set level label
        self.gameLevel = QLabel(self)
        self.gameLevel.setFont(QFont("Times", 16, QFont.Bold))
        levelX = config.BOARD_WIDTH // 2 - 50  # centar
        levelY = 0
        self.gameLevel.setGeometry(levelX, levelY, 100, 30)
        self.update_level(1)

        # Set player start positions
        if self.startPlayers == 1:
            self.playerLabel = QLabel(self)
            self.playerLabel.setPixmap(self.playerPixmap)
            playerLabelX = config.BOARD_WIDTH // 2 - config.IMAGE_WIDTH
            playerLabelY = config.BOARD_HEIGHT - config.IMAGE_HEIGHT
            self.playerLabel.setGeometry(playerLabelX, playerLabelY, config.IMAGE_WIDTH, config.IMAGE_HEIGHT)
            self.player = Player(self.playerLabel)

        elif self.startPlayers == 2:
            # set player 1 start position
            self.playerLabel = QLabel(self)
            self.playerLabel.setPixmap(self.playerPixmap)
            playerLabelX = 0
            playerLabelY = config.BOARD_HEIGHT - config.IMAGE_HEIGHT

            # set player 2 start position
            self.playerTwoLabel = QLabel(self)
            self.playerTwoLabel.setPixmap(self.playerTwoPixmap)
            playerTwoLabelX = config.BOARD_WIDTH - config.IMAGE_WIDTH
            playerTwoLabelY = config.BOARD_HEIGHT - config.IMAGE_HEIGHT

            self.playerLabel.setGeometry(playerLabelX, playerLabelY, config.IMAGE_WIDTH, config.IMAGE_HEIGHT)
            self.playerTwoLabel.setGeometry(playerTwoLabelX, playerTwoLabelY, config.IMAGE_WIDTH, config.IMAGE_HEIGHT)

            # Players
            self.player = Player(self.playerLabel)
            self.playerTwo = Player(self.playerTwoLabel)

        # Set enemy start positions
        self.enemyLabels = []

        for i in range(3):
            for j in range(10):
                enemyLabel = QLabel(self)
                randIndex = randint(0, len(self.enemyPixmaps)-1)
                enemyLabel.setPixmap(self.enemyPixmaps[randIndex])
                positionX = config.IMAGE_WIDTH * (j+3)
                positionY = config.IMAGE_WIDTH * (i+1)
                enemyLabel.setGeometry(positionX, positionY, config.IMAGE_WIDTH, config.IMAGE_HEIGHT)
                enemyLabel.show()
                self.enemyLabels.append(enemyLabel)

        self.activate_enemy_threads()

    def show_powerup(self):
        if self.powerUpQueue.qsize() < 2:
            powerUpProcess = Process(target=powerup_process, args=[self.powerUpQueue])
            powerUpProcess.start()

        powerUpX = self.powerUpQueue.get()

        powerUpPixmap = QPixmap('images/pewdiepie.png')
        powerUpLabel = QLabel(self)
        powerUpLabel.setPixmap(powerUpPixmap)
        powerUpLabel.setGeometry(powerUpX, config.BOARD_HEIGHT-config.IMAGE_HEIGHT, config.IMAGE_WIDTH, config.IMAGE_HEIGHT)
        powerUpLabel.show()

        self.deusExMachina.add_powerup(powerUpLabel)
        self.powerUpLabels.append(powerUpLabel)

    def powerup_timeout(self, powerUpLabel: QLabel):
        if powerUpLabel in self.powerUpLabels:
            self.powerUpLabels.remove(powerUpLabel)

        powerUpLabel.hide()

    def powerup_collision(self, powerUpLabel: QLabel, playerLabel: QLabel):
        if powerUpLabel in self.powerUpLabels:
            self.powerUpLabels.remove(powerUpLabel)

        powerUpLabel.hide()

        # choose random powerup
        randIndex = randint(0, len(config.POWERUPS)-1)
        powerUpAction = config.POWERUPS[0]

        print('Action: ', powerUpAction)

        if self.startPlayers == 2:
            if self.player.playerLabel == playerLabel:
                # Player 1
                print('Player 1 je pokupio powerup')
                if powerUpAction == 'sonic_speed':
                    if not self.playerOneSpeed + 10 > 30:
                        self.playerOneSpeed += 10
                        # Cooldown
                        self.powerUpCooldownTimer = QTimer()
                        self.powerUpCooldownTimer.setInterval(config.POWERUP_COOLDOWN_TIMER)
                        self.powerUpCooldownTimer.timeout.connect(lambda: self.stop_powerup(1, powerUpAction))
                        self.powerUpCooldownTimer.setSingleShot(True)
                        self.powerUpCooldownTimer.start()
                elif powerUpAction == 'additional_life':
                    if self.player.get_lives() < 3:
                        self.player.lives += 1
                        print('Player 1 lives: ', self.player.get_lives())
                        self.update_lives_label(1)
                elif powerUpAction == 'turtle_speed':
                    if self.playerOneSpeed - 10 >= 5:
                        self.playerOneSpeed -= 10
                        # Cooldown
                        self.powerUpCooldownTimer = QTimer()
                        self.powerUpCooldownTimer.setInterval(config.POWERUP_COOLDOWN_TIMER)
                        self.powerUpCooldownTimer.timeout.connect(lambda: self.stop_powerup(1, powerUpAction))
                        self.powerUpCooldownTimer.setSingleShot(True)
                        self.powerUpCooldownTimer.start()
                elif powerUpAction == 'stop_shooting':
                    self.playerOneCanShoot = False
                    # Cooldown
                    self.powerUpCooldownTimer = QTimer()
                    self.powerUpCooldownTimer.setInterval(config.POWERUP_COOLDOWN_TIMER)
                    self.powerUpCooldownTimer.timeout.connect(lambda: self.stop_powerup(1, powerUpAction))
                    self.powerUpCooldownTimer.setSingleShot(True)
                    self.powerUpCooldownTimer.start()

            if self.playerTwo.playerLabel == playerLabel:
                # Player 2
                print('Player 2 je pokupio powerup')

                if powerUpAction == 'sonic_speed':
                    if not self.playerTwoSpeed + 10 > 30:
                        self.playerTwoSpeed += 10
                        # Cooldown
                        # Power up expire timer
                        self.powerUpCooldownTimer = QTimer()
                        self.powerUpCooldownTimer.setInterval(config.POWERUP_COOLDOWN_TIMER)
                        self.powerUpCooldownTimer.timeout.connect(lambda: self.stop_powerup(2, powerUpAction))
                        self.powerUpCooldownTimer.setSingleShot(True)
                        self.powerUpCooldownTimer.start()
                elif powerUpAction == 'additional_life':
                    if self.playerTwo.get_lives() < 3:
                        self.playerTwo.lives += 1
                        self.update_lives_label(2)
                elif powerUpAction == 'turtle_speed':
                    if self.playerTwoSpeed - 10 >= 5:
                        print("PlayerTwoSpeed: ",self.playerTwoSpeed)
                        self.playerTwoSpeed -= 10
                        print("PlayerTwoSpeed: ", self.playerTwoSpeed)
                        # Cooldown
                        self.powerUpCooldownTimer = QTimer()
                        self.powerUpCooldownTimer.setInterval(config.POWERUP_COOLDOWN_TIMER)
                        self.powerUpCooldownTimer.timeout.connect(lambda: self.stop_powerup(2, powerUpAction))
                        self.powerUpCooldownTimer.setSingleShot(True)
                        self.powerUpCooldownTimer.start()
                elif powerUpAction == 'stop_shooting':
                    self.playerTwoCanShoot = False
                    # Cooldown
                    self.powerUpCooldownTimer = QTimer()
                    self.powerUpCooldownTimer.setInterval(config.POWERUP_COOLDOWN_TIMER)
                    self.powerUpCooldownTimer.timeout.connect(lambda: self.stop_powerup(2, powerUpAction))
                    self.powerUpCooldownTimer.setSingleShot(True)
                    self.powerUpCooldownTimer.start()
        else:
            # Player 1
            print('Player 1 je pokupio powerup')

            if powerUpAction == 'sonic_speed':
                if not self.playerOneSpeed + 10 > 30:
                    self.playerOneSpeed += 10
                    # Cooldown
                    self.powerUpCooldownTimer = QTimer()
                    self.powerUpCooldownTimer.setInterval(config.POWERUP_COOLDOWN_TIMER)
                    self.powerUpCooldownTimer.timeout.connect(lambda: self.stop_powerup(1, powerUpAction))
                    self.powerUpCooldownTimer.setSingleShot(True)
                    self.powerUpCooldownTimer.start()
            elif powerUpAction == 'additional_life':
                if self.player.get_lives() < 3:
                    self.player.lives += 1
                    print('Player 1 lives: ', self.player.get_lives())
                    self.update_lives_label(1)
            elif powerUpAction == 'turtle_speed':
                if self.playerOneSpeed - 10 >= 5:
                    self.playerOneSpeed -= 10
                    # Cooldown
                    self.powerUpCooldownTimer = QTimer()
                    self.powerUpCooldownTimer.setInterval(config.POWERUP_COOLDOWN_TIMER)
                    self.powerUpCooldownTimer.timeout.connect(lambda: self.stop_powerup(1, powerUpAction))
                    self.powerUpCooldownTimer.setSingleShot(True)
                    self.powerUpCooldownTimer.start()
            elif powerUpAction == 'stop_shooting':
                self.playerOneCanShoot = False
                # Cooldown
                self.powerUpCooldownTimer = QTimer()
                self.powerUpCooldownTimer.setInterval(config.POWERUP_COOLDOWN_TIMER)
                self.powerUpCooldownTimer.timeout.connect(lambda: self.stop_powerup(1, powerUpAction))
                self.powerUpCooldownTimer.setSingleShot(True)
                self.powerUpCooldownTimer.start()

    def stop_powerup(self, playerNum, powerUpAction):
        print('Stop powerup player num: ', playerNum)
        print('Stop powerup action: ', powerUpAction)

        if powerUpAction == 'sonic_speed':
            if playerNum == 1:
                self.playerOneSpeed = config.PLAYER_SPEED
            elif playerNum == 2:
                self.playerTwoSpeed = config.PLAYER_SPEED
            else:
                self.playerOneSpeed = config.PLAYER_SPEED
                self.playerTwoSpeed = config.PLAYER_SPEED
        elif powerUpAction == 'turtle_speed':
            if playerNum == 1:
                self.playerOneSpeed = config.PLAYER_SPEED
            elif playerNum == 2:
                self.playerTwoSpeed = config.PLAYER_SPEED
            else:
                self.playerOneSpeed = config.PLAYER_SPEED
                self.playerTwoSpeed = config.PLAYER_SPEED
        elif powerUpAction == 'stop_shooting':
            if playerNum == 1:
                self.playerOneCanShoot = True
            elif playerNum == 2:
                self.playerTwoCanShoot = True
            else:
                self.playerOneCanShoot = True
                self.playerTwoCanShoot = True

    def next_level(self, current_level):
        if self.activePlayers == 0 and len(self.enemyLabels) == 0:
            self.displayGameOver()

        else:
            self.enemyShoot.update_level(config.NEXTLVL_SHOOT_TIMER, config.NEXTLVL_ENEMY_LASER_SPEED)

            # Set enemy start positions
            self.enemyLabels = []
            self.update_level(current_level)

            for i in range(3):
                for j in range(10):
                    enemyLabel = QLabel(self)
                    randIndex = randint(0, len(self.enemyPixmaps) - 1)
                    enemyLabel.setPixmap(self.enemyPixmaps[randIndex])
                    positionX = config.IMAGE_WIDTH * (j + 3)
                    positionY = config.IMAGE_WIDTH * (i + 1)
                    enemyLabel.setGeometry(positionX, positionY, config.IMAGE_WIDTH, config.IMAGE_HEIGHT)
                    enemyLabel.show()
                    self.enemyLabels.append(enemyLabel)

            # add enemies for other stuff
            for i in range(len(self.enemyLabels)):
                self.moveEnemy.add_enemy(self.enemyLabels[i])
                self.enemyShoot.add_enemy(self.enemyLabels[i])
                self.shootLaser.add_enemy(self.enemyLabels[i])
                self.enemyAttack.add_enemy(self.enemyLabels[i])

    def update_level(self, current_level):
        print("LEVEL: ", current_level)
        gameLevelText = "<font color='white'>Level: {} </font>".format(current_level)
        self.gameLevel.setText(gameLevelText)

    def activate_enemy_threads(self):
        # add player for collision detection first
        self.enemyShoot.add_player(self.playerLabel)
        self.enemyAttack.add_player(self.playerLabel)
        self.deusExMachina.add_player(self.playerLabel)

        if self.startPlayers == 2:
            self.enemyShoot.add_player(self.playerTwoLabel)
            self.enemyAttack.add_player(self.playerTwoLabel)
            self.deusExMachina.add_player(self.playerTwoLabel)

        # add enemies for other stuff
        for i in range(len(self.enemyLabels)):
            self.moveEnemy.add_enemy(self.enemyLabels[i])
            self.enemyShoot.add_enemy(self.enemyLabels[i])
            self.shootLaser.add_enemy(self.enemyLabels[i])
            self.enemyAttack.add_enemy(self.enemyLabels[i])

    def remove_enemy_label(self, enemyLabel: QLabel):
        if enemyLabel in self.enemyLabels:
            self.enemyLabels.remove(enemyLabel)

    def update_lives_label(self, player):
        if player == 1:
            lives = self.player.get_lives()
            print('Update label lives: ', lives)
            if lives == 3:
                self.playerLivesLabelText = "<font color='white'>Lives: 3</font>"
                self.playerLivesLabel.setText(self.playerLivesLabelText)
            elif lives == 2:
                self.playerLivesLabelText = "<font color='white'>Lives: 2</font>"
                self.playerLivesLabel.setText(self.playerLivesLabelText)
            elif lives == 1:
                self.playerLivesLabelText = "<font color='white'>Lives: 1</font>"
                self.playerLivesLabel.setText(self.playerLivesLabelText)
            else:
                self.playerLivesLabelText = "<font color='white'>Lives: 0</font>"
                self.playerLivesLabel.setText(self.playerLivesLabelText)
                # ukloni igraca
                self.enemyShoot.remove_player(self.playerLabel)
                self.enemyAttack.remove_player(self.playerLabel)
                self.deusExMachina.remove_player(self.playerLabel)
                self.playerLabel.hide()
                self.activePlayers -= 1

        # Check for second player
        if player == 2:
            if self.startPlayers == 2:
                lives = self.playerTwo.get_lives()
                if lives == 3:
                    self.playerTwoLivesLabelText = "<font color='white'>Lives: 3</font>"
                    self.playerTwoLivesLabel.setText(self.playerTwoLivesLabelText)
                elif lives == 2:
                    self.playerTwoLivesLabelText = "<font color='white'>Lives: 2</font>"
                    self.playerTwoLivesLabel.setText(self.playerTwoLivesLabelText)
                elif lives == 1:
                    self.playerTwoLivesLabelText = "<font color='white'>Lives: 1</font>"
                    self.playerTwoLivesLabel.setText(self.playerTwoLivesLabelText)
                else:
                    self.playerTwoLivesLabelText = "<font color='white'>Lives: 0</font>"
                    self.playerTwoLivesLabel.setText(self.playerTwoLivesLabelText)
                    # ukloni igraca
                    self.enemyShoot.remove_player(self.playerTwoLabel)
                    self.enemyAttack.remove_player(self.playerTwoLabel)
                    self.deusExMachina.remove_player(self.playerTwoLabel)
                    self.playerTwoLabel.hide()
                    self.activePlayers -= 1

        # check if game over
        if self.activePlayers == 0:
            while len(self.enemyLabels) != 0:
                for enemy in self.enemyLabels:
                    try:
                        enemy.hide()
                    except Exception as e:
                        print("EXP in game for hide(): ", e)
                    self.enemyAttack.remove_enemy(enemy)
                    self.enemyAttack.remove_moving_enemy(enemy)
                    self.enemyShoot.remove_enemy(enemy)
                    self.moveEnemy.remove_enemy(enemy)
                    self.shootLaser.remove_enemy(enemy)
                    self.shootLaser.remove_falling_enemy(enemy)
                    self.remove_enemy_label(enemy)

            # hide powerup labels
            self.powerUpTimer.stop()
            self.deusExMachina.shouldCheck = False
            print('Stopped power up timer')
            for label in self.powerUpLabels:
                label.hide()

            #game over label
            self.gameOver = QLabel(self)
            self.gameOver.setFont(QFont("Times", 64, QFont.Bold))
            gameOverX = config.BOARD_WIDTH // 2 - config.IMAGE_WIDTH * 5  # centar
            gameOverY = config.BOARD_HEIGHT // 2 - config.IMAGE_HEIGHT * 5 - 100
            self.gameOver.setGeometry(gameOverX, gameOverY, 550, 550)
            gameOverText = "<font color='red'>GAME OVER </font>"
            self.gameOver.setText(gameOverText)
            self.gameOver.show()

    def displayGameOver(self):
        self.gameOverSignal.emit()

    def hideEnemy(self, enemyLabel: QLabel):
        enemyLabel.hide()

    def move_enemy(self, enemyLabel: QLabel, newX, newY):
        enemyLabel.move(newX, newY)

    def enemy_shoot_laser(self, startX, startY):
        enemyLaserPixmap = QPixmap('images/enemy_laser.png')
        enemyLaserLabel = QLabel(self)
        enemyLaserLabel.setPixmap(enemyLaserPixmap)
        enemyLaserLabel.setGeometry(startX, startY, config.IMAGE_WIDTH, config.IMAGE_HEIGHT)
        enemyLaserLabel.show()
        # dodamo laser da moze da se krece ka dole
        self.enemyShoot.add_laser(enemyLaserLabel)

    def move_enemy_laser(self, enemyLaser: QLabel, newX, newY):
        if newY < config.BOARD_HEIGHT - config.IMAGE_HEIGHT:
            enemyLaser.move(newX, newY)
        else:
            enemyLaser.hide()
            self.enemyShoot.remove_laser(enemyLaser)

    def enemy_hit_player(self, laserLabel: QLabel, playerLabel: QLabel):
        laserLabel.hide()

        if self.startPlayers == 2:
            if self.player.playerLabel == playerLabel:
                self.player.lower_lives()
                self.update_lives_label(1)
            if self.playerTwo.playerLabel == playerLabel:
                self.playerTwo.lower_lives()
                self.update_lives_label(2)
        else:
            self.player.lower_lives()
            self.update_lives_label(1)

    def enemy_attack_player(self, enemyLabel: QLabel):
        self.moveEnemy.remove_enemy(enemyLabel)
        self.shootLaser.add_falling_enemy(enemyLabel)
        self.shootLaser.remove_enemy(enemyLabel)
        self.enemyShoot.remove_enemy(enemyLabel)

    def move_enemy_down(self, enemyLabel: QLabel, newX, newY):
        if newY < config.BOARD_HEIGHT - config.IMAGE_HEIGHT:
            enemyLabel.move(newX, newY)
        else:
            enemyLabel.hide()
            self.enemyAttack.remove_moving_enemy(enemyLabel)
            self.shootLaser.remove_falling_enemy(enemyLabel)
            self.remove_enemy_label(enemyLabel)

    def enemy_attack_player_hit(self, enemyLabel: QLabel, playerLabel: QLabel):
        enemyLabel.hide()
        self.remove_enemy_label(enemyLabel)

        if self.startPlayers == 2:
            if self.player.playerLabel == playerLabel:
                self.player.lower_lives()
                self.update_lives_label(1)
            if self.playerTwo.playerLabel == playerLabel:
                self.playerTwo.lower_lives()
                self.update_lives_label(2)
        else:
            self.player.lower_lives()
            self.update_lives_label(1)

    def player_laser_enemy_collide(self, enemyLabel: QLabel, laserLabel: QLabel):
        try:
            enemyLabel.hide()
            laserLabel.hide()
            self.remove_enemy_label(enemyLabel)
            self.moveEnemy.remove_enemy(enemyLabel)
            self.enemyShoot.remove_enemy(enemyLabel)
            self.enemyAttack.remove_enemy(enemyLabel)

        except Exception as e:
            print('Exception in Main_Thread/player_laser_enemy_collide method: ', str(e))

    def player_laser_moving_enemy_collide(self, enemyLabel: QLabel, laserLabel: QLabel):
        try:
            enemyLabel.hide()
            laserLabel.hide()
            self.remove_enemy_label(enemyLabel)
            self.enemyAttack.remove_moving_enemy(enemyLabel)
        except Exception as e:
            print('Exception in Main_Thread/player_laser_enemy_collide method: ', str(e))

    def try_move_player(self, x):
        if (x > (config.BOARD_WIDTH - config.IMAGE_WIDTH)) or (x < 0):
            return False
        return True

    def player_shoot_laser(self, startX, startY):
        laserPixmap = QPixmap('images/laser.png')
        laserLabel = QLabel(self)

        laserLabel.setPixmap(laserPixmap)
        laserLabel.setGeometry(startX, startY, config.IMAGE_WIDTH, config.IMAGE_HEIGHT)
        laserLabel.show()

        self.shootLaser.add_laser(laserLabel)

    def move_laser_up(self, laserLabel: QLabel, newX, newY):
        if newY > 0:
            laserLabel.move(newX, newY)
        else:
            laserLabel.hide()
            self.shootLaser.remove_laser(laserLabel)

    def __update_position__(self, key):
        playerPos = self.playerLabel.geometry()

        if key == Qt.Key_D:
            if self.try_move_player(playerPos.x() + self.playerOneSpeed):
                self.playerLabel.setGeometry(playerPos.x() + self.playerOneSpeed, playerPos.y(), playerPos.width(), playerPos.height())
        elif key == Qt.Key_A:
            if self.try_move_player(playerPos.x() - self.playerOneSpeed):
                self.playerLabel.setGeometry(playerPos.x() - self.playerOneSpeed, playerPos.y(), playerPos.width(), playerPos.height())
        elif key == Qt.Key_Space:
            if self.player.get_lives() > 0 and self.playerOneCanShoot:
                self.player_shoot_laser(playerPos.x() + config.IMAGE_WIDTH//2, playerPos.y() - config.IMAGE_HEIGHT)

        # 2 players
        if self.startPlayers == 2:
            playerTwoPos = self.playerTwoLabel.geometry()

            # player two moving
            if key == Qt.Key_Right:
                if self.try_move_player(playerTwoPos.x() + self.playerTwoSpeed):
                    self.playerTwoLabel.setGeometry(playerTwoPos.x() + self.playerTwoSpeed, playerTwoPos.y(), playerTwoPos.width(), playerTwoPos.height())
            elif key == Qt.Key_Left:
                if self.try_move_player(playerTwoPos.x() - self.playerTwoSpeed):
                    self.playerTwoLabel.setGeometry(playerTwoPos.x() - self.playerTwoSpeed, playerTwoPos.y(), playerTwoPos.width(), playerTwoPos.height())
            elif key == Qt.Key_0:
                if self.playerTwo.get_lives() > 0 and self.playerTwoCanShoot:
                    self.player_shoot_laser(playerTwoPos.x() + config.IMAGE_WIDTH // 2, playerTwoPos.y() - config.IMAGE_HEIGHT)


# ovo je mozda moglo u Deus Ex Machina po nekoj logici
# Process for powerup positions
def powerup_process(q: Queue):
    print('Powerup process: ', current_process().pid)
    while q.qsize() < 10:
        # print('Q Size: ', q.qsize())
        randomX = randint(0, config.BOARD_WIDTH - config.IMAGE_HEIGHT)
        q.put(randomX)


# Process for powerup actions - presporo je ovako
"""
def powerup_action(q: Queue):
    powerUpActions = ['additional_life', 'sonic_speed', 'turtle_speed', 'faster_lasers']

    randIndex = randint(0, len(powerUpActions))
    powerUpAction = powerUpActions[1]   # Sonic speed

    q.put(powerUpAction)
"""
