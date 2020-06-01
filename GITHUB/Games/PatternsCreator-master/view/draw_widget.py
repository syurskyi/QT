from PyQt5.QtWidgets import QWidget


class DrawWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(0, 0, parent.geometry().width(), parent.geometry().height())
        self.show()
        self._draw_elements = list()

    def add_draw_element(self, element):
        self._draw_elements.append(element)
        self.update()

    def paintEvent(self, paint_event):
        for draw_element in self._draw_elements:
            draw_element.paint_event(self, paint_event)
