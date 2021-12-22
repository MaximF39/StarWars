from . import BasePlayer
from ..cfg.cfg_level import cfg_level
from ..cfg.cfg_status import cfg_status
import json
import ast

class Player(BasePlayer):
    def __init__(self, Game, dict_):
        super().__init__(Game, dict_)
        self.ship = self.ship
        self.freeSkills = dict_['free_skills']
        self.deleteEnqueued = dict_['deleteEnqueued']
        self.canDelete = dict_['canDelete']
        self.logged = dict_['logged']
        self.clan = dict_["clan_id"]
        self.PlayerRelation = dict_['PlayerRelation']
        self.rating = dict_['rating']
        self.cash = dict_['credit']
        self.bonus = dict_['bonus']
        self.role = dict_['role']
        self.expSkillGrowCoef = dict_["expSkillGrowCoef"]
        self.expSkillReduserCoef = dict_["expSkillReduserCoef"]
        self.clanRequestStatus = dict_["clanRequestStatus"]
        self.clanJoinRequestStatus = dict_['clanJoinRequestStatus']
        self.mov_x = self.target_x
        self.mov_y = self.target_y
        self.expForNext = self._get_exp_for_next_level()
        self.expForFirstSkillLevel= self._get_exp_for_next_status()
        self.droid = []
        self.set_space_object_on_location(self.location)

    def use_droid(self):
        self.droid.append({})

    def _get_exp_for_next_level(self):
        return cfg_level[self.level + 1]

    def _get_exp_for_next_status(self):
        return cfg_status[self.status + 1]

