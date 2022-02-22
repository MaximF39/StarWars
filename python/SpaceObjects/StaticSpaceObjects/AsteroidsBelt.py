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
        self.__base_create_asteroid()

    def __base_create_asteroid(self):
        for i in range(60):
            self.max_asteroid_id += 1
            self.asteroids.append(Asteroid(self.max_asteroid_id, self.Game, self))

    def set_player(self, PlayerClass):
        self.players.append(PlayerClass)
        PlayerClass.SpaceObject = self
        PlayerClass.PacMan.locationBattle()
        PlayerClass.PacMan.asteroids()

    def destroyed_asteroid(self, Asteroid):
        self.__remove_asteroid(Asteroid)

        PacMan = PackagesManager(PlayerKill)
        PacMan.locationBattle()
        PacMan.items()


    def exit_borders(self, Asteroid):
        self.__remove_asteroid(Asteroid)

    def __remove_asteroid(self, Asteroid):
        self.asteroids.remove(Asteroid)
        self.__send_all_packages_name(("Packages.asteroids", ))

    def __send_all_packages_name(self, packages_name:tuple):
        for Player in self.players:
            for package in packages_name:
                getattr(Player, package)()



