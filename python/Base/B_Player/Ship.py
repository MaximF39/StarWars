from python.Base.Pvp.Pvp import Pvp
from python.Base.Event.E_Ship.E_Droid import E_Droid
from python.Base.Event.E_Ship.E_Effect import E_Effect
from python.Base.Event.E_Ship.E_Move import E_Move
from python.Base.Inventory.Inventory import Inventory
from python.Static.ParseJson import parse_xml


class Ship(E_Effect, E_Move, E_Droid, Inventory, Pvp):
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
        E_Move.__init__(self, Game, data)

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
