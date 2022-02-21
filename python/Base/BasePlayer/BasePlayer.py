import math
from abc import ABC

from python.Base.BasePlayer.Pvp import Pvp
from python.Base.BasePlayer.Ship import Ship
from python.Static.cfg.cfg_main import RADIUS
from python.Utils.MyTime import MyTime
from python.Base.BasePlayer.ShipEvent.EffectEvent import EffectEvent
from python.Base.Inventory.Inventory import Inventory


class BasePlayer(Ship, MyTime, Pvp, ABC):
    SpaceObject: "SpaceObject"
    locationId: int
    skills: dict

    def __init__(self, Game, dict_: dict):
        Ship.__init__(self, Game, dict_)
        MyTime.__init__(self)
        Pvp.__init__(self, self.ship['maxHealth'], self.ship['maxEnergy'], self.ship['shields'], self.skills)

        self.Location = getattr(self.Game, f'Location_{self.locationId}')
        self.ObjectToReach = None

        self.effects = []
        self.OldTick = self.tick()
        self.OldTarget = False
        self.sendInfoLocation()

    def sendInfoLocation(self):
        self.Location.set_player(self)

    def leaveLocation(self):
        self._set_x_y(self.SpaceObject.x, self.SpaceObject.y)
        self.SpaceObject.leave(self)
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

    def _kill(self):
        self.ObjectToReach = None
        self.ObjectToAttack = None

    def dead(self):
        Ship.destroyed(self)
