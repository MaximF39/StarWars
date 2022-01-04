from python.cfg import cfg_clan
from python.Utils.ThreadBase import ThreadBase


class Clan(ThreadBase):

    def __init__(self, Game, dict_):
        self.name = dict_['name']
        self.shortName = dict_['shortName']
        self.Game = Game
        self.Leader = getattr(self.Game, f'Player_{dict_["lider_id"]}')
        self.cash = dict_['cash']
        self.bonus = dict_['bonus']
        self.repository: list = dict_['repository']
        self.lvl = dict_["lvl"]  # need get lever clan
        self.enemyClans: list = dict_["enemyClans"]  # get list enemy, if there are no enemies get empty list[]
        self.friendClans: list = dict_["friendClans"]  # as well as at the top
        self.maxMembers: int
        self.maxFriends: int
        self.points: int = 0
        self.nextLevelPointsValue: int = 0 # next level point
        self.friendRequestList = []
        self.newPlayerRequestList = {}  # key = player and valuer = message
        self.members = []
        self.update()

    def update(self):
        self.start_timer_update(self.playerPoints, 600)

    def playerPoints(self):
        self.points = sum([player.point for player in self.members])  # one variable, more productive
        # and two variable, more easy

        # self.points = 0
        # for player in self.members:
        #     self.points += player.point

    def sendCash(self, cash):
        self.cash -= cash

    def getCash(self, cash):
        self.cash += cash

    def sendBonus(self, bonus):
        self.bonus -= bonus

    def getBonus(self, bonus):
        self.bonus += bonus

    def moveNextLevel(self):
        if self.lvl != max(cfg_clan.level):
            need = cfg_clan.level
            if self.cash >= need["credit"] and self.bonus >= need["bonus"]:
                self.lvl += 1

    def friendRequest(self, ClanClass):
        self.friendRequestList.append(ClanClass)
        del self.friendRequestList[self.friendRequestList.index(ClanClass)]

    def addEnemies(self, clanClass):
        self.enemyClans.append(clanClass)
        if clanClass in self.friendClans:
            del self.friendClans[self.friendClans.index(clanClass)]
        if clanClass in self.friendRequestList:
            del self.friendRequestList[self.friendRequestList.index(clanClass)]

    def acceptFriend(self, ClanClass):
        self.friendClans.append(ClanClass)

    def nextLevelPoints(self):
        for levelPoint in cfg_clan.points:
            if self.points <= cfg_clan.points[levelPoint]:
                self.nextLevelPointsValue = self.points - cfg_clan.points[levelPoint]
                break

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
        del self.members[self.members.index(playerClass)]

    def deleteClan(self):
        pass
