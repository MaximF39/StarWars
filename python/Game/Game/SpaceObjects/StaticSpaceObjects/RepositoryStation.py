from python.Game._Component.Event.E_SpaceObject.Set.SpaceObjectSetter.PlanetSetter import PlanetSetter
from python.Game._Component.Body.B_SpaceObject.SpaceObject.StaticSpaceObject import StaticSpaceObject
from python.Game._Component.Body.B_SpaceObject import Repository
from python.Game._Component.Body.B_SpaceObject.Shop.ClanRepository import ClanRepository
from python.Game._Component.Body import Angar


class RepositoryStation(StaticSpaceObject, Repository, Angar, ClanRepository, PlanetSetter):

    def __init__(self, Game, data, Location):
        super().__init__(Game, data, Location)
        PlanetSetter.__init__(self)

