import time
from datetime import datetime

from PyQt5.QtCore import QThread, pyqtSignal

from core.CollisionHandler import CollisionHandler
from core.KeyHandler import KeyHandler
from core.LevelFactory import LevelFactory
from core.MovementHandler import MovementHandler
from core.Screen import Screen

POINTS_PER_LEVEL = 1000


class CounterThread(QThread):
    game_tick = pyqtSignal(datetime)
    tick_frequency = 50

    def run(self):
        while 1:
            self.game_tick.emit(datetime.now())
            time.sleep(float(1 / self.tick_frequency))


def _exit_game(_):
    exit()


class Game:
    def __init__(self, screen: Screen, level_factory: LevelFactory, key_handler: KeyHandler,
                 collision_handler: CollisionHandler, movement_handler: MovementHandler,
                 on_game_end=_exit_game):
        self.screen = screen
        self.level_factory = level_factory
        self.key_handler = key_handler
        self.collision_handler = collision_handler
        self.game_level = 1
        self.storage = level_factory.create_new(self.game_level)
        self.movement_handler = movement_handler
        self.update_thread = CounterThread()
        self.on_game_end = on_game_end

    def start(self):
        self.screen.keyPressed.connect(self.on_key_pressed)
        self.update_thread.game_tick.connect(self.update)
        self.update_thread.start()

    def on_key_pressed(self, pressed_key):
        self.key_handler.handle(self.storage, pressed_key)

    def update(self, current_time: datetime):
        self.movement_handler.calculate_new_positions(storage=self.storage, current_time=current_time)
        self.collision_handler.handle(storage=self.storage)

        if self._are_all_players_dead(self.storage.players):
            self._stop_threads()
            self.on_game_end(self.storage)
            return

        if self._has_level_ended():
            self.game_level += 1
            self._increase_player_points(self.storage.get_alive_players())
            self.storage = self.level_factory.create_new(self.game_level, self.storage)

    def _stop_threads(self):
        self.update_thread.game_tick.disconnect(self.update)
        self.screen.keyPressed.disconnect(self.on_key_pressed)

    def _has_level_ended(self):
        return len(self.storage.asteroids) == 0

    @staticmethod
    def _increase_player_points(players=[]):
        for player in players:
            player.increase_points(POINTS_PER_LEVEL)

    @staticmethod
    def _are_all_players_dead(players=[]):
        for player in players:
            if not player.is_dead():
                return False
        return True
