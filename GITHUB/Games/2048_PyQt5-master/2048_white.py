import sys
import os.path
import random
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Program(QWidget):
    def __init__(self, parent=None):
        super(Program, self).__init__(parent)
        self.setStyleSheet("background-color: white")

        self.Game_over = 0
        self.init_ui()

        self.result_filepath = "win.txt"
        _bill[0] = self.get_max_score()

    def init_ui(self):
        # self.setGeometry(800, 150, 350, 500)
        self.setFixedSize(350, 500)
        self.setWindowTitle("PyQt5_2048")
        self.setWindowIcon(QIcon('img/logo.png'))
        #self.setWindowOpacity(0.8)
        self.show()

    def set_map(self, mx, my, value):
        if self.exist_map(mx, my):
            _map[mx][my] = value

    def get_map(self, mx, my):
        if self.exist_map(mx, my):
            return _map[mx][my]
        return -1

    @staticmethod
    def exist_map(mx, my):
        return 0 <= mx < _size and 0 <= my < _size

    def turn(self, ex, ey, sx, sy):  # движение на одну клетку

        if self.get_map(ex, ey) > 0:
            while self.get_map(ex + sx, ey + sy) == 0:
                _map[ex + sx][ey + sy] = self.get_map(ex, ey)
                _map[ex][ey] = 0

                ex += sx
                ey += sy
                self.moved = 1

    def join(self, ex, ey, sx, sy):
        global _bill
        if self.get_map(ex, ey) > 0:
            if self.get_map(ex + sx, ey + sy) == self.get_map(ex, ey):
                self.set_map(ex + sx, ey + sy, self.get_map(ex, ey) << 1)  # сдвигаем на битовую еденицу влево
                _bill[1] += self.get_map(ex, ey) << 1  # увеличение счёта
                while self.get_map(ex - sx, ey - sy) > 0:
                    # устанавливаем значение предыдущего в текущий
                    self.set_map(ex, ey, self.get_map(ex - sx, ey - sy))
                    ex -= sx
                    ey -= sy
                self.set_map(ex, ey, 0)
                self.moved = 1

    global moved

    def game_over(self):
        for ex in range(_size):
            for ey in range(_size):
                if self.get_map(ex, ey) == 0:
                    return 0
        for ex in range(_size):
            for ey in range(_size):
                if self.get_map(ex, ey) == self.get_map(ex + 1, ey) or self.get_map(ex, ey) == self.get_map(ex, ey + 1):
                    return 0
        return 1

    def you_win(self):
        for ex in range(_size):
            for ey in range(_size):
                if self.get_map(ex, ey) == 2048:
                    return 1

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
        global _map
        if k == -1:
            sys.stdout.write('\rleft')
            self.moved = 0
            for ey in range(_size):
                for ex in range(-1, _size):
                    self.turn(ex, ey, -1, 0)
                for ex in range(-1, _size):
                    self.join(ex, ey, -1, 0)
            if self.moved == 1:
                self.random_new_numbers()

        elif k == 2:
            sys.stdout.write('\rup')
            self.moved = 0
            for ex in range(_size):
                for ey in range(-1, _size):
                    self.turn(ex, ey, 0, -1)
                for ey in range(-1, _size):
                    self.join(ex, ey, 0, -1)
            if self.moved == 1:
                self.random_new_numbers()

        elif k == 1:
            sys.stdout.write('\rright')
            self.moved = 0
            for ey in range(_size):
                for ex in range(2, -1, -1):
                    self.turn(ex, ey, 1, 0)
                for ex in range(2, -1, -1):
                    self.join(ex, ey, 1, 0)
            if self.moved == 1:
                self.random_new_numbers()

        elif k == 0:
            sys.stdout.write('\rdown')
            self.moved = 0
            for ex in range(_size):
                for ey in range(2, -1, -1):
                    self.turn(ex, ey, 0, 1)
                for ey in range(2, -1, -1):
                    self.join(ex, ey, 0, 1)
            if self.moved == 1:
                self.random_new_numbers()

        elif k == 3:
            if self.game_over() == 1:
                for ex in range(_size):
                    for ey in range(_size):
                        self.set_map(ex, ey, 0)

                if _bill[1] > _bill[0]:
                    self.set_max_score(_bill[1])
                    _bill[0] = _bill[1]
                else:
                    self.set_max_score(_bill[0])

                _bill[1] = 0

            if np.sum(_map) == 0:
                self.random_new_numbers()
                self.random_new_numbers()

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

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)

        # images = []
        #
        # for e in range(11):
        #     img = QPixmap("img/" + str(e) + ".png")
        #     images.append(img)


        qp.begin(self)
        pen = QPen(QColor(colors[0]))
        qp.setPen(pen)
        for ex in range(_size):
            for ey in range(_size):
                qp.setFont(QFont('Decorative', self.font_size(len(str(_map[ex][ey])))))  # ~30
                if self.game_over() == 0:
                    # стандартная версия
                    qp.fillRect(ex * x * 1.2 + x, ey * x * 1.2 + x, x, x,
                                  QBrush(QColor(colors[len(str(bin(_map[ex][ey]))) - 2])))

                    # версия с изображениями
                    # qp.drawPixmap(ex * x * 1.2 + x, ey * x * 1.2 + x, x, x, images[len(str(bin(_map[ex][ey]))) - 2])
                else:
                    qp.fillRect(ex * x * 1.2 + x, ey * x * 1.2 + x, x, x, QBrush(QColor(colors[12])))

                qp.drawText(ex * x * 1.2 + x, ey * x * 1.2 + x, x, x,
                             Qt.AlignHCenter | Qt.AlignVCenter, str(_map[ex][ey]))

        pen = QPen(QColor(colors[0]))
        qp.setPen(pen)
        qp.setFont(QFont('Decorative', self.font_size(len(str(_bill[1])))))
        qp.drawText(121.9, 318, 106, 53, Qt.AlignHCenter | Qt.AlignVCenter, str(_bill[1]))
        if self.game_over():
            qp.setFont(QFont('Decorative', self.font_size(len("Game Over"))))
            qp.drawText(110, 5, 120, 53, Qt.AlignHCenter | Qt.AlignVCenter, "Game Over")
            #qp.fillRect(x, x, x*4.6, x*4.6, QBrush(QColor(0, 0, 0, 50)))
        elif self.you_win():
            qp.drawText(120, 5, 120, 53, Qt.AlignHCenter | Qt.AlignVCenter, "You winner!")

        pen = QPen(QColor('#b0b5b5'))
        qp.setPen(pen)
        qp.setFont(QFont('Calibri', self.font_size(10)))
        qp.drawText(121.9, 345, 106, 53, Qt.AlignHCenter | Qt.AlignVCenter, str(_bill[0]))
        qp.drawText(2, 375, 350, 100, Qt.AlignHCenter | Qt.AlignVCenter, _rulls)
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
    def random_new_numbers():
        what_times = 0
        for i in range(50):
            eex = random.randrange(0, _size)
            eey = random.randrange(0, _size)
            if _map[eex][eey] == 0:
                _map[eex][eey] = random.choice((0b_10, 0b_10, 0b_10, 0b_10, 0b_100))  # 10% fortune for 4
                what_times += 1
            if what_times == 1:
                break


colors = ['#34486a', '#f6f4f5',
          '#cad877', '#d7ddea', '#FEC77F', '#FFB3B1',
          '#c0eb7e', '#c2e4eb', '#ffea97', '#f9c0c9',
          '#778046', '#757980', '#c78b89']

_size = 4
x = _size * 13  # размер сетки и отступы 4-13 5-9
_map = [[0 for i in range(_size)] for ii in range(_size)]  # частная переменная map
_bill = [0, 0]  # счёт рекордный и настоящий
_rulls = "Press key '+' to start."


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Program()

    sys.exit(app.exec_())
