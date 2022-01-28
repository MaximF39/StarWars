from python.BaseClass.FakeShip import FakeShip
from python.cfg.shops.cfg_shop_type import *
from python.cfg.shops.ships import *
from python.cfg.shops.inventory import *
from python.Static.Type.ShopType import ShopType
from python.Static.Type.Race import Race


class Shop:

    def __init__(self):
        if self.Game is None or self.Location is None or self.race is None:
            self.Location = None
            self.race = None
            self.Game = None
            raise NotImplementedError("Ты забыл что-то из этого: Game, Location, race")

        self.shops = self.get_shops
        self.default_shop = []
        self.get_items()

    @property
    def get_shops(self):
        if self.Location.id in default_shop:
            if self.race != 0:
                return default_type
        # elif self.Location.id ==
        return []

    def get_items(self):
        if not self.shops:
            return
        for shop_type in self.shops:
            match shop_type:
                case ShopType.ShipFactory:
                    self.ships = []
                    if self.Location.id in weak_system:
                        for ship_class in weak_ship(self.race):
                            self.ships.append(FakeShip(self.Game, ship_class))
                    elif self.Location.id in medium_system:
                        for ship_class in medium_ship(self.race):
                            self.ships.append(FakeShip(self.Game, ship_class))
                    elif self.Location.id in strong_system:
                        for ship_class in strong_ship(self.race):
                            self.ships.append(FakeShip(self.Game, ship_class))
                    else:
                        raise NotImplementedError('Нет класса для кораблей?')
                case ShopType.InventoryShop:
                    self.inventory = get_inventory(self.race)
                    for i in self.inventory:
                        self.default_shop.append(i.classNumber)

