from python.Static.cfg.shops.cfg_shop_type import *


class GetShopType:
    Game: "StarWars"
    Location: "Location"
    race: int
    id: int

    def __init__(self):
        self.shops = self.get_shops

    @property
    def get_shops(self):
        if self.Location.id in default_shop:
            if self.race != 0:
                return default_type
        if self.id in improve_resources:
            return [ShopType.UpdateResources]
        if self.id in improve_ship:
            return [ShopType.UpdateShips]
        if self.id in ginetic_lab_planet_id:
            return [ShopType.GineticLab]
        return []



    # def init_items(self):
    #     if not self.shops:
    #         return
    #     for shop_type in self.shops:
    #         match shop_type:
    #             case ShopType.ShipFactory:
    #                 pass
    #                 # if self.Location.id in weak_system:
    #                 #     for shipClass in weak_ship(self.race):
    #                 #         self.ships.append(FakeShip(self.Game, shipClass))
    #                 # elif self.Location.id in medium_system:
    #                 #     for shipClass in medium_ship(self.race):
    #                 #         self.ships.append(FakeShip(self.Game, shipClass))
    #                 # elif self.Location.id in strong_system:
    #                 #     for shipClass in strong_ship(self.race):
    #                 #         self.ships.append(FakeShip(self.Game, shipClass))
    #                 # else:
    #                 #     raise NotImplementedError('Нет класса для кораблей?')
    #             case ShopType.InventoryShop:
    #                 for item in get_default_items(race=self.race, OwnerClass=self, Game=self.Game):
    #                     self.inventory.append(item)
    #                     self.default_shop.append(item.classNumber)
