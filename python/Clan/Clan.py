from python.cfg import cfg_clan
from python.Utils.ThreadBase import ThreadBase


class Clan(ThreadBase):

    def __init__(self, Game, dict_):
        self.Game = Game
        self.name = dict_['name']
        self.shortName = dict_['short_name']
        self.description = dict_['description']
        self.Leader = getattr(self.Game, f'Player_{dict_["owner_id"]}')
        self.cash = dict_['cash']
        self.bonus = dict_['bonus']
        self.repository: list = dict_['repository']
        self.level = dict_["level"]  # need get lever clan
        self.enemies: list = dict_["enemies"]  # get list enemy, if there are no enemies get empty list[]
        self.friends: list = dict_["friends"]  # as well as at the top
        self.maxMembers: int = cfg_clan.members[self.level]
        self.maxFriends: int = cfg_clan.friends[self.level]
        self.rating: int = self.rating()
        self.nextLevelPointsValue: int = 0 # next level points
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
