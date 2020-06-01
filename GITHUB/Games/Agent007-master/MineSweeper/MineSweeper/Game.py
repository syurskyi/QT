"""
Данный модуль отвечает за логику игры
также он содержит в себе различные типы
ячеек (кнопок)
"""
from random import randint, choice
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from MineSweeper.images_for_game import IconsForGame
from MineSweeper.utils import is_border_of_field


class MyGame:
    """
    Данный класс инициализирует игру
    содержит в себе все что связано с ней
    """
    __instance = None
    __buf_instance = None

    @staticmethod
    def get_buf():
        """возврат буфера игры"""
        return MyGame.__buf_instance

    @staticmethod
    def get_instance():
        """возврат ссылки на основной экземпляр игры"""
        return MyGame.__instance

    @staticmethod
    def inst(width: int, height: int, mines_count: int, main_window):
        """реализация одиночки для инициализации игры"""
        MyPlayer.player, MyGame.__instance, MyGame.__buf_instance = None, None, None
        MyGame.__instance = MyGame(width, height, mines_count, main_window)
        MyGame.__buf_instance = MyGame(width, height, mines_count, main_window)
        return MyGame.__instance

    def __init__(self, width: int, height: int, mines_count: int, main_window):
        self.__main_window = main_window
        self.__mines_count = mines_count
        self.__width = width
        self.__height = height
        self.__main_window.field.setRowCount(height)
        self.__main_window.field.setColumnCount(width)
        self.__main_window.field.setFixedSize(38 * width, 38 * height)
        self.__count_box = width * height - mines_count - 1
        self.__score = 0
        self.__main_window.BoxesValue.setText(str(self.__count_box))
        self.__main_window.GoalValue.setText(str(int(self.__count_box / 4)))
        self.__main_window.BoxesPercent.setText(str(int((self.__count_box / (width * height) * 100))) + "%")
        self.__main_window.GoalPercent.setText(str(int((self.__count_box / (width * height) * 25))) + "%")
        self.__main_window.BoxesValue.adjustSize()
        self.__main_window.GoalValue.adjustSize()
        self.__main_window.BoxesPercent.adjustSize()
        self.__main_window.GoalPercent.adjustSize()
        self.__main_window.field.setCellWidget(0, 0, MyPlayer.inst(main_window))
        counter_of_mines, k = 0, 1
        for i in range(height):
            for j in range(k, width):
                rand_for_mine = randint(1, 7)
                if rand_for_mine == 1 and counter_of_mines < mines_count:
                    self.__main_window.field.setCellWidget(i, j, MyMine(main_window))
                    counter_of_mines += 1
                else:
                    img_digit = choice(IconsForGame.get_digits())
                    _steps = IconsForGame.get_digits().index(img_digit) + 1
                    self.__main_window.field.setCellWidget(i, j, MyCell(img_digit, _steps, i, j, main_window))
            k = 0
        self.__main_window.field.show()

    @property
    def get_mines_count(self) -> int:
        """возвращает количество мин на поле"""
        return self.__mines_count

    @property
    def get_width(self) -> int:
        """возвращает ширину поля"""
        return self.__width

    @property
    def get_height(self) -> int:
        """возвращает высоту поля"""
        return self.__height

    @property
    def get_field(self):
        """возвращает поле"""
        return self.__main_window.field

    @staticmethod
    def count_score_and_boxes(boxes: list):
        """подсчет очков и количества не обойденных клеток игроком"""
        MyGame.__instance.__count_box -= len(boxes)
        MyGame.__instance.__score += sum(boxes) * 10
        MyGame.__instance.__main_window.BoxesValue.setText(str(MyGame.__instance.__count_box))
        MyGame.__instance.__main_window.ScoreValue.setText(str(MyGame.__instance.__score))
        MyGame.__instance.__main_window.BoxesPercent.setText(str(int(
            MyGame.__instance.__count_box / (MyGame.__instance.__width * MyGame.__instance.__height) * 100)) +
                                                           "%")
        MyGame.__instance.__main_window.BoxesValue.adjustSize()
        MyGame.__instance.__main_window.BoxesPercent.adjustSize()
        MyGame.__instance.__main_window.ScoreValue.adjustSize()


class MyPlayer(QPushButton):
    """Класс клетки-игрока на поле"""

    player = None

    @staticmethod
    def inst(main_window):
        """реализация одиночки в игре для инициализации"""
        if MyPlayer.player is None:
            MyPlayer.player = MyPlayer(main_window)
        return MyPlayer.player

    def __init__(self, main_window):
        super().__init__(main_window)
        self.setText("Player")
        self.setIcon(IconsForGame.get_player())
        self.setIconSize(QSize(38, 38))
        self.__i, self.__j = 0, 0

    @property
    def coord_i(self) -> int:
        """возвращает кооординату игрока по строке"""
        return self.__i

    @property
    def coord_j(self) -> int:
        """возвращает кооординату игрока по столбцу"""
        return self.__j

    def move_to(self, cell):
        """Данный метод отвечает за передвижение игрока по клеткам"""
        field = MyGame.get_instance().get_field
        ins = MyGame.get_instance()
        _boxes = []
        diff_row, diff_column = self.__i - cell.coord_i, self.__j - cell.coord_j
        limit_row = self.__i - diff_row * cell.get_count_of_steps
        limit_column = self.__j - diff_column * cell.get_count_of_steps
        self.__i += diff_row
        self.__j += diff_column
        while self.__i != limit_row or self.__j != limit_column:
            self.__i -= diff_row
            self.__j -= diff_column
            _cell = field.cellWidget(self.__i, self.__j)
            if _cell.__class__ == MyMine or _cell.icon().cacheKey() == IconsForGame.get_cross().cacheKey() or \
                    is_border_of_field(diff_row, diff_column, _cell, ins):
                if _cell.__class__ == MyCell and not (_cell.icon().cacheKey() == IconsForGame.get_player().cacheKey()):
                    _boxes.append(_cell.get_count_of_steps)
                _cell.setText("Skull")
                _cell.setIcon(IconsForGame.get_skull())
            if _cell.icon().cacheKey() == IconsForGame.get_skull().cacheKey():
                break
            if _cell.__class__ == MyCell or _cell.__class__ == MyPlayer:
                if _cell.icon().cacheKey() != IconsForGame.get_player().cacheKey():
                    _boxes.append(_cell.get_count_of_steps)
                    _cell.clicked.disconnect(_cell.is_clicked_around_player)
                _cell.setText("Cross")
                _cell.setIcon(IconsForGame.get_cross())
                if self.__i == limit_row and self.__j == limit_column:
                    _cell.setIcon(IconsForGame.get_player())
                    _cell.setText("Player")
        MyGame.count_score_and_boxes(_boxes)


class MyCell(QPushButton):
    """класс ячейки с количеством шагов"""

    def __init__(self, img, count_steps: int, i: int, j: int, main_window):
        super().__init__(main_window)
        self.setText(str(count_steps))  # это не нужно
        self.setIcon(img)
        self.setIconSize(QSize(38, 38))
        self.clicked.connect(self.is_clicked_around_player)
        self.__count_steps, self.__i, self.__j = count_steps, i, j

    @property
    def get_count_of_steps(self) -> int:
        """возвращает количество шагов у этой кнопки"""
        return self.__count_steps

    @property
    def coord_i(self) -> int:
        """возвращает координату ячейки по строке"""
        return self.__i

    @property
    def coord_j(self) -> int:
        """возвращает координату ячейки по столбцу"""
        return self.__j

    def is_clicked_around_player(self):
        """Проверка на нажатие кнопки рядом с игроком"""
        if -1 <= MyPlayer.player.coord_i - self.__i <= 1 and -1 <= MyPlayer.player.coord_j - self.__j <= 1:
            MyPlayer.player.move_to(self)


class MyMine(QPushButton):
    """класс ячейки-мины на поле"""

    def __init__(self, main_window):
        super().__init__(main_window)
        self.setText("Mine")
        self.setIcon(IconsForGame.get_mine())
        self.setIconSize(QSize(38, 38))
