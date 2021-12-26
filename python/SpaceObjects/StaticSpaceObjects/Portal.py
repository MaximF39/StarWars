from ...BaseClass.StaticSpaceObject import StaticSpaceObject

class Portal(StaticSpaceObject):

    def __init__(self, Game, data, LocationClass):
        super().__init__(Game, data, LocationClass)