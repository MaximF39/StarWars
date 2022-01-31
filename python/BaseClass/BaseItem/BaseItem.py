import copy

from python.Static.ParseJson import item_id
from python.BaseClass.MovableSpaceObject import MovableSpaceObject
import uuid

class BaseItem(MovableSpaceObject):
    restrictions: list
    count: int

    def __init__(self, Game, classNumber, Owner, count):
        super().__init__(Game, self.get_data(classNumber, count))
        self.Owner = Owner
        self.Game = Game
        self.satisfying = self.get_satisfying
        self.inUsing = False
        self.guid = self.get_guid
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

    @property
    def get_guid(self):
        return uuid.uuid4().bytes

    @property
    def get_satisfying(self):
        raise NotImplementedError('Переопредели меня get_satisfying')

    def __sub__(self, other):
        if self.count - other >= 0:
            self._here_type(other, int())
            self.count -= other
            class_ = copy.copy(self)
            class_.guid = class_.get_guid
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
