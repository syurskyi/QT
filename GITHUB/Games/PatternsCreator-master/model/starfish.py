from PyQt5.Qt import QPointF
from enum import Enum


class StarfishType(Enum):
    Yellow = 0
    Orange = 1


class Starfish(object):
    def __init__(self):
        self._type = StarfishType.Yellow
        self._position = QPointF(0.0, 0.0)
        self._selected = False

    def type(self):
        return self._type

    def set_type(self, type):
        self._type = type

    def position(self):
        return self._position

    def set_position(self, position):
        self._position = position

    def selected(self):
        return self._selected

    def set_selected(self, selected):
        self._selected = selected
