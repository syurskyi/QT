from src.game_logic.games.game import Game


class DxBallGame(Game):
    
    def __init__(self, serial, game_api):
        Game.__init__(
            self,
            name='Dx Ball',
            serial=serial,
            game_api=game_api
        )

    def print_intro(self):
        super().print_intro()
        ggl = self.game_gl
        ggl.alphabet('B')
        ggl.horiz_line(11, 3, 4)
        ggl.horiz_line(12, 2, 6)
        ggl.horiz_line(13, 3, 4)
        ggl.draw_atoms((15, 4))
        ggl.horiz_line(17, 3, 3)
