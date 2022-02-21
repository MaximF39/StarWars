import uuid
from python.Static.ParseJson import parse_xml
from python.Utils.DotMap import DotMap


class FakeShip:
    weapon_slots:list = []
    device_slots:list = []
    level:int
    in_using:bool = True
    ship: dict = {}


    def __init__(self, Game, classNumber):
        self.Game = Game
        self.classNumber = classNumber
        self.maxDroids = 2
        self.ship['guid'] = uuid.uuid4().bytes
        self.get_ship()

    def get_ship(self):
        for ship in parse_xml("ShipParameters"):
            if ship['classNumber'] == self.classNumber:
                self.ship = DotMap(ship)