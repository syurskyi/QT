from src.game_logic.games.game import Game


class RacingGame(Game):
    
    def __init__(self, serial, game_api, lane_count=2):
        Game.__init__(
            self,
            name=f'Racing {lane_count}xlanes',
            serial=serial,
            game_api=game_api
        )
        self._lane_count = lane_count
    
    def print_intro(self):
        super().print_intro()
        ggl = self.game_gl
        ggl.alphabet('C')
        self._draw_car(10, 1)
        self._draw_car(14, 5)
    
    def _draw_car(self, h0, w0, is_me=False):
        ggl = self.game_gl
        ggl.vert_line(h0, w0 + 1, 3)
        ggl.horiz_line(h0 + 1, w0, 3)
        ggl.draw_atoms((h0 + 3, w0), (h0 + 3, w0 + 2))
