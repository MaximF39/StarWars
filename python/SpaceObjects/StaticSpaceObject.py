from ..BaseClass.SpaceObject import SpaceObject
from random import randint

class StaticSpaceObject(SpaceObject):
    class_number: int
    landable: bool


    def __init__(self, Game, data, LocationClass):
        super().__init__(Game, data)
        self.LocationClass = LocationClass
        self.StaticSpaceObjectType = data['type']
        self.landable = True
        self.x = randint(-1000, 1000)
        self.y = randint(-1000, 1000)
        self.classNumber = 256 - data['type'] # 252
        self.radius = 2
        self.aliance = 2
        self.clanID = 2
        self.angle = float('inf')
        self.QCount = 2
        self.shop = data['shop']
        self.send_info_location()

    def send_info_location(self):
        self.LocationClass.set_static_space_object(self)



