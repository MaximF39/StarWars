from python.Game import MovableSpaceObject
from python.Game import GetShopType

class SpaceBigObject(MovableSpaceObject, GetShopType):

    def __init__(self, Game, data, Location):
        super().__init__(Game, data)
        self.Location = Location
        self.clan_id = 0  # Только чей клан захвачен, могут садиться на планету
        self.QCount = 0  # Количество квестов
        self.send_info_location()
        GetShopType.__init__(self)

    def send_info_location(self):
        raise NotImplementedError(" don't send info location ")

    @property
    def __name__(self):
        return self.__class__.__name__


