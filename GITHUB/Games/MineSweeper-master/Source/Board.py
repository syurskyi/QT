from Source.Button import Button
import random
from Source import globals


class Board:
    def __init__(self, variable, signals):
        self.variable = variable
        self.all_index = [[x, y] for x in range(0, self.variable['n']) for y in range(0, self.variable['m'])]
        #self.__buttons = [Button(x, y, self.free_others_function, self.free_bombs, signals) for x, y in self.all_index]
        self.__buttons = [
            [Button(x, y, self.free_others_function, self.free_bombs, signals) for y in range(self.variable['m'])] for x
            in range(self.variable['n'])]
        self.good_range = lambda a, b: 0 <= a < self.variable['n'] and 0 <= b < self.variable['m']  # this check range
        self.bombs_index = []
        signals.reconnect(signals.cloud_bombs, self.cloud_bombs())
        signals.reconnect(signals.uncloud_bombs, self.uncloud_bombs())
        signals.set_buttons.connect(self.set_buttons)
        signals.hide_question_marks.connect(self.hide_questions_marks)
        signals.cloud_bombs.connect(self.cloud_bombs)
        signals.uncloud_bombs.connect(self.uncloud_bombs)

    def get_variable(self):
        self.variable['buttons'] = self.__buttons
        return self.variable

    @staticmethod   # return a index of neighbours
    def index_gen(i, j):
        # index are order as a clock, we start in 'top left' end finish in 'middle left':
        index = [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1], [i, j + 1], [i + 1, j + 1], [i + 1, j], [i + 1, j - 1],
                 [i, j - 1]]
        for i, j in index:
            yield i, j

    def set_buttons(self):
        if globals.no_bomb_in_first_click:
            index_to_draw = self.all_index.copy()
            for x, y in self.index_gen(globals.first_click_xy[0], globals.first_click_xy[1]):
                if self.good_range(x, y):
                    index_to_draw.remove([x, y])
            index_to_draw.remove(globals.first_click_xy)
        else:
            index_to_draw = self.all_index.copy()

        self.bombs_index = random.sample(index_to_draw, self.variable['mines'])
        for x, y in self.bombs_index:
            self.__buttons[x][y].set_bomb()

        self.set_numbers()

    def set_numbers(self):
        for i, j in self.all_index:
            number_of = 0
            for x, y in self.index_gen(i, j):
                if self.good_range(x, y) and [x, y] in self.bombs_index:
                    number_of += 1
            self.__buttons[i][j].set_number(number_of)

    def free_others_function(self, i, j):
        self.__buttons[i][j].free()
        for x, y in self.index_gen(i, j):
            if self.good_range(x, y):
                if self.__buttons[x][y].check_able_to_free() == 1:
                    self.__buttons[x][y].free_others_function(x, y)
                elif self.__buttons[x][y].check_able_to_free() == 0:
                    self.__buttons[x][y].free()

    def free_bombs(self):
        for i, j in self.bombs_index:
            self.__buttons[i][j].set_icon('../Images/bomb.png', 20, 20)
            self.__buttons[i][j].set_color(100)

    def cloud_bombs(self):
        for x, y in self.bombs_index:
            self.__buttons[x][y].set_color(25)

    def uncloud_bombs(self):
        for x, y in self.bombs_index:
            self.__buttons[x][y].set_basic_color()

    def hide_questions_marks(self):
        for i, j in self.all_index:
            self.__buttons[i][j].hide_question_mark()




