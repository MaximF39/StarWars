import copy

from python.Static.ParseJson import item_id
from python.Base.SpaceObject.MovableSpaceObject import MovableSpaceObject
import uuid

from python.Static.Type.ShopType import ShopType
from python.Static.TypeStr.PlayerSkillTypeStr import PlayerSkillTypeStr
if False:
    from python.Player.Player import Player
    from python.StarWars import StarWars

class BaseItem(MovableSpaceObject):
    restrictions: list
    count: int
    mod: str # q | noq
    def __init__(self, Game, classNumber, Owner, count):
        MovableSpaceObject.__init__(self, Game, self.get_data(classNumber, count))
        self.Owner:"Player" = Owner
        self.Game:"StarWars" = Game
        self.satisfying = self.get_satisfying
        self.inUsing = False
        self.init_guid()
        if hasattr(self, 'restrictions'):
            self.restrictions = self.restrictions['data']
        if hasattr(self, 'effects'):
            self.effects = self.effects['data']

    def ItemForPlayer(self, Player):
        Fake = copy.copy(self)
        Fake.new_owner(Player)
        return Fake

    @staticmethod
    def get_data(classNumber, count):
        return item_id(classNumber, count)

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
        if self.Owner.__name__ == 'Planet':
            if self.classNumber in self.Owner.default_shop:
                return True

    @property
    def get_satisfying(self):
        return True
        if not hasattr(self, "restrictions") or not self.Owner or self.Owner.__name__ == 'Planet':
            return True
        skills = self.Owner.skills
        SkillTypeStr = PlayerSkillTypeStr()
        for skill in self.restrictions:
            match skill["type"]:
                case 2:
                    if skill['Value'] > skills[SkillTypeStr.get_str(skill['valueType'])]:
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
        Player.PacMan.tradingItems(ShopType.InventoryShop)
        Player.PacMan.updateValue(9)

    def __sub__(self, other):
        if self.count - other >= 0:
            self._here_type(other, int())
            self.count -= other
            class_ = self.copy_class()
            class_.count = other
            if self.count == 0:
                self.Owner.remove_item(self)
            return class_
        else:
            raise NotImplementedError('Почему число отрицательное шмоток?')

    def __add__(self, other):
        self._here_type(other, self)
        self.count += other.count
        return self

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

