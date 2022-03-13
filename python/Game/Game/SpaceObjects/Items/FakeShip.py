import uuid
from python.Static.ParseJson import parse_xml
from python.Game._Component.Utils import DotMap


class FakeShip:
    level:int
    in_using:bool = True


    def __init__(self, Game, class_number):
        self.weapon_slots:list = []
        self.device_slots:list = []
        self.ship: dict = {}

        self.Game = Game
        self.class_number = class_number
        self.ship['guid'] = uuid.uuid4().bytes
        self.get_ship()

    def get_ship(self):
        for ship in parse_xml("ShipParameters"):
            if ship[Keys.class_number] == self.class_number:
                self.ship = DotMap(ship)