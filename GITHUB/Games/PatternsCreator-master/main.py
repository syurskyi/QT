from view_controller.mouse_drag import MouseDrag
from view_controller.transformations import Transformations
from view.draw_widget import DrawWidget
from view.drawer import GuidelinesDrawer, SelectionDrawer, PatternDrawer
from factory.pattern_factory import PatternFactory
from model.starfish import StarfishType

from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import QPoint, QRectF
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QListWidgetItem, QApplication
from main_window import Ui_MainWindow

import sys
import json
import random


class AppWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.file_path = None
        self.patterns = list()
        self.pattern = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionOpen.setShortcut("Ctrl+O")
        self.ui.actionOpen.triggered.connect(self.on_open_file)

        self.ui.actionSave.setShortcut("Ctrl+S")
        self.ui.actionSave.triggered.connect(self.on_save_file)

        self.ui.actionSaveAs.setShortcut("Ctrl+Shift+S")
        self.ui.actionSaveAs.triggered.connect(self.on_save_file_as)

        self.ui.actionAddPattern.setShortcut("Ctrl+A")
        self.ui.actionAddPattern.triggered.connect(self.on_add_pattern)

        self.ui.actionRemovePattern.setShortcut("Ctrl+R")
        self.ui.actionRemovePattern.triggered.connect(self.on_remove_pattern)

        self.ui.listWidget.currentRowChanged.connect(self.patterns_list_row_changed)
        self.ui.listWidget.itemChanged.connect(self.on_patterns_list_item_changed)

        self.span_mouse = MouseDrag()
        self.select_mouse = MouseDrag()
        self.move_mouse = MouseDrag()
        self.setMouseTracking(True)
        self.pattern_factory = PatternFactory()
        self._transformations = Transformations(self.ui.patternFrame, self.span_mouse)

        self._draw_widget = DrawWidget(self.ui.patternFrame)
        self._draw_widget.setObjectName("draw-widget")
        self.ui.horizontalLayout_3.addWidget(self._draw_widget)

        guidelines = GuidelinesDrawer(self.span_mouse)
        self._draw_widget.add_draw_element(guidelines)

        selection = SelectionDrawer(self._transformations, self.select_mouse)
        self._draw_widget.add_draw_element(selection)

        self._pattern_drawer = PatternDrawer(self._transformations, self.select_mouse)
        self._draw_widget.add_draw_element(self._pattern_drawer)

    def mouseReleaseEvent(self, mouse_event):
        if self.span_mouse.is_started():
            self.span_mouse.end_drag()
        elif self.select_mouse.is_started():
            self.select_mouse.end_drag()
        elif self.move_mouse.is_started():
            self.move_mouse.end_drag()
        else:
            keyboard_modifiers = QApplication.keyboardModifiers()
            if self.pattern is None or keyboard_modifiers == QtCore.Qt.ControlModifier or keyboard_modifiers == QtCore.Qt.AltModifier:
                return
            if self.pattern is not None and self.pattern.is_any_selected():
                self.pattern.unselect_all()
                self._draw_widget.update()
                return
            position = QPoint(mouse_event.x(), mouse_event.y())
            position = self.mapToGlobal(position)
            position = self.ui.patternFrame.mapFromGlobal(position)
            frame_geometry = self.ui.patternFrame.geometry()
            if position.x() >= 0 and position.x() < frame_geometry.width() and position.y() >= 0 and position.y() < frame_geometry.height():
                position = self._transformations.point_from_screen(position)
                existing_starfish = self.pattern.get_starfish_at_position(position)
                if existing_starfish is not None:
                    self.pattern.remove_starfish(existing_starfish)
                else:
                    starfish_type = StarfishType(random.randint(0,1))
                    self.pattern.add_starfish_at_position(position, starfish_type)
        self._draw_widget.update()

    def mouseMoveEvent(self, mouse_event):
        keyboard_modifiers = QApplication.keyboardModifiers()
        if keyboard_modifiers == QtCore.Qt.ControlModifier or self.span_mouse.is_started():
            self.mouse_move_event_span(mouse_event)
        elif keyboard_modifiers == QtCore.Qt.AltModifier or self.select_mouse.is_started():
            self.mouse_move_event_select(mouse_event)
        elif self.pattern is not None and self.pattern.is_any_selected():
            self.mouse_move_event_move(mouse_event)
        self._draw_widget.update()

    def mouse_move_event_span(self, mouse_event):
        position = QPoint(mouse_event.x(), mouse_event.y())
        position = self.mapToGlobal(position)
        position = self.ui.patternFrame.mapFromGlobal(position)
        if not self.span_mouse.is_started():
            self.span_mouse.start_drag(position)
        else:
            self.span_mouse.move_drag(position)

    def mouse_move_event_select(self, mouse_event):
        position = QPoint(mouse_event.x(), mouse_event.y())
        position = self.mapToGlobal(position)
        position = self.ui.patternFrame.mapFromGlobal(position)
        position = self._transformations.point_from_screen(position)
        if not self.select_mouse.is_started():
            self.select_mouse.start_drag(position)
        else:
            self.select_mouse.move_drag(position)

        if self.pattern is not None:
            selection_rect = QRectF(self.select_mouse.start_position(), self.select_mouse.end_position())
            self.pattern.select_in_rect(selection_rect)

    def mouse_move_event_move(self, mouse_event):
        position = QPoint(mouse_event.x(), mouse_event.y())
        position = self.mapToGlobal(position)
        position = self.ui.patternFrame.mapFromGlobal(position)
        if not self.move_mouse.is_started():
            self.move_mouse.start_drag(position)
        else:
            self.move_mouse.move_drag(position)
        if self.pattern is not None:
            self.pattern.move_selected_starfishes(self.move_mouse.delta())

    def keyPressEvent(self, key_event):
        if key_event.key() == QtCore.Qt.Key_Control:
            QApplication.setOverrideCursor(QtCore.Qt.OpenHandCursor)
        elif key_event.key() == QtCore.Qt.Key_Alt:
            QApplication.setOverrideCursor(QtCore.Qt.DragMoveCursor)
        return super().keyPressEvent(key_event)

    def keyReleaseEvent(self, key_event):
        if key_event.key() == QtCore.Qt.Key_Control or key_event.key() == QtCore.Qt.Key_Alt:
            QApplication.restoreOverrideCursor()
        return super().keyReleaseEvent(key_event)

    def on_open_file(self, state):
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", self.file_path,
                                                   "Groups file (*.json)")
        if file_name != "":
            self.file_path = file_name
            self.ui.listWidget.clear()
            self.patterns = list()
            with open(self.file_path, 'r') as file:
                contents = json.load(file)
                groups = contents["data"]["groups"]
                for group in groups:
                    pattern = self.pattern_factory.from_json(group)
                    self.add_pattern_object(pattern)

    def on_save_file_as(self, state):
        file_path, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", self.file_path,
                                                   "Groups file (*.json)")
        if file_path != "":
            self.file_path = file_path
            self.save_to_file()

    def on_save_file(self, state):
        if self.file_path is None:
            file_path, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", self.file_path,
                                                       "Groups file (*.json)")
            if file_path != "":
                self.file_path = file_path
        if self.file_path is not None:
            self.save_to_file()

    def save_to_file(self):
        patterns_data = list()
        for pattern in self.patterns:
            patterns_data.append(self.pattern_factory.to_json(pattern))
        contents = {
            "version": "1.0.0",
            "data": {
                "groups": patterns_data
            }
        }
        with open(self.file_path, 'w') as file:
            json.dump(contents, file, indent=4)

    def on_add_pattern(self, state):
        pattern = self.pattern_factory.make()
        pattern._name = "Pattern {}".format(len(self.patterns) + 1)
        self.add_pattern_object(pattern)

    def add_pattern_object(self, pattern):
        pattern_item = QListWidgetItem(pattern.name())
        pattern_item.setFlags(pattern_item.flags() | QtCore.Qt.ItemIsEditable)
        self.ui.listWidget.addItem(pattern_item)
        self.patterns.append(pattern)
        self.ui.listWidget.setCurrentRow(len(self.patterns) - 1)

    def on_remove_pattern(self, state):
        if self.pattern is not None:
            index = self.patterns.index(self.pattern)
            self.ui.listWidget.takeItem(index)
            pattern = self.patterns.pop(index)
            self.pattern = None
            self._pattern_drawer.set_pattern(None)
            if len(self.patterns) > 0:
                if index < len(self.patterns):
                    self.ui.listWidget.setCurrentRow(index)
                    self.patterns_list_row_changed(index)
                else:
                    self.ui.listWidget.setCurrentRow(index - 1)
                    self.patterns_list_row_changed(index - 1)

    def patterns_list_row_changed(self, row):
        if self.pattern is not None:
            self.pattern.unselect_all()
        self.pattern = self.patterns[row]
        self._pattern_drawer.set_pattern(self.pattern)
        self._draw_widget.update()

    def on_patterns_list_item_changed(self, item):
        index = self.ui.listWidget.indexFromItem(item).row()
        self.patterns[index].set_name(item.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = AppWindow()
    mainWin.show()
    sys.exit(app.exec_())
