from PyQt5.QtWidgets import QWidget

from entities.Spaceship import Spaceship
from core.utils.image_helper import get_full_image_path


class SpaceshipFactory:
    def __init__(self, screen: QWidget):
        self.screen = screen

    def create_spaceship(self, spaceship_id: str, player_id: str, color: str, x: int = 100, y: int = 100,
                         velocity: float = 0, angle: float = 0):
        if color == 'red':
            return Spaceship(screen=self.screen, x=x, y=y, velocity=velocity, angle=angle, r=30,
                             spaceship_id=spaceship_id,
                             player_id=player_id,
                             img_abs_path=get_full_image_path("spaceship_red.png"),
                             gray_img_abs_path=get_full_image_path("spaceship_red_grayscale.png"))
        elif color == 'green':
            return Spaceship(screen=self.screen, x=x, y=y, velocity=velocity, angle=angle, r=30,
                             spaceship_id=spaceship_id, player_id=player_id,
                             img_abs_path=get_full_image_path("spaceship_green.png"),
                             gray_img_abs_path=get_full_image_path("spaceship_green_grayscale.png"))
        elif color == 'yellow':
            return Spaceship(screen=self.screen, x=x, y=y, velocity=velocity, angle=angle, r=30,
                             spaceship_id=spaceship_id, player_id=player_id,
                             img_abs_path=get_full_image_path("spaceship_yellow.png"),
                             gray_img_abs_path=get_full_image_path("spaceship_yellow_grayscale.png"))
        else:
            return Spaceship(screen=self.screen, x=x, y=y, velocity=velocity, angle=angle, r=30,
                             spaceship_id=spaceship_id, player_id=player_id,
                             img_abs_path=get_full_image_path("spaceship_blue.png"),
                             gray_img_abs_path=get_full_image_path("spaceship_blue_grayscale.png"))

