import copy

from ....cfg.cfg_sell_buy import cfg_sell_buy
from ....Packages.PackagesManager import PackagesManager
from .baseItem import baseItem
class Quantitative(baseItem):

    def __init__(self, Game, classNumber, OwnerClass, count):
        self.wear = count
        super().__init__(Game, classNumber, OwnerClass)

    def add_inventory(self):
        pass

    def get_size(self, count):
        return self.size * count

    def get_cost(self, count):
        return self.cost * count

    def create_class(self, PlayerClass, count):
        class_ = copy.copy(self)
        class_.Owner = PlayerClass
        class_.wear = count
        return class_


    def buy(self, PlayerClass, count):
        if PlayerClass.cash >= self.get_cost(count)and self.wear >= count:
            PlayerClass.cash -= int(self.cost * count * cfg_sell_buy(PlayerClass.skills['Trading']).coef_buy)
            self.separation(PlayerClass, count)

            PacMan = PackagesManager(PlayerClass.id, self.Game)
            PacMan.tradingItems()
            PacMan.updateValue(9, PlayerClass.cash)

    @property
    def get_satisfying(self):
        return True

    @property
    def get_inUsing(self):
        return False

    def separation(self, Whom, count): # Кому, сколько(количество)
        Whom.inventory.append(self.create_class(Whom, count))
        self.wear -= count
        if self.wear == 0:
            self.Owner.inventory.remove(self)

    def dropItem(self, count):
        if self.wear >= count:
            self.separation(self.Owner.Location, count)
