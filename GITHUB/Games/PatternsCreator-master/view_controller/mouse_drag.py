from PyQt5.Qt import QPointF


class MouseDrag(object):
    def __init__(self):
        self._start_position = None
        self._position = None
        self._delta = QPointF(0, 0)
        self._total_offset = QPointF(0, 0)

    def total_offset(self):
        return self._total_offset

    def start_position(self):
        return self._start_position

    def end_position(self):
        return self._position

    def delta(self):
        return self._delta

    def is_started(self):
        return self._start_position is not None

    def start_drag(self, position):
        self._start_position = position
        self._position = position

    def end_drag(self):
        self._start_position = None
        self._position = None

    def move_drag(self, position):
        self._delta = position - self._position
        self._total_offset += self._delta
        self._position = position
