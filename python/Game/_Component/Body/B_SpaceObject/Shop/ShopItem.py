from python.Config.CFG_Shop.inventory import get_default_items
from python.Game import B_Inventory

class ShopItem(B_Inventory):
    race:int
    Game:"StarWars"

    def __init__(self):
        B_Inventory.__init__(self)
        self.default_shop = []

    def get_shop(self):
        return self.inventory

    def init_items(self):
        for Item in get_default_items(race=self.race, OwnerClass=self, Game=self.Game):
            B_Inventory.add_item(self, Item)
            self.default_shop.append(Item.class_number)
