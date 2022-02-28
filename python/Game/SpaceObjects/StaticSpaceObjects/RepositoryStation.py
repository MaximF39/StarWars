from python.Base.SpaceObject.SpaceObject.StaticSpaceObject import StaticSpaceObject
from python.Base.SpaceObject.Shop.Repository import Repository
from python.Base.SpaceObject.Shop.ClanRepository import ClanRepository
from python.Base.SpaceObject.Shop.Angar import Angar


class RepositoryStation(StaticSpaceObject, Repository, Angar, ClanRepository):

    def __init__(self, Game, data, LocationClass):
        StaticSpaceObject.__init__(self, Game, data, LocationClass)
