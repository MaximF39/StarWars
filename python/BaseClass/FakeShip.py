import uuid

from ..Static.ParseJson import parse_xml

class FakeShip:
    weapon_slots:list = []
    device_slots:list = []
    level:int
    in_using:bool = True
    ship: dict = {}


    def __init__(self, Game, shipClass):
        self.Game = Game
        self.classNumber = shipClass
        self.maxDroids = 2
        self.ship['guid'] = uuid.uuid4().bytes
        self.get_ship()

    def get_ship(self):
        for i in parse_xml("ShipParameters"):
            if i['classNumber'] == self.classNumber:
                self.ship['classNumber'] = i['classNumber']
                self.ship['cost'] = i["cost"]
                self.ship['size'] = i["size"]
                self.ship['weaponSlots'] = i["weaponSlots"]
                self.ship['deviceSlots'] = i["deviceSlots"]
                self.ship['armor'] = i["armor"]
                self.ship['shields'] = i["shields"]
                self.ship['maxEnergy'] = i["maxEnergy"]
                self.ship['maxHealth'] = i["maxHealth"]
                self.ship['cpu'] = i["cpu"]
                self.ship['radar'] = i["radar"]
                self.ship['maxSpeed'] = i["maxSpeed"]
                self.ship['restrictions'] = i["restrictions"]['data']
                self.ship['features'] = i["features"]['data']

                self.ship['wear'] = i["wear"]
                self.ship['level'] = i["level"]
                self.ship['inUsing'] = i["inUsing"]
                self.ship['satisfying'] = i["satisfying"]

                self.ship["health"] = self.ship["maxHealth"]
                self.ship["energy"] = self.ship["maxEnergy"]
                self.ship["speed"] = self.ship["maxSpeed"]
