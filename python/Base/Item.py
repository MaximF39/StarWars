from . import SpaceObject


class Item(SpaceObject):
    guid: bytearray
    price: int
    inUsing: bool
    class_number: int
