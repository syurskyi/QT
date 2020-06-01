from PyQt5.QtWidgets import QWidget
from PyQt5.uic.properties import QtGui

from entities.PlayerConfig import PlayerConfig
from entities.PlayerStatus import PlayerStatus


class Player:
    def __init__(self, player_id: str, spaceship_id: str, player_config: PlayerConfig = None,
                 player_status: PlayerStatus = None, num_points: int = 0, num_lives: int = 3):
        self.player_id = player_id
        self.spaceship_id = spaceship_id
        self.num_points = num_points
        self.num_lives = num_lives
        self.player_config = player_config
        self.status = player_status
        self.update_status()

    def remove_life(self):
        self.num_lives -= 1
        self.update_status()

    def update_status(self):
        self.status.update(self.player_id, self.num_lives, self.num_points)

    def add_life(self):
        self.num_lives += 1
        self.update_status()

    def increase_points(self, num_points_to_add: int):
        self.num_points += num_points_to_add
        self.update_status()

    def is_dead(self) -> bool:
        return self.num_lives <= 0
