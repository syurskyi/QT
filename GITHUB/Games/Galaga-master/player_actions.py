from PyQt5.QtCore import pyqtSignal, QThread, QObject
from PyQt5.QtWidgets import QLabel
from time import sleep
import config


class ShootLaser(QObject):
    calc_done = pyqtSignal(QLabel, int, int)
    collision_detected = pyqtSignal(QLabel, QLabel)
    moving_collision_detected = pyqtSignal(QLabel, QLabel)

    def __init__(self):
        super().__init__()

        self.threadWorking = True
        self.laserLabels = []
        self.enemyLabels = []
        self.fallingEnemies = []

        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.__work__)

    def start(self):
        self.thread.start()

    def add_laser(self, laserLabel: QLabel):
        self.laserLabels.append(laserLabel)

    def remove_laser(self, laserLabel: QLabel):
        if laserLabel in self.laserLabels:
            self.laserLabels.remove(laserLabel)

    def add_enemy(self, enemyLabel: QLabel):
        self.enemyLabels.append(enemyLabel)

    def remove_enemy(self, enemyLabel: QLabel):
        if enemyLabel in self.enemyLabels:
            self.enemyLabels.remove(enemyLabel)

    def add_falling_enemy(self, enemyLabel: QLabel):
        self.fallingEnemies.append(enemyLabel)

    def remove_falling_enemy(self, enemyLabel: QLabel):
        if enemyLabel in self.fallingEnemies:
            self.fallingEnemies.remove(enemyLabel)

    def die(self):
        self.threadWorking = False
        self.thread.quit()

    def __work__(self):
        while self.threadWorking:

            #print('Lasers: ', len(self.laserLabels))
            #print('Enemies: ', len(self.enemyLabels))
            #print('Moving enemies: ', len(self.fallingEnemies))

            try:
                collided = False

                # Collision with enemy
                for enemy in self.enemyLabels:

                    if collided:
                        break

                    enemyGeo = enemy.geometry()
                    enemyXStart = enemyGeo.x()
                    enemyXEnd = enemyGeo.x() + config.IMAGE_WIDTH
                    enemyYStart = enemyGeo.y()
                    enemyYEnd = enemyGeo.y() + config.IMAGE_HEIGHT

                    enemyXArray = range(enemyXStart, enemyXEnd)
                    enemyYArray = range(enemyYStart, enemyYEnd)

                    # check for collision with laser
                    for laser in self.laserLabels:
                        laserGeo = laser.geometry()
                        laserXStart = laserGeo.x()
                        laserXEnd = laserGeo.x() + config.IMAGE_WIDTH
                        laserYStart = laserGeo.y()
                        laserYEnd = laserGeo.y() + config.IMAGE_HEIGHT

                        laserXArray = range(laserXStart, laserXEnd)
                        laserYArray = range(laserYStart, laserYEnd)

                        # drugi nacin detekcije kolizije
                        for enemyY in enemyYArray:
                            if collided:
                                break

                            if enemyY in laserYArray:
                                for enemyX in enemyXArray:
                                    if enemyX in laserXArray:
                                        #print('Collision detected for y: {} {}'.format(enemyY, laserY))
                                        self.remove_enemy(enemy)
                                        self.remove_laser(laser)
                                        self.collision_detected.emit(enemy, laser)
                                        collided = True
                                        break

                # Collision with falling enemy
                if not collided:
                    # check for collision with falling enemy
                    for fallingEnemy in self.fallingEnemies:
                        fallingEnemyGeo = fallingEnemy.geometry()
                        fallingEnemyXStart = fallingEnemyGeo.x()
                        fallingEnemyXEnd = fallingEnemyGeo.x() + config.IMAGE_WIDTH
                        fallingEnemyY = fallingEnemyGeo.y() + config.IMAGE_HEIGHT
                        fallingEnemyXArray = range(fallingEnemyXStart, fallingEnemyXEnd)

                        # check for collision with player
                        for laser in self.laserLabels:
                            laserGeo = laser.geometry()
                            laserXStart = laserGeo.x()
                            laserXEnd = laserGeo.x() + config.IMAGE_WIDTH
                            laserYStart = laserGeo.y()
                            laserYEnd = laserGeo.y() + config.IMAGE_HEIGHT
                            laserXArray = range(laserXStart, laserXEnd)
                            laserYArray = range(laserYStart, laserYEnd)

                            # drugi nacin detekcije kolizije, moooozda
                            if fallingEnemyY in laserYArray:
                                for fallingEnemyX in fallingEnemyXArray:
                                    if fallingEnemyX in laserXArray:
                                        self.remove_falling_enemy(fallingEnemy)
                                        self.remove_laser(laser)
                                        self.moving_collision_detected.emit(fallingEnemy, laser)
                                        collided = True
                                        break

                # MOVE LABELS UP
                for label in self.laserLabels:
                    laserGeo = label.geometry()
                    laserX = laserGeo.x()
                    laserY = laserGeo.y() - config.PLAYER_LASER_SPEED
                    self.calc_done.emit(label, laserX, laserY)

                sleep(0.05)
            except Exception as e:
                print('Exception in ShootLaser_Thread: ', str(e))
