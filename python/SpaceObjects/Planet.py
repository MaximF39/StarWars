import math
# from . import parse_galaxy_map
from . import ThreadBase, cfg_update
from ..BaseClass.SpaceObject import SpaceObject

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
        self.shop = []
        self.clanID = 0
        self.QCount = 3
        self.shop = data['shop']
        self.LocationClass = LocationClass

        if self.angle != float('inf'):
            self._i += self.speed
            if self._i > 360:
                self._i = 1
            self.x = int(self.radius * math.cos(self.angle))
            self.y = int(self.radius * math.sin(self.angle))
            self.update()

        self.send_info_location()

    def send_info_location(self):
        self.LocationClass.set_planet(self)

    def set_player(self, PlayerClass):
        self.players.append(PlayerClass)


    def buy_item_shop(self):
        pass

    def sell_item_shop(self):
        pass

    def update(self):  # ready
        self.start_update('move', 5) # cfg_update['planet']

    @ThreadBase.end_thread
    def move(self):
        self._i += self.speed
        if self._i > 360:
            self._i = 1
        self.angle = self._i * 3.14 / 180
        self.x = int(self.radius * math.cos(self.angle))
        self.y = int(self.radius * math.sin(self.angle))

