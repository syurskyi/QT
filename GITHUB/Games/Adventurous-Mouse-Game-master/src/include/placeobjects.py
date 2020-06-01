# -*- coding: utf-8 -*-
from include.gameicon import GameIcon

def placeObjects(gameFrame, path, level, stage):
    """
    Place objects (mouse, cheeses and moustraps) in the game's frame.
    Objects are defined by the coordinates in the screen.

    Parameters:
        gameFrame (QWidget).
        path (str): Path to where object icons are stored.
        level (int): Difficulty level (0: Easy, 1: Medium, 2: Hard).
        stage (int): Level's stage (0, 1 or 2).

    Returns:
        cheeseList (list of GameIcon): List of cheeses of the chosen levels stage.
        trapList (list of GameIcon): List of mousetraps of the chosen levels stage.
        mouseObject (GameIcon): The moving object (the mouse), in the beginning of game's frame [coordinates (0, 0)].
    """

    cheesePoints, cheeseList = [], []
    trapPoints, trapList = [], []

    mouseIcon = path+'mouse_icon.png'
    cheeseIcon = path+'cheese_icon.png'
    trapIcon = path+'trap_icon.png'

    if level == 0:
        if stage == 1:
            cheesePoints = [(135, 80), (430, 120), (565, 320), (340, 270), (65, 350)]
        elif stage == 2:
            cheesePoints = [(135, 50), (325, 120), (565, 40), (500, 185), (180, 220), (385, 330), (600, 380), (25, 420)]
        else:
            cheesePoints = [(295, 70), (625, 25), (85, 285), (355, 250), (545, 435)]
    elif level == 1:
        if stage == 1:
            cheesePoints = [(185, 35), (75, 315), (465, 130), (455, 295)]
            trapPoints = [(325, 100), (270, 315)]
        elif stage == 2:
            cheesePoints = [(145, 40), (110, 280), (310, 170), (610, 410)]
            trapPoints = [(345, 55), (160, 160), (550, 330)]
        else:
            cheesePoints = [(280, 60), (15, 325), (515, 410), (620, 280)]
            trapPoints = [(185, 25), (40, 175), (225, 165), (550, 325)]
    else:
        if stage == 1:
            cheesePoints = [(35, 255), (630, 25), (640, 415)]
            trapPoints = [(105, 15), (10, 110), (80, 165), (145, 220), (210, 280), (110, 375), (235, 70), (340, 110)]
            trapPoints += [(260, 135), (450, 20), (435, 150), (600, 100), (385, 285), (570, 250), (515, 380), (655, 340)]
        elif stage == 2:
            cheesePoints = [(145, 235), (305, 245), (640, 435)]
            trapPoints = [(85, 45), (75, 125), (85, 205), (70, 280), (75, 360), (205, 125), (215, 225), (160, 290), (175, 440)]
            trapPoints += [(280, 80), (290, 205), (300, 365), (440, 40), (360, 150), (365, 225), (385, 295), (385, 365), (575, 90)]
            trapPoints += [(510, 185), (470, 310), (620, 380), (490, 450)]
        else:
            cheesePoints = [(150, 10), (650, 15), (355, 225), (650, 425)]
            trapPoints = [(100, 40), (130, 105), (15, 160), (70, 265), (230, 15), (175, 175), (170, 265), (195, 340), (305, 25)]
            trapPoints += [(335, 165), (260, 205), (290, 270), (330, 390), (430, 75), (405, 205), (405, 265), (410, 340), (515, 75)]
            trapPoints += [(595, 85), (630, 155), (555, 205), (560, 320), (580, 385), (515, 445)]

    for cheesePoint in cheesePoints:
        cheeseList.append(GameIcon(gameFrame, cheeseIcon, cheesePoint))

    for trapPoint in trapPoints:
        trapList.append(GameIcon(gameFrame, trapIcon, trapPoint))

    return cheeseList, trapList, GameIcon(gameFrame, mouseIcon, (0, 0), True)
