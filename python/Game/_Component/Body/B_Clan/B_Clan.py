from python.Config.CFG_Clan import cfg_clan
from python.Game._Component.Utils.ThreadBase import ThreadBase


class B_Clan(ThreadBase):
    name: str
    shortName: str
    description: str
    cash: int
    bonus: int
    repository: list
    level: int
    enemies: list
    friends: list
    members: list

    def __init__(self, Game, data):
        ThreadBase.__init__(self)
        self.__dict__.update(data)
        self.Game = Game
        self.maxMembers: int = cfg_clan.members[self.level]
        self.maxFriends: int = cfg_clan.friends[self.level]
        self.friendRequestList = []
        self.newPlayerRequestList = {}  # key = player and valuer = message

    @property
    def get_rating(self):
        rating = 0
        for member in self.members:
            rating += member.rating
        return rating

    def nextLevelPoints(self):
        return cfg_clan.points[self.level + 1]