import copy
from ..Packages.PackagesManager import PackagesManager
from ..cfg.cfg_sell_buy import cfg_sell_buy
from python.Static.ParseXml import item_id
import uuid
from python.Static.TypeStr.PlayerSkillTypeStr import PlayerSkillTypeStr

class Item:
    guid: bytes
    cost: int
    inUsing: bool
    classNumber: int

    def __init__(self, Game, classNumber, OwnerClass=None, count=None):
        data = item_id(classNumber)
        self.Owner = OwnerClass
        self.Game = Game
        self.type = data['Types']
        self.classNumber = data['classNumber']
        self.level = data['level']
        self.guid = uuid.uuid4().bytes
        self.OneSize = data['size']
        self.OneCost = data['cost']
        self.restrictions = None if not 'restrictions' in data else data['restrictions']['data']
        self.satisfying = self.get_satisfying
        self.count = count
        self.get_value()

    def get_value(self):
        if self.type in [2, 4, 5, 6]:
            if self.count is None:
                self.wear = 1000
                self.inUsing = True
                if self.type == 6:
                    self.satisfying = True
                else:
                    self.satisfying = self.get_satisfying
                self.size = self.OneSize
                self.cost = self.OneCost
        else:
            self.wear = self.count if self.count else 1
            self.inUsing = False
            self.satisfying = True
            self.size = self.wear * self.OneSize
            self.cost = self.wear * self.OneCost


    def FakeItem(self, PlayerClass):
        FakeItem:Item = copy.copy(self)
        FakeItem.Owner = PlayerClass
        # FakeItem.satisfying = FakeItem.get_satisfying
        return FakeItem

    @property
    def get_satisfying(self):
        # print('restr', self.restrictions)
        if self.restrictions is None or not 'level' in self.Owner.__dict__:
            return True
        skills = self.Owner.skills
        SkillTypeStr = PlayerSkillTypeStr()
        for skill in self.restrictions:
            # print('skiils', skill)
            if skill["type"] == 2 and skill['Value'] > skills[SkillTypeStr.get_str(skill['valueType'])]:
                # print(skill['type'])
                return False
            elif skill['type'] == 3 and skills["Control"] > skill['Value']:
                # print(skill['type'])
                return False
            elif skill['type'] == 4 and skill['Value'] > self.Owner.cpu:
                # print(skill['type'])
                return False
            elif skill['type'] == 5 and self.Owner.status > skill['Value']: # -3 > -2
                # print(skill['type'])
                return False
            elif skill['type'] == 6 and self.Owner.status < skill['Value']: # 3 < 2 # player < need -> False
                # print(skill['type'])
                return False
            else:
                print('Не понятный тип', skill['type'])
        return True


    def dropItem(self, count):
        pass

    def sell(self, PlanetClass, count):
        if self.wear - count >= 0:
            self.wear -= count
            self.Owner.cash += int(self.cost * count * cfg_sell_buy(self.Owner.skills['Trading']).coef_sell)
            PlanetClass.inventory.append(Item(self.Game, self.classNumber, PlanetClass, count))
            print(self.cost)
            print(cfg_sell_buy(self.Owner.skills['Trading']).coef_sell)
            if self.wear == 0:
                self.Owner.inventory.remove(self)
            PacMan = PackagesManager(self.id, self.Game)
            PacMan.tradingItems()
            PacMan.updateValue(9, self.Owner.cash)

    def buy(self, PlayerClass, count):
        print(PlayerClass.cash, self.cost, count) # TODO cost * count
        if PlayerClass.cash - self.cost * count > 0 and self.wear - count >= 0:
            self.wear -= count
            print(self.cost)
            print(cfg_sell_buy(PlayerClass.skills['Trading']).coef_buy)
            PlayerClass.cash -= int(self.cost * count * cfg_sell_buy(PlayerClass.skills['Trading']).coef_buy)
            PlayerClass.inventory.append(Item(self.Game, self.classNumber, PlayerClass, count))
            if self.wear == 0:
                self.Owner.inventory.remove(self)
            PacMan = PackagesManager(PlayerClass.id, self.Game)
            PacMan.tradingItems()
            PacMan.updateValue(9, PlayerClass.cash)

    def use(self):
        print(self.restrictions)
        # print
        # self.Owner

