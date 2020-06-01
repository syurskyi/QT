from src.game_logic.utils.brick_gl import BrickGl
import src.constants as constants


class Game:
    
    def __init__(self, name, serial, game_api):
        self.name = name
        self.serial = serial
        self.game_gl = BrickGl(draw_atoms=game_api['draw_game_atoms'])
        self.register_handler = game_api['register_key_handler']
        self.create_interval = game_api['create_interval']
        self.clear_game_screen = game_api['clear_game_screen']
        
        self._intervals = []
        
    def print_intro(self):
        self.game_gl.horiz_line(0, 0, 10)
        self.game_gl.horiz_line(19, 0, 10)
    
    def on_press_action(self):
        pass
    
    def on_press_up(self):
        pass
    
    def on_press_down(self):
        pass
    
    def on_press_left(self):
        pass
    
    def on_press_right(self):
        pass
    
    def on_press_help(self):
        pass
    
    def launch(self):
        self.register_handler(constants.EVENT_ACTION, self.on_press_action)
        self.register_handler(constants.EVENT_LEFT, self.on_press_left)
        self.register_handler(constants.EVENT_RIGHT, self.on_press_right)
        self.register_handler(constants.EVENT_UP, self.on_press_up)
        self.register_handler(constants.EVENT_DOWN, self.on_press_down)
        self.register_handler(constants.EVENT_HELP, self.on_press_help)
    
    def finish(self):
        for process in self._intervals:
            process.terminate()
        
        for process in self._intervals:
            process.join()
        
        self._intervals = []
    
    def set_interval(self, interval, callback):
        process = self.create_interval(interval, callback)
        self._intervals.append(process)
        process.start()
