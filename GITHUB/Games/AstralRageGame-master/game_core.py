import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

from main_shot import Ui_MainWindow
from menu_modul import Ui_MainMenu
from skins_or_skills_modul import UiSkinSkills
from window_modul import MyMainWindow
from data_modul import JsonConnector, SoundThread
from aftergame_modul import UiAfterGame
from character_modul import Postac


class GameCore(object):
    ui = None
    window = None

    def start(self):
        self.window = MyMainWindow()
        self.show_main_menu()
        self.window.showFullScreen()
        self.start_menu_music()
        # self.window.show()

    def show_main_menu(self):
        self.ui = Ui_MainMenu()
        self.set_menu_config()
        self.ui.setupUi(self.window)

    def reload_main_menu(self):
        self.ui.centralwidget.close()
        del self.ui
        self.show_main_menu()
        self.window.resize_tlo()
        self.ui.centralwidget.show()

    def set_menu_config(self):
        self.cls_game_config(self.ui, self.window)
        Ui_MainMenu.core = self
        self.window.ui = self.ui

    @classmethod
    def cls_game_config(cls, ui, window):
        cls.ui = ui
        cls.window = window

    def set_game_config(self, ui, window):
        self.cls_game_config(ui, window)
        Postac.set_parrent_objects(window, ui)
        Postac.core = self

        self.window.ui = ui
        self.ui.okno = window

    def play_main_game(self):
        self.reload_main_game()
        self.stop_menu_music()

    def reload_main_game(self):
        self.ui.centralwidget.close()
        del self.ui
        self.ui = Ui_MainWindow()

        self.set_game_config(self.ui, self.window)

        self.ui.setupUi(self.window)
        self.window.resize_tlo()
        Postac.score = 0
        self.ui.centralwidget.show()
        self.window.main_game = True
        Postac.start_enemy_clock()

        self.music = SoundThread("shotMainSoundtrack.wav", True)
        self.music.start()

    def make_aftergame(self):
        self.ui.centralwidget.close()
        del self.ui
        self.load_aftergame()

    def load_aftergame(self):
        self.ui = UiAfterGame()
        self.set_aftergame_config()
        self.ui.setupUi(self.window)
        self.window.resize_tlo()
        self.ui.centralwidget.show()

    def set_aftergame_config(self):
        self.cls_game_config(self.ui, self.window)
        self.ui.core = self
        self.window.ui = self.ui

    def load_shop(self):
        self.ui.centralwidget.close()
        del self.ui
        self.ui = UiSkinSkills()
        self.shop_config()
        self.ui.setupUi(self.window, "skins")
        self.window.resize_tlo()
        self.ui.centralwidget.show()

    def shop_config(self):
        self.window.ui = self.ui
        self.cls_game_config(self.ui, self.window)
        self.ui.core = self

    def load_skills_menu(self):
        self.ui.centralwidget.close()
        del self.ui
        self.ui = UiSkinSkills()
        self.skills_menu_config()
        self.ui.setupUi(self.window, "skills")
        self.window.resize_tlo()
        self.ui.centralwidget.show()

    def skills_menu_config(self):
        self.window.ui = self.ui
        self.cls_game_config(self.ui, self.window)
        self.ui.core = self

    def player_death(self):
        self.window.main_game = False
        self.make_aftergame()
        self.check_score()

        self.music.stop()
        x = SoundThread("shotError.wav")
        x.start()

    def check_score(self):
        x = JsonConnector.get_from_config("highscore")
        if x < Postac.score:
            JsonConnector.save_key_to_config("highscore", Postac.score)

    def start_menu_music(self):
        self.menu_music = SoundThread("shotMenuSoundtrack.wav", loop=True)
        self.menu_music.start()

    def stop_menu_music(self):
        self.menu_music.stop()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    core = GameCore()
    core.start()

    sys.exit(app.exec_())
