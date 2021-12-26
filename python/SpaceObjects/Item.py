from ..cfg.cfg_sell_buy import cfg_sell_buy
from ..Static.ParseXml import item_id
from python.BaseClass import SpaceObject
import uuid
from ..Static.TypeStr.PlayerSkillTypeStr import PlayerSkillTypeStr

class Item(SpaceObject):
    guid: bytes
    cost: int
    inUsing: bool
    classNumber: int

    def __init__(self, Game, classNumber, OwnerClass, wear=None):
        data = item_id(classNumber)
        data['id'] = OwnerClass.id
        self.Owner = OwnerClass
        super().__init__(Game, data)
        self.guid = uuid.uuid4().bytes
        self.cost = data['cost']
        self.inUsing = data['inUsing']
        self.classNumber = data['classNumber']
        self.level = data['level']
        if wear:
            self.wear = wear
        else:
            self.wear = 1 #data['wear'] # count or fix
        self.restrictions = None if not 'restrictions' in data else data['restrictions']['data']
        self.satisfying = self.get_satisfying


    @property
    def get_satisfying(self):
        if not self.restrictions or str(type(self.Owner)) == "<class 'python.SpaceObjects.Planet.Planet'>":
            return True
        skills = self.Owner.skills
        SkillTypeStr = PlayerSkillTypeStr()
        for skill in self.restrictions:
            if skills[SkillTypeStr.get_str(skill['valueType'])] != skill['Value']:
                self.satisfying = False
                break



    def sell(self, PlanetClass, count):
        if self.wear - count >= 0:
            self.wear -= count
            self.Owner.cash += int(self.cost * count * cfg_sell_buy(self.Owner.skills['Trading']).coef_sell)
            PlanetClass.inventory.append(Item(self.Game, self.classNumber, PlanetClass, count))
            print(self.cost)
            print(cfg_sell_buy(self.Owner.skills['Trading']).coef_sell)
            if self.wear == 0:
                self.Owner.inventory.remove(self)

    def buy(self, PlayerClass, count):
        print(PlayerClass.cash, self.cost, count)
        if PlayerClass.cash - self.cost * count > 0:
            if self.wear - count >= 0:
                self.wear -= count
                print(self.cost)
                print(cfg_sell_buy(PlayerClass.skills['Trading']).coef_buy)
                PlayerClass.cash -= int(self.cost * count * cfg_sell_buy(PlayerClass.skills['Trading']).coef_buy)
                PlayerClass.inventory.append(Item(self.Game, self.classNumber, PlayerClass, count))
                if self.wear == 0:
                    self.Owner.inventory.remove(self)

    def use(self):
        print(self.restrictions)
        # print
        # self.Owner

