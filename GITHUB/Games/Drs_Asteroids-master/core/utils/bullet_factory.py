from PyQt5.QtWidgets import QWidget

from entities.Bullet import Bullet
from core.utils.image_helper import get_full_image_path


class BulletFactory:
    def __init__(self, screen: QWidget):
        self.screen = screen

    def create_bullet(self, player_id: str, color: str, x: int = 0, y: int = 0, velocity: float = 5,
                      angle: float = 0, r: int = 5):
        if color == 'red':
            return Bullet(screen=self.screen, x=x, y=y, velocity=velocity, angle=angle, r=r, player_id=player_id,
                          color=color,
                          img_abs_path=get_full_image_path("bullet_red.png"))
        elif color == 'green':
            return Bullet(screen=self.screen, x=x, y=y, velocity=velocity, angle=angle, r=r, player_id=player_id,
                          color=color,
                          img_abs_path=get_full_image_path("bullet_green.png"))
        elif color == 'yellow':
            return Bullet(screen=self.screen, x=x, y=y, velocity=velocity, angle=angle, r=r, player_id=player_id,
                          color=color,
                          img_abs_path=get_full_image_path("bullet_yellow.png"))
        elif color == 'blue':
            return Bullet(screen=self.screen, x=x, y=y, velocity=velocity, angle=angle, r=r, player_id=player_id,
                          color=color,
                          img_abs_path=get_full_image_path("bullet_blue.png"))
