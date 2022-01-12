from . import SpaceObject


class MovableSpaceObject(SpaceObject):
    speed: float
    x: float
    y: float
    target_x: float
    target_y: float

    def __init__(self, Game, data):
        super().__init__(Game, data)
        self.speed = data['speed'] if 'speed' in data else None
        self.x = data['x'] if 'x' in data else None
        self.y = data['y'] if 'y' in data else None
        self.target_x = data['target_x'] if 'target_x' in data else None
        self.target_y = data['target_y'] if 'target_y' in data else None
