from PyQt5.QtWidgets import QWidget

from entities.Heart import Heart
from core.utils.image_helper import get_full_image_path


class HeartFactory:
    def __init__(self, screen: QWidget):
        self.screen = screen

    def create_heart(self, player_id: str, x: int = 100, y: int = 100, velocity: float = 0
                     , angle: float = 270, r: int = 15):
        return Heart(screen=self.screen, x=x, y=y, velocity=velocity, angle=angle, r=r, player_id=player_id,
                     img_abs_path=get_full_image_path("heart.png"))
