from python.Base.SpaceObject.SpaceObject.StaticSpaceObject import StaticSpaceObject


class Hive(StaticSpaceObject):

    def __init__(self, Game, data, LocationClass):
        StaticSpaceObject.__init__(self, Game, data, LocationClass)
