from persistance.Storage import Storage
from datetime import datetime
from core.utils.time_helper import convert_timestamp_to_microseconds


class MovementHandler:
    def __init__(self, timestamp: datetime, screen_width, screen_height):
        self.last_time_recorded = timestamp
        self.screen_width = screen_width
        self.screen_height = screen_height
        # prodje oko 100.000 usec izmedju poziva funkcije pa se redukuje ovde da bi objekti mogli nomalno
        # da se krecu
        self.reduction_factor = 10000
        pass

    def calculate_new_positions(self, storage: Storage, current_time: datetime):
        elapsed_time = (convert_timestamp_to_microseconds(current_time) -
                        convert_timestamp_to_microseconds(self.last_time_recorded)) / self.reduction_factor
        self.last_time_recorded = current_time

        for asteroid in storage.get_all_asteroids():
            asteroid.move(elapsed_time)
            self._clip(asteroid)

        for bullet in storage.get_all_bullets():
            bullet.move(elapsed_time)

        for spacecraft in storage.get_all_spacecrafts():
            spacecraft.move(elapsed_time)
            self._clip(spacecraft)
            if spacecraft.is_invincible:
                #print(f"Increase time by {elapsed_time} (current time{spacecraft.time_spent_invincible})")
                spacecraft.increase_time_invincible(elapsed_time)

        for heart in storage.get_all_hearts():
            heart.move(elapsed_time)
            self._clip(heart)

    def _clip(self, circle):
        if circle.x < 0:
            circle.x = self.screen_width + circle.x
        elif circle.x > self.screen_width:
            circle.x = circle.x - self.screen_width

        if circle.y < 0:
            circle.y = self.screen_height + circle.y
        elif circle.y > self.screen_height:
            circle.y = circle.y - self.screen_height
