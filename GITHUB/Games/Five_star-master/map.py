import matplotlib
import numpy as np
import random
# color_dict ={'green':0, 'red':1, 'yellow':2, 'blue':3, 'brown':4}
# color_dict = {v:k for k,v in color_dict.items()}
content = {1:'blue', 2:'black', 3:'red',4:'yellow',5:'brown'}
colors = {'blue':[0,0,255], 'red':[255,0,0], 'black':[0,0,0], 'yellow':[210,105,30], 'brown':[46,139,87]}
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import time
class Cell:

    def __init__(self, x: int = 0, y: int = 0, color: str = None):
        self.x = x
        self.y = y
        self.color_str = color

    def set_valid(self):
        self.color_str = None

    def _set_color(self, color):
        self.color_str = color

    def position(self):
        return self.x,  self.y

    def get_color(self):
        return self.color_str

    def __bool__(self):
        if self.color_str is None:
            return True
        else:
            return False

    def is_empty(self):
        return self.__bool__()

class Mylabel(QtWidgets.QLabel, Cell):

    selected_signal = QtCore.pyqtSignal(int,int)
    pressed_but_nonselect_signal = QtCore.pyqtSignal(int,int)

    def __init__(self, x, y, size=None, color=None, parent=None, if_valid=True):
        """
        This label class successes two father classes: QLabel and Cell
        in order to add coordinate and color information
        Add press signal to add click event to this cell which the previous origianal QLable doesn't exist
        :param x: int the row at which this label stays
        :param y: int the col at which this label stays
        :param size: the size (x_dimension, y_dimension) and default is (50,50)
        :param color: str color.... from the content(see above)
        :param parent: Qwidget parent of this label
        :param if_valid: bool whether to set this label to valid
        """
        super(Mylabel,self).__init__(parent)
        if size is None:
            size = [50, 50]
        self.x = x
        self.y = y
        self.color_str = color
        self.selected = False
        self.label_pressed = False
        self.setMinimumSize(size[0], size[1])
        self.setMaximumSize(size[0], size[1])
        self.setFrameShape(QtWidgets.QFrame.Box)
        self.setStyleSheet("border-width: 1px;border-style: solid;border-color: rgb(255, 170, 0);")
        self.setObjectName('Label_'+str(x)+str(y))
        if if_valid:
            self.set_valid()
        # self.color = pyqtProperty(QColor, fset=self._set_color)

    def mousePressEvent(self, ev:QtGui.QMouseEvent):
        # check_
        print(self.objectName(),' pressed')
        self.label_pressed = True

    def mouseReleaseEvent(self, ev: QtGui.QMouseEvent) -> None:
        print(self.objectName(),' released')
        if self.label_pressed:
            if self.color_str is not None:
                self.selected = True
                print('emit selected_signal')
                self.selected_signal.emit(self.x, self.y)
            else:
                # this cell is empty then there are two cases:
                # 1.This cell is the destination user selected
                # 2.user click this cell for other reason, so do nothing
                print('emit pressed_but_nonselect_signal')
                self.pressed_but_nonselect_signal.emit(self.x, self.y)
            self.label_pressed = False

    def _set_color(self, color_):
        self.clear()
        if type(color_)  == str:
            qcolor = QtGui.QColor(*(colors[color_]))
            self.color_str = color_
        elif type(color_) == QtGui.QColor:
            qcolor = color_
        else:
            qcolor = QtGui.QColor(*color_)
        pix = QtGui.QPixmap(50,50)
        pix.fill(QtGui.QColor(255, 255, 255))
        painter = QtGui.QPainter()
        painter.begin(pix)
        painter.setBrush(qcolor)
        painter.drawEllipse(QtCore.QPoint(25,25),23,23)
        painter.end()
        # pix.fill(QtGui.QColor(*(colors[color_])))
        self.setPixmap(pix)

    def set_valid(self):
        self.color_str = None

        self.selected = False
        self.clear()
        pix = QtGui.QPixmap(50,50)
        pix.fill(QtGui.QColor(255,255,255))
        self.setPixmap(pix)
        self.label_pressed = False

class Map:

    def __init__(self, size: tuple,parent,main_app, cell_type:object=Mylabel):
        self.size = size
        self.data = np.empty(size, dtype=Mylabel)
        self.main_app =main_app
        for x in range(size[0]):
            for y in range(size[1]):
                self.data[x][y] = Mylabel(x,y,parent=parent)

    def is_valid(self, loc):
        return self.data[loc[0], loc[1]].is_empty()

    def clear_all(self):
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                self.data[x, y].set_valid()

    def get_valid_map(self):
        """

        :return: np.array, dtype is Bool
        """
        map_valid = np.empty_like(self.data)
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                map_valid[x,y] = self.data[x,y].is_empty()
        return map_valid

    def set_loc_color(self, loc, color):
        """

        :param loc: tuple/array
        :param color: string type!!!!!
        :return:
        """
        self.data[loc[0], loc[1]]._set_color(color)

    def clear_loc(self, loc):
        self.data[loc[0],loc[1]].set_valid()

    def flash_starttoend(self, path):
        print('进入移动动画')
        path = path.copy()
        path = path.astype(np.int)
        color = self.get_loc_color(path[:,0])
        previous_loc = path[:,0]
        current_loc = path[:,1]
        for i in range(2, path.shape[1]):
            self.clear_loc(previous_loc)
            self.set_loc_color(current_loc, color)
            self.main_app.processEvents()
            time.sleep(0.05)
            previous_loc = current_loc
            current_loc = path[:, i]
            i += 1
        self.clear_loc(previous_loc)
        self.set_loc_color(current_loc, color)
    def get_valid_num(self):
        map_valid = self.get_valid_map()
        index = np.where(map_valid == True)
        return index[0].shape[0]

    def rand_gen(self, num=2):
        # get heat map
        map_valid = self.get_valid_map()
        total_kill = 0
        # print(map_valid)
        # get the valid indexes
        # index is as tuple of two arrays, the first is x, the second is y
        index = np.where(map_valid == True)
        # print(index)
        valid_num = index[0].shape[0]
        index_ran = random.sample(range(valid_num), min(num,valid_num))
        if valid_num == 0:
            print('The Space is full no space to generate new cells !!!!!')
            return None
        for i in index_ran:
            color_ran = content[random.randint(1,5)]
            self.set_loc_color((index[0][i], index[1][i]), color_ran)
            total_kill += self.judge_five([index[0][i], index[1][i]])
            print('Change the ({}, {}) location into {}'.format(index[0][i],index[1][i], color_ran))
        return total_kill

    def get_loc_color(self,loc):
        return self.data[loc[0],loc[1]].color_str

    def judge_five(self, loc:np.array):
        print('enter judge five')
        loc_color = self.get_loc_color(loc)
        print('current loc is', loc, 'current_color is', loc_color)
        clear_flag = False
        total_kill = 0
        if loc_color is None:
            return
    #     check vertical and horizontal
        for dim in [0,1]:
            num = 1
            five_ls = []
            for orientation in [-1,1]:
                loc_new = loc.copy()
                while True:
                    loc_new[dim] += orientation
                    loc_copy = loc_new.copy()
                    # print(loc_new)
                    if loc_new[0] <0 or loc_new[0]>self.size[0]-1 or loc_new[1] <0 or loc_new[1]>self.size[1]-1:
                        break
                    current_color = self.get_loc_color(loc_new)
                    if current_color == loc_color:
                        num += 1
                        five_ls.append(loc_copy)
                    else:
                        break
            print('the star number is', num)
            if num >= 5:
                clear_flag = True
                total_kill += num-1
                for remove_loc in five_ls:
                    self.clear_loc(remove_loc)
    # check cross
        for flag in [-1, 1]:

            five_ls = []
            num = 1
            for orientation in [1,-1]:
                loc_new = loc.copy()
                while True:
                    loc_new[0] += orientation
                    loc_new[1] += orientation*flag
                    loc_copy = loc_new.copy()
                    if loc_new[0] <0 or loc_new[0]>self.size[0]-1 or loc_new[1] <0 or loc_new[1]>self.size[1]-1:
                        break
                    current_color = self.get_loc_color(loc_new)
                    if current_color == loc_color:
                        num += 1
                        five_ls.append(loc_copy)
                    else:
                        break
            if num >= 5:
                clear_flag = True
                total_kill += num-1
                for remove_loc in five_ls:
                    self.clear_loc(remove_loc)
        if clear_flag is True:
            self.clear_loc(loc)
            total_kill += 1
        return total_kill

    def step(self,loc_start, loc_end):
        self.set_loc_color(loc_end,self.data[loc_start[0],loc_start[1]].get_color())
        self.clear_loc(loc_start)
        self.rand_gen()


if __name__ == '__main__':
    pass
