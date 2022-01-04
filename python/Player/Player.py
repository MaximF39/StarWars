import math

from ..SpaceObjects.Item import item
from ..Packages.PackagesManager import PackagesManager
from . import BasePlayer
from ..Utils.ThreadBase import ThreadBase
from ..cfg.cfg_level import cfg_level
from ..cfg.cfg_status import cfg_status
import json
import ast
from ..cfg.cfg_const import cfg_const

class Player(BasePlayer, ThreadBase):
    def __init__(self, Game, dict_):
        super().__init__(Game, dict_)
        self.maxSkill = cfg_const['maxSkill']
        self.freeSkills = dict_['free_skills']
        self.deleteEnqueued = dict_['deleteEnqueued']
        self.canDelete = dict_['canDelete']
        self.logged = dict_['logged']
        self.clanId = dict_["clan_id"]
        self.points = dict_['points']
        self.PlayerRelation = dict_['PlayerRelation']
        self.rating = dict_['rating']
        self.cash = dict_['credit']
        self.bonus = dict_['bonus']
        self.repository = dict_['repository']
        self.role = dict_['role']
        self.ControlUsed = 0
        self.ControlLeft = self.skills['Control']
        self.expSkillGrowCoef = dict_["expSkillGrowCoef"]
        self.expSkillReduserCoef = dict_["expSkillReduserCoef"]
        self.clanRequestStatus = dict_["clanRequestStatus"]
        self.clanJoinRequestStatus = dict_['clanJoinRequestStatus']
        self.mov_x = self.target_x
        self.mov_y = self.target_y
        self.pirateStatus = 0 if self.points > 0 else self.points
        self.policeStatus = 0 if 0 > self.points else self.points
        self.forNextLevel = int(cfg_level[self.level + 1])
        self.expForFirstSkillLevel= self._get_exp_for_next_status()
        self.engine = None
        self.droid = []
        print('sspeed', self.speed)
        print('sspeed2', self.ship['speed'])
        print('classNumber', self.classNumber)
        print('classNumber2', self.ship['classNumber'])


    def commitSkills(self, dict_:dict): # name : append count
        for k, v in dict_.items():
            if self.freeSkills - v >= 0 and self.skills[k] + v < 13:
                self.freeSkills -= v
                self.skills[k] += v

    def sellItem(self, data):
        for item_ in self.inventory:
            if item_.guid == data['guid']:
                if item_.wear >= data['count']:
                    item_.sell(self.SpaceObject, data['count'])
                break

    def buyItem(self, data):
        for item_ in self.SpaceObject.inventory:
            if item_.guid == data['guid']:
                if self.cash >= item_.get_cost(data['count']) and item_.wear >= data['count']:
                    item_.buy(self, data['count'])
                break

    def OpenShop(self, data):
        match data['type']:  # 1001 + race = shipShops
            case 10004:
                self.SpaceObject.repository(self)
            case 10005:
                self.SpaceObject.playerAngar(self)
            case 10009:
                self.SpaceObject.clanrepository(self)
            case 10002:
                self.SpaceObject.ShowShopShip(self)
            case _:
                self.SpaceObject.ShowShopItems(self)

    def buyItemByBonuses(self, dict_):
        Item_ = item(self.Game, dict_["classNumber"], self)
        bonus = Item_.cost // 1000
        if self.bonus - bonus > 0:
            self.bonus -= bonus
            self.add_item_inventory(Item_)

    def repair(self):
        self.health = self.ship['maxHealth']

    def synchron_coord_on_space_object(self):
        if self.SpaceObject:
            self.x = self.SpaceObject.x
            self.y = self.SpaceObject.y

    def hyperJump(self, id_location):
        radius = 400 * len(self.Location.planets)
        NextLocation = getattr(self.Game, f'Location_{id_location}')
        self.ObjectToReach = NextLocation
        tan = math.atan2(NextLocation.y - self.Location.y, NextLocation.x - self.Location.x)
        x = radius * math.cos(tan)
        y = radius * math.sin(tan)
        self.move(x, y)

    def get_credits(self, count):
        self.cash += count
        # self.PacMan.

    def send_credits(self, count):
        if self.cash >= count:
            self.cash -= count
            # self.PacMan.tradingCash()

    def restoreEnergy(self):
        self.energy = self.ship['maxEnergy']

    def use_item(self, data):
        for item_ in self.inventory:
            if item_.guid == data['guid']:
                item_.use()

    def unuse_item(self, data):
        for item_ in self.inventory:
            if item_.guid == data['guid']:
                item_.unuse()

    def use_weapon(self, ItemClass):
        self.active_weapons.append(ItemClass)
        self.ship['cpuUsed'] += ItemClass.cpu
        # self.inventory.remove(ItemClass)

    def unuse_weapon(self, ItemClass):
        self.active_weapons.remove(ItemClass)
        self.ship['cpuUsed'] -= ItemClass.cpu
        # self.inventory.append(ItemClass)

    def use_device(self, ItemClass):
        self.active_devices.append(ItemClass)
        # self.inventory.remove(ItemClass)

    def unuse_device(self, ItemClass):
        self.active_devices.remove(ItemClass)
        # self.inventory.append(ItemClass)

    def replace_engine(self, ItemClass):
        if self.engine:
            self.engine.inUsing = False
        self.engine = ItemClass
        self.engine.inUsing = True
        # self.inventory.remove(ItemClass)

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

