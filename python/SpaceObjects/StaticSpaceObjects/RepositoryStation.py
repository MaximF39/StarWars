from ...BaseClass.StaticSpaceObject import StaticSpaceObject

class RepositoryStation(StaticSpaceObject):

    def __init__(self, Game, data, LocationClass):
        super().__init__(Game, data, LocationClass)