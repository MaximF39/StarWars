from python.Game._Component.Event.E_SpaceObject.Set import AsteroidBeltSetter
from python.Game._Component.Body.B_SpaceObject.SpaceObject.StaticSpaceObject import StaticSpaceObject
from .Asteroid import Asteroid
from python.Static.Type.Package.T_ServerRequest import T_ServerRequest

class AsteroidsBelt(StaticSpaceObject, AsteroidBeltSetter):
    id: int
    max_asteroid_id = 0
    entry_count_asteroid = 60
    cnt_asteroid: int

    def __init__(self, Game, data: dict, Location):
        super().__init__(Game, data, Location)
        AsteroidBeltSetter.__init__(self)
        self.asteroids = []
        self.type_ore = int(str(self.id)[1:])
        self.__base_create_asteroid()

    def __base_create_asteroid(self):
         self.create_new_asteroid(50)

    def create_new_asteroid(self, count=1):
        for i in range(count):
            self.max_asteroid_id += 1
            self.asteroids.append(Asteroid(self.max_asteroid_id, self.Game, self))
            self._send_package_players(T_ServerRequest.ASTEROIDS)

    def destroyed_asteroid(self, Asteroid):
        self.__remove_asteroid(Asteroid)
        for Player in self.players:
            Player.Packages.SendPacMan(T_ServerRequest.ITEMS)

    def exit_borders(self, Asteroid):
        self.__remove_asteroid(Asteroid)

    def __remove_asteroid(self, Asteroid):
        self.asteroids.remove(Asteroid)
        self.create_new_asteroid()
        self._send_package_players(T_ServerRequest.ASTEROIDS)
