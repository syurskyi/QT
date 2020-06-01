"""
Данный класс является
основным для игры Агент_007
в нем содержится все что
связано с формой
"""
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow
from MineSweeper.game import MyGame, MyPlayer


class MainForm(QMainWindow):
    """
    Этот класс описывает основную форму
    данного приложения
    """
    def __init__(self):
        super().__init__()
        self.init_ui()

    def reset_my_game(self):
        """
        Данный метод при его вызове
        заново пересоздает поле из кнопок
        с тем же размером и количеством мин,
        которое было изначально
        """
        self.RulesWindow.hide()
        MyGame.inst(MyGame.get_buf().get_width, MyGame.get_buf().get_height,
                    MyGame.get_buf().get_mines_count, self)

    def small_field_clicked(self):
        """
        Данный метод создает поле из кнопок
        размером 10х10, с 5 минами и игроком
        """
        self.RulesWindow.hide()
        MyGame.inst(10, 10, 5, self)

    def medium_field_clicked(self):
        """
        Данный метод создает поле из кнопок
        размером 15х15, с 7 минами и игроком
        """
        self.RulesWindow.hide()
        MyGame.inst(15, 15, 7, self)

    def large_field_clicked(self):
        """
        Данный метод создает поле из кнопок
        размером 20х20, с 10 минами и игроком
        """
        self.RulesWindow.hide()
        MyGame.inst(20, 20, 10, self)

    def init_ui(self):
        """
        Данный метод загружает форму и
        все связанные с ее компонентами события
        и выводит ее на экран
        """
        loadUi('MyMainForm.ui', self)
        self.RulesWindow.hide()
        self.field.hide()
        self.MenuForWindow.setFixedWidth(16777216)
        self.SmallFieldAction.triggered.connect(self.small_field_clicked)
        self.MediumFieldAction.triggered.connect(self.medium_field_clicked)
        self.LargeFieldAction.triggered.connect(self.large_field_clicked)
        self.ResetButton.clicked.connect(self.reset_my_game)
        self.showMaximized()


if __name__ == "__main__":
    MY_APP = QApplication(sys.argv)
    MY_FORM = MainForm()
    sys.exit(MY_APP.exec_())
