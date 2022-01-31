from python.Static.cfg import cfg_clan
from python.Utils.JSONClass import JSONClass
from python.Utils.ThreadBase import ThreadBase


class Clan(JSONClass, ThreadBase):
    name: str
    shortName: str
    description: str
    cash: int
    bonus: int
    repository: list
    level: int
    enemies: list
    friends: list

    def __init__(self, Game, dict_):
        super().__init__(dict_)
        self.Game = Game
        self.Leader = getattr(self.Game, f'Player_{dict_["ownerId"]}')
        self.maxMembers: int = cfg_clan.members[self.level]
        self.maxFriends: int = cfg_clan.friends[self.level]
        self.rating: int = self.rating()
        if self.level + 1 in cfg_clan.points:
            self.nextLevelPointsValue: int = cfg_clan.points[self.level + 1] # next level points
        else:
            self.nextLevelPointsValue: int = cfg_clan.points[self.level]
        self.friendRequestList = []
        self.newPlayerRequestList = {}  # key = player and valuer = message
        self.members = []
        self.update()

    def update(self):
        self.start_timer_update(self.playerPoints, 600)

    def playerPoints(self):
        self.rating = sum(member.points for member in self.members)

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
