from . import MovableSpaceObject
from ..Static.ParseXml import parse_xml


class Ship(MovableSpaceObject):
    weapon_slots:list = []
    device_slots:list = []
    level:int
    in_using:bool = False
    ship: dict = {}


    def __init__(self, Game, data):
        super().__init__(Game, data)
        self.classNumber = data["ship_class"]
        self.maxDroids = 2
        self.get_ship()

    def get_ship(self):
        for ship in parse_xml("ShipParameters"):
            if ship['classNumber'] == self.classNumber:
                self.ship['weaponSlots'] = ship["weaponSlots"]
                self.ship['deviceSlots'] = ship["deviceSlots"]
                self.ship['armor'] = ship["armor"]
                self.ship['shields'] = ship["shields"]
                self.ship['maxEnergy'] = ship["maxEnergy"]
                self.ship['maxHealth'] = ship["maxHealth"]
                self.ship['cpu'] = ship["cpu"]
                self.ship['radar'] = ship["radar"]
                self.ship['maxSpeed'] = ship["maxSpeed"]
                self.ship['restrictions'] = ship["restrictions"]
                self.ship['features'] = ship["features"]
                self.ship['classNumber'] = ship["classNumber"]
                self.ship['guid'] = ship["guid"]
                self.ship['wear'] = ship["wear"]
                self.ship['level'] = ship["level"]
                self.ship['inUsing'] = ship["inUsing"]
                self.ship['satisfying'] = ship["satisfying"]
                self.ship['size'] = ship["size"]
                self.ship['cost'] = ship["cost"]
                self.ship["maxHealth"] = self.ship["maxHealth"]
                self.ship["maxEnergy"] = self.ship["maxEnergy"]
                self.ship["maxSpeed"] = self.ship["maxSpeed"]
                self.ship['cpuUsed'] = 0