import copy

from python.Static.TypeStr.PlayerSkillTypeStr import PlayerSkillTypeStr
from python.cfg.cfg_sell_buy import cfg_sell_buy
from python.Packages.PackagesManager import PackagesManager
from python.BaseClass.Item.BaseItem import BaseItem

class NoQuantitative(BaseItem):
    fullRepair = 1000

    def __init__(self, Game, classNumber, Owner, data):
        super().__init__(Game, classNumber, Owner, data)
        self.wear = self.fullRepair
        self.repair_cost = self.cost / 500

    def add_inventory(self):
        pass

    def get_size(self, count=None):
        return self.size

    def get_cost(self, count=None):
        return self.cost

    def create_class(self, Player, count=None):
        class_ = copy.copy(self)
        class_.Player = Player
        class_.get_satisfying
        return class_

    def buy(self, Player, count):
        Player.cash -= int(self.cost * cfg_sell_buy(Player.skills['Trading']).coef_buy)
        self.separation(Player)

        PacMan = PackagesManager(Player.id, self.Game)
        PacMan.tradingItems()
        PacMan.updateValue(9)

    def sell(self, Planet, count=None):
        self.Player.cash += int(self.cost * cfg_sell_buy(self.Player.skills['Trading']).coef_sell)
        self.separation(Planet)

        PacMan = PackagesManager(self.Player.id, self.Game)
        PacMan.tradingItems()
        PacMan.updateValue(9)

    @property
    def get_satisfying(self, m=True):
        if m:
            if self.restrictions is None or 'Planet' == self.Player.__name__:
                return True
        skills = self.Player.skills
        SkillTypeStr = PlayerSkillTypeStr()
        for skill in self.restrictions:
            match skill["type"]:
                case 2:
                    if skill['Value'] > skills[SkillTypeStr.get_str(skill['valueType'])]:
                        return False
                case 4:
                    if skill['Value'] > self.Player.ship['cpu']:
                        return False
                case 5:
                    if self.Player.status > skill['Value']:  # -3 > -2 пир или коп и ниже тоже
                        return False
                case 6:
                    if self.Player.status < skill['Value']:  # 3 < 2 # player < need -> False
                        return False
                case _:
                    print('Не понятный тип', skill['type'])
        return True


    def separation(self, Whom, count=None):
        Whom.inventory.append(self.create_class(Whom))
        self.Player.inventory.remove(self)

    def drop(self, count=None):
        self.x = self.Player.x
        self.y = self.Player.y
        self.separation(self.Player.Location)

        PacMan = PackagesManager(self.Player.id, self.Game)
        PacMan.items()

    def repair(self):
        if self.Player.cash > (self.fullRepair - self.wear) * self.repair_cost:
            self.wear = self.fullRepair
            self.Player.cash -= (self.fullRepair - self.wear) * self.repair_cost
        else:
            count = self.Player.cash // self.repair_cost
            self.wear += count
            self.Player.cash = 0