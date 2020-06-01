from PyQt5.QtWidgets import QPushButton, QMessageBox, QSpinBox
from PyQt5 import QtCore
from Source.Interface import Interface
from Source import Exceptions
from Source.Board import Board
from Source import globals


class Logic:
    def __init__(self, central_widget, signals):
        self.create_variables()
        self.signals = signals
        self.interface = Interface(self.get_variables(), central_widget, self.signals)
        self.create_new_game()     # create a default first board
        self.__new_game_button.clicked.connect(self.clicked_new_game_button)
        self.__pause_button.clicked.connect(self.clicked_pause_button)
        signals.pause.connect(self.clicked_pause_button)

    def create_variables(self):
        self.__n = QSpinBox()
        self.__n.setValue(8)
        self.__m = QSpinBox()
        self.__m.setValue(8)
        self.__mines = QSpinBox()
        self.__mines.setValue(12)
        self.__new_game_button = QPushButton("New Game")
        self.__new_game_button.setShortcut(QtCore.Qt.Key_Return)
        self.__pause_button = QPushButton("Pause")
        self.__pause_button.setShortcut(QtCore.Qt.Key_Space)

    def get_variables(self):
        return {'n': self.__n, 'm': self.__m, 'mines': self.__mines, 'ok_button': self.__new_game_button, 'pause_button': self.__pause_button}

    def clicked_new_game_button(self):
        try:
            n = int(self.__n.text())
            m = int(self.__m.text())
            mines = int(self.__mines.text())

            interval1 = [i for i in range(2, 16)]
            interval2 = [i for i in range(0, n*m+1)]
            if n not in interval1 or m not in interval1 or mines not in interval2:
                raise Exceptions.RangeException("Incorrect range!\nN, M belong to [2, 15] and Mines to [0, N*M]")

        # if game uses SpinBox value error never happen but I take that for future
        except ValueError:
            print("It's ValueError, user didn't pass 'int'\n")
            __content = "Error: Fill boxes uses natural numbers"
            __statement = QMessageBox.question(QMessageBox(), "Message", __content, QMessageBox.Ok)

        except Exceptions.RangeException as r:
            print(r.get_message())
            r.get_statement()

        else:
            self.interface.clear_board_layout(self.interface.get_board_layout())
            self.create_new_game()

    def create_new_game(self):
        globals.game_over = False
        globals.first_click = False
        globals.no_bombs = int(self.__n.text()) * int(self.__m.text()) - int(self.__mines.text())
        globals.flag_bombs = int(self.__mines.text())
        globals.bombs = int(self.__mines.text())
        if globals.game_pause:
            self.clicked_pause_button()
        self.time()
        self.signals.update_bombs_display.emit()
        self.__board = Board(self.get_int_variables(), self.signals)
        self.interface.create_board_layout(self.__board.get_variable())

    def clicked_pause_button(self):
        if not globals.game_pause:
            globals.game_pause = True
            self.signals.stop_music.emit()
            self.signals.uncloud_bombs.emit()
            self.__pause_button.setStyleSheet('background-color: rgb(38,56,76);color: rgb(255, 255, 255)')
        else:
            globals.game_pause = False
            if globals.music:
                self.signals.play_music.emit()
            self.__pause_button.setStyleSheet('background-color: rgb(, , ,)')

    def get_int_variables(self):
        return {'n': int(self.__n.text()), 'm': int(self.__m.text()), 'mines': int(self.__mines.text())}

    def time(self):
        globals.time = '00:00:00'
        self.signals.update_time_display.emit()
        self.curr_time = QtCore.QTime(00, 00, 00)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.count_time)
        self.timer.start(1000)

    def count_time(self):
        if globals.game_over or globals.game_pause or not globals.first_click:
            self.timer.stop()
            self.timer.start(1000)

        else:
            globals.time = self.curr_time.toString("hh:mm:ss")
            self.curr_time = self.curr_time.addSecs(1)
            self.signals.update_time_display.emit()
