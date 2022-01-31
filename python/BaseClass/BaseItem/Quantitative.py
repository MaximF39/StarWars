import copy


from python.Packages.PackagesManager import PackagesManager
from python.BaseClass.BaseItem.BaseItem import BaseItem
from python.Static.Type.ShopType import ShopType


class Quantitative(BaseItem):
    count: int

    def __init__(self, Game, classNumber, Owner, data):
        super().__init__(Game, classNumber, Owner, data)
        self.mod = 'q'

    def add_inventory(self):
        pass

    def get_size(self, count):
        return self.size * count

    def get_cost(self, count):
        return self.cost * count

    def create_class(self, Player, count):
        class_ = copy.copy(self)
        class_.new_owner(Player)
        class_.count = count
        return class_

    def buy(self, Player, count, Game):
        self.separation(Player, count)
        self.Game = Game

        PacMan = PackagesManager(Player.id, self.Game)
        PacMan.tradingItems(ShopType.InventoryShop)
        PacMan.updateValue(9)

    @property
    def get_wear(self):
        return self.count


    def sell(self, Planet, count, Game):
        raise NotImplementedError('eeror')
        self.Game = Game
        self.separation(Planet, count)

        PacMan = PackagesManager(self.Owner.id, self.Game)
        PacMan.tradingItems(ShopType.InventoryShop)
        PacMan.updateValue(9)

    @property
    def get_satisfying(self):
        return True

    def separation(self, Whom, count): # Кому, сколько(количество)
        Whom.add_item(self.create_class(Whom, count))

        self.count -= count
        if self.count == 0:
            self.Owner.remove_item(self)
        self.guid = self.get_guid


    def drop(self, count):
        if self.count >= count:
            self.x = self.Owner.x
            self.y = self.Owner.y
            self.separation(self.Owner.Location, count)


        PacMan = PackagesManager(self.Owner.id, self.Game)
        PacMan.items()
