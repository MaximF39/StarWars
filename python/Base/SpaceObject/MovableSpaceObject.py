from python.Base.SpaceObject.SpaceObject import SpaceObject


class MovableSpaceObject(SpaceObject):
    speed: float
    x: float
    y: float
    targetX: float
    targetY: float

    def __init__(self, Game, data):
        super().__init__(Game, data)

