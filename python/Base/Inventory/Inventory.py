from .B_Inventory import B_Inventory

class Inventory(B_Inventory):
    ship: "Ship"
    droids: list["item"]
    ControlUsed: int  # used
    ControlLeft: int  # free
    hold:int = 0

    def __init__(self):
        B_Inventory.__init__(self)
        self.activeWeapons = []
        self.activeDevices = []
        self.init_hold()

    def init_hold(self):
        for item_ in self.inventory:
            self.hold += item_.get_size

    def add_item(self, Item):
        if self.ship['size'] >= self.hold + Item.get_size:
            self.hold += Item.get_size
            B_Inventory.add_item(self, Item)

    def change_hold(self, count):
        self.hold -= count

    def remove_item(self, Item):
        self.hold -= Item.get_size
        B_Inventory.remove_item(self, Item)

    def use_item(self, data):
        for item_ in self.inventory:
            if item_.guid == data['guid']:
                item_.use()
                break

    def unuse_item(self, data):
        for item_ in self.inventory:
            if item_.guid == data['guid']:
                item_.unuse()

    def use_weapon(self, ItemClass):
        self.activeWeapons.append(ItemClass)
        self.ship['cpuUsed'] += ItemClass.cpu

    def unuse_weapon(self, ItemClass):
        self.activeWeapons.remove(ItemClass)
        self.ship['cpuUsed'] -= ItemClass.cpu

    def use_device(self, ItemClass):
        self.activeDevices.append(ItemClass)

    def unuse_device(self, ItemClass):
        self.activeDevices.remove(ItemClass)

    def replace_engine(self, ItemClass):
        if self.engine:
            self.engine.inUsing = False
            self.inventory.append(self.engine)
        self.engine = ItemClass
        self.engine.inUsing = True
        self.inventory.remove(ItemClass)

    def use_droid(self, item_):
        self.droids.append(item_ - 1)
        self.ControlUsed += item_.Control
        self.ControlLeft -= item_.Control

    def unuse_droid(self, item_):
        self.droids.remove(item_)
        self.ControlUsed -= item_.Control
        self.ControlLeft += item_.Control

    def unuse_droid_all(self):
        self.droids = []
        self.ControlUsed = 0
        self.ControlLeft = self.skills['Control']


    def drop_item(self, data):
        for item_ in self.inventory:
            if item_.guid == data['guid']:
                item_.drop(data['count'])
                break

    def device_clicked(self, data):
        if self.ship["deviceSlots"] > self.cnt_active_device:
            for item_ in self.activeDevices:
                if data["guid"] == item_.guid:
                    item_.clicked(data)
                    break
