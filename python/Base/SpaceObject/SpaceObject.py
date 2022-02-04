import uuid

from python.Utils.Vector2D import Vector2D
from python.Utils.JSONClass import JSONClass

class SpaceObject(JSONClass):
    id: int
    type: int
    size: int
    race: str
    aliance: int

    def __init__(self, StarWars, data):
        super().__init__(data)
        self.Game = StarWars
        if not 'size' in data:
            self.size = 10000
