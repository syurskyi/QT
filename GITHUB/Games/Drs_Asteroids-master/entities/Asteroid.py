from PyQt5.QtWidgets import QWidget

from entities.MovableCircle import MovableCircle


def _divide_asteroid(_):
    return []


class Asteroid(MovableCircle):
    def __init__(self,  screen: QWidget, x: float = 0, y: float = 0, velocity: float = 0, angle: float = 0, r: int = 1,
                 points: int = 1, img_abs_path: str = "", divide_asteroid=_divide_asteroid):
        super().__init__(screen=screen, img_abs_path=img_abs_path, x=x, y=y, velocity=velocity, angle=angle, r=r)
        self.points = points
        self._divide = divide_asteroid

    def divide(self):
        return self._divide(self)
