import math
from python.BaseClass.FakeShip import FakeShip
from ..BaseClass.Trade.TradeBase import TradeBase
from ..SpaceObjects.Item import item
from python.BaseClass.BasePlayer import BasePlayer
from ..Utils.ThreadBase import ThreadBase
from python.Static.cfg.cfg_player import cfg_level
from python.Static.cfg.cfg_player import cfg_status
from python.Static.cfg.shops.cfg_trading import cfg_trading
from python.Static.cfg.cfg_main import radius
from python.Packages.PackagesManager import PackagesManager
from python.Static.Type.UpdateValueType import UpdateValueType

class Player(BasePlayer, ThreadBase, TradeBase):
    points: int
    freeSkills: int
    cash: int
    bonus: int
    engine: "Item"
    cnt_active_device: int
    skills: dict
    inventory: list["Item"]
    activeWeapons: list["Item"]
    activeDevices: list["Item"]
    status: int

    def __init__(self, Game, dict_):
        super().__init__(Game, dict_)
        self.team = -1
        self.angar = []
        for shipClass in dict_['angar']:
            self.angar.append(FakeShip(self.Game, shipClass))
        self.cnt_active_device = 0
        self.ControlUsed = 0
        self.ControlLeft = self.skills['Control'] - self.ControlUsed
        self.pirateStatus = 0 if self.points > 0 else self.points
        self.policeStatus = 0 if 0 > self.points else self.points
        self.forNextLevel = int(cfg_level[self.level + 1])
        self.expForFirstSkillLevel = self._get_exp_for_next_status()
        self.droid = []

    def init(self):
        self.PacMan = PackagesManager(self.id, self.Game)

    def commitSkills(self, dict_: dict):  # name : append count
        for k, v in dict_.items():
            if self.freeSkills - v >= 0 and self.skills[k] + v < 13:
                self.freeSkills -= v
                self.skills[k] += v

    def add_item(self, item_):
        for inventory_item in self.inventory:
            if inventory_item.classNumber == item_.classNumber:
                if inventory_item.mod == 'q':
                    inventory_item + item_
                    return
        self.inventory.append(item_)

    def remove_item(self, item_):
        self.inventory.remove(item_)

    def OpenShop(self, data):
        match data['type']:
            case 1:
                self.SpaceObject.inventory_shop(self)
            case 2:
                self.SpaceObject.ship_factory(self)
            case 3:
                self.SpaceObject.ginetic_lab(self)
            case 4:
                self.SpaceObject.repository(self)
            case 5:
                self.SpaceObject.angar(self)
            case 6:
                self.SpaceObject.update_ships(self)
            case 8:
                self.SpaceObject.update_resources(self)
            case 9:
                self.SpaceObject.clan_repository(self)

    def buyItemByBonuses(self, dict_):
        Item_ = item(Game=self.Game, classNumber=dict_["classNumber"], OwnerClass=self, count=dict_['count'])
        bonus = Item_.cost // 1000
        if self.bonus - bonus >= 0:
            self.bonus -= bonus
            self.add_item_inventory(Item_)

    def repair(self):
        self.health = self.ship['maxHealth']

    def synchron_coord_on_space_object(self):
        if self.SpaceObject:
            self.x = self.SpaceObject.x
            self.y = self.SpaceObject.y

    def hyperJump(self, id_location, cost_jump=0):
        radius_ = radius * len(self.Location.planets)
        NextLocation = getattr(self.Game, f'Location_{id_location}')
        self.ObjectToReach = NextLocation
        tan = math.atan2(NextLocation.y - self.Location.y, NextLocation.x - self.Location.x)
        x = radius_ * math.cos(tan)
        y = radius_ * math.sin(tan)
        self.move(targetX=x, targetY=y)

    def get_credits(self, count):
        self.cash += count
        self.PacMan.updateValue(UpdateValueType.PlayerCash)

    def send_credits(self, count):
        if self.cash >= count:
            self.cash -= count
            self.PacMan.updateValue(UpdateValueType.PlayerCash)

    def restoreEnergy(self):
        self.energy = self.ship['maxEnergy']

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
        # self.inventory.remove(ItemClass)

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
        item_.separation(self, 1, True)
        self.ControlUsed += item_.Control
        self.ControlLeft -= item_.Control

    def unuse_droid(self, item_):
        item_.separation(self, 1)
        self.ControlUsed -= item_.Control
        self.ControlLeft += item_.Control

    def drop_item(self, data):
        for item_ in self.inventory:
            if item_.guid == data['guid']:
                item_.drop(data['count'])
                break

    def _get_exp_for_next_status(self):
        return cfg_status[self.status + 1]

    def device_clicked(self, data):
        if self.ship["deviceSlots"] > self.cnt_active_device:
            for item_ in self.activeDevices:
                if data["guid"] == item_.guid:
                    item_.clicked(data)
                    break

    @property
    def __name__(self):
        return self.__class__.__name__

    def add_effect(self, EffectClass):
        self.effects.append(EffectClass)
        self.PacMan.effectCreated(EffectClass.effect['effectType'])
        self.start_timer_update(self.remove_effect, EffectClass.effect["effectTime"], args=(EffectClass.effect["effectType"],))

    def remove_effect(self, effect_type):
        print('i send remove eff')
        for effect in self.effects:
            if effect.effectType == effect_type:
                self.effects.remove(effect)
        self.PacMan.effectRemoved(effect_type)

