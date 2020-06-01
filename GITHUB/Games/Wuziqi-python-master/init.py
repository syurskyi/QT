import pygame
import itertools
import numpy as np
import random 
import datetime
import time

#define the game object
class wuziqi_game():
    def __init__(self):
    	#size of the surface window, can be change with set_app_size()
        self.app_size = (800,800)
        #size of the actual game board, can be change with set_board_size()
        self.board_size = (600,600)
        #RGB for colors
        self.color_white = (255,255,255)
        self.color_black = (0,0,0)
        #number for blocks, can be changed with set_block_number()
        self.block_number = (10,10)
        #width of each line, can be changed with set_line_width()
        self.line_width = 3
        #number of lines, always one more than the block number
        self.line_number = np.array(self.block_number) + 1
        #calc the block size
        self.block_size = self.app_size[0] // self.block_number[0]
        #create dictionary that contains the each joints position, use get_board()
        self.board_pos = {}
        #alphabetics for marking x_axis locations
        self.x_alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        #number of total stones
        self.total_stones = self.line_number[0] * self.line_number[1]
        #stone counter variables
        self.white_stone_number = 0
        self.black_stone_number = 0
        self.white_stone_counter_pos = (self.app_size[0]/4,(self.app_size[0] + self.board_size[0])/2+20)
        self.black_stone_counter_pos = (self.app_size[0]*3/4,(self.app_size[0] + self.board_size[0])/2+20)
        #mouse clicks variables
        self.mouse_pos = None
        self.mouse_loc = None
        #stone starting color
        self.stone_color = ['white','black'][random.randint(0,1)]
        #create a list contains all placed stone locations, updated by add_stone_location()
        self.stone_locations = []
        #stone radius 
        self.stone_radius = 20
        #Round reminder position
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
            self.line_number = np.array(number) + 1
            self.block_size = self.app_size[0] // number[0]
        else:
            print(f'Please input a number that is a int divisor of the board size:{self.board_size}')
            return 
    #calculate the distance between two vectors
    def calc_distance(self,u,v):
        return np.linalg.norm(u-v)
    #get each joints position
    def get_board(self):
        for raw in range(self.line_number[0]):
            for col in range(self.line_number[1]):
                self.board_pos[f'{self.x_alphas[col]}{raw+1}'] = [100+col*(self.board_size[0]//self.block_number[0]),100+raw*(self.board_size[0]//self.block_number[0])]
    #get mouse click position
    def get_mouse_button(self,pos):
        self.mouse_pos = pos 
    #search a joint that is closest to the mouse click position
    def search_match_point(self):
        if self.mouse_pos != None:
            distances = [self.calc_distance(np.array(i),np.array(self.mouse_pos)) for i in list(self.board_pos.values())]
            self.mouse_pos = None
            return list(self.board_pos.keys())[distances.index(min(distances))]
        else:
            pass
    #check if the move is a repeated move or not
    def isValid_move(self,loc):
        if loc in [i[0] for i in self.stone_locations]:
            return 'Repeated_Move'
        else:
            return "Good"
    #update each move 
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
    #convert the board to a numpy matrix
    def board_matrix(self):
        matrix = np.zeros(self.line_number) - 1
        for stone in self.stone_locations:
            x_pos = int(self.x_alphas.index(stone[0][0]))
            y_pos = int(stone[0][1:]) - 1
            color = ['black','white'].index(stone[1])
            matrix[y_pos][x_pos] = color
        return matrix
    #search each move's all directions--{0 degree| 90 | 45 | 135}, check if there are continous 5 same color stones
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
    #check winning status, continous 5 same color stone in one line
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
    #check if the game is tied:two player's sum of stone number equal to the total stone number
    def isDraw(self):
    	draw = (self.black_stone_number + self.white_stone_number) == self.total_stones
    	if draw:
    		return True
    	else:
    		return False
