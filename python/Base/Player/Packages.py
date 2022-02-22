from python.Packages.PackagesManager import PackagesManager
from python.Static.Type.ServerRequest import ServerRequest
from python.Static.Type.ObjectToReachType import ObjectToReachType
from python.Static.Type.UpdateValueType import UpdateValueType
from python.Static.Type.UpdateValueType import UpdateValueType

class Packages:

    def __init__(self, Player):
        self.Player = Player
        self.PacMan: PackagesManager = PackagesManager(Player)

    def init(self):
        self.PacMan = self.Packages.PacMan
        self.send_entry_packages()

    def locationSystem(self):
        self.PacMan.locationSystem()

    def locationPlanet(self):
        self.PacMan.locationPlanet()

    def kill_weapon(self):
        self.PacMan.locationSystem()

    def kill_device(self):
        self.PacMan.locationSystem()

    def reset_skills(self):
        self.PacMan.playerSkills()

    def send_entry_location(self):
        entry_packs = (
            ServerRequest.LOCATION_SYSTEM,
            ServerRequest.ACTIVE_WEPONS,
            ServerRequest.ACTIVE_DEVICES,
            ServerRequest.CLAN,
            ServerRequest.SHIPS_POSITION,
            ServerRequest.SHIPS_STASE,
            ServerRequest.HIDE_SHIP,
        )
        for pack in entry_packs:
            self.PacMan.processPackages(pack)

    def send_entry_space_object(self):
        pass
        entry_packs = ()
        for pack in entry_packs:
            self.PacMan.processPackages(pack)

    def asteroids(self):
        self.PacMan.asteroids()

    def send_entry_packages(self):
        self.__base_send_entry_packages()
        if not self.SpaceObject:
            self.send_entry_location()
        else:
            self.send_entry_space_object()

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
            case "DB_Planet" | "Hive" | "Repository":
                self.PacMan.locationPlanet()
            case "AsteroidBelt":
                self.PacMan.locationBattle()
            case "Portal":
                self.Player.SpaceObject.set_player(self.Player)

    def trading_items(self):
        self.PacMan.tradingItems()

    def change_ship(self):
        self.PacMan.playerShip()

    def __base_send_entry_packages(self):
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
        )
        for pack in entry_packs:
            self.PacMan.processPackages(pack)

        update_value = (
            (ServerRequest.UPDATE_VALUE, UpdateValueType.PlayerClanPoints),
            (ServerRequest.UPDATE_VALUE, UpdateValueType.Bonuses),
            (ServerRequest.UPDATE_VALUE, UpdateValueType.PlayerCash),
            (ServerRequest.UPDATE_VALUE, UpdateValueType.ControlUsed),
            (ServerRequest.UPDATE_VALUE, UpdateValueType.ControlLeft),
            (ServerRequest.UPDATE_VALUE, UpdateValueType.HyperRadius),
            (ServerRequest.UPDATE_VALUE, UpdateValueType.HyperCost),
        )
        for pack in update_value:
            self.PacMan.processPackages(*pack)