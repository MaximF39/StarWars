from . import SpaceObject
from . import cfg_update


class MovableSpaceObject(SpaceObject):
    speed: float
    x: float
    y: float
    target_x: float
    target_y: float
    time_update = cfg_update['MovableSpaceObject']
