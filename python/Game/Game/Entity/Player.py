from typing import final

from python.Game._Component.Body.B_Entity.B_Statistics.B_Experience import Experience
from python.Packages.PackagesPlayer import PackagesPlayer
from python.Game._Component.Body.B_Entity.B_Statistics import B_Status
from python.Game._Component.Body import Rating
from python.Game._Component.Event.E_Entity.E_Player.E_Skills import E_Skills, E_Player

from python.Game._Component.Event.E_Detail.E_Cash import E_Cash

from python.Game._Component.Body.B_Entity.Ship import Ship
from python.Database.Database import DataBase
from ..SpaceObjects.Item import item
from ..._Component.Body.B_Entity import Entity, B_Statistics
from python.Game.Game.SpaceObjects.Location import Location
from python.Static.Type.Package.T_ServerRequest import T_ServerRequest
from python.Config.CFG_Player.cfg_cost_reset_skills import get_cost_reset_skills
from python.Config.CFG_Player.Statistics.cfg_level import coef_exp_by_device, coef_exp_by_weapon
from python.Config.CFG_Player.Statistics.cfg_rating import get_rating_for_level, remove_dead_rating_player, coef_rating_by_device, \
    coef_rating_by_weapon
from python.Config.CFG_Player.Statistics.cfg_status import coef_status_by_device, coef_status_by_weapon
from python.Static.Type.Keys import Keys


@final
class Player(PackagesPlayer, E_Player, B_Statistics):
    cnt_active_device: int
    angar: list
    Location: Location
    clan_id: int
    count_reset_skills: int
    login: str
    engineId: int
    Packages = None
    clan:dict
    def __init__(self, Game, dict_):
        self.droids = []
        super().__init__(Game, dict_)
        E_Player.__init__(self)
        B_Statistics.__init__(self)
        self.team = -1
        self.cnt_active_device = 0
        self.expForFirstSkillLevel = 100
        self.clan_id = self.clan[Keys.id]
        if hasattr(self, "engineId"):
            self.engine = item(self.engineId, 1000, self.Game, self)
        else:
            self.engine = item(14, 1000, self.Game, self)
        if self.clan_id:
            if not hasattr(self.Game, f"Clan_{self.clan_id}"):
                self.Game.create_clan(self.clan_id)
            self.Clan = getattr(self.Game, f"Clan_{self.clan_id}")

    def update(self):
        pass
        # ThreadBase.start_update(self, self.__to_save_db, update_player_db)

    def change_ship(self, ship_id):
        for ship in self.angar:
            if ship.class_number == ship_id:
                Ship.__init__(self, self.Game, {'shipClass': ship_id})
                self.Packages.SendPacMan(T_ServerRequest.PLAYER_SHIP)

    @property
    def __name__(self):
        return self.__class__.__name__

    def reset_skills(self):
        E_Cash.remove_cash(self, get_cost_reset_skills(self.count_reset_skills))
        self.reset_skills(self)
        self.Packages.PacMan(T_ServerRequest.PLAYER_SKILLS)

    def kill_weapon(self, Whom):
        self.get_value_for_kill(Whom, coef_exp=coef_exp_by_weapon,
                                coef_status=coef_status_by_weapon,
                                coef_rating=coef_rating_by_weapon, )
        self.Location.kill(Whom)

    def kill_device(self, Whom):
        self.get_value_for_kill(Whom, coef_exp=coef_exp_by_device,
                                coef_status=coef_status_by_device,
                                coef_rating=coef_rating_by_device)
        self.Location.kill(Whom)

    def get_value_for_kill(self, Whom, *, coef_exp, coef_status, coef_rating):
        if hasattr(Whom, "level"):
            level = Whom.level
        else:
            level = 1
        Experience.get_experience_for_kill(self, Whom, coef_exp, level)
        Rating.get_rating_for_kill(self, Whom, coef_rating)
        B_Status.get_status_for_kill(self, Whom, coef_status)

    def dead(self, Whom):
        Rating.sub_rating(self, remove_dead_rating_player(Whom))
        Entity.dead(self)

    def new_level(self):
        Rating.get_rating(self, get_rating_for_level)
        E_Skills.add_skills(self)

    def __to_save_db(self):
        DataBase().save_player(self)

    def exit_player(self):
        print("delete player class")
        if self.SpaceObject is None:
            self.SpaceObject = self.Location
        self.SpaceObject.exit_entity(self)
        self.__to_save_db()
