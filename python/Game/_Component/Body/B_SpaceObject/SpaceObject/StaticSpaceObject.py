from random import randint

from python.Game import SpaceBigObject


class StaticSpaceObject(SpaceBigObject):
    class_number: int
    landable:bool = True

    def __init__(self, Game, data, Location):
        SpaceBigObject.__init__(self, Game, data, Location)
        self.StaticSpaceObjectType = self.type
        self.x = randint(-1000, 1000)
        self.y = randint(-1000, 1000)
        self.class_number = 256 - self.type
        self.RADIUS = 2
        self.aliance = 2
        self.angle = float('inf')

    def send_info_location(self):
        self.Location.set_static_space_object(self)





