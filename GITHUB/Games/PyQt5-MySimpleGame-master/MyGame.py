# v 0.2.1

import numpy as np
from PyQt5.QtCore import QTimer
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
import MyGameUI
from MyGamePlayer import Player


class Arena(MyGameUI.Ui_MainWindow):
    # !!! It works with height, width >=6, but I recommend >=15 !!!
    def __init__(self,window,height=15,width=15):
        MyGameUI.Ui_MainWindow.__init__(self)


        self.setupUi(window)
        self.update_Ui(height,width)
        self.update_actions()


        self.intro()


    def start_game(self):
        if self.intro_ended==True and self.game_lasts==False:
            self.game_lasts = True
            self.timer = QTimer(self.MainWindow)
            self.timer.timeout.connect(self.update)
            self.timer.start(100)
        else:
            pass

    def start_intro(self):
        self.timer = QTimer(self.MainWindow)
        self.intro_i = self.intro_line_length
        self.timer.timeout.connect(self.update_intro)
        self.timer.start(300/(self.shape[1]/15))

    def reset_game(self):
        if self.intro_ended == True:
            self.game_lasts=False
            self.timer.stop()
            self.build_arena()
            self.players.clear()
            self.add_players()
            self.update_graphics()
        else:
            pass



    def intro(self):
        self.configure_rects()
        self.arena = np.full(self.shape, self.rect_destructible, dtype=int)
        self.arena[0, :] = self.arena[-1, :] = self.rect_indestructible
        self.arena[:, 0] = self.arena[:, -1] = self.rect_indestructible
        self.arena[int(self.shape[0] / 2),self.intro_line_length:self.shape[1] - self.intro_line_length] = self.rect_empty
        self.arena[int(self.shape[0]/2)+1,self.intro_line_length:self.shape[1]-self.intro_line_length]=self.rect_indestructible
        self.add_your_player(position=(int(self.shape[0]/2),self.intro_line_length))

        self.start_intro()


    def update_intro(self):
        if self.intro_i==self.shape[1] - self.intro_line_length+1:
            self.intro_ended=True
            self.reset_game()
        else:
            self.moveRight(self.players[self.your_player_index])
            self.update_graphics()
            self.intro_i+=1 #tym zakonczysz intro



    def configure_rects(self):
        self.intro_line_length=2
        self.max_bots=3
        self.rect_empty=0
        self.rect_destructible=2
        self.rect_indestructible=1
        self.rect_bomb=20
        self.rect_ticking_bomb=4
        self.rect_bot=10 #>=10 <15
        self.rect_you=0 #100?

        self.intro_ended=False
        self.game_lasts=False


    def build_arena(self):
        self.arena=np.full(self.shape, self.rect_empty,dtype=int)

        free_space = 4
        for i in range(0, self.shape[0]):
            if i >=free_space and i <self.shape[0]-free_space:
                self.arena[i, :] = self.rect_destructible
            else:
               for j in range(free_space, self.shape[1] - free_space):
                   self.arena[i, j] = self.rect_destructible
        for i in range(0, self.shape[0], free_space-1):
            if i >= free_space and i < self.shape[0] - free_space:
                for j in range(0, self.shape[1], free_space - 1):
                    self.arena[i, j] = self.rect_indestructible
            else:
                for j in range(free_space, self.shape[1]- free_space, free_space-1):
                    self.arena[i, j] = self.rect_indestructible

        self.arena[0, :] = self.arena[-1, :] = self.rect_indestructible
        self.arena[:, 0] = self.arena[:, -1] = self.rect_indestructible

    def add_players(self):
        self.corners=[ (self.shape[0] - 2, 1),(self.shape[0] - 2, self.shape[1] - 2),(1, self.shape[1] - 2) ]

        self.add_your_player()
        for index, corner in enumerate(self.corners):
            new_player=Player(corner,index+1)
            self.players.append(new_player)
            self.arena[corner]=self.rect_bot+new_player.id

    def add_your_player(self, position=(1,1)):
        self.your_player_index=0
        self.rect_you=0
        self.players=[]
        new_player = Player( position,self.rect_you,1 )
        self.players.append(new_player)
        self.arena[position] = self.rect_you+self.rect_bot


    def update(self):
        for player in self.players:
            if player.hp>0:
                if player.type == 0:
                    self.canBowlBomb(player)

                    direction=player.movement()
                    if direction==1:
                        self.moveUp(player)
                    if direction==2:
                        self.moveRight(player)
                    if direction==3:
                        self.moveDown(player)
                    if direction==4:
                        self.moveLeft(player)
            elif player.hp==0:
                self.moveLog(player.type,player.id,'Game Over')
                self.arena[player.position] = self.rect_empty
                player.hp -= 1
            else:
                pass

            if time.time() > player.bomb_start_time and player.bowled_bomb==True:
                player.bowled_bomb=False
                self.explode(player,player.bomb_position, player.explosion_range)
                self.moveLog(player.type, player.id, 'Boom')

            if time.time() > player.bomb_end_time and player.has_bomb==False:
                self.end_explode(player.bomb_position, player.explosion_range)
                player.has_bomb = True


        self.update_graphics()

    def update_graphics(self):
        side = self.side
        self.scene.clear()
        for i in range(self.shape[1]):
            for j in range(self.shape[0]):
                if self.arena[j,i] == self.rect_empty:
                    rect_item = QtWidgets.QGraphicsPixmapItem(self.img_default_rect)
                if self.arena[j,i] == self.rect_indestructible:
                    rect_item = QtWidgets.QGraphicsPixmapItem(self.img_orange_rect)
                if self.arena[j,i] == self.rect_destructible:
                    rect_item = QtWidgets.QGraphicsPixmapItem(self.img_blue_rect)
                if self.arena[j, i] ==self.rect_ticking_bomb:
                    rect_item = QtWidgets.QGraphicsPixmapItem(self.img_ticking_bomb_rect)
                if self.arena[j,i] >= self.rect_bomb and self.arena[j,i]<=self.rect_bomb+self.max_bots:
                    rect_item = QtWidgets.QGraphicsPixmapItem(self.img_explosion_rect)
                if self.arena[j,i] >=self.rect_bot and self.arena[j,i]<=self.rect_bot+self.max_bots and self.arena[j,i]!=self.rect_you+self.rect_bot:
                    rect_item = QtWidgets.QGraphicsPixmapItem(self.players[self.arena[j,i]-self.rect_bot].img)
                if self.arena[j,i] == self.rect_you+self.rect_bot:
                    rect_item = QtWidgets.QGraphicsPixmapItem(self.players[self.your_player_index].img)
                rect = QtCore.QPointF(i * side - (self.side * 0.5), j * side - (self.side * 0.5))
                rect_item.setPos(rect)
                rect_item.setScale(self.side / 90)
                self.scene.addItem(rect_item)


        if self.intro_ended==True:
            self.updateScoreBoard()
    def updateScoreBoard(self):
        self.updateSingleText('SCOREBOARD', self.shape[1] * self.side - self.side / 5 * 2, self.side * 3, bold=True)
        for i, player in enumerate(self.players):
            if player.type==0:
                img_score=self.img_player_green
            else:
                img_score = self.img_player_red
            rect_item = QtWidgets.QGraphicsPixmapItem(img_score)
            rect = QtCore.QPointF(self.shape[1]*self.side -self.side/4, self.side*3.5+i*self.side)
            rect_item.setPos(rect)
            rect_item.setScale(self.side / 90)
            self.scene.addItem(rect_item)
            self.updateSingleText('HP: ', self.shape[1] * self.side +self.side/5*4, self.side * 3+(self.side/2)+i*self.side,bold=True,size=10)
            self.updateSingleText(str(player.hp), self.shape[1] * self.side + self.side *1.5,self.side * 3 + (self.side / 2) + i * self.side, bold=True, size=12)
    def updateSingleText(self, text, x, y, bold=False, size=11):
        font = QtGui.QFont()
        font.setPointSize(size)
        font.setBold(bold)
        rect = QtCore.QPointF(x,y)
        text_item = QtWidgets.QGraphicsSimpleTextItem()
        text_item.setText(text)
        text_item.setPos(rect)
        text_item.setFont(font)
        self.scene.addItem(text_item)

    def canBowlBomb(self,player):
        if player.last_direction==1:
            self.canBowlBombGeneral(player,-1,0)
        elif player.last_direction==2:
            self.canBowlBombGeneral(player,0,1)
        elif player.last_direction==3:
            self.canBowlBombGeneral(player,1,0)
        elif player.last_direction==4:
            self.canBowlBombGeneral(player,0,-1)
        else:
            pass

    def canBowlBombGeneral(self,player,y,x):
        if self.arena[player.position[0] + y, player.position[1] + x] == self.rect_empty:
            if player.bomb((player.position[0] + y, player.position[1] + x))==0:
                self.arena[player.position[0] + y, player.position[1] + x] = self.rect_ticking_bomb
        else:
            pass

    def moveUp(self, player):
        if player.last_direction != 1:
            player.last_direction = 1
        else:
            self.moveGeneral(player, -1, 0)
            self.moveLog(player.type, player.id, 'Up')
        player.update_jpg(1)

    def moveDown(self, player):
        if player.last_direction != 3:
            player.last_direction = 3
        else:
            self.moveGeneral(player, 1,0)
            self.moveLog(player.type, player.id, 'Down')
        player.update_jpg(3)

    def moveLeft(self, player):
        if player.last_direction != 4:
            player.last_direction = 4
        else:
            self.moveGeneral(player,0,-1)
            self.moveLog(player.type, player.id, 'Left')
        player.update_jpg(4)

    def moveRight(self, player):
        if player.last_direction != 2:
            player.last_direction = 2
        else:
            self.moveGeneral(player,0,1)
            self.moveLog(player.type,player.id,'Right')
        player.update_jpg(2)

    def moveGeneral(self, player,y,x):
        if self.arena[player.position[0]+y, player.position[1] + x] == self.rect_empty or self.arena[player.position[0]+y, player.position[1] + x] == self.rect_bomb:
            if self.arena[player.position[0]+y, player.position[1] + x] == self.rect_bomb:
                player.hp-=1
            self.arena[player.position] = self.rect_empty
            self.arena[player.position[0]+y, player.position[1] + x] = self.rect_bot+player.id
            player.position = player.position[0]+y, player.position[1] + x


    def moveLog(self,player_type, player_id, direction):
        # if player_type == 0:
        #     log = 'Bot ' + str(player_id) + " : "+direction
        # elif player_type == 1:
        #     log = 'You: '+direction
        # self.lineEdit.setText(log)
        # print(log)
        pass


    def explode(self,player,position,bomb_range):
        self.arena[position[0], position[1]] = self.rect_bomb
        for i in range(1,bomb_range):
            if(position[0]+i<self.shape[0]):
                if self.explode_general(player,position, i, 0):
                    break
            else:
                break

        for i in range(1, bomb_range):
            if (position[0] - i >= 0):
                if self.explode_general(player,position, -i,0):
                    break
            else:
                break

        for i in range(1, bomb_range):
            if (position[1]+i <self.shape[1]):
                if self.explode_general(player,position, 0, i):
                    break
            else:
                break
        for i in range(1, bomb_range):
            if (position[1] - i >= 0):
                if self.explode_general(player,position,0, -i):
                    break
            else:
                break

    def explode_general(self,player,position,y,x):
        if self.arena[position[0] + y, position[1]+x] == self.rect_empty or self.arena[position[0] + y, position[1]+x] == self.rect_destructible:
            self.arena[position[0] + y, position[1]+x] = self.rect_bomb
            return False
        else:
            if (self.arena[position[0] + y, position[1]+x] >= self.rect_bot and self.arena[position[0] + y, position[1]+x] <= self.rect_bot + self.max_bots ) \
                    or self.arena[position[0] + y, position[1]+x]==self.rect_you+self.rect_bot:
                player.hp-=1
            return True

    def end_explode(self,position,bomb_range):
        self.arena[position[0], position[1]] = self.rect_empty
        for i in range(1,bomb_range):
            if (position[0] + i < self.shape[0]):
                if self.end_explode_general(position, +i, 0):
                    break
            else:
                break
        for i in range(1, bomb_range):
            if (position[0] - i >= 0):
                if self.end_explode_general(position,-i,0):
                    break
            else:
                break
        for i in range(1, bomb_range):
            if (position[1] + i < self.shape[1]):
                if self.end_explode_general(position,0,+i):
                    break
            else:
                break
        for i in range(1, bomb_range):
            if (position[1] - i >= 0):
                if self.end_explode_general(position,0,-i):
                    break
            else:
                break

    def end_explode_general(self, position, y, x ):
        if self.arena[position[0] + y, position[1]+x] == self.rect_bomb:
            self.arena[position[0] + y, position[1]+x] = self.rect_empty
            return False
        elif self.arena[position[0] + y, position[1]+x] == self.rect_indestructible:
            return True

    def update_actions(self):
        #akcje przyciskow
        self.pushButton_Start.clicked.connect(self.start_game)
        self.pushButton_End.clicked.connect(self.reset_game)
        #eventy
        self.MainWindow.keyPressEvent = self.OneKeyPressEvent
        self.scene.mousePressEvent=self.MyMousePressEvent
        self.scene.mouseReleaseEvent=self.MyMouseReleaseEvent

    def OneKeyPressEvent(self, e):
        key=e.key()
        if self.players[self.your_player_index].hp>0 and self.game_lasts==True:
            if key == QtCore.Qt.Key_Up:
                self.moveUp(player=self.players[self.your_player_index])
            elif key == QtCore.Qt.Key_Down:
                self.moveDown(player=self.players[self.your_player_index])
            elif key == QtCore.Qt.Key_Left:
                self.moveLeft(player=self.players[self.your_player_index])
            elif key == QtCore.Qt.Key_Right:
                self.moveRight(player=self.players[self.your_player_index])
            elif key == QtCore.Qt.Key_Space:
                self.canBowlBomb(self.players[self.your_player_index])
        if key == QtCore.Qt.Key_Escape:
            self.MainWindow.close()


    def MyMouseReleaseEvent(self, event):
        self.releaseX=event.scenePos().x()
        self.releaseY = event.scenePos().y()
        accu=15 #dokladnosc
        if self.players[self.your_player_index].hp>0 and self.game_lasts==True:
            while self.releaseX>self.pressX+accu:
                self.moveRight(player=self.players[self.your_player_index])
                self.releaseX-=self.side
            while self.releaseX<self.pressX-accu:
                self.moveLeft(player=self.players[self.your_player_index])
                self.releaseX+=self.side
            while self.releaseY < self.pressY-accu:
                self.moveUp(player=self.players[self.your_player_index])
                self.releaseY+=self.side
            while self.releaseY >self.pressY+accu:
                self.moveDown(player=self.players[self.your_player_index])
                self.releaseY-=self.side

    def MyMousePressEvent(self, event):
        self.pressX=event.scenePos().x()
        self.pressY = event.scenePos().y()

        self.doubleClickLog(int((self.pressX+self.side/2)/self.side),int((self.pressY+self.side/2)/self.side))

    def doubleClickLog(self, X, Y):
        if Y<self.shape[0] and X<self.shape[1]:
            decoded_rect=self.arena[Y,X]
            if decoded_rect==self.rect_empty:
                log='Pusty blok'
            elif decoded_rect==self.rect_destructible:
                log='Zniszczalny blok'
            elif decoded_rect==self.rect_indestructible:
                log='Niezniszczalny blok'
            elif decoded_rect==self.rect_ticking_bomb:
                log='Bomba'
            elif decoded_rect >= self.rect_bomb and decoded_rect <= self.rect_bomb + self.max_bots:
                log='Eksplozja'
            elif decoded_rect >= self.rect_bot and decoded_rect <= self.rect_bot + self.max_bots and decoded_rect!=self.rect_bot+self.rect_you:
                self.players[self.your_player_index].type=0
                self.players[self.your_player_index].read_jpg()

                self.players[decoded_rect-self.rect_bot].type=1
                self.players[decoded_rect-self.rect_bot].read_jpg()
                self.your_player_index=decoded_rect-self.rect_bot
                self.rect_you=decoded_rect-self.rect_bot
                #dac to wyzej do nowe funkcji
                self.update_graphics()

                log='Zmieniłeś gracza'
            elif decoded_rect == self.rect_you + self.rect_bot:
                log='Twoj gracz'
            else:
                log=''
            self.lineEdit.setText(log)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mWindow = QtWidgets.QMainWindow()

    game=Arena(mWindow)
    mWindow.show()

    sys.exit(app.exec_())
