import math
# from . import parse_galaxy_map
from . import ThreadBase, cfg_update
from ..BaseClass.SpaceObject import SpaceObject

class Planet(SpaceObject, ThreadBase):
    name: str  # my
    class_number: int  #be bytes
    radius: int = 1000
    laudable: bool = True
    is_sun: bool
    # clan_id: int # Зачем планете клан ид?
    x: int  # add
    y: int  # add
    x0: int = 0  # центр окружности по х
    y0: int = 0  # центр окружности по y
    speed: int = 12  #
    _i = 1  # Уголобразующий
    item_shop = {}
    ship_shop = {}

    def __init__(self, Game, data:dict):
        data['Types'] = 1
        super().__init__(Game, data)
        self.id = data['id']
        self.name = data['Name']
        self.race = data['race']
        self.class_number = data['classNumber']
        self.aliance = data["aliance"]
        self.location = data['location']
        self.is_sun = bool(6 > self.class_number)
        self.angel = float("inf") if 6 > self.class_number else None
        self.x = 300
        self.y = 300
        self.item_shop = self.get_item_shop()
        self.ship_shop = self.get_ship_shop()
        self.update()
        self.set_planet_on_location(data["location"])

    def set_planet_on_location(self, id_location):
        getattr(self.Game, f"Location_{id_location}").set_planet(self.__dict__)

    def get_ship_shop(self):
        # packages_entrance data BaseClass
        return 'sss'

    def get_item_shop(self):
        # packages_entrance data BaseClass
        return 'sss'

    def buy_item_shop(self):
        pass

    def sell_item_shop(self):
        pass

    def update(self):  # ready
        self.start_update('move', cfg_update['planet'])

    @ThreadBase.end_thread
    def move(self):
        self._i += self.speed
        if self._i > 360:
            self._i = 1
        self.angle = self._i * 3.14 / 180
        self.x = int(self.radius * math.cos(self.angle) + self.x0)
        self.y = int(self.radius * math.sin(self.angle) + self.y0)
