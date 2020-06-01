from random import randint, Random

from datetime import datetime
from PyQt5.QtWidgets import QWidget

from entities.Asteroid import Asteroid
from core.utils.Enums import AsteroidSize
from core.utils.image_helper import get_full_image_path


class AsteroidFactory:
    def __init__(self, screen: QWidget, seed=datetime.now()):
        self.random_gen = Random(seed)
        self.screen = screen

    def create_asteroid(self, asteroid_type: AsteroidSize, x=0, y=0, velocity: float = 1, angle: float = 0) -> Asteroid:
        if asteroid_type == AsteroidSize.small:
            return Asteroid(screen=self.screen, x=x, y=y, velocity=velocity, angle=angle, r=35, points=200,
                            img_abs_path=get_full_image_path("asteroid_small.png"))
        if asteroid_type == AsteroidSize.medium:
            return Asteroid(screen=self.screen, x=x, y=y, velocity=velocity, angle=angle, r=52, points=150,
                            img_abs_path=get_full_image_path("asteroid_medium.png"),
                            divide_asteroid=self._divide_medium_asteroid)
        return Asteroid(screen=self.screen, x=x, y=y, velocity=velocity, angle=angle, r=75, points=100,
                        img_abs_path=get_full_image_path("asteroid_large.png"),
                        divide_asteroid=self._divide_large_asteroid)

    def _divide_medium_asteroid(self, asteroid: Asteroid) -> list:
        return self._divide_asteroid(asteroid=asteroid, new_asteroid_type=AsteroidSize.small, velocity_increase=2.0)

    def _divide_large_asteroid(self, asteroid: Asteroid) -> list:
        return self._divide_asteroid(asteroid=asteroid, new_asteroid_type=AsteroidSize.medium, velocity_increase=1.5)

    def _divide_asteroid(self, asteroid: Asteroid, new_asteroid_type: AsteroidSize, velocity_increase: float = 1.0,
                         num_new_asteroids: int = 2) -> list:
        new_asteroids = []
        for _ in range(num_new_asteroids):
            new_asteroids.append(self.create_asteroid(
                asteroid_type=new_asteroid_type,
                x=asteroid.x,
                y=asteroid.y,
                velocity=asteroid.velocity * velocity_increase,
                angle=self.randomize_angle(asteroid.angle)
            ))
        return new_asteroids

    def randomize_angle(self, angle: float) -> float:
        return angle + self.random_gen.randint(-180, 180)  # TODO: Increase randomness of this function
