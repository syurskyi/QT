import random

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from character_modul import Postac, Parowka, Benek, Laser, Scout
from menu_modul import Ui_MainMenu
from main_shot import Ui_MainWindow
from aftergame_modul import UiAfterGame
from skins_or_skills_modul import UiSkinSkills


class MyMainWindow(QMainWindow):
    resized = QtCore.pyqtSignal()
    ui = None

    def __init__(self):
        super().__init__()
        self.resized.connect(self.resize_tlo)
        self.main_game = False
        self.gHeight = self.height()
        self.gWidth = int(self.height() * 3/2)

        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)
        Postac.okno = self

    def resizeEvent(self, event):
        self.resized.emit()
        return super(MyMainWindow, self).resizeEvent(event)

    def keyPressEvent(self, event):
        if self.main_game:
            if event.key() == Qt.Key_Space:
                self.ui.player.shot()
            if event.key() == Qt.Key_A and not event.isAutoRepeat():
                self.ui.player.rusz_benek_lewo()
            if event.key() == Qt.Key_D and not event.isAutoRepeat():
                self.ui.player.rusz_benek_prawo()

    def keyReleaseEvent(self, event):
        if self.main_game and not event.isAutoRepeat():
            if event.key() == Qt.Key_A:
                self.ui.player.stop_rusz_benek_lewo()
            if event.key() == Qt.Key_D:
                self.ui.player.stop_rusz_benek_prawo()

    def resize_tlo(self):
        self.gHeight = self.height()
        self.gWidth = int(self.height() * 3 / 2)
        if type(self.ui) == Ui_MainWindow:
            self.resize_main_game()
        elif type(self.ui) == Ui_MainMenu:
            self.resize_main_menu()
        elif type(self.ui) == UiAfterGame:
            self.resize_aftergame()
        elif type(self.ui) == UiSkinSkills:
            self.resize_shop()

    def resize_main_game(self):
        self.ui.tlo.setGeometry(QtCore.QRect(int((self.width() - self.gWidth) / 2), 0, self.gWidth, self.gHeight))
        self.ui.score.setGeometry(QtCore.QRect(int((self.width() - self.gWidth) / 2), 100, self.gWidth, 200))
        for postac in Postac.lista_postaci:
            if super(type(postac)) != Parowka:
                px = postac.x()
                if (px + postac.width()) >= int((self.width() - self.gWidth) / 2 + self.gWidth):
                    postac.setGeometry(
                        QtCore.QRect((int((self.width() - self.gWidth) / 2 + self.gWidth) - postac.width()), postac.y(), postac.width(),
                                     postac.height()))
                else:
                    postac.setGeometry(
                        QtCore.QRect(px, self.height() - postac.height(), postac.width(), postac.height()))

    def resize_main_menu(self):
        self.ui.menu_background.setGeometry(QtCore.QRect(0, 0, self.width(), self.height()))
        self.ui.play_btn.setGeometry(
            QtCore.QRect(int(self.width() / 20 * 9), int(self.height() / 2), int(self.width() / 10),
                         int(self.height() / 10)))
        self.ui.shop_btn.setGeometry(
            QtCore.QRect(int(self.width() / 20 * 7), int(self.height() / 1.5), int(self.width() / 10),
                         int(self.height() / 10)))
        self.ui.skills_btn.setGeometry(
            QtCore.QRect(int(self.width() / 20 * 11), int(self.height() / 1.5), int(self.width() / 10),
                         int(self.height() / 10)))
        self.ui.exit_btn.setGeometry(
            QtCore.QRect(int(self.width() / 20 * 9), int(self.height() / 6 * 5), int(self.width() / 10),
                         int(self.height() / 10)))
        self.ui.menu_title.setGeometry(
            QtCore.QRect(0, int(self.height() / 10), int(self.width()), int(self.height() / 10)))
        self.ui.menu_highscore.setGeometry(
            QtCore.QRect(0, int(self.height() / 7), int(self.width()/3), int(self.height() / 3)))

    def resize_aftergame(self):
        self.ui.menu_background.setGeometry(QtCore.QRect(0, 0, self.width(), self.height()))
        self.ui.play_btn.setGeometry(
            QtCore.QRect(int(self.width() / 20 * 9), int(self.height() / 2), int(self.width() / 10),
                         int(self.height() / 10)))
        self.ui.menu_btn.setGeometry(
            QtCore.QRect(int(self.width() / 20 * 9), int(self.height() / 1.5), int(self.width() / 10),
                         int(self.height() / 10)))
        self.ui.exit_btn.setGeometry(
            QtCore.QRect(int(self.width() / 20 * 9), int(self.height() / 6 * 5), int(self.width() / 10),
                         int(self.height() / 10)))
        self.ui.menu_title.setGeometry(
            QtCore.QRect(0, int(self.height() / 10), int(self.width()), int(self.height() / 10)))
        self.ui.menu_highscore.setGeometry(
            QtCore.QRect(0, int(self.height() / 8), int(self.width() / 2), int(self.height() / 3)))
        self.ui.score.setGeometry(
            QtCore.QRect(0, int(self.height() / 6), int(self.width() / 2), int(self.height() / 3)))
        self.ui.menu_info.setGeometry(
            QtCore.QRect(0, int(self.height() / 5), int(self.width() / 2), int(self.height() / 3)))
        self.ui.coin_label.setGeometry(
            QtCore.QRect(0, int(self.height() / 3), int(self.width() / 2), int(self.height() / 3)))
        self.ui.chest_btn.setGeometry(
            QtCore.QRect(int(self.width()/1.5), int(self.height() / 1.7), int(self.width() / 12), int(self.height() / 8)))
        # int(abs(int(self.width() / 4) - int(self.height() / 3)) / 2) - ustala tak pozycje aby guziki były wypośrodkowane
        self.ui.chest_image.setGeometry(
            QtCore.QRect(int(self.width()/1.7) + int(abs(int(self.width() / 4) - int(self.height() / 3)) / 2), int(self.height() / 4), int(self.height() / 3), int(self.height() / 3)))
        self.ui.chest_label.setGeometry(
            QtCore.QRect(int(self.width()/1.5), int(self.height() / 1.7), int(self.width() / 12), int(self.height() / 8)))

    def resize_shop(self):
        self.ui.sbackground.setGeometry(QtCore.QRect(0, 0, int(self.width()), int(self.height())))
        self.ui.returnBtn.setGeometry(QtCore.QRect(int(self.width() / 7 * 6), int(self.height() / 8 * 7),
                                                   int(self.width() / 7) - 10, int(self.height() / 8) - 10))
        self.ui.label_2.setGeometry(QtCore.QRect(0, 0, int(self.width()), int(self.height()/5)))

        for ind, lab in enumerate(self.ui.label_list):
            lab.setGeometry(QtCore.QRect(int(self.width()/3 * ind), 0,
                            int(self.width()/3), int(self.height()/5)))
        for ind, img in enumerate(self.ui.image_list):
            img.setGeometry(QtCore.QRect(int(self.width() / 3 * ind), int(self.height() / 6),
                            int(self.height() / 5 * 2), int(self.height() / 5 * 2)))
        for ind, btn in enumerate(self.ui.btn_list):
            btn.setGeometry(QtCore.QRect(int(self.width() / 3 * ind), int(self.height() / 6 * 3),
                            int(self.width() / 3/2), int(self.height() / 10)))
        self.ui.scroll.setGeometry(QtCore.QRect(5, int(self.height()/6), int(self.width() - 10), int(self.height()/6 * 4)))
        self.ui.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, int(self.width() / 3 * (ind + 1)), int(self.height()/6 * 4)))
        self.ui.coin_label.setGeometry(QtCore.QRect(10, int(self.height() / 8 * 7),
                                                 int(self.width() / 3), int(self.height() / 8) - 10))
