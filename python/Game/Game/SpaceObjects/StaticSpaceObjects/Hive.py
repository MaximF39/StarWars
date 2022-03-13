from python.Game._Component.Event.E_SpaceObject.Set.SpaceObjectSetter.PlanetSetter import PlanetSetter
from python.Game._Component.Body.B_SpaceObject.SpaceObject.StaticSpaceObject import StaticSpaceObject


class Hive(StaticSpaceObject, PlanetSetter):

    def __init__(self, Game, data, LocationClass):
        StaticSpaceObject.__init__(self, Game, data, LocationClass)

