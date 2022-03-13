import math

from python.Game import Ship
from python.Game import Inventory
from python.Game import EntitySetter

from python.Config.cfg_main import RADIUS_BETWEEN_PLANET


class Entity(Ship, EntitySetter, Inventory):
    SpaceObject: object
    locationId: int
    skills: dict
    NextLocation:object = None

    def __init__(self, Game, dict_: dict):
        self.__dict__.update(dict_)
        super().__init__(Game, dict_)
        self.Location = getattr(self.Game, f'Location_{self.locationId}')
        self.Location.entry_entity(self)
        self.ObjectToReach = None
        if not hasattr(self, "I_SpaceObject"):
            self.SpaceObject = self.Location

        self.effects = []
        self.OldTick = self.tick()
        self.OldTarget = False

    def move_hyper_jump(self, id_location):
        radius_ = RADIUS_BETWEEN_PLANET * len(self.Location.planets)
        NextLocation = getattr(self.Game, f'Location_{id_location}')
        self.ObjectToReach = NextLocation
        tan = math.atan2(self.ObjectToReach.map_y - self.SpaceObject.map_y, self.ObjectToReach.map_x - self.SpaceObject.map_x)
        x = radius_ * math.cos(tan)
        y = radius_ * math.sin(tan)
        self.move(targetX=x, targetY=y)

    def _kill(self):
        self.ObjectToReach = None
        self.ObjectToAttack = None

    def dead(self):
        Ship.destroyed(self)

    def hyperJump(self, Location):
        self.__replace_location(Location)

    def __replace_location(self, Location):
        self.__remove_location()
        self.__set_location(Location)

    def __remove_location(self):
        self.Location = None

    def __set_location(self, Location):
        self.Location = Location