from ...BaseClass.StaticSpaceObject import StaticSpaceObject
from ...Packages.PackagesManager import PackagesManager

class RepositoryStation(StaticSpaceObject):

    def __init__(self, Game, data, LocationClass):
        super().__init__(Game, data, LocationClass)

    def SetPlayer(self, PlayerClass):
        PlayerClass.SpaceObject = self
        self.players.append(PlayerClass)
        PacMan = PackagesManager(PlayerClass.id, self.Game)
        PacMan.locationPlanet()

    def repository(self, Player):
        PackagesManager(Player.id, self.Game).repository()


    def angar(self, Player):
        PacMan = PackagesManager(Player.id, self.Game)
        PacMan.playerAngar()

    def clan_repository(self, Player):
        PackagesManager(Player.id, self.Game).clan_repository()