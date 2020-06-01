from model.starfish import Starfish
from view.drawer import PatternDrawer

from PyQt5.Qt import QPointF, QSizeF, QRectF


class Pattern(object):
    def __init__(self):
        self._name = ""
        self._starfishes = list()

    def name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def starfishes(self):
        return self._starfishes

    def add_starfish_at_position(self, position, type):
        starfish = Starfish()
        starfish.set_type(type)
        starfish.set_position(position)
        self._starfishes.append(starfish)

    def remove_starfish(self, starfish):
        self._starfishes.remove(starfish)

    def get_starfish_at_position(self, position):
        for starfish in self._starfishes:
            top_left = QPointF(starfish.position().x() - PatternDrawer.IMAGE_SIZE[0]*0.5, starfish.position().y() - PatternDrawer.IMAGE_SIZE[1]*0.5)
            rect = QRectF(top_left, QSizeF(PatternDrawer.IMAGE_SIZE[0], PatternDrawer.IMAGE_SIZE[1]))
            if rect.contains(position):
                return starfish
        return None

    def unselect_all(self):
        for starfish in self._starfishes:
            starfish.set_selected(False)

    def select_in_rect(self, rect):
        for starfish in self._starfishes:
            starfish.set_selected(rect.contains(starfish.position()))

    def is_any_selected(self):
        for starfish in self._starfishes:
            if starfish.selected():
                return True
        return False

    def move_selected_starfishes(self, delta):
        for starfish in self._starfishes:
            if starfish.selected():
                starfish.set_position(QPointF(starfish.position().x() + delta.x(), starfish.position().y() + delta.y()))
