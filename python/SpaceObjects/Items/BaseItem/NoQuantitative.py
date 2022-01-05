import copy

from ....Static.TypeStr.PlayerSkillTypeStr import PlayerSkillTypeStr
from ....cfg.cfg_sell_buy import cfg_sell_buy
from ....Packages.PackagesManager import PackagesManager
from .baseItem import baseItem

class NoQuantitative(baseItem):
    fullRepair = 1000

    def __init__(self, Game, classNumber, OwnerClass):
        super().__init__(Game, classNumber, OwnerClass)
        self.wear = self.fullRepair
        self.repair_cost = self.cost / 500

    def add_inventory(self):
        pass

    def get_size(self, count=None):
        return self.size

    def get_cost(self, count=None):
        return self.cost

    def create_class(self, PlayerClass, count=None):
        class_ = copy.copy(self)
        class_.Owner = PlayerClass
        return class_

    def buy(self, PlayerClass, count):
        if PlayerClass.cash - self.cost > 0:
            PlayerClass.cash -= int(self.cost * cfg_sell_buy(PlayerClass.skills['Trading']).coef_buy)
            self.separation(PlayerClass)

            PacMan = PackagesManager(PlayerClass.id, self.Game)
            PacMan.tradingItems()
            PacMan.updateValue(9)

    def sell(self, PlanetClass, count=None):
        self.Owner.cash += int(self.cost * cfg_sell_buy(self.Owner.skills['Trading']).coef_sell)
        self.separation(PlanetClass)

        PacMan = PackagesManager(self.Owner.id, self.Game)
        PacMan.tradingItems()
        PacMan.updateValue(9)

    @property
    def get_satisfying(self):
        if self.restrictions is None or not 'level' in self.Owner.__dict__:
            return True
        skills = self.Owner.skills
        SkillTypeStr = PlayerSkillTypeStr()
        for skill in self.restrictions:
            match skill["type"]:
                case 2:
                    if skill['Value'] > skills[SkillTypeStr.get_str(skill['valueType'])]:
                        return False
                case 4:
                    if skill['Value'] > self.Owner.ship['cpu']:
                        self.cpu = skill['Value']
                        print('create cpu', self.cpu)
                        return False
                case 5:
                    if self.Owner.status > skill['Value']:  # -3 > -2 пир или коп и ниже тоже
                        return False
                case 6:
                    if self.Owner.status < skill['Value']:  # 3 < 2 # player < need -> False
                        return False
                case _:
                    print('Не понятный тип', skill['type'])
        return True


    def separation(self, Whom, count=None):
        Whom.inventory.append(self.create_class(Whom))
        self.Owner.inventory.remove(self)

    def drop(self, count=None):
        self.x = self.Owner.x
        self.y = self.Owner.y
        self.separation(self.Owner.Location)

        PacMan = PackagesManager(self.Owner.id, self.Game)
        PacMan.items()

    def repair(self):
        if self.Owner.cash > (self.fullRepair - self.wear) * self.repair_cost:
            self.wear = self.fullRepair
            self.Owner.cash -= (self.fullRepair - self.wear) * self.repair_cost
        else:
            count = self.Owner.cash // self.repair_cost
            self.wear += count
            self.Owner.cash = 0