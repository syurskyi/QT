import sys
import os.path
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Program(QWidget):
    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        self.theme = "dark"
        self.images_theme = False

        self.load_resources()

        self.set_theme()
        self.init_ui()

        self.result_filepath = "win.txt"
        self.score[0] = self.get_max_score()

    def init_ui(self):
        self.setFixedSize(350, 500)
        self.setWindowTitle("2048")
        self.setWindowIcon(QIcon('img/logo.png'))
        self.show()

    def load_resources(self):
        self.images = [QPixmap("img/" + str(i) + ".png") for i in range(11)]

        self.background_color = {"dark": "#000000", "light": "#f6f4f5"}

        self.colors = ['#34486a', '', # индекс 1 - background_color
                       '#cad877', '#d7ddea', '#fec77f', '#ffb3b1',
                       '#c0eb7e', '#c2e4eb', '#ffea97', '#f9c0c9',
                       '#778046', '#757980', '#c78b89']

        self.size = 4
        self.x = self.size * 13  # размер сетки и отступы 4-13 5-9
        self.map = [[0 for i in range(self.size)] for ii in range(self.size)]  # частная переменная map
        self.score = [0, 0]  # счёт рекордный и настоящий
        self.rules = "Press key '+' to start.\nPress key '-' to change theme\nPress key '_' to use images"


    def set_map(self, mx, my, value):
        if self.exist_map(mx, my, self.size):
            self.map[mx][my] = value

    def get_map(self, mx, my):
        if self.exist_map(mx, my, self.size):
            return self.map[mx][my]
        return -1

    def change_theme(self):
        if self.theme == "dark":
            self.theme = "light"
        elif self.theme == "light":
            self.theme = "dark"

    def set_theme(self):
        if self.theme == "dark":
            self.setStyleSheet("background-color: black")
            self.setWindowOpacity(0.8)
        elif self.theme == "light":
            self.setStyleSheet("background-color: white")
            self.setWindowOpacity(1)

    @staticmethod
    def exist_map(mx, my, size):
        return 0 <= mx < size and 0 <= my < size

    def turn(self, ex, ey, sx, sy):  # движение на одну клетку
        if self.get_map(ex, ey) > 0:
            while self.get_map(ex + sx, ey + sy) == 0:
                self.map[ex + sx][ey + sy] = self.get_map(ex, ey)
                self.map[ex][ey] = 0

                ex += sx
                ey += sy
                self.moved = 1

    def join(self, ex, ey, sx, sy):
        if self.get_map(ex, ey) > 0:
            if self.get_map(ex + sx, ey + sy) == self.get_map(ex, ey):
                self.set_map(ex + sx, ey + sy, self.get_map(ex, ey) << 1)  # сдвигаем на битовую еденицу влево
                self.score[1] += self.get_map(ex, ey) << 1  # увеличение счёта
                while self.get_map(ex - sx, ey - sy) > 0:
                    # устанавливаем значение предыдущего в текущий
                    self.set_map(ex, ey, self.get_map(ex - sx, ey - sy))
                    ex -= sx
                    ey -= sy
                self.set_map(ex, ey, 0)
                self.moved = 1

    def game_over(self):
        for ex in range(self.size):
            for ey in range(self.size):
                if self.get_map(ex, ey) == 0:
                    return False
        for ex in range(self.size):
            for ey in range(self.size):
                if self.get_map(ex, ey) == self.get_map(ex + 1, ey) \
                      or self.get_map(ex, ey) == self.get_map(ex, ey + 1):
                    return False
        return True

    def you_win(self):
        for ex in range(self.size):
            for ey in range(self.size):
                if self.get_map(ex, ey) == 2048:
                    return True

    def get_max_score(self):
        if os.path.isfile(self.result_filepath):
            with open(self.result_filepath, "r") as result_file:
                return int(result_file.read(), 2)
        else:
            return 0

    def set_max_score(self, max_score):
        with open(self.result_filepath, "w") as result_file:
            result_file.write(bin(max_score))

    def clicked(self, k):
        if k == -1:
            self.moved = 0
            for ey in range(self.size):
                for ex in range(-1, self.size):
                    self.turn(ex, ey, -1, 0)
                for ex in range(-1, self.size):
                    self.join(ex, ey, -1, 0)
            if self.moved == 1:
                self.random_new_numbers(self.map, self.size)

        elif k == 2:
            self.moved = 0
            for ex in range(self.size):
                for ey in range(-1, self.size):
                    self.turn(ex, ey, 0, -1)
                for ey in range(-1, self.size):
                    self.join(ex, ey, 0, -1)
            if self.moved == 1:
                self.random_new_numbers(self.map, self.size)

        elif k == 1:
            self.moved = 0
            for ey in range(self.size):
                for ex in range(2, -1, -1):
                    self.turn(ex, ey, 1, 0)
                for ex in range(2, -1, -1):
                    self.join(ex, ey, 1, 0)
            if self.moved == 1:
                self.random_new_numbers(self.map, self.size)

        elif k == 0:
            self.moved = 0
            for ex in range(self.size):
                for ey in range(2, -1, -1):
                    self.turn(ex, ey, 0, 1)
                for ey in range(2, -1, -1):
                    self.join(ex, ey, 0, 1)
            if self.moved == 1:
                self.random_new_numbers(self.map, self.size)

        elif k == 3:
            if self.game_over() == 1:
                for ex in range(self.size):
                    for ey in range(self.size):
                        self.set_map(ex, ey, 0)

                self.score[1] = 0

            if sum([sum([i for i in j]) for j in self.map]) == 0:
                self.random_new_numbers(self.map, self.size)
                self.random_new_numbers(self.map, self.size)

        self.update()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Left:
            self.clicked(-1)
        elif e.key() == Qt.Key_Right:
            self.clicked(1)
        elif e.key() == Qt.Key_Down:
            self.clicked(0)
        elif e.key() == Qt.Key_Up:
            self.clicked(2)
        elif e.key() == Qt.Key_Plus:
            self.clicked(3)
        elif e.key() == Qt.Key_Minus:
            self.change_theme()
            self.set_theme()
        elif e.key() == Qt.Key_Underscore:
            self.images_theme = not self.images_theme
            self.set_theme()

    def save_new_score(self):
        if self.score[1] > self.score[0]:
            self.set_max_score(self.score[1])
            self.score[0] = self.score[1]
        else:
            self.set_max_score(self.score[0])

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.begin(self)
        pen = QPen(QColor(self.background_color[self.theme]))
        qp.setPen(pen)
        for ex in range(self.size):
            for ey in range(self.size):
                qp.setFont(QFont('Decorative', self.font_size(len(str(self.map[ex][ey])))))  # ~30

                c1 = ex * self.x * 1.2 + self.x
                c2 = ey * self.x * 1.2 + self.x
                if not self.game_over():
                    k = len(str(bin(self.map[ex][ey]))) - 2
                    if k == 1:
                        # background_color
                        qp.fillRect(c1, c2, self.x, self.x, QBrush(QColor(self.background_color[self.theme])))
                    else:
                        if self.images_theme:
                            qp.drawPixmap(c1, c2, self.x, self.x, self.images[k])
                        else:
                            qp.fillRect(c1, c2, self.x, self.x, QBrush(QColor(self.colors[k])))
                else:
                    qp.fillRect(c1, c2, self.x, self.x, QBrush(QColor(self.colors[12])))

                if not self.images_theme:
                    qp.drawText(c1, c2, self.x, self.x, Qt.AlignHCenter | Qt.AlignVCenter, str(self.map[ex][ey]))

        pen = QPen(QColor(self.colors[0]))
        qp.setPen(pen)
        qp.setFont(QFont('Decorative', self.font_size(len(str(self.score[1])))))
        qp.drawText(121.9, 318, 106, 53, Qt.AlignHCenter | Qt.AlignVCenter, str(self.score[1]))
        if self.game_over():
            qp.setFont(QFont('Decorative', self.font_size(len("Game Over"))))
            qp.drawText(110, 5, 120, 53, Qt.AlignHCenter | Qt.AlignVCenter, "Game Over")
            self.save_new_score()
        elif self.you_win():
            qp.drawText(120, 5, 120, 53, Qt.AlignHCenter | Qt.AlignVCenter, "You winner!")
            self.save_new_score()
        pen = QPen(QColor('#b0b5b5'))

        qp.setPen(pen)
        qp.setFont(QFont('Calibri', self.font_size(10)))
        qp.drawText(121.9, 345, 106, 53, Qt.AlignHCenter | Qt.AlignVCenter, str(self.score[0]))
        qp.drawText(2, 375, 350, 100, Qt.AlignHCenter | Qt.AlignVCenter, self.rules)
        qp.end()

    @staticmethod
    def font_size(count):
        if count < 2:
            return 30
        elif count < 3:
            return 26
        elif count < 4:
            return 22
        elif count < 6:
            return 18
        else:
            return 14

    @staticmethod
    def random_new_numbers(field, size):
        while True:
            eex = random.randrange(0, size)
            eey = random.randrange(0, size)
            if field[eex][eey] == 0:
                field[eex][eey] = random.choice([2] * 9 + [4] * 1)  # 10% fortune for 4
                break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Program()
    sys.exit(app.exec_())