from python.Static.cfg.shops.cfg import default_value
from ..Packages.PackagesManager import PackagesManager
from .Item import item
import math
# from . import parse_galaxy_map
from python.Utils.ThreadBase import ThreadBase
from ..BaseClass.SpaceObject import SpaceObject
from python.BaseClass.Shop import Shop
from ..Static.Type.ShopType import ShopType


class Planet(SpaceObject, ThreadBase, Shop):
    name: str  # my
    class_number: int  #be bytes
    radius: int
    landable: bool
    is_sun: bool
    speed: int = 3  #
    _i = 1  # Уголобразующий

    def __init__(self, Game, data:dict, LocationClass):
        super().__init__(Game, data)
        self.name = self.Name
        self.is_sun = bool(6 > self.classNumber)
        self.angle = float("inf") if 6 > self.classNumber else self._i * 3.14 / 180
        self.landable = False if self.is_sun else True
        self.players = []
        self.clanId = 0 # Только чей клан захвачен, могут садиться на планету
        self.QCount = 0 # Количество квестов
        self.Location = LocationClass
        Shop.__init__(self)

        if self.angle != float('inf'):
            self._i += self.speed
            if self._i > 360:
                self._i = 1
            self.x = int(self.radius * math.sin(self.angle))
            self.y = int(self.radius * math.cos(self.angle))
            self.update()

        self.send_info_location()

    @property
    def __name__(self):
        return self.__class__.__name__

    def update_ships(self, Player):
        PackagesManager(Player.id, self.Game).shipUpdateInfo()

    def add_item(self, Item):
        if Item.classNumber in self.default_shop:
            Item.guid = Item.get_guid
            return
        for inventory_item in self.inventory:
            if inventory_item.classNumber == Item.classNumber:
                if inventory_item.mod == 'q':
                    inventory_item + Item
                    return
        self.inventory.append(Item)

    def remove_item(self, Item):
        if Item.classNumber in self.default_shop:
            if Item.count != default_value:
                Item.count = default_value
            Item.guid = Item.get_guid
            return
        self.inventory.remove(Item)

    def SetPlayer(self, PlayerClass):
        self.players.append(PlayerClass)
        PlayerClass.SpaceObject = self
        PacMan = PackagesManager(PlayerClass.id, self.Game)
        PacMan.locationPlanet()

    def inventory_shop(self, Player):
        PacMan = PackagesManager(Player.id, self.Game)
        PacMan.tradingItems(ShopType.InventoryShop)

    def fake_items(self, Player):
        ItemsForPlayer = []
        for Item_ in self.inventory:
            ItemsForPlayer.append(Item_.ItemForPlayer(Player))
        return ItemsForPlayer


    def ship_factory(self, Player):
        PacMan = PackagesManager(Player.id, self.Game)
        PacMan.tradingShips()

    def leaveLocation(self, playerClass):
        self.players.remove(playerClass)

    def send_info_location(self):
        self.Location.set_planet(self)

    def update(self):  # ready
        self.start_timer_update(self.move, 1) # cfg_update['SpaceObject']

    def move(self):
        self._i += self.speed
        if self._i > 360:
            self._i = 1
        self.angle = self._i * 3.14 / 180
        self.x = int(self.radius * math.sin(self.angle))
        self.y = -1 * int(self.radius * math.cos(self.angle))

