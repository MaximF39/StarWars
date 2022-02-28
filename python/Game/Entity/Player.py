from typing import final

from python.Base.Event.E_Planet.E_Trade import E_Trade
from python.Base.Inventory.Inventory import Inventory
from python.Base.Player.Statistics.Experience import Experience
from python.Base.Player.Packages import Packages
from python.Base.Player.Statistics.Status import Status
from python.Base.Player.Statistics.Rating import Rating
from python.Base.Event.E_Skills import E_Skills

from python.Base.Event.E_Ship.E_Droid import E_Droid
from python.Base.Event.E_Cash import E_Cash
from python.Base.Event.E_Planet.E_Planet import E_Planet

from python.Base.B_Player.Ship import Ship
from python.DataBase.Database import DataBase
from ..SpaceObjects.Item import item
from python.Base.B_Player.B_Player import B_Player
from python.Game.SpaceObjects.Location import Location
from python.Static.Type.Package.T_ServerRequest import T_ServerRequest
from python.Config.CFG_Player.cfg_cost_reset_skills import get_cost_reset_skills
from python.Config.CFG_Player.Statistics.cfg_level import coef_exp_by_device, coef_exp_by_weapon
from python.Config.CFG_Player.Statistics.cfg_rating import get_rating_for_level, remove_dead_rating_player, coef_rating_by_device, \
    coef_rating_by_weapon
from python.Config.CFG_Player.Statistics.cfg_status import coef_status_by_device, coef_status_by_weapon


@final
class Player(B_Player, E_Trade, E_Skills,  E_Planet, E_Cash, Status, Experience, Rating):
    cnt_active_device: int
    angar: list
    Location: Location
    clanId: int
    count_reset_skills: int
    login: str
    engineId: int
    Packages = None
    clan:dict
    def __init__(self, Game, dict_):
        B_Player.__init__(self, Game, dict_)
        Inventory.__init__(self)
        E_Droid.__init__(self)
        E_Skills.__init__(self)
        self.team = -1
        self.cnt_active_device = 0
        self.expForFirstSkillLevel = 100
        self.clanId = self.clan['id']
        if hasattr(self, "engineId"):
            self.engine = item(self.engineId, 1000, self.Game, self)
        else:
            self.engine = item(14, 1000, self.Game, self)
        if self.clanId:
            if not hasattr(self.Game, f"Clan_{self.clanId}"):
                self.Game.create_clan(self.clanId)
            self.Clan = getattr(self.Game, f"Clan_{self.clanId}")

    def update(self):
        pass
        # ThreadBase.start_update(self, self.__to_save_db, update_player_db)

    def init(self):
        self.Packages = Packages(self)
        self.Packages.init()

    def change_ship(self, ship_id):
        for ship in self.angar:
            if ship.classNumber == ship_id:
                Ship.__init__(self, self.Game, {'shipClass': ship_id})
                self.Packages.SendPacMan(T_ServerRequest.PLAYER_SHIP)

    def hyper_jump(self, locationId):
        B_Player.hyper_jump(self, locationId)
        self.Packages.hyper_jump()

    @property
    def __name__(self):
        return self.__class__.__name__

    def set_space_object(self, SpaceObject):
        self.SpaceObject = SpaceObject
        self.Packages.set_space_object()

    def reset_skills(self):
        self.remove_cash(get_cost_reset_skills(self.count_reset_skills))
        E_Skills.reset_skills(self)
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
        Status.get_status_for_kill(self, Whom, coef_status)

    def dead(self, Whom):
        Rating.sub_rating(self, remove_dead_rating_player(Whom))
        B_Player.dead(self)

    def new_level(self):
        Rating.get_rating(self, get_rating_for_level)
        E_Skills.add_skills(self)

    def __to_save_db(self):
        DataBase().save_player(self.__dict__)

    def __del__(self):
        self.__to_save_db()
