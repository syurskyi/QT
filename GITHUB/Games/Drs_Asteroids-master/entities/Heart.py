from PyQt5.QtWidgets import QWidget

from entities.MovableCircle import MovableCircle


class Heart(MovableCircle):
    def __init__(self,  screen: QWidget, x: int, y: int, velocity: float, angle: float, r: int
                 , player_id: str = "", img_abs_path: str = ""):
        super().__init__(screen=screen, img_abs_path=img_abs_path, x=x, y=y, velocity=velocity, angle=angle, r=r)
        self.player_id = player_id
