from python.BaseClass.SpaceObject import SpaceObject
from random import randint
from python.cfg.cfg_shop_type import repository

class StaticSpaceObject(SpaceObject):
    class_number: int
    landable: bool


    def __init__(self, Game, data, Location):
        super().__init__(Game, data)
        self.Location = Location
        self.StaticSpaceObjectType = data['type']
        self.landable = True
        self.x = randint(-1000, 1000)
        self.y = randint(-1000, 1000)
        self.classNumber = 256 - data['type']
        self.radius = 2
        self.aliance = 2
        self.clanId = 2
        self.angle = float('inf')
        self.players = []
        self.QCount = 2
        self.shops = repository
        self.send_info_location()

    def send_info_location(self):
        self.Location.set_static_space_object(self)

    def leaveLocation(self, PlayerClass):
        self.players.remove(PlayerClass)




