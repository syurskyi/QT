from PyQt5.Qt import QPointF


class Transformations(object):
    def __init__(self, frame_widget, drag_mouse):
        self._frame_widget = frame_widget
        self._drag_mouse = drag_mouse

    def point_from_screen(self, point):
        geometry = self._frame_widget.geometry()
        offset = self._drag_mouse.total_offset()
        x = point.x() - geometry.width() * 0.5 - offset.x()
        y = point.y() - geometry.height() * 0.5 - offset.y()
        return QPointF(x, y)

    def point_to_screen(self, point):
        geometry = self._frame_widget.geometry()
        offset = self._drag_mouse.total_offset()
        x = point.x() + geometry.width() * 0.5 + offset.x()
        y = point.y() + geometry.height() * 0.5 + offset.y()
        return QPointF(x, y)

    def rect_to_screen(self, rect):
        t = type(rect)
        top_left = self.point_to_screen(rect.topLeft())
        return t(top_left, rect.size())

    def rect_from_screen(self, rect):
        t = type(rect)
        top_left = self.point_from_screen(rect.topLeft())
        return t(top_left, rect.size())
