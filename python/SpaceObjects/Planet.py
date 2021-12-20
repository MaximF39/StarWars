import math
# from . import parse_galaxy_map
from . import ThreadBase, cfg_update
from ..Base.SpaceObject import SpaceObject

class Planet(SpaceObject, ThreadBase):
    name: str  # my
    class_number: int  #be bytes
    radius: int = 100
    laudable: bool = True
    is_sun: bool
    # clan_id: int # Зачем планете клан ид?
    x: int  # add
    y: int  # add
    x0: int = 300  # центр окружности по х
    y0: int = 300  # центр окружности по y
    speed: int = 12  #
    _i = 1  # Уголобразующий
    item_shop = {}
    ship_shop = {}

    def __init__(self, data:dict):
        super().__init__(data)
        self.id = data['id']
        self.name = data['Name']
        self.race = data['race']
        self.class_number = data['classNumber']
        self.aliance = data["aliance"]
        self.is_sun = bool(6 > self.class_number)
        self.x = 0
        self.y = 0
        self.item_shop = self.get_item_shop()
        self.ship_shop = self.get_ship_shop()
        self.update()

    def get_ship_shop(self):
        # get data Base
        return 'sss'

    def get_item_shop(self):
        # get data Base
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
        angle = self._i * 3.14 / 180
        self.x = int(100 * math.cos(angle) + self.x0) + self.radius
        self.y = int(100 * math.sin(angle) + self.y0) + self.radius
