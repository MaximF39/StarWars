from python.cfg.cfg_shop_type import *
from python.cfg.shops.ships import *
from python.cfg.shops.inventory import *
from python.Static.Type.ShopType import ShopType
from python.Static.Type.Race import Race


class Shop:

    def __init__(self, Game):
        self.Game = Game
        self.shops = self.get_shops
        self.default_shop = []
        self.get_items()

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
                        self.ships = weak_ship(self.race)
                    elif self.Location.id in medium_system:
                        self.ships = medium_ship(self.race)
                    elif self.Location.id in strong_system:
                        self.ships = strong_ship(self.race)
                    else:
                        raise NotImplementedError('Нет класса для кораблей?')
                case ShopType.InventoryShop:
                    self.inventory = get_inventory(self.race)
                    for i in self.inventory:
                        self.default_shop.append(i.classNumber)




