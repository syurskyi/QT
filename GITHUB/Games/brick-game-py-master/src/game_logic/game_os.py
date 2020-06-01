import time
from threading import Thread
import src.constants as constants
from src.game_logic.games.dx_ball_game.dx_ball_game import DxBallGame
from src.game_logic.games.battle_game.main import BattleGame
from src.game_logic.games.racing_game.racing_game import RacingGame
from PyQt5.QtCore import Qt
from .utils.interval_thread import Interval


class GameOS(Thread):
    
    def __init__(self, screen_controller, buttons):
        Thread.__init__(self)
        
        self.screen_controller = screen_controller
        self.buttons = buttons
        self.state = self._create_os_state()
        
        self.draw_game_atoms = self.screen_controller['draw_game_atoms']
        self.draw_option_atoms = self.screen_controller['draw_option_atoms']

        self._set_button_handlers()
        self.screen_controller['set_key_event_handler'](self._key_event_handler)
        self.toggle_power()
    
    @staticmethod
    def _create_os_state():
        return {
            'is_paused': False,
            'game_list': [],
            'current_game_idx': 0,
            'is_game_running': False,
            'events': [],
            'handlers': {},
            'is_terminated': False,
            'is_power_on': False,
        }

    def _set_button_handlers(self):
        def set_button_onclick(button_name, event_name):
            self.buttons[button_name].clicked.connect(self._add_event(event_name))
    
        self.buttons['power'].clicked.connect(self.toggle_power)
        set_button_onclick('pause', constants.EVENT_PAUSE_TOGGLE)
        set_button_onclick('up', constants.EVENT_UP)
        set_button_onclick('down', constants.EVENT_DOWN)
        set_button_onclick('left', constants.EVENT_LEFT)
        set_button_onclick('right', constants.EVENT_RIGHT)
        set_button_onclick('action', constants.EVENT_ACTION)
        set_button_onclick('escape', constants.EVENT_ESCAPE)
        set_button_onclick('help', constants.EVENT_HELP)

    def _key_event_handler(self, event):
        if not self.state['is_power_on'] or self.state['is_paused']:
            return
    
        key = event.key()
        target_event = None
        
        if key == Qt.Key_I:
            target_event = constants.EVENT_UP
        elif key == Qt.Key_K:
            target_event = constants.EVENT_DOWN
        elif key == Qt.Key_J:
            target_event = constants.EVENT_LEFT
        elif key == Qt.Key_L:
            target_event = constants.EVENT_RIGHT
        elif key == Qt.Key_A:
            target_event = constants.EVENT_ACTION
        elif key == Qt.Key_Escape:
            target_event = constants.EVENT_ESCAPE
    
        self.state['events'].append(target_event)

    def toggle_power(self):
        self.state['is_power_on'] = not self.state['is_power_on']
        
        if self.state['is_power_on']:
            self._boot()
        else:
            self._shut_down()

    def _boot(self):
        self._set_os_event_handlers()
        self.state['game_list'] = self._init_game_list()
        self.screen_controller['show_labels']()
        self.screen_controller['show_music_icon']()
        self.state['events'].append(constants.EVENT_POWER_ON)
        self._clear_game_screen()
        self._clear_option_screen()

    def _shut_down(self):
        self.state['events'] = []
        self.state['handlers'] = {}
        self.screen_controller['hide_labels']()
        self.screen_controller['hide_music_icon']()
        self.screen_controller['hide_pause_icon']()
        self._clear_game_screen()
        self._clear_option_screen()

    def _register_handler(self, event, handler):
        self.state['handlers'][event] = handler

    def _set_os_event_handlers(self):
        register = self._register_handler
        
        register(constants.EVENT_RIGHT, self._next_game)
        register(constants.EVENT_LEFT, self._previous_game)
        register(constants.EVENT_POWER_ON, self._welcome_msg)
        register(constants.EVENT_PAUSE_TOGGLE, self._toggle_pause)
        register(constants.EVENT_ACTION, self._start_game)
        register(constants.EVENT_ESCAPE, self._stop_game)

    def _clear_game_screen(self, h0=0, w0=0, h=20, w=10):
        atoms = [(x, y) for x in range(h0, h0 + h) for y in range(w0, w0 + w)]
        self.draw_game_atoms(*atoms, value=False)

    def _clear_option_screen(self):
        atoms = [(x, y) for x in range(4) for y in range(4)]
        self.draw_option_atoms(*atoms, value=False)

    def run(self):
        while not self.state['is_terminated']:
            time.sleep(0.01)
            if len(self.state['events']) == 0:
                continue
            
            event = self.state['events'].pop()
            
            if self.state['is_paused'] and event != constants.EVENT_PAUSE_TOGGLE:
                continue
            
            if event not in self.state['handlers']:
                continue

            thread = Thread(target=self.state['handlers'][event])
            thread.setDaemon(True)
            thread.start()

    def _add_event(self, event_name):
        def add():
            if not self.state['is_power_on']:
                return
            self.state['events'].append(event_name)
        return add

    def _start_game(self):
        self._clear_game_screen()
        self._clear_option_screen()
        
        current_game_idx = self.state['current_game_idx']
        game = self.state['game_list'][current_game_idx]
        self.state['is_game_running'] = True
        game.launch()
    
    def _stop_game(self):
        if not self.state['is_game_running']:
            return
        
        self.state['is_game_running'] = False
        
        current_game_idx = self.state['current_game_idx']
        game = self.state['game_list'][current_game_idx]
        game.finish()
        
        self._clear_game_screen()
        self._clear_option_screen()
        self._set_os_event_handlers()
        game.print_intro()

    def _init_game_list(self):
        return [
            BattleGame(serial='A', game_api=self.get_game_api()),
            DxBallGame(serial='B', game_api=self.get_game_api()),
            RacingGame(serial='C', game_api=self.get_game_api()),
        ]

    def _toggle_pause(self):
        self.state['is_paused'] = not self.state['is_paused']
        
        if self.state['is_paused']:
            self.screen_controller['show_pause_icon']()
        else:
            self.screen_controller['hide_pause_icon']()

    def _next_game(self):
        self._clear_game_screen()
        
        game_list = self.state['game_list']
        self.state['current_game_idx'] += 1
        self.state['current_game_idx'] %= len(game_list)
        idx = self.state['current_game_idx']
        
        game_list[idx].print_intro()
    
    def _previous_game(self):
        self._clear_game_screen()
        
        game_list = self.state['game_list']
        idx = self.state['current_game_idx']
        self.state['current_game_idx'] = idx - 1 if idx > 0 else len(game_list) - 1
        idx = self.state['current_game_idx']
        
        game_list[idx].print_intro()
    
    def _welcome_msg(self):
        game_atoms = [(x, y) for x in range(20) for y in range(10)]
        option_atoms = [(x, y) for x in range(4) for y in range(4)]
        self.draw_game_atoms(*game_atoms)
        self.draw_option_atoms(*option_atoms)
        
        time.sleep(2)
        self._clear_game_screen()
        
        cur_game_idx = self.state['current_game_idx']
        self.state['game_list'][cur_game_idx].print_intro()
    
    def kill(self):
        self.state['is_terminated'] = True

    def get_game_api(self):
        return {
            'draw_game_atoms': self.draw_game_atoms,
            'register_key_handler': self._register_handler,
            'create_interval': self.create_interval,
            'clear_game_screen': self._clear_game_screen
        }

    @staticmethod
    def create_interval(interval, callback):
        return Interval(interval, callback)
