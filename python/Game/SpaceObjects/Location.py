import math

from python.Utils.ThreadBase import ThreadBase
from python.Base.SpaceObject.Set.SetLocation import SetLocation
from python.Static.Type.Package.T_ServerRequest import T_ServerRequest
from python.Config.cfg_main import RADIUS_BETWEEN_PLANET
from python.Base.Inventory.Inventory import Inventory
from python.Base.SpaceObject.Create.C_SpaceObject import C_SpaceObject

class Location(ThreadBase, SetLocation, Inventory, C_SpaceObject):
    id: int

    def __init__(self, StarWars, data: dict):
        self.__dict__.update(data)
        SetLocation.__init__(self)
        Inventory.__init__(self)
        self.Game = StarWars

        C_SpaceObject.create_space_object(self)

    def hyper_jump_player(self, Player):
        radius_ = RADIUS_BETWEEN_PLANET * len(self.planets)
        OldLocation = Player.Location

        tan = math.atan2(OldLocation.y - self.y, OldLocation.x - self.x)

        Player.x = radius_ * math.cos(tan)
        Player.y = radius_ * math.sin(tan)
        Player.not_target()

        Player.Location._remove_player(Player)
        SetLocation.set_entity(self, Player)
        Player.Location = self

    def get_drop(self, drop):
        self.inventory.extend(drop)

    def kill(self, Entity):
        self.__remove_entity(Entity)
        SetLocation.send_all_player_packages(T_ServerRequest.LOCATION_SYSTEM)
