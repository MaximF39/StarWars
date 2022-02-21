from python.Base.SpaceObject.MovableSpaceObject import MovableSpaceObject
from python.Base.SpaceObject.GetShopType import GetShopType
from python.Base.SpaceObject.SetPlayer import SetPlayer


class SpaceBigObject(MovableSpaceObject, GetShopType, SetPlayer):

    def __init__(self, Game, data, Location):
        self.Location = Location
        self.clanId = 0  # Только чей клан захвачен, могут садиться на планету
        self.QCount = 0  # Количество квестов
        self.players = []
        MovableSpaceObject.__init__(self, Game, data)
        GetShopType.__init__(self)
        self.send_info_location()

    def send_info_location(self):
        raise NotImplementedError(" don't send info location ")

    def leave(self, Player):
        self.remove_player(Player)
        for player in self.players:
            player.Packages.locationPlanet()

    @property
    def __name__(self):
        return self.__class__.__name__


