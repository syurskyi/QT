from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QWidget

from core.utils.qt_utils import create_label, create_pixmap, rotate_pixmap
from entities.MovableObject import MovableObject


class MovableCircle(MovableObject):
    def __init__(self, screen: QWidget, x: float = 0, y: float = 0, velocity: float = 0, angle: float = 0, r: int = 1,
                 img_abs_path: str = "", gray_img_abs_path: str = ""):
        super().__init__(x=x, y=y, velocity=velocity, angle=angle)
        self.r = r
        self.img_abs_path = img_abs_path
        self.image = QImage(img_abs_path)
        self.gray_image = QImage(gray_img_abs_path)
        self.screen = screen
        self.label = create_label(screen=screen, r=r)
        self.pixmap = create_pixmap(label=self.label, image=self.image)
        self.gray_pixmap = create_pixmap(label=self.label, image=self.gray_image)
        self._rotate_label()
        self.label.show()
        self.move(0)

    @property
    def top_left_x(self):
        return self.x - self.r

    @property
    def top_left_y(self):
        return self.y - self.r

    def rotate_left(self):
        super().rotate_left()
        self._rotate_label()

    def rotate_right(self):
        super().rotate_right()
        self._rotate_label()

    def _rotate_label(self):
        self.label.setPixmap(rotate_pixmap(self.pixmap, self.angle + 90))
        self.label.update()

    def move(self, elapsed_time: float):
        super().move(elapsed_time)
        self.label.move(self.top_left_x, self.top_left_y)
        self.label.update()

    def move_off_screen(self):
        self.x = 0 - self.r * 2 - 100
        self.y = 0 - self.r * 2 - 100
        self.label.hide()

    def is_off_screen(self, screen_width: int, screen_height: int):
        return (self.x + self.r) < 0 or (self.x - self.r) > screen_width or \
               (self.y + self.r) < 0 or (self.y - self.r) > screen_height

    def destroy(self):
        self.label.hide()

    def is_hidden(self):
        return self.label.isHidden()
