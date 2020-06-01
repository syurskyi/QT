import random
import time
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Player:
    def __init__(self,start_position,id,type=0):
        # Type:
        # 0 - bot
        # 1 - gracz lokalny
        self.type=type
        self.id=id
        self.position=start_position
        self.has_bomb=True #nie zmieniac
        self.bowled_bomb=False #nie zmieniac
        self.last_direction=3
        self.bomb_end_time=time.time()
        self.bomb_start_time = time.time()
        self.explosion_duration=3
        self.explosion_delay=2
        self.explosion_range=5 #tak na prawde to -1, bo liczymy od 0
        self.bomb_position=start_position
        self.hp=50
        self.read_jpg()

    def movement(self, key=0):
        if self.type==0:
            direction=random.randint(1,4) # 1 - gora, 2 - prawa, 3 - dol, 4 - lewa
            self.last_direction=direction
            return direction
        else:
                return 0


    def bomb(self,new_bomb_position):
        if self.has_bomb:
            if self.type == 0:
                decision=random.randint(0,5)
            else:
                decision=0
            if decision==0:
                self.bomb_stats_update(new_bomb_position)
            return decision
        else:
            return -1

    def bomb_stats_update(self,new_bomb_position):
        self.has_bomb=False
        self.bowled_bomb=True
        self.bomb_start_time = time.time() + self.explosion_delay
        self.bomb_end_time = time.time() + self.explosion_delay + self.explosion_duration  #
        self.bomb_position = new_bomb_position

    def update_jpg(self, direction):
        self.last_direction=direction
        if direction==1:
            self.img = self.img_back
        elif direction==2:
            self.img = self.img_right
        elif direction==3:
            self.img = self.img_front
        elif direction==4:
            self.img = self.img_left
        else:
            pass


    def read_jpg(self):
        if self.type==0:
            color='green'
        else: #self.type==1:
            color='red'

        path_img = 'images/bomberman_' + color
        self.img_back=QtGui.QPixmap(path_img+'_back.png')
        self.img_right = QtGui.QPixmap(path_img + '_right.png')
        self.img_front = QtGui.QPixmap(path_img + '_front.png')
        self.img_left = QtGui.QPixmap(path_img + '_left.png')
        self.img=self.img_front