from ...BaseClass.StaticSpaceObject import StaticSpaceObject
import random
from ...Packages.PackagesManager import PackagesManager
from .Asteroid import Asteroid

class AsteroidsBelt(StaticSpaceObject):
    id: int
    max_asteroid_id = 0
    asteroids = []
    entry_count_asteroid = 60
    # cnt_asteroid: int

    def __init__(self, Game, data: dict, LocationClass):
        super().__init__(Game, data, LocationClass)
        self.id = data['id']
        self.type_ore = int(str(self.id)[1:])
        self.sector = 1
        self.players = []
        self.create_asteroid()

    # def get_type(self):
    #     self.

    def create_asteroid(self):
        for i in range(60):
            self.max_asteroid_id += 1
            self.asteroids.append(Asteroid(self.max_asteroid_id, self.Game, self))

    def SetPlayer(self, PlayerClass):
        self.players.append(PlayerClass)
        PlayerClass.SpaceObject = self

        PacMan = PackagesManager(PlayerClass.id, self.Game)
        PacMan.locationBattle()
        PacMan.asteroids()

    def remove_asteroid(self, AsteroidClass):
        for Aster in self.asteroids:
            if Aster == AsteroidClass:
                self.asteroids.remove(Aster)
                for player in self.players:
                    PacMan = PackagesManager(player.id, self.Game)
                    PacMan.asteroids()


    # def update(self):
    #     for id_asteroid in range(self.cnt_asteroid):
    #         setattr(self, f"asteroid_{id_asteroid}", Asteroid(id_asteroid))

