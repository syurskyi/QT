# Drs_Asteroids

[![Board Status](https://dev.azure.com/dakenzi97/01c2902e-59ee-433b-aa35-c40b021d674a/09380402-6d26-4f33-9bb5-8b83e83e272a/_apis/work/boardbadge/fb528986-8ca7-489e-94e9-fdd74a1cb627)](https://dev.azure.com/dakenzi97/01c2902e-59ee-433b-aa35-c40b021d674a/_boards/board/t/09380402-6d26-4f33-9bb5-8b83e83e272a/Microsoft.RequirementCategory/)

School project for a Distributed Computer System class in Faculty of Technical Sciences - Novi Sad. The goal is to recreate Asteroids game using PyQt5.

## Table of Contents

- [Getting Started](#Getting-Started)
  - [Prerequisites](#Prerequisites)
  - [Setup](#Setup)
- [Usage Guide](#Usage-Guide)
  - [Menu](#Menu)
  - [Key Bindings](#Key-Bindings)
  - [Game Rules](#Game-Rules)
- [Architecture](#Architecture)
  - [Entities](#Entities)
  - [Storage](#Storage)
  - [Core](#Core)
  - [Bootstrappers](#Bootstrappers)

---

## Getting Started

Use these instructions to get the project up and running.

### Prerequisites

You will need the following tools:

- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Python3](https://www.python.org/)
- [PyQt5](https://pypi.org/project/PyQt5/)

### Setup

Follow these steps to get your development environment set up:

1. Open project in `PyCharm`
1. Run `__main__.py` as start project

---

## Usage Guide

This section will focus on how to use this application, as well as give brief explanation on what each display does.

### Menu

Once you start application you are greeted with starting menu.

![Starting Menu](./doc/menu.PNG)

From here you have option to start singleplayer game, multiplayer, tournament, to see high scores or to exit game.

All of the buttons (except `Score`) lead you to "settings" page from which you can chose your username and ship.

![Multiplayer Setting](./doc/multiplayer-settings.PNG)

### Key Bindings

Local multiplayer has following key bindings:

| Action | Player1 | Player2 |
| :--- | :---: | ---: |
| **Shoot**  | `Spacebar`  | `Ctrl`|
| **Accelerate** | `Up-Arrow` | `W` |
| **Deccelerate** | `Down-Arrow` | `S` |
| **Rotate Left** | `Left-Arrow` | `A` |
| **Rotate Right** | `Right-Arrow` | `D` |

### Game Rules

At the start of the game two players spawn at the center and asteroids are going towards them.

![Game display 2](./doc/in_game_screen_2.PNG)

As they destroy asteroids they gain points which is displayed at the upper-left corner of the screen, as well as the name of the game (ex. "Game 1", "Game 2" or "Finale" in case of Tournament)

![Tournament Game Info](./doc/tournament_game_display.PNG)

Once both players are dead, the winner is the one who earned most points and his name is displayed on screen, with `Ok` button.

![Winner display](./doc/winner_display.PNG)

> In case of tournament clicking on `Ok` button will start next game in tournament

#### Additional rules

- Destroying asteroid will split it into two smaller parts (100 points for biggest, 150 for medium, and 200 for smallest)
- At the start of new level all players that are alive will get 1000 points as reward
- Players cannot hit each other
- Upon hitting an asteroid players spaceship will _"grey out"_ for few seconds. During this time he will be invulnerable and he won't be able to shoot bullets.
- Collecting `heart` will grant player extra life.

---

## Architecture

### Entities

![Entities Class Diagram](./doc/entities_uml.PNG)

Core class that is used for `x`, and `y` calculations (movement) is `MovableObject` class. It's methods are strictly tied to movement (such as `accelerate`, `deccelerate` and `rotate`)

Using the decorator pattern (or it's variant) `MovableCircle` "decorates" it's parent's behavior by also updating the `Screen` (passed in it's constructor) upon calling any of the methods:

```python
class MovableCircle(MovableObject):
  # ...
  def move(self, elapsed_time: float):
    super().move(elapsed_time)
    self.label.move(self.top_left_x, self.top_left_y)
    self.label.update()
  # ...
```

Thus `MovableCircle` and it's variants are actually more of "ViewModel" classes then regular entities to be stored in databases since they have rendering logic instead of just raw data.

![Player Class Diagram](./doc/player_Uml.PNG)

Similarly, `Player` class calls `PlayerStatus`'s `update` method upon each modification to update player score label in the top left corner.

```python
class Player
    # ...
    def remove_life(self):
        self.num_lives -= 1
        self.update_status()

    def update_status(self):
        self.status.update(self.player_id, self.num_lives, self.num_points)
    # ...
```

### Storage

Acts like a local database. It holds collection of entities, also acts like repository by providing helpers methods such as "get_player_with_most_points", "get_alive_players" and similar, for cleaner code that is easier to mantain.

### Core

![Core Class Diagram](./doc/core_uml.PNG)

`Core` folder holds core business logic for the game such as collision handling, position calculations, level creation, key-press handling and rendering.

For each of these tasks mentioned aboved there exists a "handler" class that handles that part of the logic (as to adhere to SOLID principles)

These handlers are then injected into `Game` class following the Strategy/Behavior design pattern who are then called from it's `start` (called once) and `update` (called periodically) methods.

### Bootstrappers

Classes like `AsteroidsGame` are "bootstrappers", meaning that they know how to handle **dependency injection** and start `Game` by calling their `start` method
