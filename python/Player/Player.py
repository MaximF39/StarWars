import random
from typing import final

from python.Base.Event.PlanetEvent.TradeEvent import Trading
from python.Base.Inventory.Inventory import Inventory
from ..Base.BaseItem.BaseItem import BaseItem
from python.Base.Player.Experience import Experience
from python.Base.Player.Packages import Packages
from python.Base.Player.Status import Status
from ..Base.BasePlayer.Rating import Rating
from python.Base.BasePlayer.ShipEvent.DroidEvent import DroidEvent
from ..Base.Event.CashEvent import CashEvent
from ..Base.Event.PlanetEvent.PlanetEvent import PlanetEvent

from ..Base.Player.SkillsEvent import SkillsEvent
from python.Base.BasePlayer.Ship import Ship
from ..DataBase.Database import DataBase
from ..SpaceObjects.Item import item
from python.Base.BasePlayer.BasePlayer import BasePlayer
from python.SpaceObjects.Location import Location
from ..Static.cfg.cfg_player import get_cost_reset_skills
from ..Static.cfg.cfg_main import update_player_db
from ..Utils.ThreadBase import ThreadBase

@final
class Player(BasePlayer, Trading, SkillsEvent, Status, Experience, Rating, PlanetEvent, CashEvent):
    cnt_active_device: int
    activeWeapons: list[BaseItem]
    activeDevices: list[BaseItem]
    angar: list
    Location: Location
    clanId: int
    count_reset_skills: int
    login: str
    engineId: int
    Packages = None
    def __init__(self, Game, dict_):
        BasePlayer.__init__(self, Game, dict_)
        Inventory.__init__(self)
        DroidEvent.__init__(self)
        SkillsEvent.__init__(self)
        self.team = -1
        self.cnt_active_device = 0
        self.expForFirstSkillLevel = 100
        self.engine = item(self.engineId, 1000, self.Game, self)
        if self.clanId:
            if not hasattr(self.Game, f"Clan_{self.clanId}"):
                self.Game.create_clan(self.clanId)
            self.Clan = getattr(self.Game, f"Clan_{self.clanId}")

    def update(self):
        ThreadBase.start_update(self, self.__to_save_db, update_player_db)

    def init(self):
        self.Packages = Packages(self)
        self.Packages.init()

    def change_ship(self, ship_id):
        for ship in self.angar:
            if ship.classNumber == ship_id:
                Ship.__init__(self, self.Game, {'shipClass': ship_id})
                self.Packages.change_ship()

    def hyper_jump(self, locationId):
        BasePlayer.hyper_jump(self, locationId)
        self.Packages.hyper_jump()

    @property
    def __name__(self):
        return self.__class__.__name__

    def set_space_object(self, SpaceObject):
        self.SpaceObject = SpaceObject
        self.Packages.set_space_object()

    def reset_skills(self):
        self.remove_cash(get_cost_reset_skills(self.count_reset_skills))
        SkillsEvent.reset_skills(self)
        self.Packages.reset_skills()

    def kill_weapon(self, Whom):
        self.get_value_for_kill(Whom, 1)
        self.Packages.kill_weapon()

    def kill_device(self, Whom):
        self.get_value_for_kill(Whom, 0.1)
        self.Packages.kill_device()

    def get_value_for_kill(self, Whom, coef):
        if hasattr(Whom, "level"):
            level = 1
        else:
            level = Whom.level
        exp = int((Whom.health + 30 * level) * coef)
        self.get_experience(random.randint(exp, int(1.1 * exp)))
        if hasattr(Whom, "rating"):
            rating = int(Whom.rating * 0.01 * coef)
            self.get_rating(random.randint(rating, int(1.1 * rating)))
        if hasattr(Whom, "status"):
            status = int(self.status * coef)
            self.get_status(random.randint(status, int(1.1 * status)))

    def dead(self, Whom):
        Rating.sub_rating(self, Whom.rating * 0.01)
        BasePlayer.dead(self)

    def update_ship(self):
        self.PacMan.shipUpdateInfo()

    def __to_save_db(self):
        DataBase().save_player(self.__dict__)

    def __del__(self):
        self.__to_save_db()