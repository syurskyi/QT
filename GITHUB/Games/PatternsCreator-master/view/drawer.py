from model.starfish import StarfishType

from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt5 import QtCore
from PyQt5.Qt import QPoint, QRectF

import os


class Drawer(object):
    def paint_event(self, draw_widget, paint_event):
        raise Exception("paint_event() must be overridden")


class GuidelinesDrawer(Drawer):
    def __init__(self, drag_mouse):
        super().__init__()
        self._drag_mouse = drag_mouse

    def paint_event(self, draw_widget, paint_event):
        painter = QPainter()
        painter.begin(draw_widget)
        pen = QPen(QtCore.Qt.black, 3)
        painter.setPen(pen)

        offset = self._drag_mouse.total_offset()

        width = paint_event.rect().width()
        height = paint_event.rect().height()
        half_width = width * 0.5 + offset.x()
        half_height = height * 0.5 + offset.y()

        painter.drawLine(half_width, 0, half_width, height)
        painter.drawLine(0, half_height, width, half_height)

        painter.setPen(QPen(QtCore.Qt.black, 1))
        separation = 25
        n_vertical_left = int(half_width / separation)
        for i in range(1, n_vertical_left+1):
            x = half_width - separation * i
            painter.drawLine(x, 0, x, height)
        n_vertical_right = int((width - half_width) / separation)
        for i in range(1, n_vertical_right+1):
            x = half_width + separation * i
            painter.drawLine(x, 0, x, height)

        n_horizontal_top = int(half_height / separation)
        for i in range(1, n_horizontal_top+1):
            y = half_height - separation * i
            painter.drawLine(0, y, width, y)
        n_horizontal_bottom = int((height - half_height) / separation)
        for i in range(1, n_horizontal_bottom+1):
            y = half_height + separation * i
            painter.drawLine(0, y, width, y)
        painter.end()


class PatternDrawer(Drawer):
    IMAGE_SIZE = (56, 50)

    class Asset(object):
        def __init__(self, normal, selected):
            self.normal = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", normal))
            self.selected = QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", selected))

    def __init__(self, transformations, selection_drag):
        self._transformations = transformations
        self._selection_drag = selection_drag
        self._pattern = None
        self._assets_by_type = {
            StarfishType.Yellow: PatternDrawer.Asset("res/starfish_orange.png", "res/starfish_orange_selected.png"),
            StarfishType.Orange: PatternDrawer.Asset("res/starfish_yellow.png", "res/starfish_yellow_selected.png"),
        }

    def set_pattern(self, pattern):
        self._pattern = pattern

    def paint_event(self, draw_widget, paint_event):
        if self._pattern is None:
            return

        painter = QPainter()
        painter.begin(draw_widget)
        pen = QPen(QtCore.Qt.black, 1)
        painter.setPen(pen)
        for starfish in self._pattern.starfishes():
            position = self._transformations.point_to_screen(starfish.position())
            center = QPoint(position.x() - self.IMAGE_SIZE[0]*0.5, position.y() - self.IMAGE_SIZE[1]*0.5)
            painter.drawPixmap(center, self._pixmap_for_starfish(starfish))
        painter.end()

    def _pixmap_for_starfish(self, starfish):
        asset = self._assets_by_type[starfish.type()]
        if starfish.selected():
            return asset.selected
        else:
            return asset.normal


class SelectionDrawer(Drawer):
    def __init__(self, transformations, mouse_drag):
        super().__init__()
        self._transformations = transformations
        self._mouse_drag = mouse_drag

    def paint_event(self, draw_widget, paint_event):
        if self._mouse_drag.is_started():
            painter = QPainter()
            painter.begin(draw_widget)
            pen = QPen(QtCore.Qt.white, 1)
            painter.setPen(pen)
            rect = self._transformations.rect_to_screen(QRectF(self._mouse_drag.start_position(), self._mouse_drag.end_position()))
            painter.drawRect(rect)
            painter.fillRect(rect, QColor(255, 255, 255, 85))
            painter.end()

