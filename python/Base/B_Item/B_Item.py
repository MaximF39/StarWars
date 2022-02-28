import copy
from python.Base.SpaceObject.SpaceObject.MovableSpaceObject import MovableSpaceObject
import uuid

from python.Static.Type.SpaceObject.T_Shop import T_Shop

if False:
    from python.Game import Game


class B_Item(MovableSpaceObject):
    restrictions: list
    count: int
    mod: str  # q | noq
    wear: int
    cost: int
    guid: object

    def __init__(self, Game, data, Owner):
        MovableSpaceObject.__init__(self, Game, data)
        self.Owner: "CFG_Player" = Owner
        self.Game: "StarWars" = Game
        self.satisfying = self.get_satisfying
        self.init_guid()

    def ItemForPlayer(self, Player):
        Fake = copy.copy(self)
        Fake.new_owner(Player)
        return Fake

    @property
    def get_wear(self):
        return self.wear

    def new_owner(self, Owner, count=None):
        self.Owner = Owner
        self.get_satisfying

    def init_guid(self):
        self.guid = uuid.uuid4().bytes

    def copy_class(self):
        class_ = copy.copy(self)
        class_.init_guid()
        return class_

    def check_default_shop(self):
        if self.Owner.__name__ == 'DB_Planet':
            if self.classNumber in self.Owner.default_shop:
                return True

    @property
    def get_satisfying(self):
        return True
        if not hasattr(self, "restrictions") or not self.Owner or self.Owner.__name__ == 'DB_Planet':
            return True
        skills = self.Owner.skills
        for skill in self.restrictions:
            match skill["type"]:
                case 2:
                    if skill['Value'] > skills[skill['valueType']]:
                        return False
                case 4:
                    if skill['Value'] > self.Owner.ship['cpu']:
                        return False
                case 5:
                    if self.Owner.status > skill['Value']:  # -3 > -2 пир или коп и ниже тоже
                        return False
                case 6:
                    if self.Owner.status < skill['Value']:  # 3 < 2 # player < need -> False
                        return False
                case _:
                    print('Не понятный тип', skill['type'])
            return True

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

    @staticmethod
    def _here_type(other, type_):
        if not isinstance(other, type(type_)):
            raise TypeError('Не является классом', type(type_))

    def separation(self, Whom, count):
        raise NotImplementedError("Метод separation должен быть определён")

    def buy(self, Player, count):
        raise NotImplementedError()

    def sell(self, Planet, count):
        raise NotImplementedError()

    @property
    def get_size(self):
        raise NotImplementedError()

    def get_cost(self, count):
        raise NotImplementedError()

    def drop(self, count):
        raise NotImplementedError()
