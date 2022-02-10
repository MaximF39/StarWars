from python.Packages.PackagesManager import PackagesManager
from python.Static.Type.ServerRequest import ServerRequest
from python.Static.Type.ObjectToReachType import ObjectToReachType

class Packages:
    PacMan: PackagesManager

    def __init__(self, Player):
        self.Player = Player
        self.PacMan: PackagesManager = PackagesManager(Player)

    def init(self):
        self.PacMan = self.Packages.PacMan

    def send_entry_packages(self):
        # if not self.SpaceObject:
        entry_packs = (
            ServerRequest.VERSION,
            ServerRequest.ONLINE,
            ServerRequest.TOP_LIST,
            ServerRequest.TOP_CLANS_LIST,
            ServerRequest.TOP_RATING_LIST,
            ServerRequest.WEAPONS_PARAMETERS,
            ServerRequest.AMMOS_PARAMETERS,
            ServerRequest.RESOURCE_PARAMETERS,
            ServerRequest.ENGINES_PARAMETERS,
            ServerRequest.DEVICE_PARAMETERS,
            ServerRequest.DROID_PARAMETERS,
            ServerRequest.MAP,
            ServerRequest.SHIP_PARAMETERS,
            ServerRequest.LOGGED,
            ServerRequest.PLAYER,
            ServerRequest.PLAYER_SHIP,
            ServerRequest.TO_GAME,
            ServerRequest.LOCATION_SYSTEM,
            ServerRequest.ACTIVE_WEPONS,
            ServerRequest.ACTIVE_DEVICES,
            ServerRequest.CLAN,
            ServerRequest.SHIPS_POSITION,
            ServerRequest.SHIPS_STASE,
            ServerRequest.HIDE_SHIP,
        )
        update_value = (
            (ServerRequest.UPDATE_VALUE, 3),
            (ServerRequest.UPDATE_VALUE, 13),
            (ServerRequest.UPDATE_VALUE, 9),
            (ServerRequest.UPDATE_VALUE, 10),
            (ServerRequest.UPDATE_VALUE, 11),
            (ServerRequest.UPDATE_VALUE, 14),
            (ServerRequest.UPDATE_VALUE, 15),
        )

        for pack in entry_packs:
            self.PacMan.processPackages(pack)
        for pack in update_value:
            self.PacMan.processPackages(*pack)

    def hyper_jump(self):
        self.PacMan.shipsPosition()
        self.PacMan.shipsState()
        self.PacMan.ship()
        self.PacMan.playerShip()
        self.PacMan.locationSystem()
        self.PacMan.activeDevices()
        self.PacMan.activeWeapons()

    def set_space_object(self):
        match self.Player.SpaceObject.__name__:
            case "Planet" | "Hive" | "Repository":
                self.PacMan.locationPlanet()
            case "AsteroidBelt":
                pass
            case "Portal":
                pass

    def trading_items(self):
        self.PacMan.tradingItems()

    def change_ship(self):
        self.PacMan.playerShip()


