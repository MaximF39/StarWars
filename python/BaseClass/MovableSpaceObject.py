from . import SpaceObject
from . import cfg_update


class MovableSpaceObject(SpaceObject):
    speed: float
    x: float
    y: float
    target_x: float
    target_y: float

    def __init__(self, Game, data):
        super().__init__(Game, data)
        self.speed = data['speed'] if 'speed' in data else None
        self.x = data['x']
        self.y = data['y']
        self.target_x = data['x'] # data['target_x']
        self.target_y = data['y'] # data['target_y']
