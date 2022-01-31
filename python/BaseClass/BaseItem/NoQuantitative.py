import copy
from python.Static.Type.ShopType import ShopType
from python.Static.TypeStr.PlayerSkillTypeStr import PlayerSkillTypeStr
from python.Packages.PackagesManager import PackagesManager
from python.BaseClass.BaseItem.BaseItem import BaseItem

class NoQuantitative(BaseItem):
    fullRepair = 1000

    def __init__(self, Game, classNumber, Owner, data):
        super().__init__(Game, classNumber, Owner, data)
        self.stability = self.fullRepair
        self.repair_cost = self.cost / 500
        self.count = 1
        self.mod = 'noq'

    def add_inventory(self):
        pass

    def get_size(self, count=None):
        return self.size

    def get_cost(self, count=None):
        return self.cost

    def create_class(self, Player, count=None):
        class_ = copy.copy(self)
        class_.new_owner(Player)
        return class_

    def buy(self, Player, count, Game):
        self.Game = Game
        self.separation(Player, count)

        PacMan = PackagesManager(Player.id, self.Game)
        PacMan.tradingItems(ShopType.InventoryShop)
        PacMan.updateValue(9)

    def sell(self, Planet, count, Game):
        self.Game = Game
        self.separation(Planet)

        PacMan = PackagesManager(self.Owner.id, self.Game)
        PacMan.tradingItems(ShopType.InventoryShop)
        PacMan.updateValue(9)

    @property
    def get_wear(self):
        return self.stability

    @property
    def get_satisfying(self):
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


    def separation(self, Whom, count=None):
        Whom.add_item(self.create_class(Whom))
        self.Owner.remove_item(self)

    def drop(self, count=None):
        self.x = self.Owner.x
        self.y = self.Owner.y
        self.separation(self.Owner.Location)

        PacMan = PackagesManager(self.Owner.id, self.Game)
        PacMan.items()

    def repair(self):
        if self.Owner.cash > (self.fullRepair - self.stability) * self.repair_cost:
            self.stability = self.fullRepair
            self.Owner.cash -= (self.fullRepair - self.stability) * self.repair_cost
        else:
            repair_count = self.Owner.cash // self.repair_cost
            self.stability += repair_count
            self.Owner.cash = 0
