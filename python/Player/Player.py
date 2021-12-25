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
        self.clan = dict_["clan_id"]
        self.PlayerRelation = dict_['PlayerRelation']
        self.rating = dict_['rating']
        self.cash = dict_['credit']
        self.bonus = dict_['bonus']
        self.repository = dict_['repository']
        self.role = dict_['role']
        self.expSkillGrowCoef = dict_["expSkillGrowCoef"]
        self.expSkillReduserCoef = dict_["expSkillReduserCoef"]
        self.clanRequestStatus = dict_["clanRequestStatus"]
        self.clanJoinRequestStatus = dict_['clanJoinRequestStatus']
        self.mov_x = self.target_x
        self.mov_y = self.target_y
        self.pirateStatus = 0 if self.pointStatus > 0 else self.pointStatus
        self.policeStatus = 0 if 0 > self.pointStatus else self.pointStatus
        self.forNextLevel = int(cfg_level[self.level + 1])
        self.expForFirstSkillLevel= self._get_exp_for_next_status()
        self.droid = []
        self.send_info_location()

    def upgrade(self):
        self.start_update('synchron_coord_on_space_object', 1)
    #     self.start_update('sendPackagesUpdate', 1)
    #
    #
    # @ThreadBase.end_thread
    # def sendPackagesUpdate(self):
    #     if not self.on_planet:
    #         PacMan = PackagesManager(self.id, self.Game)
    #         PacMan.locationSystem()

    def send_info_location(self):
        getattr(self.Game, f'Location_{self.location}').set_player(self)

    def commitSkills(self, dict_:dict): # name : append count
        for k, v in dict_.items():
            if self.freeSkills - v > 0 and self.skills[k] + v < 13:
                self.freeSkills -= v
                self.skills[k] += v

    def buyItemByBonuses(self, dict_):
        from ..Static.ParseXml import item_id
        item = item_id(dict_['id'])
        bonus = item['cost'] / 1000
        if self.bonus - bonus > 0:
            pass

    def repair(self):
        self.health = self.ship['maxHealth']

    @ThreadBase.end_thread
    def synchron_coord_on_space_object(self):
        if self.on_planet:
            self.x = self.on_planet.x
            self.y = self.on_planet.y

    def hyperJump(self, id_location):
        getattr(self.Game, f"Location_{self.location}").remove_player(self)
        self.location = id_location
        getattr(self.Game, f"Location_{self.location}").set_player(self)
        PackagesManager(self.id, self.Game).locationSystem()

    def restoreEnergy(self):
        self.energy = self.ship['maxEnergy']

    def use_droid(self):
        self.droid.append({})

    def _get_exp_for_next_status(self):
        return cfg_status[self.status + 1]

