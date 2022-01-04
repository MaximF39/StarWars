from python.Utils.ThreadBase import ThreadBase

class Clan(ThreadBase):

    def __init__(self, Game, dict_):
        self.name = dict_['name']
        self.shortName = dict_['shortName']
        self.Game = Game
        self.Leader = getattr(self.Game, f'Player_{dict_["lider_id"]}')
        self.cash = dict_['cash']
        self.bonus = dict_['bonus'] # Если тебе надо что-то из бд, то добавляй такую запись. Это значит что из бд придёт эта инфа
        self.repository = dict_['repository']
        self.maxMembers: int
        self.maxFriends: int
        self.members = []
        self.update()

    def update(self):
        self.start_timer_update(self.playerPoints, 600)

    def playerPoints(self):
        for player in self.members:
            pass

    def sendCash(self, cash):
        pass

    def getCash(self, cash):
        pass

    def sendBonus(self, bonus):
        pass

    def moveNextLevel(self):
        pass

    def friendRequest(self, ClanClass):
        pass

    def addEnemies(self, clanClass):
        pass

    def acceptFriend(self, ClanClass):
        pass

    def nextLevelPoints(self):
        pass

    def joinRequestStatus(self, playerClass, result):
        pass

    def buyBonusItem(self):
        pass

    def setPlayerRole(self, PlayerClass, role):
        pass

    def ClanJoinRequest(self, playerClass, message):
        pass

    def removeMember(self, playerClass):
        pass

    def deleteClan(self):
        pass