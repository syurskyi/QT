from src.game_logic.games.game import Game
from .constants import *
from .soldier import Soldier
from .bullet import Bullet
import random
from threading import Lock
import time


lock = Lock()


class BattleGame(Game):
    def __init__(self, serial, game_api):
        Game.__init__(
            self,
            name='Battle',
            serial=serial,
            game_api=game_api
        )
        self.state = None
    
    @staticmethod
    def _create_state():
        return {
            'my_soldier': None,
            'enemies_alive': [],
            'bullets': []
        }
    
    def launch(self):
        super().launch()

        self.state = self._create_state()
        self.state['my_soldier'] = Soldier(pos_h=7, pos_w=4, is_me=True)
        
        self._init_game_view()
        
        self.set_interval(1, self._add_enemy)
        self.set_interval(1, self._move_enemy)
        self.set_interval(1.5, self._engage_enemy)
        self.set_interval(0.5, self._process_bullets)

    def _init_game_view(self):
        self._draw_soldier(self.state['my_soldier'])

    def _erase_soldier(self, soldier):
        self.clear_game_screen(h0=soldier.last_pos_h, w0=soldier.last_post_w, h=3, w=3)
        
    def _draw_soldier(self, soldier):
        self._erase_soldier(soldier)
        self.game_gl.draw_atoms(*soldier.get_atoms())
    
    def print_intro(self):
        super().print_intro()
        self.game_gl.alphabet('A')
        self._draw_soldier(Soldier(pos_w=1, pos_h=13))
        self._draw_soldier(Soldier(pos_w=7, pos_h=13, face=LEFT))
        self.game_gl.draw_atoms((14, 5))
    
    def _get_an_open_position(self):
        possible_positions = [(0, 0), (0, 7), (17, 0), (17, 7)]
        random.shuffle(possible_positions)

        for h, w in possible_positions:
            if not self._will_collide_with_others(h, w):
                return h, w
    
    def _move_enemy(self):
        if len(self.state['enemies_alive']) == 0:
            return
        
        enemy = random.choice(self.state['enemies_alive'])
        direction = random.choice([UP, enemy.face, DOWN, enemy.face, LEFT, enemy.face, RIGHT, enemy.face])
        self._move_soldier(enemy, direction)
    
    def _add_enemy(self):
        if len(self.state['enemies_alive']) >= 4:
            return
        
        open_pos = self._get_an_open_position()
        if open_pos is None:
            return
        
        h, w = open_pos
        face = random.choice([UP, DOWN, LEFT, RIGHT])
        
        new_enemy = Soldier(pos_h=h, pos_w=w, face=face)
        self.state['enemies_alive'].append(new_enemy)
        self._draw_soldier(new_enemy)

    def _will_collide_with_others(self, pos_h, pos_w, whom=None):
        all_soldiers = [self.state['my_soldier']] + self.state['enemies_alive']
        try:
            all_soldiers.remove(whom)
        except ValueError:
            pass
        
        all_soldier_positions = [(s.pos_h, s.pos_w) for s in all_soldiers]

        for hi, wi in all_soldier_positions:
            dif_h, dif_w = abs(pos_h - hi), abs(pos_w - wi)
            if dif_h < 3 and dif_w < 3:
                return True
        return False

    def _move_soldier(self, soldier, direction):
        pos_h, pos_w = soldier.get_next_position(direction)
        
        will_collide = self._will_collide_with_others(pos_h, pos_w, soldier)
        if will_collide:
            pos_h, pos_w = soldier.pos_h, soldier.pos_w
        
        soldier.change_position(pos_h, pos_w, face=direction)
        
        if not will_collide:
            self._draw_soldier(soldier)
    
    def _engage_enemy(self):
        for enemy in self.state['enemies_alive']:
            self.fire_bullet(enemy)
    
    def fire_bullet(self, soldier):
        bullet = Bullet(shooter=soldier)
        self.state['bullets'].append(bullet)

    def on_press_action(self):
        self.fire_bullet(soldier=self.state['my_soldier'])
    
    def on_press_up(self):
        self._move_soldier(self.state['my_soldier'], UP)
    
    def on_press_down(self):
        self._move_soldier(self.state['my_soldier'], DOWN)
    
    def on_press_left(self):
        self._move_soldier(self.state['my_soldier'], LEFT)
    
    def on_press_right(self):
        self._move_soldier(self.state['my_soldier'], RIGHT)
    
    def on_press_help(self):
        pass

    @staticmethod
    def _is_shot(soldier, bullet):
        heart_h, heart_w = soldier.pos_h + 1, soldier.pos_w + 1
        return abs(heart_h - bullet.pos_h) < 2 and abs(heart_w - bullet.pos_w) < 2

    def _is_friendly_fire(self, bullet):
        for enemy in self.state['enemies_alive']:
            if enemy is not bullet.shooter:
                if self._is_shot(enemy, bullet):
                    return True
        return False
    
    def _enemy_strikes_me(self, bullet):
        return self._is_shot(self.state['my_soldier'], bullet)
    
    def _i_shot_someone(self, bullet):
        for enemy in self.state['enemies_alive']:
            if self._is_shot(enemy, bullet):
                return enemy
        return None

    def _collided_bullets(self, bullet):
        collided = []
        for other in self.state['bullets']:
            if other != bullet:
                if bullet.pos_h == other.pos_h and bullet.pos_w == other.pos_w:
                    collided.append(other)
        return collided

    def _process_bullets(self):
        to_remove = []
        
        for bullet in self.state['bullets']:
            if bullet.out_of_edge():
                to_remove.append(bullet)
                continue
            
            collided_bullets = self._collided_bullets(bullet)
            if len(collided_bullets) > 0:
                to_remove += collided_bullets
                to_remove.append(bullet)
                continue
            
            if bullet.shooter.is_me:
                if self._i_shot_someone(bullet):
                    pass
            else:
                if self._is_friendly_fire(bullet):
                    to_remove.append(bullet)
                    continue
                elif self._enemy_strikes_me(bullet):
                    pass
            
            self.game_gl.draw_atoms((bullet.pos_h, bullet.pos_w))

        time.sleep(0.2)
        for bullet in to_remove:
            try:
                self.state['bullets'].remove(bullet)
            except ValueError:
                pass
        
        for bullet in self.state['bullets']:
            self.game_gl.draw_atoms((bullet.pos_h, bullet.pos_w), value=False)
            bullet.move_forward()
