from python.Base.Event.PlanetEvent.TradeEvent import TradeBase
from python.Base.Inventory.Inventory import Inventory
from ..Base.BaseItem.BaseItem import BaseItem
from python.Base.Player.Experience import Experience
from python.Base.Player.Packages import Packages
from python.Base.Player.Status import Status
from ..Base.BasePlayer.Rating import Rating
from ..Base.Event.DroidEvent import DroidEvent
from ..Base.Event.PlanetEvent.PlanetEvent import PlanetEvent

from ..Base.Player.Skills import Skills
from python.Base.BasePlayer.Ship import Ship
from ..SpaceObjects.Item import item
from python.Base.BasePlayer.BasePlayer import BasePlayer
from python.SpaceObjects.Location import Location


class Player(BasePlayer, TradeBase, Skills, Status, Experience, Rating, DroidEvent, PlanetEvent):
    cnt_active_device: int
    activeWeapons: list[BaseItem]
    activeDevices: list[BaseItem]
    angar: list
    Location: Location
    clanId: int
    count_reset_skills: int
    login: str
    engineId: int

    def __init__(self, Game, dict_):
        BasePlayer.__init__(self, Game, dict_)
        Inventory.__init__(self)
        DroidEvent.__init__(self)
        Skills.__init__(self)
        self.team = -1
        self.cnt_active_device = 0
        self.expForFirstSkillLevel = 100
        # self.angar.append(FakeShip(self.Game, self.ship['classNumber']))
        self.engine = item(self.engineId, 1000, self.Game, self)
        if self.clanId:
            if not hasattr(self.Game, f"Clan_{self.clanId}"):
                self.Game.create_clan(self.clanId)
            self.Clan = getattr(self.Game, f"Clan_{self.clanId}")

    def init(self):
        self.Packages = Packages(self)
        # self.Packages.init()
        self.Packages.send_entry_packages()

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


