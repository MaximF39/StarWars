import copy

from python.Base.BaseItem.BaseItem import BaseItem
from python.Static.Type.ShopType import ShopType


class Quantitative(BaseItem):
    count: int

    def __init__(self, Game, classNumber, Owner, data):
        BaseItem.__init__(self, Game, classNumber, Owner, data)
        self.count = self.wear
        self.mod = 'q'

    @property
    def get_wear(self):
        return self.count

    @property
    def get_size(self):
        return self.count * self.size

    def get_cost(self, count):
        return count * self.cost

    def drop(self, count):
        Player = self.Owner
        BaseItem.set_x_y_owner(self)
        if self.count == count:
            self.transfer(self.Owner.Location)
        elif self.count > count:
            new_item = self - count
            self.Owner.Location.add_item(new_item)
        Player.PacMan.items()

    def buy(self, Player, count):
        if BaseItem.check_default_shop(self):
            class_ = self.copy_class()
            class_.separation(Player, count)
        else:
            self.separation(Player, count)
        BaseItem.good_trade(self, Player)

    def sell(self, Planet, count):
        Player = self.Owner
        self.separation(Planet, count)
        BaseItem.good_trade(self, Player)

    def get_cost_count(self, count):
        return count * self.cost

    def separation(self, Whom, count):
        if self.count == count:
            self.transfer(Whom)
        elif self.count > count:
            new_item = self - count
            Whom.add_item(new_item)
