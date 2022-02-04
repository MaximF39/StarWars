import math

from python.Base.BasePlayer.Ship import Ship
from python.Static.cfg.cfg_main import RADIUS
from python.Utils.MyTime import MyTime
from python.Base.Event.MoveEvent import Move
from python.Base.Player.Packages import Packages
from python.Base.BasePlayer.Pvp import Pvp
from python.Base.Event.EffectEvent import EffectEvent
from python.Base.Inventory.Inventory import Inventory

class BasePlayer(Ship, Pvp, EffectEvent, Inventory, MyTime):
    SpaceObject: "SpaceObject"
    locationId: int

    def __init__(self, Game, dict_: dict):
        Ship.__init__(self, Game, dict_)
        MyTime.__init__(self)
        Pvp.__init__(self)

        self.Location = getattr(self.Game, f'Location_{self.locationId}')
        self.ObjectToReach = None

        self.object_to_reach_id: int = self.Location

        self.effects = []
        self.OldTick = self.tick()
        self.OldTarget = False
        self.sendInfoLocation()

    def sendInfoLocation(self):
        self.Location.sendInfo(self, (self.x, self.y))

    def leaveLocation(self):
        self.SpaceObject.leaveLocation(self)
        self.x = self.SpaceObject.x
        self.y = self.SpaceObject.y
        self.not_target()
        self.SpaceObject = None
        self.ObjectToReach = None

    def hyper_jump(self, id_location):
        radius_ = RADIUS * len(self.Location.planets)
        NextLocation = getattr(self.Game, f'Location_{id_location}')
        self.ObjectToReach = NextLocation
        tan = math.atan2(NextLocation.y - self.Location.y, NextLocation.x - self.Location.x)
        x = radius_ * math.cos(tan)
        y = radius_ * math.sin(tan)
        self.move(targetX=x, targetY=y, Location=True)

    def get_drop(self):  # TODO return experiences (maybe credits) and return items
        drop = {}
        for count, dict_ in enumerate(self.inventory.copy()):
            if dict_['drop']:
                name = dict_['name']
                value = dict_['value']
                drop[name] = 0.8 * value
                self.inventory[count][name] = 0.2 * value
        return drop
