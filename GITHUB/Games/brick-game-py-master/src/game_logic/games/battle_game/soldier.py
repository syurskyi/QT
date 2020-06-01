from .constants import *


class Soldier:
    def __init__(self, is_me=False, face=UP, pos_h=0, pos_w=0):
        self.is_me = is_me
        self.face = face

        self.pos_w, self.pos_h = pos_w, pos_h
        self.last_post_w, self.last_pos_h = pos_w, pos_h
        
        self._set_matrix()
    
    def _set_matrix(self):
        face = self.face
        is_me = self.is_me

        p00 = face == DOWN or face == RIGHT
        p01 = not (face == DOWN and not is_me)
        p02 = face == DOWN or face == LEFT
        p10 = not (face == RIGHT and not is_me)
        p11 = True
        p12 = not (face == LEFT and not is_me)
        p20 = face == UP or face == RIGHT
        p21 = not (face == UP and not is_me)
        p22 = face == UP or face == LEFT

        self.matrix = [
            [p00, p01, p02],
            [p10, p11, p12],
            [p20, p21, p22]
        ]
    
    def get_atoms(self):
        h, w = self.pos_h, self.pos_w
        return [(h + i, w + j) for i in range(3) for j in range(3) if self.matrix[i][j] is True]
    
    def get_next_position(self, direction):
        h, w = self.pos_h, self.pos_w

        if self.face != direction:
            # face change, position won't change now
            return h, w
        
        if direction == UP:
            h = max(0, self.pos_h - 1)
        elif direction == DOWN:
            h = min(17, self.pos_h + 1)
        elif direction == LEFT:
            w = max(0, self.pos_w - 1)
        elif direction == RIGHT:
            w = min(7, self.pos_w + 1)
        return h, w
    
    def change_position(self, h, w, face=None):
        self.last_pos_h, self.last_post_w = self.pos_h, self.pos_w
        self.pos_h, self.pos_w = h, w
        if face:
            self.face = face
            self._set_matrix()
