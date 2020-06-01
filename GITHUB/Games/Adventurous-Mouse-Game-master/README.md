# Adventurous Mouse Game

> A simple game which consists of guiding a mouse towards objective points (cheese), both located in a 2D interface. The mouse is moved in the direction of an arrow described by two colors: start and end, thus, it's about detecting the arrow's direction defined by these colors (choosen manually). These shoud be preferably in a uniform background (for precise detection).

## General Info

Project realized in **January 2020** as a university practical work, field : *Artificial Intelligence (AI)*, level : *Master 2*. The goal was to put into practice the different *OpenCV*'s functions related to the artificial processing of digital images for the creation of a small game.

## ScreenShots

<p align="center">
    <p align="center">
      <img width="60%" height="40%" src="screenShots/gameInProgress.png" alt="Game in progress">
    </p>
    <p align="center">
      <img width="40%" height="60%" src="screenShots/gameWonStatus.png" alt="Game 'Won' status">
      <img width="40%" height="60%" src="screenShots/gameOverStatus.png" alt="Game 'Over' status">
    </p>
</p>

## Project content

```text
.
├── screenShots                     <- Contains images used as illustration of the game
│
├── src                             <- Contains Python source-code of the project
│    ├── icons                      <- Contains different objects icons used in the game
│    │
│    ├── include                    <- Contains the core of the game (functions and classes)
│    │      ├── colors.xml          <- Color definition file, minimum and maximum color thresholds
│    │      ├── detect.py           <- Color contour and arrow direction detection function
│    │      ├── gamegroup.py        <- Class of the game interface (current state and movement of objects)
│    │      ├── gameicon.py         <- Class of a game object (location and collision detection)
│    │      ├── importcolors.py     <- Import function for colors defined in "colors.xml"
│    │      ├── mainwindow.py       <- Main GUI class of the application (grouping of the game interface, settings and camera capture)
│    │      ├── paramsgroup.py      <- Class of game parameters (colors, speed and difficulty levels)
│    │      └── placeobjects.py     <- Function for defining difficulty levels (placing objects in the game interface)
│    │
│    └── __main__.py                <- Application entry point (the main file to execute)
│
├── Report.pdf                      <- Project report: Detailed description of developed algorithms for the game (in French)
│
└── README.md                       <- Current project info
```

## Technologies

- **Python** (Used version: *3.7.4*), with some external packages:
  - [**OpenCV**](https://pypi.org/project/opencv-python/) (Used version: *4.1.2*).
  - [**Numpy**](https://pypi.org/project/numpy/) (Used version: *1.16.5*).
  - [**PyQt5**](https://pypi.org/project/PyQt5/) (Used version: *5.13.1*).

## Application use

To run this game, make sure that all the packages are installed. Then, an adjustment of the min/max thresholds for the colors to be detected (which define the arrow) in HSV format must be made. For this, a modification of the values and/or addition of other colors is necessary in the file ***"./src/include/colors.xml"*** (respecting the syntax described in the comment at the beginning of the file) which contains by default two colors: *red* and *green*. Finally, the game can be launched via the entry point:

```bash
$ python3 src/__main__.py
```

## Features

- Detection of an arrow described by two colors (start and end):
  - Identification of the contours of each color by drawing the *AABB (Axis-Aligned Bounding Box)*.
  - Specification of the angle (in an interval [0, 360]°) created by the arrow.
  - Definition of the direction of the arrow (8 possible directions).

- A simple game based on moving a mouse according to the detected arrow:
  - Collision detection with other objects (eating cheeses while avoiding mice traps).
  - Adjustment of the speed of movement.
  - Three difficulty levels (easy, medium and hard) with three stages each.

## Status

Since this simple game was developed as a practical work, it will **no longer be developed or improved**.
