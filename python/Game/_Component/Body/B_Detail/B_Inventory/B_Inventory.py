
class B_Inventory:

    def __init__(self):
        self.inventory: list = []

    def add_item(self, Item):
        for inventory_item in self.inventory:
            if inventory_item.class_number == Item.class_number:
                if inventory_item.mod == 'q':
                    inventory_item + Item
                    return
                # return
        self.inventory.append(Item)

    def remove_item(self, Item):
        self.inventory.remove(Item)