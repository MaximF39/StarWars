from ...BaseClass.StaticSpaceObject import StaticSpaceObject
from ...Packages.PackagesManager import PackagesManager

class Hive(StaticSpaceObject):

    def __init__(self, Game, data, LocationClass):
        super().__init__(Game, data, LocationClass)

    def SetPlayer(self, PlayerClass):
        self.players.append(PlayerClass)
        PacMan = PackagesManager(self.id, self.Game)
        PacMan.locationPlanet()
