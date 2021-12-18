from . import MovableSpaceObject, parse_ship


class Ship(MovableSpaceObject):
    weapon_slots = None
    device_slots = None
    armor = None
    shields = None
    max_energy = None
    max_health = None
    cpu = None
    radar = None
    max_speed = None
    restrictions = None
    features = None
    class_number = None
    guid = None
    wear = None
    level = None
    in_using = None
    satisfying = None
    cost = None

    def __init__(self, class_number):
        self.class_number = class_number
        self.get_ship()

    def get_ship(self):
        for i in parse_ship():
            if i['classNumber'] == self.class_number:
                self.weapon_slots = i['weaponSlots']
                self.device_slots = i['deviceSlots']
                self.armor = i['armor']
                self.shields = i['shields']
                self.max_energy = i['maxEnergy']
                self.max_health = i['maxHealth']
                self.cpu = i['cpu']
                self.radar = i['radar']
                self.max_speed = i['maxSpeed']
                self.restrictions = i['restrictions']
                self.features = i['features']
                self.class_number = i['classNumber']
                self.guid = i['guid']
                self.wear = i['wear']
                self.level = i['level']
                self.in_using = i['inUsing']
                self.satisfying = i['satisfying']
                self.size = i['size']
                self.cost = i['cost']
                self.types = i['Types']
