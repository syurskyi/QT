import random

import PyQt5
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QTimer, QByteArray
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QMovie

from data_modul import JsonConnector, SoundThread


class Postac(QLabel):       # klasa do wszystkich niestandardowych table w projekcie
    lista_postaci = []
    enemies = []
    disabled = []       # składuje instancje którezostały trafione pociskiem i odgrywają animację zniszczenia
    ui = None
    okno = None
    score = 0
    core = None

    def __init__(self, layout, *args):
        super().__init__(layout, *args)
        Postac.lista_postaci.append(self)   # odpowiada za dodawanie elementów do listy przez co będzie można się do nich wszystkich odwoła

    @classmethod
    def set_parrent_objects(cls, okno_inst, ui_inst):
        cls.ui = ui_inst
        cls.okno = okno_inst

    @classmethod
    def show_score(cls):
        txt = cls.ui.score.text()
        cls.ui.score.setText(txt[:7] + str(cls.score))

    @classmethod
    def start_enemy_clock(cls):
        cls.ui.centralwidget.close()
        Gunner(cls.ui.centralwidget)
        Scout(cls.ui.centralwidget)
        Heavy(cls.ui.centralwidget)
        Speed(cls.ui.centralwidget)
        cls.ui.centralwidget.show()
        cls.etimer = QTimer()
        cls.etimer.timeout.connect(cls.make_enemy_wave)
        cls.etimer.start(19000)

    @classmethod
    def make_enemy_wave(cls):
        cls.ui.centralwidget.close()
        if cls.score < 2000:
            cls.enemy_wave_lvl1()
        elif cls.score < 5000:
            cls.enemy_wave_lvl2()
        elif cls.score < 10000:
            cls.enemy_wave_lvl3()
        elif cls.score < 25000:
            cls.enemy_wave_lvl4()
        else:
            cls.enemy_wave_lvl5()
        cls.ui.centralwidget.show()

    @classmethod
    def enemy_wave_lvl1(cls):
        for i in range(random.randint(3, 8)):
            Scout(cls.ui.centralwidget, ob_width=random.randint(9, 15), ob_height=random.randint(9, 15), speed=random.randint(50, 75),
                  max_move=random.randint(20, 50), frequency_change_direction=random.randint(20, 50), shot_frequency=random.randint(700, 1500))

    @classmethod
    def enemy_wave_lvl2(cls):
        for i in range(random.randint(4, 7)):
            Scout(cls.ui.centralwidget, ob_width=random.randint(9, 20), ob_height=random.randint(9, 20),
                  speed=random.randint(50, 75),
                  max_move=random.randint(20, 50), frequency_change_direction=random.randint(20, 50),
                  shot_frequency=random.randint(800, 1500))
        for i in range(random.randint(1, 3)):
            Heavy(cls.ui.centralwidget, ob_width=random.randint(5, 8), ob_height=random.randint(5, 8),
                  shot_frequency=random.randint(1000, 2500), speed=random.randint(60, 85),
                  max_move=random.randint(15, 30), frequency_change_direction=random.randint(60, 100))

    @classmethod
    def enemy_wave_lvl3(cls):
        for i in range(random.randint(3, 6)):
            Scout(cls.ui.centralwidget, ob_width=random.randint(9, 20), ob_height=random.randint(9, 20),
                  speed=random.randint(50, 75),
                  max_move=random.randint(20, 50), frequency_change_direction=random.randint(20, 50),
                  shot_frequency=random.randint(1000, 1500))
        for i in range(random.randint(2, 4)):
            Heavy(cls.ui.centralwidget, ob_width=random.randint(5, 8), ob_height=random.randint(5, 8),
                  shot_frequency=random.randint(1000, 2500), speed=random.randint(60, 85),
                  max_move=random.randint(15, 30), frequency_change_direction=random.randint(60, 100))
        for i in range(random.randint(3, 4)):
            Gunner(cls.ui.centralwidget, ob_width=random.randint(6, 15), ob_height=random.randint(6, 15),
                   shot_frequency=random.randint(2500, 4500), speed=random.randint(45, 75),
                   max_move=random.randint(25, 40), frequency_change_direction=random.randint(20, 60))

    @classmethod
    def enemy_wave_lvl4(cls):
        for i in range(random.randint(3, 4)):
            Scout(cls.ui.centralwidget, ob_width=random.randint(9, 14), ob_height=random.randint(9, 14),
                  speed=random.randint(20, 45),
                  max_move=random.randint(20, 50), frequency_change_direction=random.randint(20, 50),
                  shot_frequency=random.randint(1000, 1500))
        for i in range(random.randint(2, 3)):
            Heavy(cls.ui.centralwidget, ob_width=random.randint(5, 8), ob_height=random.randint(5, 8),
                  shot_frequency=random.randint(1000, 2500), speed=random.randint(60, 85),
                  max_move=random.randint(15, 30), frequency_change_direction=random.randint(60, 100))
        for i in range(random.randint(3, 6)):
            Gunner(cls.ui.centralwidget, ob_width=random.randint(6, 15), ob_height=random.randint(6, 15),
                   shot_frequency=random.randint(2500, 4500), speed=random.randint(45, 75),
                   max_move=random.randint(25, 40), frequency_change_direction=random.randint(20, 60))
        for i in range(random.randint(3, 6)):
            Speed(cls.ui.centralwidget, ob_width=random.randint(15, 23), ob_height=random.randint(15, 23),
                  speed=random.randint(40, 62), max_move=random.randint(40, 60),
                  frequency_change_direction=random.randint(15, 30), shot_frequency=random.randint(500, 1000))

    @classmethod
    def enemy_wave_lvl5(cls):
        for i in range(random.randint(2, 3)):
            Scout(cls.ui.centralwidget, ob_width=random.randint(9, 14), ob_height=random.randint(9, 14),
                  speed=random.randint(50, 75),
                  max_move=random.randint(20, 50), frequency_change_direction=random.randint(20, 50),
                  shot_frequency=random.randint(1000, 1500))
        for i in range(random.randint(3, 5)):
            Heavy(cls.ui.centralwidget, ob_width=random.randint(5, 8), ob_height=random.randint(5, 8),
                  shot_frequency=random.randint(1000, 2500), speed=random.randint(60, 85),
                  max_move=random.randint(15, 30), frequency_change_direction=random.randint(60, 100))
        for i in range(random.randint(5, 7)):
            Gunner(cls.ui.centralwidget, ob_width=random.randint(6, 15), ob_height=random.randint(6, 15),
                   shot_frequency=random.randint(2500, 4500), speed=random.randint(45, 75),
                   max_move=random.randint(25, 40), frequency_change_direction=random.randint(20, 60))
        for i in range(random.randint(2, 5)):
            Speed(cls.ui.centralwidget, ob_width=random.randint(15, 23), ob_height=random.randint(15, 23),
                  speed=random.randint(45, 60), max_move=random.randint(40, 60),
                  frequency_change_direction=random.randint(15, 30), shot_frequency=random.randint(1500, 2500))

    @classmethod
    def make_enemy_wave_early(cls):
        cls.etimer.stop()
        cls.make_enemy_wave()
        cls.etimer.start()

    def kill(self):
        if self in self.enemies:
            self.enemies.remove(self)
        Postac.lista_postaci.remove(self)
        self.setParent(None)
        self.deleteLater()
        self = None

    @classmethod
    def endgame(cls):
        cls.etimer.stop()
        cls.ui.movie.stop()

        for x in cls.lista_postaci:
            if type(x) == PlayerLaser or type(x) == EnemyLaser:
                x.timer.stop()
            if type(x) == Benek:
                cls.stop_player_clocks(x)
                x.kill()
        for x in cls.lista_postaci:
            if type(x) == PlayerLaser or type(x) == EnemyLaser:
                x.kill()

        for x in cls.enemies:
            x.timer.stop()
            x.stimer.stop()
            x.kill()

        cls.lista_postaci = []
        cls.enemies = []
        cls.core.player_death()

    @classmethod
    def stop_player_clocks(cls, hit):
        for x in hit.clocks:
            x.stop()


class Parowka(Postac):
    """ klasa rodzica dla wszystkich wrogów, w praktyce aby stworzyć nwego wroga wystarczy nowa klasa dziedzicząca,
    dodanie jej jako cel do laseru gracza, oraz wywołanie odpowiedniego inita, ewentualnie nadpisaniu metod"""

    def __init__(self, layout, ob_width=100, ob_height=100, speed=25, max_move=50, frequency_change_direction=50, shot_frequency=3500, *args):
        super().__init__(layout, *args)
        self.enemies.append(self)

        self.make_random_pos(ob_width, ob_height)
        self.setText("")
        self.setPixmap(QtGui.QPixmap("images/parowa.png"))
        self.setScaledContents(True)

        self.speed = speed
        self.max_move = max_move
        self.frequency_change_direction = frequency_change_direction
        self.shot_frequency = shot_frequency

        self.start_enemy_action_clock()
        self.start_enemy_shot_clock()

    def make_random_pos(self, ob_width, ob_height):     # ustawia parowke w losową pozycje
        lb = int((self.okno.width() - self.okno.gWidth) / 2)    # lewy bok
        self.setGeometry(QtCore.QRect((lb + random.randint(10, (self.okno.gWidth - int(self.okno.gWidth/ob_width)))),
                                      0, int(self.okno.gWidth/ob_width), int(self.okno.gHeight/ob_height)))

    def start_enemy_action_clock(self):
        """ tworzy zegar który odpowiada za ruch wrogów """
        self.timer = QTimer()
        self.timer.timeout.connect(self.move_enemy)
        self.il_ruch_w_bok = random.randint(1, 26)      # losuje ile ruchów odbyć w danym kierunku
        self.enemy_move_licz = self.il_ruch_w_bok
        self.enemy_move_direction = bool(random.getrandbits(1))     # losuje kierunek ruchu
        self.timer.start(self.speed)

    def move_enemy(self):       # odpowiada za ruch wroga
        if self.enemy_move_licz == 0:   # jeśli licznik ruchu w jedną strone się skończył to go znów generuje
            self.il_ruch_w_bok = random.randint(1, self.frequency_change_direction)
            self.enemy_move_licz = self.il_ruch_w_bok
            self.enemy_move_direction = bool(random.getrandbits(1))       # 1 - prawo, 0 - lewo
        self.enemy_move_licz -= 1
        e_x = self.x()
        e_y = self.y()

        if self.enemy_move_direction:   # jeśli ruch jest true czyli 1 to dodaje x czyi przesuwa w prawo
            e_x += self.max_move
        else:
            e_x -= self.max_move

        if ((self.okno.gWidth + ((self.okno.width() - self.okno.gWidth) / 2)) - self.width()) >= e_x >= ((self.okno.width() - self.okno.gWidth) / 2):       # odpowiada za odbijanie kierunku ruchu przy ścianie
            self.setGeometry(e_x, e_y, self.width(), self.height())
        else:
            self.enemy_move_direction = not self.enemy_move_direction

    def start_enemy_shot_clock(self):
        self.stimer = QTimer()
        self.stimer.timeout.connect(self.enemy_shot)
        self.stimer.start(self.shot_frequency)

    def enemy_shot(self):
        x = SoundThread("shotLaserEnemy.wav")
        x.start()

        self.ui.centralwidget.close()
        x = EnemyLaser(self.ui.centralwidget,
                       cause_geo=self.geometry())  # aby poprawnie dodać element do główneg widgetu należy go wyłączyć a następnie pokazać, czli zresetować
        self.ui.centralwidget.show()

    def explosion_animation(self):
        self.disabled.append(self)
        self.death_movie = QMovie("images/explosion.gif", QByteArray(), self)
        self.death_movie.setCacheMode(QMovie.CacheAll)
        self.death_movie.setSpeed(100)  # ustala tak prędkość aby pokrywała się z szybkostrzelnością
        self.setMovie(self.death_movie)
        self.death_movie.start()

        self.stimer.stop()
        self.timer.stop()

        self.death_timer = QTimer()
        self.death_timer.timeout.connect(self.explosion_animation2)
        self.death_timer.start(100)

    def explosion_animation2(self):
        self.disabled.remove(self)
        self.kill()
        if not self.enemies:
            self.make_enemy_wave_early()


class Benek(Postac):
    def __init__(self, layout, move_distance=100, *args):
        super().__init__(layout, *args)
        self.clocks = []

        self.load_player_config()

        self.set_player_geo()
        self.setText("")
        self.setPixmap(QtGui.QPixmap("images/skins/" + JsonConnector.get_from_config("skin") + ".png"))
        self.setScaledContents(True)        # odpowiada za pozwolenie na skalowanie grafik

        self.move_distance = self.okno.gWidth / move_distance
        self.can_shot = True

        self.playing_sound = False

        self.rtimer = QTimer()
        self.clocks.append(self.rtimer)
        self.rtimer.timeout.connect(self.ruch_prawo)
        self.ltimer = QTimer()
        self.clocks.append(self.ltimer)
        self.ltimer.timeout.connect(self.ruch_lewo)

        self.shot_block_timer = QTimer()
        self.clocks.append(self.shot_block_timer)
        self.shot_block_timer.timeout.connect(self.shot_accuracy_unblock)

        self.make_move_animations()
        self.make_reload_bar()

    def load_player_config(self):
        config = JsonConnector.get_from_config("shipConfig")
        self.laser_penetrate = config["penetrate"]
        self.ship_size = config["shipSize"]
        self.fire_speed = config["fireSpeed"]
        self.ammo_size = config["ammoSize"]
        self.ammo_dist = config["ammoSpeed"]

    def set_player_geo(self):
        size = int(self.okno.gWidth/self.ship_size)
        self.setGeometry(QtCore.QRect((self.okno.width() - size)/2, self.okno.height() - size, size, size))

    def rusz_benek_prawo(self):
        self.rtimer.start(15)
        self.pg = int((self.okno.width() - self.okno.gWidth) / 2 + self.okno.gWidth)    # prawa granica
        self.x_ = self.geometry().x()

        self.move_sound_start()
        self.expand_anim_movie(self.lmove_anim)

    def ruch_prawo(self):
        if self.pg >= (self.x_ + self.width()):     # zapezpiecza postać przed wyjściem poza okno
            if (self.pg - (self.x_ + self.width())) < self.move_distance:   # jeśli odległość od lewego krańca jest mniejsza od ruchu to zmienia pozycje benka na krańcową
                self.x_ = self.pg - self.width()
            else:
                self.x_ += self.move_distance
            geo = QtCore.QRect(self.x_, self.geometry().y(), self.geometry().width(), self.geometry().height())
            self.setGeometry(geo)

    def stop_rusz_benek_prawo(self):
        self.rtimer.stop()
        self.move_sound_stop()
        self.collapse_anim_movie(self.lmove_anim)

    def rusz_benek_lewo(self):
        self.ltimer.start(15)
        self.x_ = self.geometry().x()
        self.lg = int((self.okno.width() - self.okno.gWidth) / 2) # lewa granica

        self.move_sound_start()
        self.expand_anim_movie(self.rmove_anim)

    def ruch_lewo(self):
        if self.x_ > self.lg:           # zabezpiecza przed wyjściem benka poza ekran
            if self.x_ - self.lg < self.move_distance:      # jeśli benkowi brakuje mniej niż dystans ruchu to przyjmuje zerową pozycje
                self.x_ = self.lg
            else:
                self.x_ -= self.move_distance
            geo = QtCore.QRect(self.x_, self.geometry().y(), self.geometry().width(), self.geometry().height())
            self.setGeometry(geo)

    def stop_rusz_benek_lewo(self):
        self.ltimer.stop()
        self.move_sound_stop()
        self.collapse_anim_movie(self.rmove_anim)

    def shot(self):     # tworzy nowy strzał
        if self.can_shot:
            x = SoundThread("shotLaser.wav")
            x.start()

            self.ui.centralwidget.close()
            x = PlayerLaser(self.ui.centralwidget, cause_geo=self.geometry(), can_penetrate=self.laser_penetrate, bullet_width=self.ammo_size[0], bullet_height=self.ammo_size[1], bullet_distance=self.ammo_dist)       # aby poprawnie dodać element do główneg widgetu należy go wyłączyć a następnie pokazać, czli zresetować
            self.ui.centralwidget.show()
            self.shot_accuracy_block()

    def shot_accuracy_block(self):
        self.can_shot = False
        self.shot_block_timer.start(self.fire_speed)

        self.movie.start()

    def shot_accuracy_unblock(self):
        self.can_shot = True
        self.shot_block_timer.stop()

        self.movie.stop()
        self.movie.jumpToFrame(self.movie.frameCount()-1)

    def move_sound_start(self):
        if not self.playing_sound:
            self.playing_sound = True
            self.move_sound = SoundThread("shotEngineNoise.wav", loop=True)
            self.clocks.append(self.move_sound)
            self.move_sound.start()

    def move_sound_stop(self):
        if self.playing_sound and not (self.ltimer.isActive() or self.rtimer.isActive()):
            self.move_sound.stop()
            self.clocks.remove(self.move_sound)
            self.playing_sound = False

    def make_reload_bar(self):
        self.reload_bar = QLabel(self)
        self.reload_bar.setGeometry(QtCore.QRect(int(self.width()/6), 0, int(self.width()/6), int(self.height()/2)))
        self.reload_bar.setText("aa")
        self.reload_bar.setPixmap(QtGui.QPixmap("images/reloadBar.gif"))
        self.reload_bar.setScaledContents(True)

        self.movie = QMovie("images/reloadBar.gif", QByteArray(), self.reload_bar)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setSpeed(100 * 1000 / self.fire_speed)   # ustala tak prędkość aby pokrywała się z szybkostrzelnością
        self.reload_bar.setMovie(self.movie)
        self.movie.jumpToFrame(self.movie.frameCount()-1)

    def make_move_animations(self):
        self.lmove_lab = QLabel(self)
        self.lmove_lab.setText("")
        self.lmove_lab.setGeometry(QtCore.QRect(0, 0, int(self.width() / 3), self.height()))
        self.lmove_lab.setScaledContents(True)

        self.lmove_anim = QMovie("images/lPlayerMove.gif", QByteArray(), self.lmove_lab)
        self.lmove_anim.setCacheMode(QMovie.CacheAll)
        self.lmove_anim.setSpeed(7000)
        self.lmove_lab.setMovie(self.lmove_anim)
        self.lmove_anim.jumpToFrame(0)

        self.rmove_lab = QLabel(self)
        self.rmove_lab.setText("")
        self.rmove_lab.setGeometry(QtCore.QRect(int(self.width() / 3*2), 0, int(self.width() / 3), self.height()))
        self.rmove_lab.setScaledContents(True)

        self.rmove_anim = QMovie("images/rPlayerMove.gif", QByteArray(), self.rmove_lab)
        self.rmove_anim.setCacheMode(QMovie.CacheAll)
        self.rmove_anim.setSpeed(7000)
        self.rmove_lab.setMovie(self.rmove_anim)
        self.rmove_anim.jumpToFrame(0)
        self.rmove_anim.frameCount()

    def expand_anim_movie(self, movie):
        movie.jumpToFrame(int(movie.frameCount() / 2))

    def collapse_anim_movie(self, movie):
        movie.jumpToFrame(0)


class Laser(Postac):
    """ klasa naboju wystrzelonego przez gracza lub wroga, można ustawić wiele opcji tego obiektu, więc łatwo będzie go
    przerobić, korzysta z wartości self.x_ aby zaoszczędzić takty zegara na sprawdzaniu x naboju który i ttak jest stały
     dla każdego naboju"""
    def __init__(self, layout, cause_geo, bullet_width, bullet_height, bullet_speed, bullet_distance, *args):
        super().__init__(layout, *args)
        self.bullet_distance = bullet_distance
        self.targets = []       # lista na klasy obiektów w które strzał ma przynieść efekt

        self.setText("")
        self.setObjectName('laser')
        self.setStyleSheet("QLabel#laser {background-color: red}")

        self.set_start_pos(cause_geo, bullet_width, bullet_height)
        self.x_ = self.x()
        self.start_bullet_move_clock(bullet_speed)

    def set_start_pos(self, cause_geo, bullet_width, bullet_height):
        """ ustawia początkową pozycję naboju tak aby był wypośrodkowany w celu """
        pass    # to override

    def start_bullet_move_clock(self, speed):
        """ tworzy zegar który odpowiada za ruch naboju """
        self.timer = QTimer()
        self.timer.timeout.connect(self.move_laser)
        self.timer.start(speed)

    def move_laser(self):
        """ odpowiednio przesuwa laser """
        pass    # to override

    def check_hit(self):
        """ sprawdza kolizję obiektu """
        for x in Postac.lista_postaci:
            if type(x) in self.targets:
                if self.y() < (x.y() + x.height()) and self.y() + self.height() > x.y():
                    if self.x() < (x.x() + x.width()) and (self.x() + self.width()) > x.x():
                        self.when_hit(x)
                        break

    def when_hit(self, hit):
        """ wywoływane gdy nabój styka się z celem z self.targets """
        pass        # to override


class PlayerLaser(Laser):
    """ laser gracza za cele przyjmuje wrogów Parowka i ich naboje które niszczy przy trafieniu """
    def __init__(self, layout, cause_geo, bullet_width=100, bullet_height=20, bullet_speed=13, bullet_distance=15, can_penetrate=False, *args):
        self.bullet_distance = self.okno.gHeight/bullet_distance
        self.bullet_height = self.okno.gHeight/bullet_height
        self.bullet_width = self.okno.gHeight/bullet_width
        super().__init__(layout, cause_geo, self.bullet_width, self.bullet_height, bullet_speed, self.bullet_distance, *args)
        self.targets = [EnemyLaser, Scout, Parowka, Heavy, Gunner, Speed]
        self.can_penetrate = can_penetrate

    def set_start_pos(self, cause_geo, bullet_width, bullet_height):
        x = cause_geo.x() + ((cause_geo.width() + bullet_width) / 2)
        y = self.okno.height() - (cause_geo.height()/1.5) - bullet_height
        self.setGeometry(QtCore.QRect(x, y, bullet_width, bullet_height))

    def move_laser(self):
        if self.y() + self.height() >= 0:
            self.check_hit()
            self.setGeometry(QtCore.QRect(self.x_, self.y() - self.bullet_distance, self.width(), self.height()))
        else:
            self.kill()

    def when_hit(self, hit):
        if hit not in self.disabled:
            if not self.can_penetrate:
                self.kill()
            if type(hit) == Scout:
                Postac.score += 100
            elif type(hit) == Heavy:
                Postac.score += 200
            elif type(hit) == Gunner:
                Postac.score += 300
                hit.sstimer.stop()
            elif type(hit) == Speed:
                Postac.score += 500

            if hit in self.enemies:
                hit.explosion_animation()   # po tym wywoływany jest kill
            else:
                hit.kill()
            Postac.show_score()
            self.play_hit_sound()

    @staticmethod
    def play_hit_sound():
        sound = SoundThread("shotLaserExplosion.wav", loop=False)
        sound.start()


class EnemyLaser(Laser):
    def __init__(self, layout, cause_geo, bullet_width=10, bullet_height=50, bullet_speed=60, bullet_distance=25, *args):
        self.bullet_distance = self.okno.gHeight/bullet_distance
        super().__init__(layout, cause_geo, bullet_width, bullet_height, bullet_speed, self.bullet_distance, *args)
        self.targets = [Benek]

    def set_start_pos(self, cause_geo, bullet_width, bullet_height):
        x = cause_geo.x() + ((cause_geo.width() + bullet_width) / 2)
        y = cause_geo.height()/1.5
        self.setGeometry(QtCore.QRect(x, y, bullet_width, bullet_height))

    def move_laser(self):
        if self.y() <= self.okno.height():
            self.setGeometry(QtCore.QRect(self.x_, self.y() + self.bullet_distance, self.width(), self.height()))
            self.check_hit()
        else:
            self.kill()

    def when_hit(self, hit):
        self.timer.stop()
        Postac.okno.main_game = False

        self.kill()
        Postac.endgame()


class Scout(Parowka):
    def __init__(self, layout, ob_width=10, ob_height=10, speed=45, max_move=35, frequency_change_direction=50, shot_frequency=3500, *args):
        super().__init__(layout, ob_width, ob_height, speed, max_move, frequency_change_direction, shot_frequency, *args)
        self.setPixmap(QtGui.QPixmap("images/enemy1.png"))


class Heavy(Parowka):
    def __init__(self, layout, ob_width=5, ob_height=7, speed=55, max_move=30, frequency_change_direction=80,
                 shot_frequency=2500, *args):
        super().__init__(layout, ob_width, ob_height, speed, max_move, frequency_change_direction, shot_frequency,
                         *args)
        self.setPixmap(QtGui.QPixmap("images/enemy2.png"))

    def enemy_shot(self):
        x = SoundThread("shotLaserLow.wav")
        x.start()

        self.ui.centralwidget.close()
        x = EnemyLaser(self.ui.centralwidget, cause_geo=self.geometry(), bullet_width=50, bullet_height=80)  # aby poprawnie dodać element do główneg widgetu należy go wyłączyć a następnie pokazać, czli zresetować
        self.ui.centralwidget.show()


class Gunner(Parowka):
    def __init__(self, layout, ob_width=12, ob_height=12, speed=45, max_move=40, frequency_change_direction=30,
                 shot_frequency=2500, *args):
        super().__init__(layout, ob_width, ob_height, speed, max_move, frequency_change_direction, shot_frequency,
                         *args)
        self.setPixmap(QtGui.QPixmap("images/enemy3.png"))
        self.sstimer = QTimer()
        self.sstimer.timeout.connect(self.one_shot)

    def enemy_shot(self):
        self.iter_shot = 5
        self.sstimer.start(100)
        self.one_shot()

    def one_shot(self):
        x = SoundThread("shotLaserEnemy.wav")
        x.start()

        self.ui.centralwidget.close()
        x = EnemyLaser(self.ui.centralwidget,
                       cause_geo=self.geometry(), bullet_width=12, bullet_height=55)  # aby poprawnie dodać element do główneg widgetu należy go wyłączyć a następnie pokazać, czli zresetować
        self.ui.centralwidget.show()
        self.iter_shot -= 1
        if self.iter_shot == 0:
            self.sstimer.stop()


class Speed(Parowka):
    def __init__(self, layout, ob_width=22, ob_height=22, speed=35, max_move=45, frequency_change_direction=30, shot_frequency=2500, *args):
        super().__init__(layout, ob_width, ob_height, speed, max_move, frequency_change_direction, shot_frequency, *args)
        self.setPixmap(QtGui.QPixmap("images/enemy4.png"))

    def enemy_shot(self):
        x = SoundThread("shotLaserHeight.wav")
        x.start()

        self.ui.centralwidget.close()
        x = EnemyLaser(self.ui.centralwidget, cause_geo=self.geometry(), bullet_width=7, bullet_height=25)  # aby poprawnie dodać element do główneg widgetu należy go wyłączyć a następnie pokazać, czli zresetować
        self.ui.centralwidget.show()
