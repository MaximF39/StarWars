from python.Static.cfg.shops.inventory import get_default_items
from python.Base.Inventory.BaseInventory import BaseInventory

class ShopItem(BaseInventory):
    default_shop = []

    def get_shop(self):
        return self.inventory

    def get_items(self):
        for Item in get_default_items(race=self.race, OwnerClass=self, Game=self.Game):
            BaseInventory.add_item(self, Item)
            self.default_shop.append(Item.classNumber)
