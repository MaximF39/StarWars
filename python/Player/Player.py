import math
from typing import Match

from ..SpaceObjects.Item import item
from ..Packages.PackagesManager import PackagesManager
from . import BasePlayer
from ..Utils.ThreadBase import ThreadBase
from ..cfg.cfg_player import cfg_level
from ..cfg.cfg_player import cfg_status
import json
import ast
from ..cfg.cfg_const import cfg_const
from ..cfg.cfg_trading import cfg_trading


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
        self.expForFirstSkillLevel = self._get_exp_for_next_status()
        self.engine = None
        self.droid = []

    def commitSkills(self, dict_: dict):  # name : append count
        for k, v in dict_.items():
            if self.freeSkills - v >= 0 and self.skills[k] + v < 13:
                self.freeSkills -= v
                self.skills[k] += v

    def sellItem(self, data):
        for item_ in self.inventory:
            if item_.guid == data['guid']:
                if item_.wear >= data['count']:
                    if item_.count == 1:
                        self.cash += int(item_.cost * 1 * cfg_trading(self.skills['Trading']).coef_sell)
                    else:
                        self.cash += int(item_.cost * data['count'] * cfg_trading(self.skills['Trading']).coef_sell)
                    item_.sell(self.SpaceObject, data['count'], self.Game)
                break

    def add_item(self, item_):
        self.inventory.append(item_)

    def buyItem(self, data):
        for item_ in self.SpaceObject.inventory:
            if item_.guid == data['guid']:
                if self.cash >= item_.get_cost(data['count']) and item_.wear >= data['count']:
                    if item_.count == 1:
                        self.cash -= int(item_.cost * 1 * cfg_trading(self.skills['Trading']).coef_buy)
                    else:
                        self.cash -= int(item_.cost * data['count'] * cfg_trading(self.skills['Trading']).coef_buy)

                    item_.buy(self, data['count'], self.Game)
                break

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
        raise 'Надо сделать'
        Item_ = item(self.Game, dict_["classNumber"], self, )
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

    def hyperJump(self, id_location, cost_jump=0):
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

    def unuse_weapon(self, ItemClass):
        self.active_weapons.remove(ItemClass)
        self.ship['cpuUsed'] -= ItemClass.cpu

    def use_device(self, ItemClass):
        self.active_devices.append(ItemClass)
        # self.inventory.remove(ItemClass)

    def unuse_device(self, ItemClass):
        self.active_devices.remove(ItemClass)

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
        if self.cnt_active_device > self.ship["deviceSlots"]:
            for item in self.active_devices:
                if data["guid"] == item.guid:
                    item.clicked()
                    break

    @property
    def __name__(self):
        return self.__class__.__name__

    def add_effect(self, effect):
        pass