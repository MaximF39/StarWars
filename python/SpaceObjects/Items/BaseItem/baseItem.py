import copy

from python.Static.ParseXml import item_id
import uuid

class baseItem:

    def __init__(self, Game, classNumber, OwnerClass):
        self.Owner = OwnerClass
        self.Game = Game
        data = item_id(classNumber)
        self.type = data['Types']
        self.classNumber = data['classNumber']
        self.level = data['level']
        self.guid = uuid.uuid4().bytes
        self.size = data['size']
        self.cost = data['cost']
        self.restrictions = None if not 'restrictions' in data else data['restrictions']['data']
        self.satisfying = self.get_satisfying
        self.inUsing = False

    def ItemForPlayer(self, PlayerClass):
        FakeClass = copy.copy(self)
        FakeClass.Owner = PlayerClass
        FakeClass.satisfying = FakeClass.get_satisfying
        return FakeClass
