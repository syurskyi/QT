from .constants import *


class Bullet:
    
    def __init__(self, shooter):
        self.shooter = shooter
        direction = shooter.face

        if direction == UP:
            self.pos_h = shooter.pos_h - 1
            self.pos_w = shooter.pos_w + 1
            self.move_forward = self.go_up
        elif direction == DOWN:
            self.pos_h = shooter.pos_h + 3
            self.pos_w = shooter.pos_w + 1
            self.move_forward = self.go_down
        elif direction == LEFT:
            self.pos_h = shooter.pos_h + 1
            self.pos_w = shooter.pos_w - 1
            self.move_forward = self.go_left
        elif direction == RIGHT:
            self.pos_h = shooter.pos_h + 1
            self.pos_w = shooter.pos_w + 3
            self.move_forward = self.go_right

    def go_up(self):
        self.pos_h -= 1
    
    def go_down(self):
        self.pos_h += 1

    def go_left(self):
        self.pos_w -= 1
    
    def go_right(self):
        self.pos_w += 1
    
    def out_of_edge(self):
        h, w = self.pos_h, self.pos_w
        return h < 0 or h > 19 or w < 0 or w > 9
