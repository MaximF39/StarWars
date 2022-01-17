import copy

from python.Static.ParseXml import item_id
from python.BaseClass.MovableSpaceObject import MovableSpaceObject
import uuid

class BaseItem(MovableSpaceObject):

    def __init__(self, Game, classNumber, Owner, data):
        super().__init__(Game, data)
        self.Player = Owner
        self.Game = Game
        self.data = item_id(classNumber)
        data = item_id(classNumber)
        self.classNumber = data['classNumber']
        self.level = data['level']
        self.cost = data['cost']
        self.restrictions = None if not 'restrictions' in data else data['restrictions']['data']
        self.satisfying = self.get_satisfying
        self.inUsing = False

    def ItemForPlayer(self, Player):
        Fake = copy.copy(self)
        Fake.get_owner(Player)
        return Fake

    def get_owner(self, class_, count=None):
        self.Player = class_
        self.get_satisfying

    @property
    def get_guid(self):
        return uuid.uuid4().bytes