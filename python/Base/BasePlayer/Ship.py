from python.Base.Event.MoveEvent import Move
from python.Base.SpaceObject.MovableSpaceObject import MovableSpaceObject
from python.Static.ParseJson import parse_xml


class Ship(Move):
    weapon_slots:list = []
    device_slots:list = []
    level:int
    in_using:bool = False
    ship: dict = {}
    shields: int

    def __init__(self, Game, data):
        Move.__init__(self, Game, data)
        self.maxDroids = 2
        self.get_ship()
        self.speed = self.ship['maxSpeed']

    def get_ship(self):
        for ship in parse_xml("ShipParameters"):
            if ship['classNumber'] == self.classNumber:
                self.ship = ship
                # self.ship['weaponSlots'] = ship["weaponSlots"]
                # self.ship['deviceSlots'] = ship["deviceSlots"]
                # self.ship['armor'] = ship["armor"]
                # self.ship['shields'] = ship["shields"]
                # self.ship['maxEnergy'] = ship["maxEnergy"]
                # self.ship['maxHealth'] = ship["maxHealth"]
                # self.ship['cpu'] = ship["cpu"]
                # self.ship['radar'] = ship["radar"]
                # self.ship['maxSpeed'] = ship["maxSpeed"]
                # self.ship['restrictions'] = ship["restrictions"]
                # self.ship['features'] = ship["features"]
                # self.ship['classNumber'] = ship["classNumber"]
                # self.ship['guid'] = ship["guid"]
                # self.ship['wear'] = ship["wear"]
                # self.ship['level'] = ship["level"]
                # self.ship['inUsing'] = ship["inUsing"]
                # self.ship['satisfying'] = ship["satisfying"]
                # self.ship['size'] = ship["size"]
                # self.ship['cost'] = ship["cost"]
                # self.ship["maxHealth"] = self.ship["maxHealth"]
                # self.ship["maxEnergy"] = self.ship["maxEnergy"]
                # self.ship["maxSpeed"] = self.ship["maxSpeed"]