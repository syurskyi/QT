from math import sin, cos, radians

MIN_VELOCITY = 0
MAX_VELOCITY = 3
MAX_SPEEDUP_FACTOR = 10


class MovableObject:
    def __init__(self, x: float = 0, y: float = 0, velocity: float = 0, angle: float = 0):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.angle = angle
        self.rotation_speed = 10
        self.acceleration_speed = 0.1

    def move(self, elapsed_time: float):
        self.x = self.x + cos(radians(self.angle)) * self.velocity * elapsed_time
        self.y = self.y + sin(radians(self.angle)) * self.velocity * elapsed_time

    def accelerate(self):
        if self.velocity < MAX_VELOCITY:
            self.velocity = self.velocity + self.acceleration_speed

    def decelerate(self):
        if self.velocity > MIN_VELOCITY:
            self.velocity = self.velocity - self.acceleration_speed

    def rotate_left(self):
        self.angle = (self.angle - self.rotation_speed) % 360

    def rotate_right(self):
        self.angle = (self.angle + self.rotation_speed) % 360

    def increase_speed(self, factor=1):
        if factor > MAX_SPEEDUP_FACTOR:
            factor = MAX_SPEEDUP_FACTOR
        self.rotation_speed += factor
        self.acceleration_speed += factor / 10
