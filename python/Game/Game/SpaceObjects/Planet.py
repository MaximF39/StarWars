import math
# from . import parse_galaxy_map
from python.Game._Component.Event.E_SpaceObject.Set.SpaceObjectSetter.PlanetSetter import PlanetSetter
from python.Game._Component.Utils.ThreadBase import ThreadBase
from python.Game._Component.Body.B_SpaceObject.SpaceObject import SpaceBigObject
from python.Config.cfg_main import RADIUS_BETWEEN_PLANET

class Planet(SpaceBigObject, ThreadBase, PlanetSetter):
    class_number: int  #be bytes
    radius: int = RADIUS_BETWEEN_PLANET
    landable: bool
    is_sun: bool
    speed: int = 3  #
    _i = 1  # Уголобразующий
    RADIUS_BETWEEN_PLANET:int

    def __init__(self, Game, data: dict, Location):
        super().__init__(Game, data, Location)
        PlanetSetter.__init__(self)
        self.name = self.name
        self.is_sun = bool(6 > self.class_number)
        self.x = self.RADIUS_BETWEEN_PLANET
        self.y = self.RADIUS_BETWEEN_PLANET
        self.angle = float("inf") if 6 > self.class_number else self._i * 3.14 / 180
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
        pass
        # self.start_timer_update(self.move, 1) # cfg_update['SpaceObjectItems']

    def move(self):
        self._i += self.speed
        if self._i > 360:
            self._i = 1
        self.angle = self._i * 3.14 / 180
        self.x = int(self.radius * math.sin(self.angle))
        self.y = -1 * int(self.radius * math.cos(self.angle))

