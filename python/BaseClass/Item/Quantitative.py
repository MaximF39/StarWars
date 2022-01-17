import copy

from python.cfg.cfg_trading import cfg_trading
from python.Packages.PackagesManager import PackagesManager
from python.BaseClass.Item.BaseItem import BaseItem

class Quantitative(BaseItem):

    def __init__(self, Game, classNumber, Owner, data):
        self.wear = data['count']
        self.count = data['count']
        super().__init__(Game, classNumber, Owner, data)

    def add_inventory(self):
        pass

    def get_size(self, count):
        return self.size * count

    def get_cost(self, count):
        return self.cost * count

    def create_class(self, Player, count):
        class_ = copy.copy(self)
        class_.get_owner(Player, count)
        return class_

    def buy(self, Player, count, Game):
        self.separation(Player, count)
        self.Game = Game

        PacMan = PackagesManager(Player.id, self.Game)
        PacMan.tradingItems()
        PacMan.updateValue(9)

    def sell(self, Planet, count, Game):
        self.Game = Game
        self.separation(Planet, count)

        PacMan = PackagesManager(self.Player.id, self.Game)
        PacMan.tradingItems()
        PacMan.updateValue(9)

    @property
    def get_satisfying(self):
        return True

    def separation(self, Whom, count): # Кому, сколько(количество)
        Whom.add_item(self.create_class(Whom, count))

        if self.Player:
            self.wear -= count
            if self.wear == 0:
                self.Player.inventory.remove(self)
        else:
            self.guid = self.get_guid


    def drop(self, count):
        if self.wear >= count:
            self.x = self.Player.x
            self.y = self.Player.y
            self.separation(self.Player.Location, count)


        PacMan = PackagesManager(self.Player.id, self.Game)
        PacMan.items()
