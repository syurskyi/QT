"""
Данный модуль содержит
в себе изображения для игры
"""
from PyQt5.QtGui import QIcon


class IconsForGame:
    """класс, содержащий изображения для игры"""
    __ImgMine = QIcon(":/img_resources/Images/Mine.png")
    __ImgCross = QIcon(":/img_resources/Images/Cross.png")
    __ImgPlayer = QIcon(":/img_resources/Images/Player.png")
    __ImgSkull = QIcon(":/img_resources/Images/Skull.jpg")
    __ImgDigits = (QIcon(":/img_resources/Images/1.jpg"), QIcon(":/img_resources/Images/2.png"),
                   QIcon(":/img_resources/Images/3.bmp"), QIcon(":/img_resources/Images/4.jpg"),
                   QIcon(":/img_resources/Images/5.jpg"), QIcon(":/img_resources/Images/6.jpg"))

    @staticmethod
    def get_mine() -> QIcon:
        """возвращает изображение мины"""
        return IconsForGame.__ImgMine

    @staticmethod
    def get_cross() -> QIcon:
        """возвращает изображение крестика"""
        return IconsForGame.__ImgCross

    @staticmethod
    def get_player() -> QIcon:
        """возвращает изображение игрока"""
        return IconsForGame.__ImgPlayer

    @staticmethod
    def get_skull() -> QIcon:
        """возвращает изображение черепка"""
        return IconsForGame.__ImgSkull

    @staticmethod
    def get_digits() -> tuple:
        """возвращает список изображений цифр"""
        return IconsForGame.__ImgDigits
