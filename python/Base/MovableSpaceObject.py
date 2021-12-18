from . import SpaceObject
from . import cfg_update


class MovableSpaceObject(SpaceObject):
    speed: float
    time_update = cfg_update['MovableSpaceObject']
