from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtGui
from Source import globals


class Button(QPushButton):
    def __init__(self, x, y, free_others_function, free_bombs, signals):
        super().__init__()
        self.signals = signals
        self.x = x
        self.y = y
        self.bomb = False
        self.flag = False
        self.question_mark = False
        self.deactivate = False
        self.number = 0
        self.free_others_function = free_others_function
        self.free_bombs_function = free_bombs
        self.setMaximumSize(35, 35)
        self.setMinimumSize(35, 35)
        self.set_basic_color()
        self.update()
    # def leaveEvent(self, event):
        # self.set_basic_color()

    # def enterEvent(self, event):
        # self.setStyleSheet('')

    def mousePressEvent(self, mouse_event):
        if mouse_event.button() == Qt.LeftButton and not self.deactivate and not globals.game_pause and not globals.game_over:
            self.mouse_left_click()
        elif mouse_event.button() == Qt.RightButton and not self.deactivate and not globals.game_pause and not globals.game_over:
            self.mouse_right_click()

    def mouse_left_click(self):
        if not globals.first_click:
            globals.first_click = True
            globals.first_click_xy = [self.x, self.y]
            self.signals.set_buttons.emit()

        if self.bomb:
            globals.game_over = True
            self.free_bombs_function()
            self.signals.loose.emit()
        elif not self.flag and not self.question_mark:
            if self.number != 0:
                self.free()
            else:
                self.free_others_function(self.x, self.y)

    def mouse_right_click(self):
        if not self.flag and not self.question_mark:
            self.flag = True
            globals.flag_bombs -= 1
            if self.bomb:
                globals.bombs -= 1
            self.signals.update_bombs_display.emit()
            self.set_icon('../Images/flag.png', 40, 40)
        elif self.flag and globals.question_marks:
            self.flag = False
            globals.flag_bombs += 1
            if self.bomb:
                globals.bombs += 1
            self.signals.update_bombs_display.emit()
            self.question_mark = True
            self.set_icon('../Images/question_mark.png', 20, 20)
        elif not globals.question_marks:
            self.flag = False
            globals.flag_bombs += 1
            if self.bomb:
                globals.bombs += 1
            self.signals.update_bombs_display.emit()
            self.set_icon(None)
        else:
            self.question_mark = False
            self.set_icon(None)

        self.check_win()

    def free(self):
        self.deactivate = True
        globals.no_bombs -= 1
        self.setStyleSheet('font-size: 12px;'
                           'font-family: Arial;color: rgb(255, 255, 255);'
                           'background-color: rgb(38,56,76);')
        self.check_win()
        if self.number != 0:
            self.setText(str(self.number))

    def check_win(self):
        if globals.no_bombs == 0 or (globals.bombs == 0 and globals.flag_bombs == 0):
            globals.game_over = True
            self.signals.win.emit()

    def check_able_to_free(self):
        if self.bomb or self.flag or self.question_mark or self.deactivate:
            return -1   # field cant be free
        elif self.number != 0:
            return 0    # field can be free but has a bombs near
        else:
            return 1    # field can be free and has not bombs near

    def set_bomb(self):
        self.bomb = True

    def set_number(self, neighbours_bomb):
        self.number = neighbours_bomb

    def set_icon(self, path, x=35, y=35):
        self.setIcon(QtGui.QIcon(path))
        self.setIconSize(QSize(x, y))

    def set_color(self, darker=0):
        color_range = lambda col, d: col - d if 0 < col - d < 255 else 0
        self.r = color_range(self.r, darker)
        self.g = color_range(self.g, darker)
        self.b = color_range(self.b, darker)
        self.setStyleSheet('background-color: rgb({}, {}, {});'.format(self.r, self.g, self.b))

    def set_basic_color(self):
        self.r, self.g, self.b = 100, 100, 255
        self.setStyleSheet('background-color: rgb({}, {}, {});'.format(self.r, self.g, self.b))

    def hide_question_mark(self):
        if self.question_mark and not self.deactivate:
            self.question_mark = False
            self.set_icon(None)