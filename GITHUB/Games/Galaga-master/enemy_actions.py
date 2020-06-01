from PyQt5.QtCore import pyqtSignal, QThread, QObject, QTimer
from PyQt5.QtWidgets import QLabel
from time import sleep
import numpy as np
import config
from random import randint


class MoveEnemy(QObject):
    calc_done = pyqtSignal(QLabel, int, int)

    def __init__(self):
        super().__init__()

        self.threadWorking = True
        self.enemies = []
        self.goLeft = True
        self.goRight = False

        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.__work__)

    def start(self):
        self.thread.start()

    def add_enemy(self, enemyLabel: QLabel):
        self.enemies.append(enemyLabel)

    def remove_enemy(self, enemyLabel: QLabel):
        if enemyLabel in self.enemies:
            self.enemies.remove(enemyLabel)

    def die(self):
        self.threadWorking = False
        self.thread.quit()

    def __work__(self):
        while self.threadWorking:
            try:
                # movement logic
                if self.goLeft:
                    for enemy in self.enemies:
                        enemyGeo = enemy.geometry()
                        enemyX = enemyGeo.x()
                        enemyY = enemyGeo.y()
                        if enemyX > 0:
                            self.goLeft = True
                            self.goRight = False
                            self.calc_done.emit(enemy, enemyX - 10, enemyY)
                        else:
                            self.goLeft = False
                            self.goRight = True
                            break
                    sleep(config.ENEMY_MOVE_SLEEP)

                elif self.goRight:
                    for enemy in reversed(self.enemies):
                        enemyGeo = enemy.geometry()
                        enemyX = enemyGeo.x()
                        enemyY = enemyGeo.y()

                        if enemyX < config.BOARD_WIDTH - config.IMAGE_WIDTH:
                            self.goRight = True
                            self.goLeft = False
                            self.calc_done.emit(enemy, enemyX + 10, enemyY)
                        else:
                            self.goRight = False
                            self.goLeft = True
                            break
                    sleep(config.ENEMY_MOVE_SLEEP)
            except Exception as e:
                print('Exception in MoveEnemy_Thread: ', str(e))



class EnemyShoot(QObject):
    can_shoot = pyqtSignal(int, int)
    move_down = pyqtSignal(QLabel, int, int)
    collision_detected = pyqtSignal(QLabel, QLabel)
    next_level = pyqtSignal(int)

    def __init__(self):
        super().__init__()

        self.current_level = 1

        self.threadWorking = True
        self.enemies = []
        self.lasers = []
        self.players = []

        self.enemyLaserSpeed = config.ENEMY_LASER_SPEED
        self.shootingTimerInterval = config.ENEMY_SHOOT_TIMER
        self.canShoot = False
        self.shootingTimer = QTimer()
        self.shootingTimer.setInterval(config.ENEMY_SHOOT_TIMER)
        self.shootingTimer.timeout.connect(self.alert_shooting)
        self.shootingTimer.start()

        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.__work__)

    def start(self):
        self.thread.start()

    def add_enemy(self, enemyLabel: QLabel):
        self.enemies.append(enemyLabel)

    def remove_enemy(self, enemyLabel: QLabel):
        if enemyLabel in self.enemies:
            self.enemies.remove(enemyLabel)

    def add_laser(self, laserLabel: QLabel):
        self.lasers.append(laserLabel)

    def remove_laser(self, laserLabel: QLabel):
        if laserLabel in self.lasers:
            self.lasers.remove(laserLabel)

    def add_player(self, playerLabel: QLabel):
        self.players.append(playerLabel)

    def remove_player(self, playerLabel: QLabel):
        if playerLabel in self.players:
            self.players.remove(playerLabel)

    def update_level(self, newInterval, newLaserSpeed):
        if (self.shootingTimerInterval - newInterval) >= 200:
            self.shootingTimerInterval -= newInterval
            self.shootingTimer.setInterval(self.shootingTimerInterval)
            print('Changed shooting interval to: ', self.shootingTimerInterval)

        if (self.enemyLaserSpeed + newLaserSpeed) <= 18:
            self.enemyLaserSpeed += newLaserSpeed
            print('Changed enemy laser speed to: ', self.enemyLaserSpeed)

    def die(self):
        self.threadWorking = False
        self.shootingTimer.stop()
        print('Stopping shooting timer')
        self.thread.quit()

    def find_ymax(self):
        if len(self.enemies) > 0:
            enemy = self.enemies[0]
            enemyGeo = enemy.geometry()
            yMax = enemyGeo.y()
            for i in range(1, len(self.enemies)):
                enemy = self.enemies[i]
                enemyGeo = enemy.geometry()
                y = enemyGeo.y()
                if yMax < y:
                    yMax = y
            return yMax

    def get_enemies_from_y(self, yParam):
        result = []
        if len(self.enemies) > 0:
            for i in range(len(self.enemies)):
                enemy = self.enemies[i]
                enemyGeo = enemy.geometry()
                y = enemyGeo.y()
                if y == yParam:
                    result.append(enemy)
        return result

    def alert_shooting(self):
        if not self.canShoot:
            self.canShoot = True

    def __work__(self):
        while self.threadWorking:
            try:
                if self.canShoot:
                    # CHOOSE A SHOOTER
                    yArray = []
                    for enemy in self.enemies:
                        enemyGeo = enemy.geometry()
                        enemyY = enemyGeo.y()
                        if enemyY not in yArray:
                            yArray.append(enemyY)

                    sortedYs = yArray

                    if len(sortedYs) == 0:
                        #Dozvoli prvo da se svi laseri spuste
                        if len(self.lasers) == 0:
                            sleep(config.NEXT_LEVEL_SLEEP)
                            self.current_level += 1
                            self.next_level.emit(self.current_level)

                    else:
                        yMax = sortedYs[-1]
                        lowestRowEnemies = self.get_enemies_from_y(yMax)

                        if len(lowestRowEnemies) == 10:
                            # Posto ih imamo 10, mozemo ih sve uzeti i jedan od njih ce da puca
                            randIndex = randint(0, 9)
                            enemy = lowestRowEnemies[randIndex]
                            enemyGeo = enemy.geometry()
                            laserX = enemyGeo.x() + (config.IMAGE_WIDTH // 2)
                            laserY = enemyGeo.y() + config.IMAGE_HEIGHT
                            self.can_shoot.emit(laserX, laserY)
                            self.canShoot = False

                        elif len(lowestRowEnemies) < 10:
                            # Imamo manje od 10, mozda neko iznad moze da puca
                            if len(sortedYs) > 1:
                                y = sortedYs[-2]
                            else:
                                #print("Ostao je samo jedan red")
                                y = sortedYs[-1]

                            upperEnemies = self.get_enemies_from_y(y)

                            for lowerEnemy in lowestRowEnemies:
                                lowerEnemyGeo = lowerEnemy.geometry()
                                lowerRowEnemyX = lowerEnemyGeo.x()
                                for upperEnemy in upperEnemies:
                                    upperEnemyGeo = upperEnemy.geometry()
                                    upperEnemyX = upperEnemyGeo.x()
                                    if lowerRowEnemyX == upperEnemyX:
                                        if upperEnemies in upperEnemies:
                                            upperEnemies.remove(upperEnemy)

                            lowestRowEnemies += upperEnemies

                            # probaj pucati
                            randIndex = randint(0, len(lowestRowEnemies)-1)
                            enemy = lowestRowEnemies[randIndex]
                            enemyGeo = enemy.geometry()
                            laserX = enemyGeo.x() + (config.IMAGE_WIDTH // 2)
                            laserY = enemyGeo.y() + config.IMAGE_HEIGHT
                            self.can_shoot.emit(laserX, laserY)
                            self.canShoot = False

                        else:
                            print('Okej, nesto ovde ne radi ...')
            except Exception as e:
                print('Exception in EnemyShoot_Thread: ', str(e))

            try:
                # MOVE LASER DOWN
                if len(self.lasers) > 0:
                    for laser in self.lasers:
                        laserGeo = laser.geometry()
                        laserX = laserGeo.x()
                        laserY = laserGeo.y() + self.enemyLaserSpeed

                        # Check for collision with players
                        #print('Broj igraca: ', len(self.players))
                        if len(self.players) > 0:
                            for player in self.players:

                                playerGeo = player.geometry()
                                playerXStart = playerGeo.x()
                                playerXEnd = playerGeo.x() + config.IMAGE_WIDTH
                                playerY = playerGeo.y()

                                xIsEqual = False

                                if playerXStart <= laserX <= playerXEnd:
                                    xIsEqual = True

                                # nova provera za Y osu zbog brzih lasera
                                playerYRange = range(playerY, playerY+config.IMAGE_HEIGHT)
                                laserYRange = range(laserY, laserY+config.IMAGE_HEIGHT)
                                #print('Player Y Range: {} - {}'.format(playerYRange[1], playerYRange[-1]))
                                #print('Laser Y Range: {} - {}'.format(laserYRange[1], laserYRange[-1]))

                                for y in laserYRange:
                                    if y in playerYRange and xIsEqual:
                                        print('enemy hit player with laser')
                                        self.collision_detected.emit(laser, player)
                                        self.remove_laser(laser)
                                        break
                                    else:
                                        self.move_down.emit(laser, laserX, laserY)

                        else:
                            self.move_down.emit(laser, laserX, laserY)

            except Exception as e:
                print('Exception in Moving_Laser: ', str(e))

            sleep(0.05)


class EnemyAttack(QObject):
    can_attack = pyqtSignal(QLabel)
    move_down = pyqtSignal(QLabel, int, int)
    player_collision = pyqtSignal(QLabel, QLabel)
    laser_collision = pyqtSignal(QLabel, QLabel)

    def __init__(self):
        super().__init__()

        self.threadWorking = True
        self.enemies = []
        self.players = []
        self.movingEnemies = []

        self.canAttack = False
        self.fallingTimer = QTimer()
        self.fallingTimer.setInterval(config.ENEMY_FALL_TIMER)
        self.fallingTimer.timeout.connect(self.alert_attack)
        self.fallingTimer.start()

        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.__work__)

    def start(self):
        self.thread.start()

    def add_enemy(self, enemyLabel: QLabel):
        self.enemies.append(enemyLabel)

    def remove_enemy(self, enemyLabel: QLabel):
        if enemyLabel in self.enemies:
            self.enemies.remove(enemyLabel)

    def add_moving_enemy(self, enemyLabel: QLabel):
        self.movingEnemies.append(enemyLabel)

    def remove_moving_enemy(self, enemyLabel: QLabel):
        if enemyLabel in self.movingEnemies:
            self.movingEnemies.remove(enemyLabel)

    def add_player(self, playerLabel: QLabel):
        self.players.append(playerLabel)

    def remove_player(self, playerLabel: QLabel):
        if playerLabel in self.players:
            self.players.remove(playerLabel)

    def die(self):
        self.threadWorking = False
        self.fallingTimer.stop()
        print('Stopping falling timer')
        self.thread.quit()

    def find_ymax(self):
        if len(self.enemies) > 0:
            enemy = self.enemies[0]
            enemyGeo = enemy.geometry()
            yMax = enemyGeo.y()
            for i in range(1, len(self.enemies)):
                enemy = self.enemies[i]
                enemyGeo = enemy.geometry()
                y = enemyGeo.y()
                if yMax < y:
                    yMax = y
            return yMax

    def get_enemies_from_y(self, yParam):
        result = []
        if len(self.enemies) > 0:
            for i in range(len(self.enemies)):
                enemy = self.enemies[i]
                enemyGeo = enemy.geometry()
                y = enemyGeo.y()
                if y == yParam:
                    result.append(enemy)
        return result

    def alert_attack(self):
        if not self.canAttack:
            self.canAttack = True

    def __work__(self):
        while self.threadWorking:
            collided = False
            #print("Enemy length: " , len(self.enemies))
            #print("Faling enemy length: ",len(self.movingEnemies))
            try:
                # Try attacking
                if self.canAttack:
                    if len(self.enemies) > 0:
                        yMax = self.find_ymax()
                        yRowEnemies = self.get_enemies_from_y(yMax)

                        # nasumicno jedan napada iz poslednjeg reda
                        if len(yRowEnemies) > 0:
                            randIndex = randint(0, len(yRowEnemies)-1)
                            enemy = yRowEnemies[randIndex]
                            enemyGeo = enemy.geometry()
                            # try to remove from moving enemies
                            self.can_attack.emit(enemy)
                            self.remove_enemy(enemy)
                            self.add_moving_enemy(enemy)
                            self.canAttack = False

                # move down for attack
                if not collided:
                    for movingEnemy in self.movingEnemies:
                        enemyGeo = movingEnemy.geometry()
                        enemyXStart = enemyGeo.x()
                        enemyXEnd = enemyGeo.x() + config.IMAGE_WIDTH
                        enemyY = enemyGeo.y() + config.IMAGE_HEIGHT
                        enemyXArray = range(enemyXStart, enemyXEnd)
                        self.move_down.emit(movingEnemy, enemyGeo.x(), enemyGeo.y() + config.ENEMY_FALLING_SPEED)

                        # check for collision with player
                        for player in self.players:
                            playerGeo = player.geometry()
                            playerXStart = playerGeo.x()
                            playerXEnd = playerGeo.x() + config.IMAGE_WIDTH
                            playerYStart = playerGeo.y()
                            playerYEnd = playerGeo.y() + config.IMAGE_HEIGHT
                            playerXArray = range(playerXStart, playerXEnd)
                            playerYArray = range(playerYStart, playerYEnd)

                            # drugi nacin detekcije kolizije, moooozda
                            if enemyY in playerYArray:
                                for enemyX in enemyXArray:
                                    if enemyX in playerXArray:
                                        self.player_collision.emit(movingEnemy, player)
                                        self.remove_moving_enemy(movingEnemy)
                                        collided = True
                                        break
                sleep(0.05)
            except Exception as e:
                print('Exception in EnemyAttack_Thread {EnemyAttack}: ', str(e))
