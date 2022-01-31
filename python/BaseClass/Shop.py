from python.BaseClass.FakeShip import FakeShip
from python.Packages.PackagesManager import PackagesManager
from python.Static.Type.ShopType import ShopType
from python.Static.cfg.shops.cfg_shop_type import *
from python.Static.cfg.shops.inventory import get_default_items


class Shop:
    Game: "StarWars"
    Location: "Location"
    race: int

    def __init__(self):
        if self.Game is None or self.Location is None or self.race is None:
            raise NotImplementedError("Ты забыл что-то из этого: Game, Location, race")

        self.shops = self.get_shops
        self.inventory = []
        self.default_shop = []
        self.ships = []

        self.get_items()

    def buy_item(self):
        pass

    def sell_item(self, ItemClass):
        raise NotImplementedError("Сломал надо будет починю")
        PacMan = PackagesManager(self.Owner.id, self.Game)
        PacMan.tradingItems(ShopType.InventoryShop)
        PacMan.updateValue(9)

    @property
    def get_shops(self):
        if self.Location.id in default_shop:
            if self.race != 0:
                return default_type
        return []

    def get_items(self):
        if not self.shops:
            return
        for shop_type in self.shops:
            match shop_type:
                case ShopType.ShipFactory:
                    if self.Location.id in weak_system:
                        for shipClass in weak_ship(self.race):
                            self.ships.append(FakeShip(self.Game, shipClass))
                    elif self.Location.id in medium_system:
                        for shipClass in medium_ship(self.race):
                            self.ships.append(FakeShip(self.Game, shipClass))
                    elif self.Location.id in strong_system:
                        for shipClass in strong_ship(self.race):
                            self.ships.append(FakeShip(self.Game, shipClass))
                    else:
                        raise NotImplementedError('Нет класса для кораблей?')
                case ShopType.InventoryShop:
                    for item in get_default_items(race=self.race, OwnerClass=self, Game=self.Game):
                        self.inventory.append(item)
                        self.default_shop.append(item.classNumber)
