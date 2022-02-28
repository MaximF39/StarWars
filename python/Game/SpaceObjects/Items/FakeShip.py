import uuid
from python.Static.ParseJson import parse_xml
from python.Utils.DotMap import DotMap


class FakeShip:
    level:int
    in_using:bool = True


    def __init__(self, Game, classNumber):
        self.weapon_slots:list = []
        self.device_slots:list = []
        self.ship: dict = {}

        self.Game = Game
        self.classNumber = classNumber
        self.ship['guid'] = uuid.uuid4().bytes
        self.get_ship()

    def get_ship(self):
        for ship in parse_xml("ShipParameters"):
            if ship['classNumber'] == self.classNumber:
                self.ship = DotMap(ship)