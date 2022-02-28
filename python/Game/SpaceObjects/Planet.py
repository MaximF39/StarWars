import math
# from . import parse_galaxy_map
from python.Utils.ThreadBase import ThreadBase
from python.Base.SpaceObject.SpaceObject.SpaceBigObject import SpaceBigObject
from python.Config.cfg_main import RADIUS_BETWEEN_PLANET

class Planet(SpaceBigObject, ThreadBase):
    classNumber: int  #be bytes
    radius: int = RADIUS_BETWEEN_PLANET
    landable: bool
    is_sun: bool
    speed: int = 3  #
    _i = 1  # Уголобразующий

    def __init__(self, Game, data:dict, Location):
        SpaceBigObject.__init__(self, Game, data, Location)
        self.name = self.Name
        self.is_sun = bool(6 > self.classNumber)
        self.angle = float("inf") if 6 > self.classNumber else self._i * 3.14 / 180
        self.landable = False if self.is_sun else True
        if self.angle != float('inf'):
            self._i += self.speed
            if self._i > 360:
                self._i = 1
            self.x = int(self.radius * math.sin(self.angle))
            self.y = int(self.radius * math.cos(self.angle))
            self.update()

    # def fake_items(self, PlayerItems):
    #     ItemsForPlayer = []
    #     for Item_ in self.inventory:
    #         ItemsForPlayer.append(Item_.ItemForPlayer(PlayerItems))
    #     return ItemsForPlayer

    def send_info_location(self):
        self.Location.set_planet(self)

    def update(self):  # ready
        self.start_timer_update(self.move, 1) # cfg_update['SpaceObjectItems']

    def move(self):
        self._i += self.speed
        if self._i > 360:
            self._i = 1
        self.angle = self._i * 3.14 / 180
        self.x = int(self.radius * math.sin(self.angle))
        self.y = -1 * int(self.radius * math.cos(self.angle))

