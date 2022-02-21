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
    data = get_item_data(classNumber, wear)
    match data['Types']:
        case 1:
            return Resource(Game, data, OwnerClass)
        case 2:
            return Ammo(Game, data, OwnerClass)
        case 3:
            return Engine(Game, data, OwnerClass)
        case 4:
            return Weapon(Game, data, OwnerClass)
        case 5:
            return Device(Game, data, OwnerClass)
        case 6:
            return Droid(Game, data, OwnerClass)

def get_item_data(classNumber, wear):
    return item_id(classNumber, wear)

def get_ship_data(classNumber):
    return ship_id(classNumber)
