""" 
    Batteships game. Basics of IT semester project.
    Author: Piotr Kucharski 
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

import window

def main():
    game = QApplication(sys.argv)
    gameWindow = window.Window()

    sys.exit(game.exec_())

if __name__ == "__main__":
    main()