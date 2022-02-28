from python.Base.SpaceObject.Set.SetPlayer import SetPlayer
from python.Base.SpaceObject.SpaceObject.StaticSpaceObject import StaticSpaceObject
from .Asteroid import Asteroid
from python.Static.Type.Package.T_ServerRequest import T_ServerRequest

if False:
    pass

class AsteroidsBelt(StaticSpaceObject):
    id: int
    max_asteroid_id = 0
    entry_count_asteroid = 60
    cnt_asteroid: int

    def __init__(self, Game, data: dict, LocationClass):
        self.asteroids = []
        self.players: list["CFG_Player"] = []
        StaticSpaceObject.__init__(self, Game, data, LocationClass)
        self.type_ore = int(str(self.id)[1:])
        self.sector = 1
        self.__base_create_asteroid()

    def __base_create_asteroid(self):
        for i in range(60):
            self.max_asteroid_id += 1
            self.asteroids.append(Asteroid(self.max_asteroid_id, self.Game, self))

    def _set_player(self, PlayerClass):
        self.players.append(PlayerClass)
        PlayerClass.SpaceObject = self
        PlayerClass.Packages.SendPacMan(T_ServerRequest.ASTEROIDS, T_ServerRequest.LOCATION_BATTLE)

    def destroyed_asteroid(self, Asteroid):
        self.__remove_asteroid(Asteroid)
        for Player in self.players:
            Player.Packages.SendPacMan(T_ServerRequest.LOCATION_BATTLE, T_ServerRequest.ITEMS)

    def exit_borders(self, Asteroid):
        self.__remove_asteroid(Asteroid)

    def __remove_asteroid(self, Asteroid):
        self.asteroids.remove(Asteroid)
        SetPlayer.send_all_player_packages(self, T_ServerRequest.ASTEROIDS)

    def remove_asteroid(self, Asteroid):
        self.__remove_asteroid(Asteroid)