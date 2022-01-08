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

    def create_class(self, PlayerClass, count, droidUsing):
        class_ = copy.copy(self)
        class_.Owner = PlayerClass
        class_.wear = count
        if droidUsing:
            self.inUsing = droidUsing
        return class_

    def buy(self, PlayerClass, count):
        PlayerClass.cash -= int(self.cost * count * cfg_sell_buy(PlayerClass.skills['Trading']).coef_buy)
        self.separation(PlayerClass, count)

        PacMan = PackagesManager(PlayerClass.id, self.Game)
        PacMan.tradingItems()
        PacMan.updateValue(9)

    def sell(self, PlanetClass, count):
        self.Owner.cash += int(self.cost * count * cfg_sell_buy(self.Owner.skills['Trading']).coef_sell)
        self.separation(PlanetClass, count)

        PacMan = PackagesManager(self.Owner.id, self.Game)
        PacMan.tradingItems()
        PacMan.updateValue(9)

    @property
    def get_satisfying(self):
        return True

    def separation(self, Whom, count, droidUsing=False): # Кому, сколько(количество)
        Whom.inventory.append(self.create_class(Whom, count, droidUsing))
        self.wear -= count
        if self.wear == 0:
            self.Owner.inventory.remove(self)


    def drop(self, count):
        if self.wear >= count:
            self.x = self.Owner.x
            self.y = self.Owner.y
            self.separation(self.Owner.Location, count)


        PacMan = PackagesManager(self.Owner.id, self.Game)
        PacMan.items()
