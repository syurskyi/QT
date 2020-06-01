import sys
from multiprocessing import Queue, Process

from PyQt5.QtWidgets import QApplication

from AsteroidsGame import AsteroidsGame
from entities.PlayerInput import PlayerInput


class AsteroidsTournament(AsteroidsGame):
    def __init__(self, queue: Queue, player_inputs=[], screen_width=1000, screen_height=600, title="Asteroids"):
        self.queue = queue
        super().__init__(player_inputs, screen_width, screen_height, title)

    def on_game_end(self, storage):
        winner = storage.get_player_with_most_points()
        self.screen.display_winner(winner=winner, on_end=lambda: self._notify_winner(winner))

    def _notify_winner(self, winner):
        self.queue.put(winner.player_id)
        self.queue.close()


def start_tournament(player1_input, player2_input, player3_input, player4_input):
    player_by_id = dict()
    player_by_id[player1_input.player_id] = player1_input
    player_by_id[player2_input.player_id] = player2_input
    player_by_id[player3_input.player_id] = player3_input
    player_by_id[player4_input.player_id] = player4_input

    q = Queue()
    winner1_id = _start_game_process(q, player1_input, player2_input, "Tournament - Game 1")
    print("Game 1 winner: ", winner1_id)

    winner2_id = _start_game_process(q, player3_input, player4_input, "Tournament - Game 2")
    print("Game 2 winner: ", winner2_id)

    tournament_winner_id = _start_game_process(q, player_by_id[winner1_id], player_by_id[winner2_id],
                                               "Tournament - Finale")
    print(f"Tournament winner is: {tournament_winner_id}")
    exit()


def _start_game_process(q, player1_input, player2_input, title="Tournament") -> str:
    process = Process(target=_start_game, args=(q, player1_input.player_id, player1_input.color,
                                                player2_input.player_id, player2_input.color,
                                                title))
    process.start()
    winner_id = q.get()
    process.terminate()
    return winner_id


def _start_game(queue: Queue, player1_id, player1_color, player2_id, player2_color, title="Tournament"):
    app = QApplication(sys.argv)
    game = AsteroidsTournament(
        queue=queue,
        player_inputs=[
            PlayerInput(player_id=player1_id, color=player1_color),
            PlayerInput(player_id=player2_id, color=player2_color)
        ], title=title)
    game.start()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start_tournament(player1_input=PlayerInput("A", "red"),
                     player2_input=PlayerInput("B", "yellow"),
                     player3_input=PlayerInput("C", "green"),
                     player4_input=PlayerInput("D", "blue"))
