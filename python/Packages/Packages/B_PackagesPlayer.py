from python.Game import Entity
from python.Packages.PackagesManager import PackagesManager
from python.Static.Type.Package.T_ServerRequest import T_ServerRequest
from python.Static.Type.Package.T_UpdateValue import T_UpdateValue

class B_PackagesPlayer(Entity):

    def __init__(self, Game, dict_: dict):
        super().__init__(Game, dict_)
        self.PacMan = PackagesManager(self)

    def init(self):
        self.send_entry_packages()

    def message(self, Player, data):
        self.PacMan.message(Player, data)

    def SendPacMan(self, *PackagesNumber):
        if not hasattr(self, 'PacMan'):
            self.PacMan = PackagesManager(self)
        for PackageNumber in PackagesNumber:
            self.PacMan.processPackages(PackageNumber)

    def updateValues(self, *updateNumbers):
        for updateNumber in updateNumbers:
            self.PacMan.updateValue(updateNumber)

    def send_entry_location(self):
        self.SendPacMan(
            T_ServerRequest.LOCATION_SYSTEM,
            T_ServerRequest.ACTIVE_WEPONS,
            T_ServerRequest.ACTIVE_DEVICES,
            T_ServerRequest.CLAN,
            T_ServerRequest.SHIPS_POSITION,
            T_ServerRequest.SHIPS_STASE,
            T_ServerRequest.HIDE_SHIP,
        )

    def send_entry_packages(self):
        self.__base_send_entry_packages()

    def hyper_jump(self, Location):
        super().hyper_jump(Location)
        self.SendPacMan(
            T_ServerRequest.SHIPS_POSITION,
            T_ServerRequest.SHIPS_STASE,
            T_ServerRequest.SHIP,
            T_ServerRequest.PLAYER_SHIP,
            T_ServerRequest.LOCATION_SYSTEM,
            T_ServerRequest.ACTIVE_DEVICES,
            T_ServerRequest.ACTIVE_WEPONS,)

    def set_space_object(self, SpaceObject):
        super().set_space_object(SpaceObject)
        match self.SpaceObject.__class__.__name__:
            case "DB_Planet" | "Hive" | "Repository":
                self.SendPacMan(T_ServerRequest.LOCATION_PLANET)
            case "AsteroidBelt":
                self.SendPacMan(T_ServerRequest.LOCATION_PLANET)
            case "Location" | "Portal":
                self.SendPacMan(T_ServerRequest.LOCATION_SYSTEM)

    def __base_send_entry_packages(self):

        entry_packs = (
            T_ServerRequest.VERSION,
            T_ServerRequest.ONLINE,
            T_ServerRequest.TOP_LIST,
            T_ServerRequest.TOP_CLANS_LIST,
            T_ServerRequest.TOP_RATING_LIST,
            T_ServerRequest.WEAPONS_PARAMETERS,
            T_ServerRequest.AMMOS_PARAMETERS,
            T_ServerRequest.RESOURCE_PARAMETERS,
            T_ServerRequest.ENGINES_PARAMETERS,
            T_ServerRequest.DEVICE_PARAMETERS,
            T_ServerRequest.DROID_PARAMETERS,
            T_ServerRequest.MAP,
            T_ServerRequest.SHIP_PARAMETERS,
            T_ServerRequest.LOGGED,
            T_ServerRequest.PLAYER,
            T_ServerRequest.PLAYER_SHIP,
            T_ServerRequest.TO_GAME,
            T_ServerRequest.LOCATION_SYSTEM,
            T_ServerRequest.ACTIVE_WEPONS,
            T_ServerRequest.ACTIVE_DEVICES,
            T_ServerRequest.CLAN,
            T_ServerRequest.SHIPS_POSITION,
            T_ServerRequest.SHIPS_STASE,
            T_ServerRequest.HIDE_SHIP,
        )

        
        self.SendPacMan(*entry_packs)

        update_values = (
            T_UpdateValue.PlayerClanPoints,
            T_UpdateValue.Bonuses,
            T_UpdateValue.PlayerCash,
            T_UpdateValue.ControlUsed,
            T_UpdateValue.ControlLeft,
            T_UpdateValue.HyperRadius,
            T_UpdateValue.HyperCost,
        )
        self.updateValues(*update_values)