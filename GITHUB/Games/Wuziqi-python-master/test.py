# import the pygame module, so you can use it
import pygame
import itertools
import numpy as np
import random 
import datetime
import time
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class quit_box(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Question Box'
        self.left = 500
        self.top = 300
        self.width = 300
        self.height = 300
        self.status = None
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        buttonReply = QMessageBox.question(self, 'QUIT?', "Do you want to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.status = 'QUIT'
        else:
            self.status = 'RESTART'
 
        self.show()

class win_box(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Question Box'
        self.left = 500
        self.top = 300
        self.width = 300
        self.height = 300
        self.status = None
        self.winner = None

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        buttonReply = QMessageBox.question(self, 'RESTART?', f"Congrates to {self.winner}!!\nDo you want to restart?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.status = 'RESTART'
        else:
            self.status = 'QUIT'
 
        self.show()

    def set_winner(self,name):
        self.winner = name

class wuziqi_game():
    def __init__(self):

        self.app_size = (800,800)
        self.board_size = (600,600)
        self.color_white = (255,255,255)
        self.color_black = (0,0,0)
        self.block_number = (15,15)
        self.line_width = 3
        self.line_number = np.array(self.block_number) + 1
        self.block_size = self.app_size[0] // self.block_number[0]
        self.board_pos = {}
        self.x_alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.total_stones = self.line_number[0] * self.line_number[1]
        self.white_stone_number = 0
        self.black_stone_number = 0
        self.white_stone_counter_pos = (self.app_size[0]/4,(self.app_size[0] + self.board_size[0])/2+20)
        self.black_stone_counter_pos = (self.app_size[0]*3/4,(self.app_size[0] + self.board_size[0])/2+20)
        self.mouse_pos = None
        self.mouse_loc = None
        self.stone_color = ['white','black'][random.randint(0,1)]
        self.stone_locations = []
        self.stone_radius = (self.board_size[0]/self.block_number[0])/2
        self.reminder_pos = np.array((self.app_size[0]/2,(self.app_size[0] - self.board_size[0])/5))-self.stone_radius

    def set_app_size(self,size):
        if type(size) == tuple:
            pass
        else:
            print('Please input a tuple, e.g:(800,800)')
            return 

        self.app_size = size

    def set_line_width(self,width):
        self.line_width = width

    def set_board_size(self,size):
        if type(size) != tuple:
            print('Please input a tuple, e.g:(600,600)')
            return 
        elif size[0] > self.app_size[0]:
            print(f"Please input a size that is smaller than the window size:{self.app_size}")
            return 
        else:
            pass

        self.board_size = size

    def set_block_number(self,number):
        if type(number) == tuple:
            pass
        else:
            print('Please input a tuple, e.g:(16,16)')
            return 

        if (self.board_size[0] % number[0] == 0) and (self.board_size[1] % number[1] == 0):
            self.block_number = number
            self.line_number = number + (1,1)
        else:
            print(f'Please input a number that is a int divisor of the board size:{self.board_size} ')
            return 

    def calc_distance(self,u,v):
        return np.linalg.norm(u-v)

    def get_board(self):
        for raw in range(self.line_number[0]):
            for col in range(self.line_number[1]):
                self.board_pos[f'{self.x_alphas[col]}{raw+1}'] = [100+col*(self.board_size[0]//self.block_number[0]),100+raw*(self.board_size[0]//self.block_number[0])]

    def get_mouse_button(self,pos):
        self.mouse_pos = pos 

    def search_match_point(self):
        if self.mouse_pos != None:
            distances = [self.calc_distance(np.array(i),np.array(self.mouse_pos)) for i in list(self.board_pos.values())]
            self.mouse_pos = None
            return list(self.board_pos.keys())[distances.index(min(distances))]
        else:
            pass

    def isValid_move(self,loc):
        if loc in [i[0] for i in self.stone_locations]:
            return 'Repeated_Move'
        else:
            return "Good"

    def add_stone_location(self):
        self.mouse_loc = self.search_match_point()

        if self.isValid_move(self.mouse_loc) == 'Good':
            pass
        else:
            print('Repeated move, does not count')
            return

        if self.stone_locations == []:            
            if self.stone_color == 'black':
                self.stone_locations.append([self.mouse_loc,'black'])
                self.black_stone_number += 1
                self.stone_color = 'white'
            else:
                self.stone_locations.append([self.mouse_loc,'white'])
                self.white_stone_number += 1
                self.stone_color = 'black'
        else:
            if self.stone_locations[-1][-1] == 'black':
                self.stone_locations.append([self.mouse_loc,'white'])
                self.white_stone_number += 1
                self.stone_color = 'black'
            else:
                self.stone_locations.append([self.mouse_loc,'black'])
                self.black_stone_number += 1
                self.stone_color = 'white'

        self.mouse_loc = None

    def board_matrix(self):
        matrix = np.zeros(self.line_number) - 1
        for stone in self.stone_locations:
            x_pos = int(self.x_alphas.index(stone[0][0]))
            y_pos = int(stone[0][1:]) - 1
            color = ['black','white'].index(stone[1])
            matrix[y_pos][x_pos] = color
        return matrix

    def search_all_directions(self,matrix,move):
        x_pos, y_pos, color = int(self.x_alphas.index(move[0][0])),int(move[0][1:]) - 1,['black','white'].index(move[1])
        #UP&DOWN
        up_move = y_pos
        down_move = self.block_number[0] - y_pos
        up_down_count = 1
        if up_move == 0:
            pass
        else:
            for i in range(1,up_move+1):
                if matrix[y_pos-i][x_pos] == color:
                    up_down_count += 1
                else:
                    break

        if down_move == 0:
            pass
        else:
            for i in range(1,down_move+1):
                if matrix[y_pos+i][x_pos] == color:
                    up_down_count += 1
                else:
                    break

        if up_down_count == 5:
            return 'WIN'
        else:
            pass

        #LEFT&RIGHT
        left_move = x_pos
        right_move = self.block_number[0] - x_pos
        left_right_count = 1
        if left_move == 0:
            pass
        else:
            for i in range(1,left_move+1):
                if matrix[y_pos][x_pos-i] == color:
                    left_right_count += 1
                else:
                    break

        if right_move == 0:
            pass
        else:
            for i in range(1,right_move+1):
                if matrix[y_pos][x_pos+i] == color:
                    left_right_count += 1
                else:
                    break

        if left_right_count == 5:
            return 'WIN'
        else:
            pass

        #UP_RIGHT&DOWN_LEFT
        ur_move = min(self.block_number[0] - x_pos,y_pos)
        dl_move = min(x_pos,self.block_number[0]-y_pos)
        ur_dl_count = 1
        if ur_move == 0:
            pass
        else:
            for i in range(1,ur_move+1):
                if matrix[y_pos-i][x_pos+i] == color:
                    ur_dl_count += 1
                else:
                    break

        if dl_move == 0:
            pass
        else:
            for i in range(1,dl_move+1):
                if matrix[y_pos+i][x_pos-i] == color:
                    ur_dl_count += 1
                else:
                    break

        if ur_dl_count == 5:
            return 'WIN'
        else:
            pass

        #UP_LEFT&DOWN_RIGHT
        ul_move = min(x_pos,y_pos)
        dr_move = min(self.block_number[0]-x_pos,self.block_number[0]-y_pos)
        ul_dr_count = 1
        if ul_move == 0:
            pass
        else:
            for i in range(1,ul_move+1):
                if matrix[y_pos-i][x_pos-i] == color:
                    ul_dr_count += 1
                else:
                    break

        if dr_move == 0:
            pass
        else:
            for i in range(1,dr_move+1):
                if matrix[y_pos+i][x_pos+i] == color:
                    ul_dr_count += 1
                else:
                    break

        if ul_dr_count == 5:
            return 'WIN'
        else:
            pass


    def isWin(self):

        if self.stone_locations == []:
            return False
        else:
            pass

        matrix = self.board_matrix()
        stone = self.stone_locations[-1]
        last_move = self.stone_locations[-1]
        wining = self.search_all_directions(matrix,last_move)
        if wining == 'WIN':
            return True
        else:
            return False

# define the game function
def game():
     
    # initialize the pygame module and game class
    pygame.init()
    wuziqi = wuziqi_game()
    #create the game board
    wuziqi.get_board()

    # load images
    logo = pygame.image.load("image/wuziqi.png")
    background = pygame.image.load('image/wooden_background.jpg')
    black_stone = pygame.image.load('image/black_stone.png')
    white_stone = pygame.image.load('image/white_stone.png')

    #set up logo
    pygame.display.set_icon(logo)
    pygame.display.set_caption("wuziqi")

    # create a surface on screen that has assigned size 
    screen = pygame.display.set_mode(wuziqi.app_size)

    #set up cursor appearence
    pygame.mouse.set_cursor(*pygame.cursors.arrow)
    
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT or type KEYDOWN and key is ESCAPE
            if (event.type == pygame.QUIT) or ((event.type == pygame.KEYDOWN) and (pygame.key.name(event.key) == 'escape')):
                #exit the main loop
                pygame.quit()
                return 'Normal Exit'
            #get mouse click events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #pass the mouse position to game class
                wuziqi.get_mouse_button(event.pos)
                #find match location for each mouse click and add to a list
                wuziqi.add_stone_location()
                print(wuziqi.stone_locations[-1])


        #set up background
        screen.blit(background,(0,0))

        #set up stone color reminder for players
        font = pygame.font.Font(None, 48)
        reminder_text = font.render('Round', 1, wuziqi.color_black)
        screen.blit(reminder_text,wuziqi.reminder_pos - np.array([150,-5]))
        if wuziqi.stone_color == 'black':
            screen.blit(black_stone,wuziqi.reminder_pos)
        else:
            screen.blit(white_stone,wuziqi.reminder_pos)

        #set up timer
        font = pygame.font.Font(None, 36)
        tim = str(datetime.timedelta(milliseconds=pygame.time.get_ticks()))[:-7]
        timer = font.render(tim,1,wuziqi.color_black)
        screen.blit(timer,np.array(wuziqi.app_size)-np.array([100,800]))

        #set up stone counter
        font = pygame.font.Font(None, 48)
        white_stone_number = font.render(f'{wuziqi.white_stone_number}', 1, wuziqi.color_black)
        black_stone_number = font.render(f'{wuziqi.black_stone_number}', 1, wuziqi.color_black)
        screen.blit(black_stone,np.array(wuziqi.black_stone_counter_pos)-np.array([75,5]))
        screen.blit(white_stone,np.array(wuziqi.white_stone_counter_pos)-np.array([75,5]))
        screen.blit(white_stone_number,wuziqi.white_stone_counter_pos)
        screen.blit(black_stone_number,wuziqi.black_stone_counter_pos)

        for y_pos,x_pos in enumerate(wuziqi.x_alphas[:wuziqi.line_number[0]]):

            #draw the wuziqi board
            pygame.draw.line(screen,wuziqi.color_black,wuziqi.board_pos[f"{x_pos}1"],wuziqi.board_pos[f"{x_pos}{wuziqi.line_number[0]}"],1)
            pygame.draw.line(screen,wuziqi.color_black,wuziqi.board_pos[f"A{y_pos+1}"],wuziqi.board_pos[f"{wuziqi.x_alphas[wuziqi.line_number[0]-1]}{y_pos+1}"],1)
            
            #draw axis text
            font = pygame.font.Font(None, 24)
            alphas = font.render(x_pos, 1, wuziqi.color_black)
            numerics = font.render(f"{y_pos+1}", 1, wuziqi.color_black)
            screen.blit(alphas,np.array(wuziqi.board_pos[f'{x_pos}1'])+np.array([-5,-30]))
            screen.blit(numerics,np.array(wuziqi.board_pos[f'A{y_pos+1}'])+np.array([-30,-6]))

        #display stones
        for stone in wuziqi.stone_locations:
            if stone[-1] == 'black':
                screen.blit(black_stone,np.array(wuziqi.board_pos[stone[0]])-wuziqi.stone_radius)
            else:
                screen.blit(white_stone,np.array(wuziqi.board_pos[stone[0]])-wuziqi.stone_radius)

        #check if one player won
        if wuziqi.isWin():
            pygame.quit()
            return f'{wuziqi.stone_locations[-1][-1]} Player'

        pygame.display.flip()

#define the question box function
def question_screen(types):
    if types == 'Normal Exit':
        app = QApplication(sys.argv)
        ex = quit_box()
    else:
        app = QApplication(sys.argv)
        ex = win_box()
        ex.set_winner(types)
        ex.initUI()
    return ex.status

# define the main function
def main():
    while 1:
        status = game()
        confirm = question_screen(status)
        if confirm == 'QUIT':
            print('Game Quit')
            return
        else:
            print('Game Restart')



# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()


