from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout


class BoardInterface:
    def __init__(self, variable):
        self.create_board(variable)

    def create_board(self, variable):
        self.__board = QVBoxLayout()
        self.__board.setSpacing(2)
        for i in range(variable['n']):
            self.__row = QHBoxLayout()
            self.__row.setSpacing(2)
            for j in range(variable['m']):
                self.__row.addWidget(variable['buttons'][i][j])
            self.__board.addLayout(self.__row)

    def layout(self):
        self.__layout = QHBoxLayout()
        self.__layout.addLayout(self.__board)
        return self.__layout
