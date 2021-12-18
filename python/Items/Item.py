import math
from . import SpaceObject

class Item(MovableSpaceObject):
    MIN_LEVEL: int = 1
    MAX_LEVEL: int = 5
    _sBitmapName: str
    guid: bytearray
    inUsing: bool
    _iClassfloat: int
    wear: int
    maxWear: int = 1
    _iLevel: int
    owner: SpaceObject
    satisfying: bool = True
    zeroCost: bool = False
    restrictions: list
    _oParameters: BaseParameters
    ownerid: int
    price: int
    ransom: int
    lastPlayerID: int
    ownerName: str
    lastPlayerName: str

    def __init__(self, param1: int, param2: BaseParameters):
        self.restrictions = []
        self._iClassfloat = param1
        self._oParameters = param2

        if param2 != None:
            self.restrictions = param2.restrictions
            self.maxWear = param2.maxWear
            self.wear = self.maxWear

