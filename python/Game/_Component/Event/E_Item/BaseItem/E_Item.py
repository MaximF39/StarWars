import copy
import uuid

from python.Static.Type.SpaceObject.T_Shop import T_Shop


class E_Item:
    restrictions: list
    count: int
    mod: str  # q | noq
    wear: int
    cost: int
    guid: object
    in_using = False

    def ItemForPlayer(self, Player):
        Fake = copy.copy(self)
        Fake.new_owner(Player)
        return Fake

    def new_owner(self, Owner, count=None):
        self.Owner = Owner
        self.get_satisfying

    def transfer(self, Whom):
        self.Owner.remove_item(self)
        self.Owner = Whom
        self.Owner.add_item(self)

    def set_x_y_owner(self):
        self.x = self.Owner.x
        self.y = self.Owner.y

    def good_trade(self, Player):
        Player.SendPacMan.tradingItems(T_Shop.InventoryShop)
        Player.Packages.updateValue(9)

    def drop(self, count):
        raise NotImplementedError()
