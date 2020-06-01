from entities import Asteroid, Bullet, Player, Spaceship, Heart


class Storage:
    def __init__(self, asteroids=(), players=(), spacecrafts=(), bullets=(), hearts=()):
        self.asteroids = list(asteroids)
        self.players = list(players)
        self.spacecrafts = list(spacecrafts)
        self.bullets = list(bullets)
        self.hearts = list(hearts) #srca koje igrac moze da pokupi

    '''Getters for all objects on screen'''

    def get_all_asteroids(self):
        return self.asteroids

    def get_all_spacecrafts(self):
        return self.spacecrafts

    def get_all_bullets(self):
        return self.bullets

    def get_all_hearts(self):
        return self.hearts

    '''Getters for single objects on screen'''

    def get_player_by_id(self, player_id) -> Player:
        for player in self.players:
            if player.player_id == player_id:
                return player
        raise Exception(f"Player with id {player_id} not found!")

    def get_first_player_id(self) -> Player:
        for player in self.players:
            return player.player_id

    def get_spaceship_by_player_id(self, player_id) -> Spaceship:
        for spaceship in self.spacecrafts:
            if spaceship.player_id == player_id:
                return spaceship
        raise Exception(f"Spaceship with player id {player_id} not found!")

    def get_spaceship_by_player(self, player) -> Spaceship:
        player_id = player.player_id
        for spaceship in self.spacecrafts:
            if spaceship.player_id == player_id:
                return spaceship
        raise Exception(f"Spaceship with player id {player_id} not found!")

    def get_player_by_spaceship(self, spaceship: Spaceship) -> Player:
        for player in self.players:
            if player.spaceship_id == spaceship.spaceship_id:
                return player
        raise Exception(f"Player with spaceship{spaceship.spaceship_id} not found!")

    def get_alive_players(self) -> list:
        return list(filter(lambda player: not player.is_dead(), self.players))

    def get_player_with_most_points(self) -> Player:
        max_num_points = 0
        winner_player = None
        for player in self.players:
            if player.num_points >= max_num_points:
                max_num_points = player.num_points
                winner_player = player
        return winner_player

    '''Object generators'''

    def add_bullet(self, bullet: Bullet):
        self.bullets.append(bullet)

    def add_asteroid(self, asteroid: Asteroid):
        self.asteroids.append(asteroid)

    def add_spaceship(self, spaceship: Spaceship):
        self.spacecrafts.append(spaceship)

    def add_heart(self, heart: Heart):
        self.hearts.append(heart)
