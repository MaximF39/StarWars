from python.Config.CFG_Shop.cfg_shop_type import default_shop, default_type, improve_resources, improve_ship, \
    ginetic_lab_planet_id
from python.Static.Type.SpaceObject.T_Shop import T_Shop


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
            return [T_Shop.UpdateResources]
        if self.id in improve_ship:
            return [T_Shop.UpdateShips]
        if self.id in ginetic_lab_planet_id:
            return [T_Shop.GineticLab]
        return []



    # def init_items(self):
    #     if not self.CFG_Shop:
    #         return
    #     for shop_type in self.CFG_Shop:
    #         match shop_type:
    #             case T_Shop.ShipFactory:
    #                 pass
    #                 # if self.Location.id in weak_system:
    #                 #     for shipClass in weak_ship(self.race):
    #                 #         self.ships.append(FakeShip(self.StarWars, shipClass))
    #                 # elif self.Location.id in medium_system:
    #                 #     for shipClass in medium_ship(self.race):
    #                 #         self.ships.append(FakeShip(self.StarWars, shipClass))
    #                 # elif self.Location.id in strong_system:
    #                 #     for shipClass in strong_ship(self.race):
    #                 #         self.ships.append(FakeShip(self.StarWars, shipClass))
    #                 # else:
    #                 #     raise NotImplementedError('Нет класса для кораблей?')
    #             case T_Shop.InventoryShop:
    #                 for item in get_default_items(race=self.race, OwnerClass=self, StarWars=self.StarWars):
    #                     self.inventory.append(item)
    #                     self.default_shop.append(item.classNumber)
