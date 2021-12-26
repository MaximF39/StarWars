from ..SpaceObjects.Item import Item
from ..Packages.PackagesManager import PackagesManager
from . import BasePlayer
from ..MyUtils.ThreadBase import ThreadBase
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
        self.PlayerRelation = dict_['PlayerRelation']
        self.rating = dict_['rating']
        self.cash = dict_['credit']
        self.bonus = dict_['bonus']
        self.repository = dict_['repository']
        self.role = dict_['role']
        self.ControlUsed = self.skills['Control'] # - self.droid.all_control ?
        self.ControlLeft = self.skills['Control']
        self.expSkillGrowCoef = dict_["expSkillGrowCoef"]
        self.expSkillReduserCoef = dict_["expSkillReduserCoef"]
        self.clanRequestStatus = dict_["clanRequestStatus"]
        self.clanJoinRequestStatus = dict_['clanJoinRequestStatus']
        self.mov_x = self.target_x
        self.mov_y = self.target_y
        self.pirateStatus = 0 if self.point > 0 else self.point
        self.policeStatus = 0 if 0 > self.point else self.point
        self.forNextLevel = int(cfg_level[self.level + 1])
        self.expForFirstSkillLevel= self._get_exp_for_next_status()
        self.droid = []
        self.send_info_location()

    def upgrade(self):
        self.start_timer_update(self.synchron_coord_on_space_object, 1)
    #     self.start_update('sendPackagesUpdate', 1)
    #
    #
    # @ThreadBase.end_thread
    # def sendPackagesUpdate(self):
    #     if not self.on_planet:
    #         PacMan = PackagesManager(self.id, self.Game)
    #         PacMan.locationSystem()

    def send_info_location(self):
        self.Location.set_player(self)

    def commitSkills(self, dict_:dict): # name : append count
        for k, v in dict_.items():
            if self.freeSkills - v >= 0 and self.skills[k] + v < 13:
                self.freeSkills -= v
                self.skills[k] += v

    def sellItem(self, data):
        for item in self.inventory:
            if item.guid == data['guid']:
                print(self.cash)
                item.sell(self.SpaceObject, data['count'])
                print(self.cash)

    def buyItem(self, data):
        for item in self.SpaceObject.inventory:
            if item.guid == data['guid']:
                item.buy(self, data['count'])

    def buyItemByBonuses(self, dict_):
        item = Item(self.Game, dict_["classNumber"], self)
        bonus = item.cost // 1000
        if self.bonus - bonus > 0:
            self.bonus -= bonus
            self.inventory.append(item)

    def repair(self):
        self.health = self.ship['maxHealth']

    def synchron_coord_on_space_object(self):
        if self.SpaceObject:
            self.x = self.SpaceObject.x
            self.y = self.SpaceObject.y

    def hyperJump(self, id_location):
        self.Location.remove_player(self)
        self.Location = getattr(self.Game, f'Location_{id_location}')
        self.Location.set_player(self)
        PackagesManager(self.id, self.Game).locationSystem()

    def restoreEnergy(self):
        self.energy = self.ship['maxEnergy']

    def use_droid(self):
        self.droid.append({})

    def _get_exp_for_next_status(self):
        return cfg_status[self.status + 1]

