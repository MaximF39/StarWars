from python.Base.SpaceObject.StaticSpaceObject import StaticSpaceObject
from .Asteroid import Asteroid
if False:
    from python.Player.Player import Player

class AsteroidsBelt(StaticSpaceObject):
    id: int
    max_asteroid_id = 0
    entry_count_asteroid = 60
    cnt_asteroid: int

    def __init__(self, Game, data: dict, LocationClass):
        self.asteroids = []
        self.players: list["Player"] = []
        StaticSpaceObject.__init__(self, Game, data, LocationClass)
        self.type_ore = int(str(self.id)[1:])
        self.sector = 1
        self.create_asteroid()

    def create_asteroid(self):
        for i in range(60):
            self.max_asteroid_id += 1
            self.asteroids.append(Asteroid(self.max_asteroid_id, self.Game, self))

    def set_player(self, PlayerClass):
        self.players.append(PlayerClass)
        PlayerClass.SpaceObject = self
        PlayerClass.PacMan.locationBattle()
        PlayerClass.PacMan.asteroids()

    def remove_asteroid(self, AsteroidClass):
        for Aster in self.asteroids:
            if Aster == AsteroidClass:
                self.asteroids.remove(Aster)
                for Player in self.players:
                    Player.PacMan.asteroids()


