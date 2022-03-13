from .Items.Ammo import Ammo
from .Items.Resource import Resource
from .Items.Weapon import Weapon
from .Items.Device import Device
from .Items.Engine import Engine
from .Items.Droid import Droid
from .Items.FakeShip import FakeShip
from python.Static.ParseJson import item_id
from python.Static.ParseJson import ship_id
from python.Static.Type.Keys import Keys


def item(class_number, wear, Game=None, OwnerClass=None):
    data = get_item_data(class_number, wear)
    match data[Keys.type]:
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

def get_item_data(class_number, wear):
    return item_id(class_number, wear)

def get_ship_data(class_number):
    return ship_id(class_number)
