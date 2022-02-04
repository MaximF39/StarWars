from .Items.Ammo import Ammo
from .Items.Resource import Resource
from .Items.Weapon import Weapon
from .Items.Device import Device
from .Items.Engine import Engine
from .Items.Droid import Droid
from .Items.FakeShip import FakeShip
from python.Static.ParseJson import item_id
from python.Static.ParseJson import ship_id


def item(classNumber, wear, Game=None, OwnerClass=None):
    match get_type(classNumber):
        case 1:
            return Resource(Game, classNumber, OwnerClass, wear)
        case 2:
            return Ammo(Game, classNumber, OwnerClass, wear)
        case 3:
            return Engine(Game, classNumber, OwnerClass, wear)
        case 4:
            return Weapon(Game, classNumber, OwnerClass, wear)
        case 5:
            return Device(Game, classNumber, OwnerClass, wear)
        case 6:
            return Droid(Game, classNumber, OwnerClass, wear)


def ship(Game, classNumber, OwnerClass, data):
    return FakeShip(Game, classNumber, OwnerClass, data)

def get_type(classNumber):
    return item_id(classNumber)['Types']


