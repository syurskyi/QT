from PyQt5.QtWidgets import QWidget

from core.utils.qt_utils import create_pixmap, convert_to_grayscale
from entities.MovableCircle import MovableCircle


class Spaceship(MovableCircle):
    def __init__(self, screen: QWidget, x: float, y: float, velocity: float, angle: float, r: int,
                 spaceship_id: str, player_id: str, img_abs_path: str = '',
                 gray_img_abs_path: str = ''):
        super().__init__(screen=screen, img_abs_path=img_abs_path, gray_img_abs_path=gray_img_abs_path,
                         x=x, y=y, velocity=velocity, angle=angle, r=r)
        self.spaceship_id = spaceship_id
        self.player_id = player_id
        self.is_invincible = False
        self.time_spent_invincible = 0
        self.MAX_TIME_INVINCIBLE = 250
        self.original_pixmap = self.pixmap
        self.invincible_pixmap = self.gray_pixmap

    def set_invincibility(self, is_invincible: bool):
        if not self.is_invincible and is_invincible:
            self.time_spent_invincible = 0
        self.is_invincible = is_invincible
        self._update_image()

    def _update_image(self):
        if self.is_invincible:
            self.pixmap = self.invincible_pixmap
        else:
            self.pixmap = self.original_pixmap
        self._rotate_label()

    def increase_time_invincible(self, elapsed_time: float):
        self.time_spent_invincible += elapsed_time
        if self.time_spent_invincible >= self.MAX_TIME_INVINCIBLE:
            self.set_invincibility(False)
