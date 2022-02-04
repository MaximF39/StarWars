from random import randint

from python.Base.SpaceObject.SpaceBigObject import SpaceBigObject


class StaticSpaceObject(SpaceBigObject):
    class_number: int
    landable: bool

    def __init__(self, Game, data, Location):
        SpaceBigObject.__init__(self, Game, data, Location)
        self.StaticSpaceObjectType = data['type']
        self.landable = True
        self.x = randint(-1000, 1000)
        self.y = randint(-1000, 1000)
        self.classNumber = 256 - data['type']
        self.RADIUS = 2
        self.aliance = 2
        self.angle = float('inf')

    def send_info_location(self):
        self.Location.set_static_space_object(self)





