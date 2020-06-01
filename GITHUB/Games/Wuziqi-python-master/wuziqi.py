#!/usr/bin/env python 3.6.3
# -*- coding: utf-8 -*-

"""wuziqi.py: A classic Chinese game, based on PyGame&PyQt5."""

__author__    = "Hao Zhu"
__copyright__ = "Copyright 2019, WuziqiGame"
__date__      = '2019/02/09'
__license__   = "MIT"
__version__   = "1.0.0"
__email__     = "hz808@nyu.edu"

'''
import all modules 
init -- the main game class
game -- the main game function
question -- the question box class&function
'''
from init import *
from question import *
from game import *

# define the main function
def main():
    while 1:
        #define the initial status
        status = "Game Start"
        #Choose board size
        size_selection = question_screen(status)
        #run the game function and check the exit status
        status = game(size_selection)
        #two exit status:win/quit, ask if restart is needed or just exit
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