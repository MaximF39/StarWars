from python.Static.cfg import cfg_clan
from python.Utils.ThreadBase import ThreadBase


class Clan(ThreadBase):
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
        self.__dict__.update(data)
        self.Game = Game
        self.maxMembers: int = cfg_clan.members[self.level]
        self.maxFriends: int = cfg_clan.friends[self.level]
        if self.level + 1 in cfg_clan.points:
            self.nextLevelPointsValue: int = cfg_clan.points[self.level + 1]  # next level points
        else:
            self.nextLevelPointsValue: int = cfg_clan.points[self.level]
        self.friendRequestList = []
        self.newPlayerRequestList = {}  # key = player and valuer = message

    @property
    def get_rating(self):
        rating = 0
        for member in self.members:
            rating += member.rating
        return rating

    def sendCash(self, cash, Whom):
        if self.cash >= cash:
            self.cash -= cash
            Whom.getCash(cash)

    def getCash(self, cash):
        self.cash += cash

    def sendBonus(self, bonus):
        self.bonus -= bonus

    def getBonus(self, bonus):
        self.bonus += bonus

    def moveNextLevel(self):
        if self.level != max(cfg_clan.level):
            need = cfg_clan.level[self.level]
            if self.cash >= need["credit"] and self.bonus >= need["bonus"]:
                self.cash -= need["credit"]
                self.bonus -= need["bonus"]
                self.level += 1

    def friendRequest(self, ClanClass):
        self.friendRequestList.append(ClanClass)
        self.friendRequestList.remove(ClanClass)

    def addEnemies(self, clanClass):
        self.enemies.append(clanClass)
        if clanClass in self.friends:
            self.friends.remove(clanClass)
        if clanClass in self.friendRequestList:
            self.friendRequestList.remove(clanClass)

    def acceptFriend(self, ClanClass):
        if self.maxFriends > len(self.friends):
            self.friends.append(ClanClass)

    def nextLevelPoints(self):
        return cfg_clan.points[self.level + 1]

    def joinRequestStatus(self, playerClass, result):
        pass

    def buyBonusItem(self, price, item):
        if self.bonus >= price:
            self.bonus -= price
            self.repository.append(item)
            return True  # if the purchase has been completed
        else:
            return False

    def setPlayerRole(self, PlayerClass, role):
        self.members[self.members.index(PlayerClass)].role = role

    def ClanJoinRequest(self, playerClass, message):
        self.newPlayerRequestList[playerClass] = message

    def removeMember(self, playerClass):
        if playerClass in self.members:
            self.members.remove(playerClass)

    def deleteClan(self):
        pass
