from ..Packages.PackagesManager import PackagesManager
from .Item import item
import math
# from . import parse_galaxy_map
from . import ThreadBase, cfg_update
from ..BaseClass.SpaceObject import SpaceObject
from ..BaseClass.FakeShip import FakeShip

class Planet(SpaceObject, ThreadBase):
    name: str  # my
    class_number: int  #be bytes
    radius: int
    landable: bool
    is_sun: bool
    # clan_id: int # Зачем планете клан ид?
    speed: int = 3  #
    _i = 1  # Уголобразующий

    def __init__(self, Game, data:dict, LocationClass):
        data['Types'] = 1
        super().__init__(Game, data)
        self.id = data['id']
        self.name = data['Name']
        self.race = data['race']
        self.classNumber = data['classNumber']
        self.aliance = data["aliance"]
        self.radius = data['radius']
        self.is_sun = bool(6 > self.classNumber)
        self.angle = float("inf") if 6 > self.classNumber else self._i * 3.14 / 180
        self.landable = False if self.is_sun else True
        self.players = []
        self.clanId = 0 # Только чей клан захвачен, могут садиться на планету
        self.QCount = 0 # Количество квестов
        self.ships = []
        for ship in data['ships']:
            self.ships.append(FakeShip(self.Game, ship))
        self.inventory = []
        for item_ in data['inventory']:
            self.inventory.append(item(self.Game, item_['classNumber'], self, item_['count'] if 'count' in item_ else None))
        self.shops = data['shops']
        self.LocationClass = LocationClass

        if self.angle != float('inf'):
            self._i += self.speed
            if self._i > 360:
                self._i = 1
            self.x = int(self.radius * math.sin(self.angle))
            self.y = int(self.radius * math.cos(self.angle))
            self.update()

        self.send_info_location()


    def SetPlayer(self, PlayerClass):
        self.players.append(PlayerClass)
        PlayerClass.SpaceObject = self
        PacMan = PackagesManager(PlayerClass.id, self.Game)
        PacMan.locationPlanet()

    def ShowForPlayer(self, PlayerClass):
        ItemsForPlayer = []
        for Item_ in self.inventory:
            ItemsForPlayer.append(Item_.ItemForPlayer(PlayerClass))
        return ItemsForPlayer

    def ShowShopItems(self, PlayerClass):
        PacMan = PackagesManager(PlayerClass.id, self.Game)
        ItemsForPlayer = []
        for Item_ in self.inventory:
            ItemsForPlayer.append(Item_.ItemForPlayer(PlayerClass))
        PacMan.tradingItems()

    def send_info_location(self):
        self.LocationClass.set_planet(self)

    def update(self):  # ready
        self.start_timer_update(self.move, 1) # cfg_update['SpaceObject']

    def move(self):
        self._i += self.speed
        if self._i > 360:
            self._i = 1
        self.angle = self._i * 3.14 / 180
        self.x = int(self.radius * math.sin(self.angle))
        self.y = -1 * int(self.radius * math.cos(self.angle))

