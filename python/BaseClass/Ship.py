from . import MovableSpaceObject, parse_xml


class Ship(MovableSpaceObject):
    weapon_slots:list = []
    device_slots:list = []
    level:int
    in_using:bool = False
    ship: dict = {}


    def __init__(self, Game, data):
        super().__init__(Game, data)
        self.classNumber = data["ship_class"]
        self.ship['id'] =  data['id']
        self.ship['setPosition'] = [data['x'], data['y']]
        self.ship['team'] = -1
        self.get_ship()

    def get_ship(self):
        for i in parse_xml("ShipParameters"):
            if i['classNumber'] == self.classNumber:
                self.ship['weaponSlots'] = i["weaponSlots"]
                self.ship['deviceSlots'] = i["deviceSlots"]
                self.ship['armor'] = i["armor"]
                self.ship['shields'] = i["shields"]
                self.ship['maxEnergy'] = i["maxEnergy"]
                self.ship['maxHealth'] = i["maxHealth"]
                self.ship['cpu'] = i["cpu"]
                self.ship['radar'] = i["radar"]
                self.ship['maxSpeed'] = i["maxSpeed"]
                self.ship['restrictions'] = i["restrictions"]
                self.ship['features'] = i["features"]
                self.ship['classNumber'] = i["classNumber"]
                self.ship['guid'] = i["guid"]
                self.ship['wear'] = i["wear"]
                self.ship['level'] = i["level"]
                self.ship['inUsing'] = i["inUsing"]
                self.ship['satisfying'] = i["satisfying"]
                self.ship['size'] = i["size"]
                self.ship['cost'] = i["cost"]
                self.ship["health"] = self.ship["maxHealth"]
                self.ship["energy"] = self.ship["maxEnergy"]
                self.ship["speed"] = self.ship["maxSpeed"]
