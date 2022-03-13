from python.Game._Component.Event.E_Entity.E_Pvp import Pvp
from python.Game._Component.Event.E_Entity.E_Ship.E_Droid import E_Droid
from python.Game._Component.Event.E_Entity.E_Ship import E_Move, E_Effect
from python.Game._Component.Body.B_Detail.B_Inventory.Inventory import Inventory
from python.Static.ParseJson import parse_xml
from python.Static.Type.Keys import Keys


class Ship(E_Move, E_Effect, E_Droid, Inventory, Pvp):
    level: int
    in_using: bool = False
    shields: int
    Location: object

    def __init__(self, Game, data):
        self.activeWeapons = []
        self.activeDevices = []
        self.ship: dict = {}
        self.__dict__.update(data)
        super().__init__(Game, data)
        self.get_ship()
        self.speed = self.ship[Keys.max_speed]
        self.maxDroids = 2
        Pvp.__init__(self)
        Inventory.__init__(self)


    def get_ship(self):
        for ship in parse_xml("ShipParameters"):
            if ship[Keys.class_number] == self.class_number:
                self.ship = ship
                self.ship[Keys.cpu_used] = 0

    def destroyed(self):
        self.Location.__get_drop(self.__get_drop())

    def __get_drop(self):  # TODO return experiences (maybe credits) and return items
        drop = []
        for Item in enumerate(self.inventory.copy()):
            if Item.drop:
                drop.append(Item - Item.count)
        return drop
