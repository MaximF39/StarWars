import copy

from python.cfg.cfg_sell_buy import cfg_sell_buy
from python.Packages.PackagesManager import PackagesManager
from python.BaseClass.Item.BaseItem import BaseItem

class Quantitative(BaseItem):

    def __init__(self, Game, classNumber, Owner, data):
        self.wear = data['count']
        super().__init__(Game, classNumber, Owner, data)

    def add_inventory(self):
        pass

    def get_size(self, count):
        return self.size * count

    def get_cost(self, count):
        return self.cost * count

    def create_class(self, Player, count, droidUsing):
        class_ = copy.copy(self)
        class_.Player = Player
        class_.wear = count
        if droidUsing:
            self.inUsing = droidUsing
        return class_

    def buy(self, Player, count):
        Player.cash -= int(self.cost * count * cfg_sell_buy(Player.skills['Trading']).coef_buy)
        self.separation(Player, count)

        PacMan = PackagesManager(Player.id, self.Game)
        PacMan.tradingItems()
        PacMan.updateValue(9)

    def sell(self, Planet, count):
        self.Player.cash += int(self.cost * count * cfg_sell_buy(self.Player.skills['Trading']).coef_sell)
        self.separation(Planet, count)

        PacMan = PackagesManager(self.Player.id, self.Game)
        PacMan.tradingItems()
        PacMan.updateValue(9)

    @property
    def get_satisfying(self):
        return True

    def separation(self, Whom, count, droidUsing=False): # Кому, сколько(количество)
        Whom.inventory.append(self.create_class(Whom, count, droidUsing))
        self.wear -= count
        if self.wear == 0:
            self.Player.inventory.remove(self)


    def drop(self, count):
        if self.wear >= count:
            self.x = self.Player.x
            self.y = self.Player.y
            self.separation(self.Player.Location, count)


        PacMan = PackagesManager(self.Player.id, self.Game)
        PacMan.items()
