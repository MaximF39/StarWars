from python.Packages.PackagesManager import PackagesManager
from python.Static.Type.Package.T_ServerRequest import T_ServerRequest
from python.Static.Type.Package.T_UpdateValue import T_UpdateValue

class Packages:

    def __init__(self, Player):
        self.Player = Player
        self.PacMan: PackagesManager = PackagesManager(Player)

    def init(self):
        self.send_entry_packages()

    def message(self, Player, data):
        self.PacMan.message(Player, data)

    def SendPacMan(self, *PackagesNumber):
        for PackageNumber in PackagesNumber:
            self.PacMan.processPackages(PackageNumber)

    def updateValues(self, *updateNumbers):
        for updateNumber in updateNumbers:
            print(updateNumber)
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

    def send_entry_space_object(self):
        entry_packs = ()
        for pack in entry_packs:
            self.PacMan.processPackages(pack)

    def send_entry_packages(self):
        self.__base_send_entry_packages()
        if hasattr(self, "SpaceObject"):
            self.send_entry_space_object()
        else:
            self.send_entry_location()

    def hyper_jump(self):
        self.PacMan(
            T_ServerRequest.SHIPS_POSITION,
            T_ServerRequest.SHIPS_STASE,
            T_ServerRequest.SHIP,
            T_ServerRequest.PLAYER_SHIP,
            T_ServerRequest.LOCATION_SYSTEM,
            T_ServerRequest.ACTIVE_DEVICES,
            T_ServerRequest.ACTIVE_WEPONS,)

    def set_space_object(self):
        match self.Player.SpaceObject.__name__:
            case "DB_Planet" | "Hive" | "Repository":
                self.SendPacMan(T_ServerRequest.LOCATION_PLANET)
            case "AsteroidBelt":
                self.SendPacMan(T_ServerRequest.LOCATION_PLANET)
            case "Portal":
                self.Player.SpaceObject._set_player(self.Player)

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
        )
        self.SendPacMan(entry_packs)

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