from python.Base.BasePlayer.Pvp import Pvp
from python.Base.BasePlayer.ShipEvent.DroidEvent import DroidEvent
from python.Base.BasePlayer.ShipEvent.EffectEvent import EffectEvent
from python.Base.BasePlayer.ShipEvent.MoveEvent import MoveEvent
from python.Base.Inventory.Inventory import Inventory
from python.Static.ParseJson import parse_xml


class Ship(EffectEvent, MoveEvent, DroidEvent, Inventory):
    level: int
    in_using: bool = False
    shields: int
    Location: "Location"

    def __init__(self, Game, data):
        self.weapon_slots: list = []
        self.device_slots: list = []
        self.ship: dict = {}
        self.__dict__.update(data)
        self.get_ship()
        self.speed = self.ship['maxSpeed']
        self.maxDroids = 2
        MoveEvent.__init__(self, Game, data)

    def get_ship(self):
        for ship in parse_xml("ShipParameters"):
            if ship['classNumber'] == self.classNumber:
                self.ship = ship

    def destroyed(self):
        self.Location.__get_drop(self.__get_drop())

    def __get_drop(self):  # TODO return experiences (maybe credits) and return items
        drop = []
        for Item in enumerate(self.inventory.copy()):
            if Item.drop:
                drop.append(Item - Item.count)
        return drop
