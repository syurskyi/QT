from PyQt5.uic.properties import QtGui

from persistance.Storage import Storage
from core.utils.collision import are_circles_collided
from entities.Player import Player


class CollisionHandler:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def handle(self, storage: Storage):
        self._handle_spacecraft_with_asteroid_collision(storage)
        self._handle_bullets_with_asteroid_collision(storage)
        self._handle_spacecraft_with_heart_collision(storage)
        self._remove_destroyed_elements(storage)

    def _handle_spacecraft_with_asteroid_collision(self, storage: Storage):
        """
        Removes life of the player if his spacecraft has hit the asteroid.
        If player has no lives left then spacecraft will be removed from screen
        """
        for spacecraft in storage.spacecrafts:
            if spacecraft.is_invincible:
                continue
            for asteroid in storage.asteroids:
                if not are_circles_collided(spacecraft, asteroid):
                    continue
                player = storage.get_player_by_id(spacecraft.player_id)
                player.remove_life()
                spacecraft.set_invincibility(True)
                if player.is_dead():
                    spacecraft.destroy()

                break



    @staticmethod
    def _handle_spacecraft_with_heart_collision(storage: Storage):
        """
        Removes life of the player if his spacecraft has hit the asteroid.
        If player has no lives left then spacecraft will be removed from screen
        """
        for spacecraft in storage.spacecrafts:
            for heart in storage.hearts:
                if not are_circles_collided(spacecraft, heart):
                    continue
                player = storage.get_player_by_id(spacecraft.player_id)
                player.add_life()
                heart.destroy()

    @staticmethod
    def _handle_bullets_with_asteroid_collision(storage: Storage):
        """
        Checks if bullet has hit asteroid.
        Upon collision asteroid will be divided or removed and player will gain points.
        """
        new_asteroids = []
        for bullet in storage.bullets:
            for asteroid in storage.asteroids:
                if not are_circles_collided(bullet, asteroid):
                    continue
                player = storage.get_player_by_id(bullet.player_id)
                player.increase_points(asteroid.points)

                divided_asteroids = asteroid.divide()
                new_asteroids.extend(divided_asteroids)

                bullet.destroy()
                asteroid.destroy()
                break
        storage.asteroids.extend(new_asteroids)



    def _remove_destroyed_elements(self, storage: Storage):
        storage.asteroids = self._filter_out_hidden_elements(storage.asteroids)
        storage.bullets = self._filter_out_hidden_elements(storage.bullets)
        storage.hearts = self._filter_out_hidden_elements(storage.hearts)
        storage.spacecrafts = self._filter_out_hidden_elements(storage.spacecrafts)

    def _filter_out_hidden_elements(self, elements: list) -> list:
        return list(filter(lambda circle: not circle.is_hidden(), elements))
