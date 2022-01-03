from python.Static.TypeStr.ServerRequestStr import ServerRequestStr
from python.Packages.PackagesEntry import *
from python.Static.ParseXml import parse_xml
from python.Utils.DotMap import DotMap
from python.Static.Type.ServerRequest import ServerRequest
from python.Packages.PackageCreator import PackageCreator
from ..cfg.cfg_sell_buy import cfg_sell_buy

class PackagesManager:
    count_guid = 0
    _aAvailablePackages: list = list()
    _iStateKey: int
    _iLastPackageLength: int
    _iLastServerRequest: int
    _aBuffer: bytearray
    # _iLastTime: int = getTimer()
    lastFiveStateKeys: list = list()
    stateLoop: int

    def __init__(self, id_:int, StarWars):
        self.id = id_
        self.Game = StarWars
        self.Player = getattr(self.Game, f'Player_{self.id}')
        self.Location = self.Player.Location

    @staticmethod
    def isValidPackageLength(creator: int) -> bool:
        return 0 <= creator < 60000

    def processPackages(self, _loc1_: ServerRequest, *args):
        _loc2_: list = list()
        match _loc1_:
            case ServerRequest.SHIPS_POSITION:
                return self.shipsPosition()
            case ServerRequest.SHIPS_STASE:
                return self.shipsState()
            case ServerRequest.MESSAGE:
                return self.message()
            case ServerRequest.PLAYER_SHIP_UPDATE:
                return self.playerShipUpdate()
            case ServerRequest.PLANETS_STATE:
                return self.planetsState()
            case ServerRequest.PLANETS_UPDATE:
                return self.planetsUpdate()
            case ServerRequest.REPOSITORY:
                return self.repository()
            case ServerRequest.CLAN_REPOSITORY:
                return self.clanrepository()
            case ServerRequest.WEAPON_TROUBLES:
                return self.weaponTroubles()
            case ServerRequest.SHIP:
                return self.ship()
            case ServerRequest.SHOOTS:
                return self.shoots()
            case ServerRequest.ITEMS:
                return self.items()
            case ServerRequest.ACTIVE_DEVICES:
                return self.activeDevices()
            case ServerRequest.ACTIVE_WEPONS:
                return self.activeWeapons()
            case ServerRequest.HIDE_SHIP:
                return self.hideShip()
            case ServerRequest.SHIP_DESTROYED:
                return self.shipDestroyed()
            case ServerRequest.SHIP_JUMPED:
                return self.shipJumped()
            case ServerRequest.PLANET:
                return self.planet()
            case ServerRequest.INVENTORY:
                return self.inventory()
            case ServerRequest.TRADING_ITEMS:
                return self.tradingItems()
            case ServerRequest.RESOURCE_UPDATE_INFO:
                return self.resourceUpdate()
            case ServerRequest.ASTEROIDS:
                return self.asteroids()
            case ServerRequest.EFFECT_CREATED:
                return self.effectCreated()
            case ServerRequest.LOCATION_PLANET:
                return self.locationPlanet()
            case ServerRequest.LOCATION_SYSTEM:
                return self.locationSystem()
            case ServerRequest.LOCATION_BATTLE:
                return self.locationBattle()
            case ServerRequest.PLAYER:
                return self.player()
            case ServerRequest.QUEST_MESSAGE:
                return self.questMessage()
            case ServerRequest.PLAYER_SKILLS:
                return self.playerSkills()
            case ServerRequest.PLAYER_SKILLS_DATA:
                return self.playerSkillsData()
            case ServerRequest.PLAYER_SHIP:
                return self.playerShip()
            case ServerRequest.DROID_BUILDING_DIALOG:
                return self.droidBuildingDialog()
            case ServerRequest.TRADING_SHIPS:
                return self.tradingShips()
            case ServerRequest.WEAPONS_PARAMETERS:
                return self.weaponsParameters()
            case ServerRequest.ENGINES_PARAMETERS:
                return self.engineParameters()
            case ServerRequest.AMMOS_PARAMETERS:
                return self.ammoParameters()
            case ServerRequest.RESOURCE_PARAMETERS:
                return self.resourceParameters()
            case ServerRequest.DEVICE_PARAMETERS:
                return self.deviceParameters()
            case ServerRequest.DROID_PARAMETERS:
                return self.droidParameters()
            case ServerRequest.SHIP_PARAMETERS:
                return self.shipParameters()
            case ServerRequest.LOGGED:
                return self.logged()
            case ServerRequest.REACHABLE_SYSTEMS:
                return self.reachableSystems()
            case ServerRequest.SYSTEM_MESSAGE:
                return self.systemMessage()
            case ServerRequest.LOG_MESSAGE:
                return self.logMessage()
            case ServerRequest.LOG_MESSAGE_STRING:
                return self.logMessagestr()
            case ServerRequest.SYSTEM_MESSAGE_STRING:
                return self.systemMessagestr()
            case ServerRequest.MAP:
                return self.map()
            case ServerRequest.QUESTS_JOURNAL:
                return self.questsJournal()
            case ServerRequest.ARENA_REQUESTS:
                return self.arenaRequests()
            case ServerRequest.PLANET_QUESTS:
                return self.planetQuests()
            case ServerRequest.ADDITIONAL_QUEST_MESSAGE:
                return self.additionalQuestMessage()
            case ServerRequest.BATTLE_REQUEST_CHANGED:
                return self.battleRequestChanged()
            case ServerRequest.TOP_LIST:
                return self.topList()
            case ServerRequest.TOP_RATING_LIST:
                return self.topRatingList()
            case ServerRequest.TOP_CLANS_LIST:
                return self.topClansList()
            case ServerRequest.NEWS_LIST:
                return self.newsList()
            case ServerRequest.ONLINE:
                return self.online()
            case ServerRequest.VERSION:
                return self.version()
            case ServerRequest.SHIP_HEALTH:
                return self.shipHealth()
            case ServerRequest.NPC_MESSAGE:
                return self.npcMessage()
            case ServerRequest.UPDATE_HOLD:
                return self.updateHold()
            case ServerRequest.GINETIC_LAB_OPTIONS:
                return self.gineticLabOptions()
            case ServerRequest.CLAN:
                return self.clan()
            case ServerRequest.CHECK_VALUE_RESULT:
                return self.checkValueResult()
            case ServerRequest.ACCEPTED_CLAN_INFO:
                return self.acceptedClanInfo()
            case ServerRequest.CLAN_ID:
                return self.clanId()
            case ServerRequest.CLANS_LETTERS:
                return self.clansLetters()
            case ServerRequest.CLANS_LIST:
                return self.clansList()
            case ServerRequest.CLAN_JOIN_REQUESTS:
                return self.clanJoinRequests()
            case ServerRequest.PLAYER_INFO:
                return self.playerInfo()
            case ServerRequest.PLAYER_LOGGED_ON:
                return self.playerLoggedOn()
            case ServerRequest.PLAYER_LOGGED_OFF:
                return self.playerLoggedOff()
            case ServerRequest.PLAYER_CLAN:
                return self.playerClan()
            case ServerRequest.FRIEND_CLANS:
                return self.friendClans()
            case ServerRequest.ENEMY_CLANS:
                return self.enemyClans()
            case ServerRequest.UPDATE_VALUE:
                return self.updateValue(*args)
            case ServerRequest.FRIEND_REQUESTS:
                return self.friendRequests()
            case ServerRequest.DROID_EVENT:
                return self.droidEvent()
            case ServerRequest.EFFECT_REMOVED:
                return self.effectRemoved()
            case ServerRequest.MISSIONS:
                return self.missions()
            case ServerRequest.TO_GAME:
                return self.toGame()
            case ServerRequest.PLAYER_ANGAR:
                return self.playerAngar()
            case ServerRequest.TRADE_INVITATION:
                return self.tradeInvitation()
            case ServerRequest.SHOW_TRADING:
                return self.showTrading()
            case ServerRequest.TRADING_CASH:
                return self.tradingCash()
            case ServerRequest.TRADE_SELL_ITEMS:
                return self.tradeSellItems()
            case ServerRequest.EVIL:
                return self.Evil()
            case ServerRequest.TRADE_ACCEPTED:
                return self.tradeAccept()
            case ServerRequest.TRADE_BUY_ITEMS:
                return self.tradeBuyItems()
            case ServerRequest.FINISH_TRADING:
                return self.finishTrading()
            case ServerRequest.SHIP_UPDATE_INFO:
                return self.shipUpdateInfo()
            case ServerRequest.TEAM_LIST:
                return self.teamList()

    def tradingCash(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TRADING_CASH
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.TRADING_CASH))
        creator.write_int(5)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def tradeAccept(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TRADE_ACCEPTED
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.TRADE_ACCEPTED))
        creator.write_bool(bool())
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def shipUpdateInfo(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIP_UPDATE_INFO
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.SHIP_UPDATE_INFO))
        _loc6_ = DotMap()
        creator.write_short(_loc6_.classNumber)
        creator.write_short(_loc6_.size)
        creator.write_unsigned_byte(_loc6_.weaponSlots)
        creator.write_unsigned_byte(_loc6_.deviceSlots)
        creator.write_unsigned_byte(_loc6_.armor)
        creator.write_unsigned_byte(_loc6_.shields)
        creator.write_short(_loc6_.maxEnergy)
        creator.write_short(_loc6_.maxHealth)
        creator.write_short(_loc6_.cpu)
        creator.write_short(_loc6_.radar)
        creator.write_unsigned_byte(_loc6_.maxSpeed)
        data = []
        creator.write_unsigned_byte(len(data))
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_unsigned_byte(_loc2_.type)
            creator.write_unsigned_byte(_loc2_.valueType)
            creator.write_int(_loc2_.value)

        data_ship_feature = []
        creator.write_unsigned_byte(len(data_ship_feature))
        _loc4_ = 0
        for i in data_ship_feature:
            _loc3_ = DotMap(i)
            creator.write_unsigned_byte(_loc3_.type)
            creator.write_int(_loc3_.value)
            _loc4_ += 1
        _loc9_ = DotMap()
        creator.write_short(_loc9_.classNumber)
        creator.write_short(_loc9_.size)
        creator.write_unsigned_byte(_loc9_.weaponSlots)
        creator.write_unsigned_byte(_loc9_.deviceSlots)
        creator.write_unsigned_byte(_loc9_.armor)
        creator.write_unsigned_byte(_loc9_.shields)
        creator.write_short(_loc9_.maxEnergy)
        creator.write_short(_loc9_.maxHealth)
        creator.write_short(_loc9_.cpu)
        creator.write_short(_loc9_.radar)
        creator.write_unsigned_byte(_loc9_.maxSpeed)
        data = []
        creator.write_unsigned_byte(len(data))
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_unsigned_byte(_loc2_.type)
            creator.write_unsigned_byte(_loc2_.valueType)
            creator.write_int(_loc2_.value)
        data = []
        creator.write_unsigned_byte(len(data))
        for i in data:
            _loc3_ = DotMap(i)
            creator.write_unsigned_byte(_loc3_.type)
            creator.write_int(_loc3_.value)
            _loc4_ += 1
        creator.write_bool(_loc9_.satisfying)
        UpdateCost = []
        _loc10_ = DotMap()
        creator.write_int(_loc10_.cash)
        for i in UpdateCost:
            _loc5_ = DotMap(i)
            creator.write_short(_loc5_.classNumber)
            creator.write_int(_loc5_.count)
            creator.write_bool(_loc5_.enough)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def finishTrading(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.FINISH_TRADING
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.FINISH_TRADING))
        _loc2_ = 0
        creator.write_int(_loc2_)
        self._write_items(creator, True, False, False)
        _loc4_: int = 0
        creator.write_int(_loc4_)
        self._write_items(creator, True, False, False)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def tradeSellItems(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TRADE_SELL_ITEMS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.TRADE_SELL_ITEMS))
        self._write_items(creator, True, True)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def tradeBuyItems(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TRADE_BUY_ITEMS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.TRADE_BUY_ITEMS))
        self._write_items(creator, True, True)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def playerAngar(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_ANGAR
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.PLAYER_ANGAR))
        data = []
        creator.write_unsigned_byte(len(data))
        for i in data:
            _loc6_ = DotMap(i)
            creator.write_short(_loc6_.classNumber)
            creator.write_int(_loc6_.cost)
            creator.write_short(_loc6_.size)
            creator.write_bytes(_loc6_.weaponSlots)
            creator.write_bytes(_loc6_.deviceSlots)
            creator.write_bytes(_loc6_.armor)
            creator.write_bytes(_loc6_.shields)
            creator.write_short(_loc6_.maxEnergy)
            creator.write_short(_loc6_.maxHealth)
            creator.write_short(_loc6_.cpu)
            creator.write_short(_loc6_.radar)
            creator.write_unsigned_byte(_loc6_.maxSpeed)
            data_restr = []
            creator.write_unsigned_byte(len(data_restr))
            for i in data:
                _loc4_ = DotMap(i)
                creator.write_unsigned_byte(_loc4_.type)
                creator.write_unsigned_byte(_loc4_.valueType)
                creator.write_int(_loc4_.value)
                data_loc3_ = []
                creator.write_unsigned_byte(len(data_loc3_))
                for i in data_loc3_:
                    _loc5_ = DotMap(i)
                    creator.write_unsigned_byte(_loc5_.type)
                    creator.write_int(_loc5_.value)
                    creator.write_bool(_loc6_.satisfying)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    #
    def updateHold(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.UPDATE_HOLD
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.UPDATE_HOLD))
        update_hold = bool()
        creator.write_bool(update_hold)
        self._write_items(creator, True, True, True, update_hold)
        self._write_items(creator, True, True, True, update_hold)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def gineticLabOptions(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.GINETIC_LAB_OPTIONS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.GINETIC_LAB_OPTIONS))
        data = []
        creator.write_unsigned_byte(len(data))
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_unsigned_byte(_loc2_.option)
            creator.write_int(_loc2_.cost)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def npcMessage(self, text=4, avatar=2001):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.NPC_MESSAGE
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.NPC_MESSAGE))
        creator.write_int(text)  # message SystemMessageType
        creator.write_int(avatar)  # avatar
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def additionalQuestMessage(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ADDITIONAL_QUEST_MESSAGE
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.ADDITIONAL_QUEST_MESSAGE))
        _loc2_: int = 0
        _loc3_: int = 0
        creator.write_int(_loc2_)
        creator.write_int(_loc3_)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def arenaRequests(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ARENA_REQUESTS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.ARENA_REQUESTS))
        data = []
        creator.write_int(len(data))
        _loc5_: int = 0
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.id)
            creator.write_int(_loc2_.playersCount)
            creator.write_int(_loc2_.maxPlayers)
            creator.write_int(_loc2_.maxShipType)
            creator.write_int(_loc2_.minShipType)
            creator.write_unsigned_byte(_loc2_.type)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    #     #
    def battleRequestChanged(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.BATTLE_REQUEST_CHANGED
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.BATTLE_REQUEST_CHANGED))
        _loc3_ = DotMap()
        creator.write_int(_loc3_.id)
        creator.write_int(_loc3_.playersCount)
        creator.write_int(_loc3_.maxPlayers)
        creator.write_int(_loc3_.maxShipType)
        creator.write_int(_loc3_.minShipType)
        creator.write_unsigned_byte(_loc3_.type)
        creator.write_int(_loc3_.award)
        _loc3_.cost = (_loc3_.type - 1) * 2000
        for i in _loc3_.playersCoun:
            _loc2_ = DotMap(i)
            creator.write_bool(_loc2_.isReady)
            creator.write_int(_loc2_.id)
            creator.write_utf(_loc2_.login)
            creator.write_int(_loc2_.level)
            creator.write_int(_loc2_.shipClass)
            creator.write_int(_loc2_.race)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def questsJournal(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.QUESTS_JOURNAL
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.QUESTS_JOURNAL))
        data = []
        creator.write_int(len(data))
        _loc5_: int = 0
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.questId)
            creator.write_int(_loc2_.giverType)
            creator.write_utf(_loc2_.giverName)
            creator.write_utf(_loc2_.Name)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def activeDevices(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ACTIVE_DEVICES
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.ACTIVE_DEVICES))
        player = getattr(self.Game, f"Player_{self.id}")
        data_active_device = player.active_devices
        creator.write_unsigned_byte(len(data_active_device))
        for _loc3_ in data_active_device:
            creator.write_short(_loc3_.classNumber)
            creator.write_bytes(_loc3_.guid)
            creator.write_float(_loc3_.reloadedTime)

        self.Game.id_to_conn[self.id].send(creator.get_package())

    def activeWeapons(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ACTIVE_WEPONS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.ACTIVE_WEPONS))

        active_weapons = self.Player.active_weapons
        creator.write_unsigned_byte(len(active_weapons))
        for active_weapon in active_weapons:
            creator.write_short(active_weapon.classNumber)
            creator.write_unsigned_byte(5)#active_weapon.index) # hz
        self.Game.id_to_conn[self.id].send(creator.get_package())

    #     #
    def playerShipUpdate(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_SHIP_UPDATE
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.PLAYER_SHIP_UPDATE))
        _loc2_ = DotMap({
            "energy": 10,
            "health": 10,
            "controlLeft": 10,
            "controlUsed": 10,
        })
        creator.write_short(_loc2_.energy)
        creator.write_short(_loc2_.health)
        creator.write_unsigned_byte(_loc2_.controlLeft)
        creator.write_unsigned_byte(_loc2_.controlUsed)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    #     #
    def tradingShips(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TRADING_SHIPS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.TRADING_SHIPS))

        data = self.Player.SpaceObject.ships

        creator.write_int(5999)#ship.id)  # id
        creator.write_int(100000)#ship.cost)  # ship cost
        creator.write_float(2.0) #ship.buy_coef)  # buyCoeficient
        creator.write_float(1.0) #ship.sell_coef)  # sellCoeficient

        creator.write_int(len(data))
        print(len(data))
        for _loc6_ in data:
            creator.write_unsigned_byte(5999) #_loc6_.ship["id"]
            creator.write_short(_loc6_.ship["classNumber"])
            creator.write_int(_loc6_.ship["cost"])
            creator.write_short(_loc6_.ship["size"])
            creator.write_unsigned_byte(_loc6_.ship["weaponSlots"])
            creator.write_unsigned_byte(_loc6_.ship["deviceSlots"])
            creator.write_unsigned_byte(_loc6_.ship["armor"])
            creator.write_unsigned_byte(_loc6_.ship["shields"])
            creator.write_short(_loc6_.ship["maxEnergy"])
            creator.write_short(_loc6_.ship["maxHealth"])
            creator.write_short(_loc6_.ship["cpu"])
            creator.write_short(_loc6_.ship["radar"])
            creator.write_unsigned_byte(_loc6_.ship["maxSpeed"])
            data_restr = _loc6_.ship["restrictions"]['data']
            creator.write_unsigned_byte(len(data_restr))
            print('restr', len(data_restr))
            for i in data_restr:
                _loc4_ = DotMap(i)
                print(_loc4_)
                creator.write_unsigned_byte(_loc4_.type)
                creator.write_unsigned_byte(_loc4_.valueType)
                creator.write_int(_loc4_.value)
            data_ship_feature = _loc6_.ship["features"]['data']
            creator.write_unsigned_byte(len(data_ship_feature))
            print(len(data_ship_feature))
            for i in data_ship_feature:
                _loc5_ = DotMap(i)
                print(i)
                creator.write_unsigned_byte(_loc5_.type)
                creator.write_int(_loc5_.value)

            creator.write_bool(_loc6_.ship["satisfying"])
            self.Game.id_to_conn[self.id].send(creator.get_package())

    def tradingItems(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TRADING_ITEMS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.TRADING_ITEMS))
        Planet = getattr(self.Game, f'Player_{self.id}').SpaceObject
        creator.write_int(Planet.id)  # id
        creator.write_float(cfg_sell_buy(self.Player.skills['Trading']).coef_sell)  # sellCoeficient
        creator.write_float(cfg_sell_buy(self.Player.skills['Trading']).coef_buy)  # buyCoeficient

        PlayerItems = self.Player.inventory
        self._write_items(creator, PlayerItems, True, True, True, True)

        PlanetItems = self.Player.SpaceObject.ShowForPlayer(self.Player)
        self._write_items(creator, PlanetItems, True, True, True, True)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def resourceUpdate(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.RESOURCE_UPDATE_INFO
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.RESOURCE_UPDATE_INFO))
        ss = 22
        creator.write_int(ss)  # id
        self._write_items(creator, True, True)
        self._write_items(creator, True, True)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def _write_items(self, creator, items, param2: bool, param3: bool, param4: bool = True,
                     param5: bool = False) -> None:
        creator.write_int(len(items))
        for item in items:
            creator.write_int(item.classNumber)
            creator.write_bytes(item.guid)
            creator.write_int(item.wear)
            if param4:
                item.level = 0
                creator.write_int(item.level)
            else:
                item.level = 1
            if param2:
                item.zeroCost = 0
                creator.write_bool(item.zeroCost)
            if param5:
                creator.write_int(12)  # random don't use
            if param3:
                creator.write_bool(item.satisfying)

    def shipsPosition(self):
        """ id, x, y, targetX, targetY """
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIPS_POSITION
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.SHIPS_POSITION))
        players = self.Location.players
        creator.write_int(len(players))
        for player in players:
            creator.write_int(player.id)
            creator.write_float(player.x)
            creator.write_float(player.y)
            creator.write_float(player.target_x)
            creator.write_float(player.target_y)
        self.Game.id_to_conn[self.id].send(creator.get_package())


    def shipsState(self):
        """id, speed, health, energy, PlayerRelation"""
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIPS_STASE
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.SHIPS_STASE))
        players = self.Location.players
        for _loc2_ in players:
            creator.write_int(_loc2_.id)
            creator.write_unsigned_byte(_loc2_.speed)
            creator.write_short(_loc2_.health)
            creator.write_short(_loc2_.energy)
            creator.write_short(_loc2_.PlayerRelation)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def weaponTroubles(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.WEAPON_TROUBLES
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.WEAPON_TROUBLES))
        data = []
        creator.write_unsigned_byte(len(data))
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_unsigned_byte(_loc2_.trouble)
            creator.write_unsigned_byte(_loc2_.index)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def repository(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.REPOSITORY
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.REPOSITORY))

        data = self.Player.repository
        self._write_items(creator, data, False, False)

        creator.write_float(1.0)  # costCoef _loc4_.costCoef
        creator.write_int(len(data))
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.classNumber)
            creator.write_bytes(_loc2_.guid)
            creator.write_int(_loc2_.wear)
            creator.write_int(_loc2_.level)
            creator.write_int(12)  # random don't use
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def clanrepository(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CLAN_REPOSITORY
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.CLAN_REPOSITORY))
        data = []
        self._write_items(creator, False, False)
        _loc4_ = DotMap({"costCoef": 255.0})
        creator.write_float(_loc4_.costCoef)
        creator.write_int(len(data))
        for i in data:
            _loc2_ = DotMap()
            creator.write_int(_loc2_.classNumber)
            creator.write_bytes(_loc2_.guid)
            creator.write_int(_loc2_.wear)
            creator.write_int(_loc2_.level)
            creator.write_int(12)  # don't use
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def planetsState(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLANETS_STATE
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.PLANETS_STATE))
        data = []
        creator.write_unsigned_byte(len(data))
        for i in data:
            _loc1_ = DotMap(i)
            creator.write_int(_loc1_.id)  # id SpaceObject
            creator.write_float(_loc1_.angel)  # angel
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def planetsUpdate(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLANETS_UPDATE
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.PLANETS_UPDATE))
        data = []
        creator.write_unsigned_byte(len(data))
        for i in data:
            _loc1_ = DotMap(i)
            creator.write_int(_loc1_.id)
            creator.write_float(_loc1_.angel)
            creator.write_bytes(_loc1_.race)
            creator.write_bytes(_loc1_.aliance)
            creator.write_int(_loc1_.clanId)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    #     #
    def ship(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIP
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.SHIP))
        _loc3_ = self.Player
        creator.write_short(_loc3_.race)
        creator.write_int(_loc3_.id)
        creator.write_utf(_loc3_.login)
        creator.write_short(_loc3_.size)
        creator.write_float(_loc3_.x)
        creator.write_float(_loc3_.y)
        creator.write_int(_loc3_.level)
        creator.write_short(_loc3_.maxHealth)
        creator.write_short(_loc3_.maxEnergy)
        creator.write_int(_loc3_.avatar)
        creator.write_unsigned_byte(_loc3_.maxSpeed)
        creator.write_float(_loc3_.target_x)
        creator.write_float(_loc3_.target_y)
        creator.write_unsigned_byte(_loc3_.aliance)
        creator.write_unsigned_byte(_loc3_.status)
        creator.write_int(_loc3_.clanId)
        drodata = _loc3_.droid
        creator.write_unsigned_byte(len(drodata))
        for i in drodata:
            _loc2_ = DotMap(i)
            creator.write_unsigned_byte(_loc2_.id)
            creator.write_short(_loc2_.type)
            creator.write_short(_loc2_.weaponClass)
            creator.write_short(_loc2_.health)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    #     #
    def planet(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLANET
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.PLANET))
        _loc2_ = DotMap()
        creator.write_bytes(_loc2_.classNumber)
        creator.write_int(_loc2_.id)
        creator.write_unsigned_byte(_loc2_.race)
        creator.write_int(_loc2_.radius)
        creator.write_int(_loc2_.size)
        creator.write_float(_loc2_.serverAngle)
        creator.write_bool(_loc2_.landable)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def inventory(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.INVENTORY
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.INVENTORY))
        player = getattr(self.Game, f"Player_{self.id}")
        inventory = player.inventory
        _loc5_: int = creator.write_short(len(inventory))
        for ItemClass in inventory:
            creator.write_short(ItemClass.classNumber)
            creator.write_bytes(ItemClass.guid)
            creator.write_short(ItemClass.wear)
            creator.write_bool(ItemClass.inUsing)
            creator.write_unsigned_byte(ItemClass.level)
            creator.write_bool(ItemClass.satisfying)
        creator.write_unsigned_byte(player.ship['armor'])
        creator.write_unsigned_byte(player.ship['shields'])
        creator.write_short(player.hold) # Трюм
        creator.write_short(player.ship['cpu'])
        creator.write_short(player.ship['cpuUsed']) # ship.cpuUsed
        creator.write_unsigned_byte(player.ship['level'])
        creator.write_unsigned_byte(3) # ship.maxDroids

        # for i in data: # Какие-то дополнительные предметы
        #     _loc2_ = DotMap(i)
        #     creator.write_short(_loc2_.ItemClass)
        #     creator.write_bytes(_loc2_.id)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def player(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.PLAYER))

        creator.write_int(self.Player.id)
        creator.write_utf(self.Player.login)
        creator.write_int(self.Player.level)
        creator.write_int(self.Player.cash)
        creator.write_unsigned_byte(self.Player.race)
        creator.write_int(self.Player.avatar)
        creator.write_unsigned_byte(self.Player.aliance)
        creator.write_int(self.Player.clanId)
        creator.write_int(self.Player.role)
        creator.write_unsigned_byte(self.Player.clanRequestStatus)
        creator.write_unsigned_byte(self.Player.clanJoinRequestStatus)
        creator.write_int(self.Player.PlayerRelation)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    #     #
    def questMessage(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.QUEST_MESSAGE
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.QUEST_MESSAGE))
        quest = DotMap()
        creator.write_int(quest.questId)
        creator.write_int(quest.nextQuestId)
        creator.write_int(quest.giverType)
        creator.write_int(quest.status)
        creator.write_utf(quest.giverName)
        data = []
        creator.write_int(len(data))
        for i in data:
            _loc2_ = ''
            creator.write_utf(_loc2_)
        creator.write_int(quest.ParentSystemID)
        creator.write_unsigned_byte(quest.LocationType)
        creator.write_int(quest.LocationID)
        quest_award = []
        creator.write_int(len(quest_award))
        for i in quest_award:
            _loc3_ = DotMap(i)
            creator.write_int(_loc3_.classNumber)
            creator.write_int(_loc3_.level)
            creator.write_int(_loc3_.type)
            creator.write_int(_loc3_.value)
        quest_target = []
        creator.write_int(quest_target)
        for i in quest_target:
            _loc4_ = DotMap(i)
            creator.write_int(_loc4_.targetId)
            creator.write_int(_loc4_.targetSystemId)
            creator.write_int(_loc4_.targetPlanetId)
            creator.write_int(_loc4_.type)
            creator.write_int(_loc4_.value)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def playerSkills(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_SKILLS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.PLAYER_SKILLS))
        Player = getattr(self.Game, f"Player_{self.id}")
        creator.write_unsigned_byte(Player.level)
        creator.write_int(Player.experience)
        creator.write_int(Player.forNextLevel)
        self.write_skills(creator, Player.skills)
        creator.write_int(Player.freeSkills)
        creator.write_int(Player.expForFirstSkillLevel)
        creator.write_float(Player.expSkillGrowCoef)
        creator.write_float(Player.expSkillReduserCoef)
        creator.write_unsigned_byte(Player.maxSkill)
        creator.write_unsigned_byte(Player.status)
        creator.write_unsigned_byte(Player.level)
        if Player.point > 0:
            creator.write_int(0)
            creator.write_int(Player.point)
        else:
            creator.write_int(Player.point)
            creator.write_int(0)
        creator.write_int(Player.forNextLevel)
        self.Game.id_to_conn[self.id].send(creator.get_package())
        # self.Game.id_to_conn[self.id].send(creator.get_package())

    @staticmethod
    def write_skills(creator, param2) -> None:
        if isinstance(param2, DotMap):
            param2 = dict(param2)
        creator.write_unsigned_byte(param2["Control"])
        creator.write_unsigned_byte(param2["Defending"])
        creator.write_unsigned_byte(param2["EnergyWeapons"])
        creator.write_unsigned_byte(param2["KineticWeapons"])
        creator.write_unsigned_byte(param2["Mining"])
        creator.write_unsigned_byte(param2["Piloting"])
        creator.write_unsigned_byte(param2["Repairing"])
        creator.write_unsigned_byte(param2["RocketWeapons"])
        creator.write_unsigned_byte(param2["Trading"])
        creator.write_unsigned_byte(param2["Attacking"])
        creator.write_unsigned_byte(param2["Tactics"])
        creator.write_unsigned_byte(param2["Targeting"])
        creator.write_unsigned_byte(param2["Electronics"])
        creator.write_unsigned_byte(param2["Biocemistry"])
        creator.write_unsigned_byte(param2["Mechanics"])
        creator.write_unsigned_byte(param2["Cybernetics"])

    def playerSkillsData(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_SKILLS_DATA
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.PLAYER_SKILLS_DATA))
        Player = getattr(self.Game, f"Player_{self.id}")        
        creator.write_unsigned_byte(Player.level)
        creator.write_int(Player.experience)
        creator.write_int(Player.forNextLevel)
        self.write_skills(creator, Player.skills)
        creator.write_int(Player.freeSkills)
        creator.write_int(Player.expForFirstSkillLevel)
        creator.write_float(Player.expSkillGrowCoef)
        creator.write_float(Player.expSkillReduserCoef)
        creator.write_unsigned_byte(Player.maxSkill)
        creator.write_unsigned_byte(Player.status)
        creator.write_unsigned_byte(Player.level)
        creator.write_int(Player.pirateStatus)
        creator.write_int(Player.policeStatus)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def playerShip(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_SHIP
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.PLAYER_SHIP))
        
        creator.write_int(self.Player.race) # raca
        creator.write_int(self.Player.id)
        creator.write_utf(self.Player.login)
        creator.write_int(self.Player.size)
        creator.write_int(self.Player.energy)
        creator.write_int(self.Player.maxEnergy)
        creator.write_float(self.Player.x)
        creator.write_float(self.Player.y)
        creator.write_int(self.Player.team)
        print('maxSpeed 958', self.Player.maxSpeed)
        creator.write_unsigned_byte(self.Player.maxSpeed)
        creator.write_unsigned_byte(self.Player.ship['weaponSlots'])
        creator.write_unsigned_byte(self.Player.ship['deviceSlots'])
        creator.write_int(self.Player.maxHealth)
        creator.write_short(self.Player.ship['radar'])
        creator.write_short(self.Player.ship['cpu'])
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def weaponsParameters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.WEAPONS_PARAMETERS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.WEAPONS_PARAMETERS))
        data_weapons = parse_xml("WeaponParameters")
        cnt_weapon: int = len(data_weapons)
        creator.write_int(cnt_weapon)
        for i in data_weapons:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.classNumber)
            creator.write_int(_loc2_.autoShots)
            creator.write_int(_loc2_.radius)
            creator.write_int(_loc2_.reloadTime)
            creator.write_int(_loc2_.energyCost)
            creator.write_float(_loc2_.size)
            creator.write_int(_loc2_.cost)
            creator.write_bool(_loc2_.needAmmo)
            creator.write_int(_loc2_.ammoClass)
            creator.write_int(_loc2_.minDamage)
            creator.write_int(_loc2_.maxDamage)
            creator.write_unsigned_byte(_loc2_.type)
            creator.write_unsigned_byte(_loc2_.effect)
            creator.write_int(_loc2_.maxWear)
            restr = _loc2_.restrictions
            creator.write_unsigned_byte(restr['Length'])
            for i in restr['data']:
                _loc5_ = DotMap(i)
                creator.write_unsigned_byte(_loc5_.type)
                creator.write_unsigned_byte(_loc5_.valueType)
                creator.write_int(_loc5_.Value)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    #     #
    def ammoParameters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.AMMOS_PARAMETERS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.AMMOS_PARAMETERS))
        data_ammo = parse_xml("AmmoParameters")
        cnt_ammo: int = len(data_ammo)
        creator.write_int(cnt_ammo)
        for i in data_ammo:
            _loc2_ = DotMap(i)  # AmmoParameters()
            creator.write_int(_loc2_.classNumber)
            creator.write_float(_loc2_.size)
            creator.write_int(_loc2_.cost)
            creator.write_int(_loc2_.damage)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def resourceParameters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.RESOURCE_PARAMETERS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.RESOURCE_PARAMETERS))
        data_resourse = parse_xml('ResourseParameters')
        creator.write_int(len(data_resourse))
        for i in data_resourse:
            _loc2_ = DotMap(i)  # ResourceParameters()
            creator.write_int(_loc2_.classNumber)
            creator.write_float(_loc2_.size)
            creator.write_int(_loc2_.cost)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def deviceParameters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.DEVICE_PARAMETERS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.DEVICE_PARAMETERS))
        data_device = parse_xml("DeviceParameters")
        creator.write_int(len(data_device))
        for i in data_device:
            _loc4_ = DotMap(i)
            creator.write_int(_loc4_.classNumber)
            creator.write_float(_loc4_.size)
            creator.write_int(_loc4_.cost)
            creator.write_int(_loc4_.energyCost)
            creator.write_int(_loc4_.reloadTime)
            creator.write_int(_loc4_.maxWear)

            cnt_dev_eff = _loc4_.effects['Length']
            creator.write_unsigned_byte(cnt_dev_eff)
            data_dev_eff = _loc4_.effects['data']
            for i in data_dev_eff:
                _loc3_ = DotMap(i)  # DeviceEffect()
                creator.write_unsigned_byte(_loc3_.targetType)
                creator.write_int(_loc3_.value)
                creator.write_int(_loc3_.effectTime)
                creator.write_unsigned_byte(_loc3_.effectType)

            cnt_dev_restr = _loc4_.restrictions['Length']
            creator.write_unsigned_byte(cnt_dev_restr)
            data_dev_restr = _loc4_.restrictions["data"]
            for i in data_dev_restr:
                _loc8_ = DotMap(i)  # Restriction()
                creator.write_unsigned_byte(_loc8_.type)
                creator.write_unsigned_byte(_loc8_.valueType)
                creator.write_int(_loc8_.Value)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def droidParameters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.DROID_PARAMETERS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.DROID_PARAMETERS))
        data_droids = parse_xml("DroidParameters")
        creator.write_int(len(data_droids))
        for i in data_droids:
            _loc2_ = DotMap(i)  # DroidParameters()
            creator.write_short(_loc2_.classNumber)
            creator.write_float(_loc2_.size)
            creator.write_int(_loc2_.cost)
            creator.write_unsigned_byte(_loc2_.energyCost)
            creator.write_unsigned_byte(_loc2_.armor)
            creator.write_short(_loc2_.droidType)
            creator.write_short(_loc2_.weaponClass)
            creator.write_short(_loc2_.health)
            cnt_restr = _loc2_.restrictions['Length']
            creator.write_unsigned_byte(cnt_restr)
            data_restr = _loc2_.restrictions['data']
            for i in data_restr:
                _loc5_ = DotMap(i)  # Restriction()
                creator.write_unsigned_byte(_loc5_.type)
                creator.write_unsigned_byte(_loc5_.valueType)
                creator.write_int(_loc5_.Value)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    #     #
    def shipParameters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIP_PARAMETERS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.SHIP_PARAMETERS))
        data_ship = parse_xml('ShipParameters')
        creator.write_int(len(data_ship))
        for i in data_ship:
            _loc2_ = DotMap(i)
            creator.write_short(_loc2_.classNumber)
            creator.write_int(_loc2_.cost)
            creator.write_short(_loc2_.size)
            creator.write_unsigned_byte(_loc2_.weaponSlots)
            creator.write_unsigned_byte(_loc2_.deviceSlots)
            creator.write_unsigned_byte(_loc2_.armor)
            creator.write_unsigned_byte(_loc2_.shields)
            creator.write_short(_loc2_.maxEnergy)
            creator.write_short(_loc2_.maxHealth)
            creator.write_short(_loc2_.cpu)
            creator.write_short(_loc2_.radar)
            creator.write_unsigned_byte(_loc2_.maxSpeed)
            cnt_restr = _loc2_.restrictions['Length']
            creator.write_unsigned_byte(cnt_restr)
            data_restr = _loc2_.restrictions['data']
            for i in data_restr:
                _loc7_ = DotMap(i)
                creator.write_unsigned_byte(_loc7_.type)
                creator.write_unsigned_byte(_loc7_.valueType)
                creator.write_int(_loc7_.Value)
            cnt_ship_feat = _loc2_.features['Length']
            creator.write_unsigned_byte(cnt_ship_feat)
            data_ship_feat = _loc2_.features['data']
            for i in data_ship_feat:
                _loc8_ = DotMap(i)
                creator.write_unsigned_byte(_loc8_.type)
                creator.write_int(_loc8_.Value)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def engineParameters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ENGINES_PARAMETERS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.ENGINES_PARAMETERS))
        data_engine = parse_xml("EngineParameters")
        creator.write_int(len(data_engine))
        for i in data_engine:
            _loc2_ = DotMap(i)  # EngineParameters()
            creator.write_short(_loc2_.classNumber)
            creator.write_float(_loc2_.size)
            creator.write_int(_loc2_.cost)
            creator.write_unsigned_byte(_loc2_.hyperjumpRadius)
            creator.write_int(_loc2_.maxWear)
            creator.write_unsigned_byte(_loc2_.energyCost)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    #     #
    def map(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.MAP
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.MAP))
        data_system = parse_xml('GalaxyMap')
        creator.write_short(len(data_system))
        for i in data_system:
            _loc2_ = DotMap(i)  # ReachableSystem()
            creator.write_unsigned_byte(_loc2_.id)
            creator.write_unsigned_byte(_loc2_.classNumber)
            creator.write_short(_loc2_.x)
            creator.write_short(_loc2_.y)
            creator.write_unsigned_byte(_loc2_.Sector)
            creator.write_unsigned_byte(_loc2_.lineTo)
            cnt_planet = _loc2_.Planets['Length']
            creator.write_unsigned_byte(cnt_planet)
            data_planet = _loc2_.Planets['data']
            for i in data_planet:
                _loc7_ = DotMap(i)  # PlanetData()
                creator.write_short(_loc7_.id)
                creator.write_unsigned_byte(_loc7_.race)
                creator.write_unsigned_byte(_loc7_.classNumber)
                creator.write_unsigned_byte(_loc7_.aliance)
            cnt_space_objects = _loc2_.SpaceObjects['Length']
            creator.write_unsigned_byte(cnt_space_objects)
            data_space_objects = _loc2_.SpaceObjects['data']
            for i in data_space_objects:
                _loc8_ = DotMap(i)  # StaticObjectData()
                creator.write_unsigned_byte(_loc8_.type)
                creator.write_unsigned_byte(_loc8_.aliance)
                creator.write_unsigned_byte(_loc8_.race)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def reachableSystems(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.REACHABLE_SYSTEMS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.REACHABLE_SYSTEMS))
        data_system = []
        creator.write_unsigned_byte(len(data_system))
        for i in data_system:
            _loc2_ = DotMap(i)
            creator.write_unsigned_byte(_loc2_.id)
            creator.write_bool(_loc2_.current)
            creator.write_short(_loc2_.energyForJump)
        _loc6_: int = 0
        creator.write_unsigned_byte(_loc6_)  # radiuse
        _loc7_: int = 0
        creator.write_unsigned_byte(_loc7_)  # sector
        self.Game.id_to_conn[self.id].send(creator.get_package())

    #     #
    def version(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.VERSION
        version = '0.9.0.1'
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.VERSION))
        creator.write_utf(version)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def shipHealth(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIP_HEALTH
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.SHIP_HEALTH))
        ship = getattr(self.Game, f'Player_{self.id}').ship
        creator.write_int(ship.id)
        creator.write_int(ship.health)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def online(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ONLINE
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.ONLINE))
        creator.write_int(1)
        creator.write_int(self.Game.online)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def topList(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TOP_LIST
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.TOP_LIST))
        all_player = PackagesEntry(self.Game, self.id).top_list
        cnt: int = len(all_player)
        creator.write_int(cnt)
        for i in all_player:
            _loc2_ = i
            creator.write_utf(_loc2_.login)
            creator.write_int(_loc2_.level)
            creator.write_int(_loc2_.experience)
            creator.write_int(_loc2_.clan_id)
            creator.write_unsigned_byte(_loc2_.race)
            creator.write_short(_loc2_.shipClass)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def topRatingList(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TOP_RATING_LIST
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.TOP_RATING_LIST))
        top_players = PackagesEntry(self.Game, self.id).top_rating_list
        cnt: int = len(top_players)
        creator.write_int(cnt)
        for i in top_players:
            _loc2_ = i  # PlayerData()
            creator.write_utf(_loc2_.login)
            creator.write_int(_loc2_.level)
            creator.write_int(_loc2_.points)
            creator.write_int(_loc2_.clanId)
            creator.write_unsigned_byte(_loc2_.race)
            creator.write_short(_loc2_.shipClass)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def topClansList(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TOP_CLANS_LIST
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.TOP_CLANS_LIST))
        players = PackagesEntry(self.Game, self.id).top_clan_list
        cnt: int = len(players)
        creator.write_int(cnt)
        for i in players:
            _loc2_ = i
            creator.write_int(_loc2_.id)
            creator.write_int(_loc2_.points)
            creator.write_int(_loc2_.leaderID)
            creator.write_unsigned_byte(_loc2_.aliace)
            creator.write_unsigned_byte(_loc2_.level)
            creator.write_utf(_loc2_.name)
            creator.write_utf(_loc2_.shortName)
            creator.write_utf(_loc2_.logoFileName)
        self.Game.id_to_conn[self.id].send(creator.get_package())

        #
        # def auctionList(self):
        #     creator = PackageCreator()
        #     creator.PackageNumber = ServerRequest.AUCTION_SHOP_PACKAGE
        # PacStr = ServerRequestStr()
        # print('Пакет отправлен', PacStr.get_str(ber = ServerRequest))
        #     data = []
        #     creator.write_int(len(data))
        #     for i in data:
        #         _loc3_ = DotMap(i)
        #         creator.write_int(_loc2_.ItemClass)
        #         creator.write_guid(_loc3_.guid)
        #         creator.write_int(_loc3_.wear)
        #         creator.write_int(_loc3_.ownerid)
        #         creator.write_int(_loc3_.price)
        #         creator.write_int(_loc3_.ransom)
        #         creator.write_int(_loc3_.lastPlayerID)
        #         creator.write_utf(_loc3_.ownerName)
        #         creator.write_utf(_loc3_.lastPlayerName)
        #     self.Game.id_to_conn[self.id].send(creator.get_package())

    def newsList(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.NEWS_LIST
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.NEWS_LIST))
        data = []
        creator.write_int(len(data))
        for i in data:
            creator.write_utf(i)  # text
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def Evil(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.EVIL
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.EVIL))
        _loc2_ = ''
        creator.write_utf(_loc2_)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def locationPlanet(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOCATION_PLANET
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.LOCATION_PLANET))

        player = getattr(self.Game, f'Player_{self.id}')
        SpaceObject = player.SpaceObject

        creator.write_unsigned_byte(SpaceObject.classNumber)
        creator.write_int(SpaceObject.id)
        creator.write_unsigned_byte(SpaceObject.race)
        creator.write_int(SpaceObject.radius)
        creator.write_int(SpaceObject.size)
        creator.write_unsigned_byte(SpaceObject.aliance)
        creator.write_int(SpaceObject.clanId)
        creator.write_float(SpaceObject.angle)
        creator.write_unsigned_byte(SpaceObject.QCount)
        shops = SpaceObject.shops
        creator.write_short(len(shops)) # len(shop_data))

        for type_shop in shops:
            print(shops)
            creator.write_int(type_shop["id"]) #_loc3_.id)
            creator.write_unsigned_byte(type_shop["type"])#_loc3_.type)

        player_info_data = []
        for i in player_info_data:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.id)
            creator.write_utf(_loc2_.name)
            creator.write_int(_loc2_.clanId)
            creator.write_int(_loc2_.level)

        self.Game.id_to_conn[self.id].send(creator.get_package())

    def planetQuests(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLANET_QUESTS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.PLANET_QUESTS))
        data = []
        creator.write_short(len(data))
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.questId)
            creator.write_int(_loc2_.giverType)
            creator.write_utf(_loc2_.giverName)
            creator.write_utf(_loc2_.Name)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def locationSystem(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOCATION_SYSTEM
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.LOCATION_SYSTEM))
        Location = self.Player.Location
        creator.write_int(Location.id) # id
        creator.write_float(Location.x)  # Location.x
        creator.write_float(Location.y)  # Location.y
        creator.write_unsigned_byte(Location.sector)  # Location.sector
        creator.write_short(len(Location.players))
        for Player in Location.players:
            creator.write_short(Player.race) #
            creator.write_int(Player.id)
            creator.write_utf(Player.login)
            creator.write_short(Player.size)
            creator.write_float(Player.x)  # setPosition
            creator.write_float(Player.y)
            creator.write_int(Player.level)
            creator.write_short(Player.maxHealth)
            creator.write_short(Player.maxEnergy)
            creator.write_int(Player.avatar)
            print('maxSpeed 1404', Player.maxSpeed)
            creator.write_unsigned_byte(int(Player.maxSpeed))
            creator.write_float(Player.target_x)
            creator.write_float(Player.target_y)  # setMovePoint
            creator.write_unsigned_byte(Player.aliance)
            creator.write_unsigned_byte(Player.status)
            creator.write_int(Player.clanId)

            creator.write_unsigned_byte(len(Player.droid))

            for Driod in Player.droid:
                creator.write_unsigned_byte(Driod.id)
                creator.write_short(Driod.type)
                creator.write_short(Driod.weaponClass)
                creator.write_short(Driod.health)

        creator.write_short(len(Location.planets))
        for planet in Location.planets:
            creator.write_unsigned_byte(planet.classNumber)
            creator.write_int(planet.id)
            creator.write_unsigned_byte(planet.race)
            creator.write_int(planet.radius)
            creator.write_int(planet.size)
            creator.write_float(planet.angle)
            creator.write_bool(planet.landable)
            creator.write_unsigned_byte(planet.aliance)
            creator.write_int(planet.clanId)

        creator.write_short(len(Location.StaticSpaceObjects))
        for StaticSpaceObject in Location.StaticSpaceObjects:
            creator.write_int(StaticSpaceObject.StaticSpaceObjectType)
            creator.write_int(StaticSpaceObject.id)
            creator.write_float(StaticSpaceObject.x)
            creator.write_float(StaticSpaceObject.y)
            creator.write_bool(StaticSpaceObject.landable)

        self.Game.id_to_conn[self.id].send(creator.get_package())

    def locationBattle(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOCATION_BATTLE
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.LOCATION_BATTLE))
        _loc6_ = self.Player
        creator.write_int(_loc6_.id)
        creator.write_float(_loc6_.x)
        creator.write_float(_loc6_.y)
        player_info_data = self.Player.ObjectToReach.players
        creator.write_short(len(player_info_data))
        for ship_data in player_info_data:
            creator.write_short(ship_data.race)
            creator.write_int(ship_data.id)
            creator.write_utf(ship_data.login)
            creator.write_short(ship_data.size)
            creator.write_float(ship_data.x)
            creator.write_float(ship_data.y)
            creator.write_int(ship_data.ship['classNumber']) # hz
            creator.write_short(ship_data.maxHealth)
            creator.write_short(ship_data.maxEnergy)
            creator.write_int(ship_data.ship['classNumber']) # hz
            creator.write_unsigned_byte(ship_data.aliance)
            creator.write_unsigned_byte(ship_data.status)
            creator.write_int(ship_data.clanId)
            droids = ship_data.droid
            creator.write_unsigned_byte(len(droids))
            for _loc4_ in droids:
                creator.write_unsigned_byte(_loc4_.id)
                creator.write_short(_loc4_.type)
                creator.write_short(_loc4_.weaponClass)
                creator.write_short(_loc4_.health)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def shoots(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHOOTS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.SHOOTS))
        data = []
        creator.write_short(len(data))
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.id)
            shoot_data = _loc2_.shoot
            creator.write_short(len(shoot_data))
            for shoot in shoot_data:
                _loc5_ = DotMap(shoot)
                creator.write_short(_loc5_.classNumber)
                creator.write_short(_loc5_.damage)
                creator.write_unsigned_byte(_loc5_.destroyedTarget)
                creator.write_int(_loc5_.targetId)
                creator.write_unsigned_byte(_loc5_.targetType)
                creator.write_unsigned_byte(_loc5_.muzzleIndex)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    #     #
    def items(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ITEMS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.ITEMS))
        data = self.Location.inventory
        for item_ in data:
            creator.write_int(self.Location.id)
            creator.write_short(item_.classNumber)
            creator.write_short(int(item_.x))
            creator.write_short(int(item_.y))
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def message(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.MESSAGE
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.MESSAGE))
        _loc2_ = DotMap({
            "from_player": 'Max223',
            "text": "Hello",
            "type": 1,
            "isPrivate": False,
            "isAdmin": False,
        })
        creator.write_utf(_loc2_.from_player)  # name player
        creator.write_utf(_loc2_.text)
        creator.write_unsigned_byte(_loc2_.type)  # 1 - global  2 - local 3 - clanId 4 - trade 5 - client chat
        creator.write_bool(_loc2_.isPrivate)
        creator.write_bool(_loc2_.isAdmin)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    #     #
    def asteroids(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ASTEROIDS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.ASTEROIDS))
        data = self.Player.ObjectToReach.asteroids
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.id)
            creator.write_float(_loc2_.x)
            creator.write_float(_loc2_.y)
            creator.write_float(_loc2_.targetX)
            creator.write_float(_loc2_.targetY)
            creator.write_unsigned_byte(_loc2_.speed)
            creator.write_int(_loc2_.size)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def effectCreated(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.EFFECT_CREATED
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.EFFECT_CREATED))
        ss = 22
        creator.write_int(ss)
        data = []
        creator.write_unsigned_byte(len(data))
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.targetId)
            creator.write_unsigned_byte(_loc2_.destroyedTarget)
            creator.write_bool(_loc2_.effectFailed)
        _loc7_: int = 0
        creator.write_unsigned_byte(_loc7_)  # EffectType
        _loc8_: float = 1.0
        creator.write_float(_loc8_)  # don't use
        _loc9_: int = 0
        creator.write_int(_loc9_)  # damage damageToShow
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def effectRemoved(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.EFFECT_REMOVED
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.EFFECT_REMOVED))
        _loc2_: int = 0
        _loc3_: int = 0
        creator.write_int(_loc2_)
        creator.write_unsigned_byte(_loc3_)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def logMessage(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOG_MESSAGE
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.LOG_MESSAGE))
        _loc2_: int = 0
        _loc3_: int = 0
        creator.write_int(_loc2_)
        creator.write_int(_loc3_)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def logMessagestr(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOG_MESSAGE_STRING
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.LOG_MESSAGE_STRING))
        _loc2_: str = ''
        creator.write_utf(_loc2_)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def systemMessage(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SYSTEM_MESSAGE
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.SYSTEM_MESSAGE))
        _loc2_ = 6
        _loc3_ = 5
        creator.write_int(_loc2_)  # SystemMessageType
        creator.write_int(_loc3_)  # hz
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def systemMessagestr(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SYSTEM_MESSAGE_STRING
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.SYSTEM_MESSAGE_STRING))
        _loc2_: str = ''
        creator.write_utf(_loc2_)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def droidBuildingDialog(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.DROID_BUILDING_DIALOG
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.DROID_BUILDING_DIALOG))
        creator.write_bytes(16)# hz _loc3_.deviceGuid)
        creator.write_int(len(self.Player.droids))#len(data))
        for droid in self.Player.droids:
            creator.write_bytes(droid.guid)
            creator.write_int(droid.classNumber)
            creator.write_int(droid.level)
            creator.write_int(droid.energyCost)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def hideShip(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.HIDE_SHIP
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.HIDE_SHIP))
        creator.write_int(-13)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    #     #
    def shipDestroyed(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIP_DESTROYED
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.SHIP_DESTROYED))
        ship_destroyed = DotMap()
        creator.write_int(ship_destroyed.id)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    #     #
    def shipJumped(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIP_JUMPED
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.SHIP_JUMPED))
        location = DotMap()
        creator.write_int(location.id)  # findShip
        self.Game.id_to_conn[self.id].send(creator.get_package())

    #     #
    def clan(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CLAN
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.CLAN))
        data = parse_xml('Clans')  # Если больше 1 клан, то сломается
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.id)
            creator.write_int(_loc2_.leaderID)
            creator.write_utf(_loc2_.leaderName)
            creator.write_utf(_loc2_.logoFileName)
            creator.write_utf(_loc2_.name)
            creator.write_utf(_loc2_.shortName)
            creator.write_unsigned_byte(_loc2_.alliance)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def playerClan(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_CLAN
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.PLAYER_CLAN))
        _loc5_ = DotMap()
        creator.write_int(_loc5_.id)
        creator.write_int(_loc5_.leaderID)
        creator.write_utf(_loc5_.leaderName)
        creator.write_utf(_loc5_.logoFileName)
        creator.write_utf(_loc5_.name)
        creator.write_utf(_loc5_.shortName)
        creator.write_unsigned_byte(_loc5_.aliace)
        creator.write_utf(_loc5_.description)
        creator.write_short(_loc5_.joinRequestsCount)
        creator.write_int(_loc5_.points)
        creator.write_int(_loc5_.cash)
        creator.write_unsigned_byte(_loc5_.level)
        creator.write_unsigned_byte(_loc5_.maxMembers)
        creator.write_unsigned_byte(_loc5_.maxFriends)
        creator.write_short(_loc5_.friendRequests)
        creator.write_int(_loc5_.currentLevelPoints)
        creator.write_int(_loc5_.nextLevelPoints)
        creator.write_int(_loc5_.nextLevelCash)
        creator.write_int(_loc5_.bonuses)
        # cnt = _loc2_
        data2 = []
        creator.write_int(len(data2))
        for i in data2:
            creator.write_int(_loc5_.enemyClans)
        data2 = []
        creator.write_int(len(data2))
        for i in data2:
            creator.write_int(_loc5_.friendClans)
        data2 = []
        creator.write_int(len(data2))
        for i in data2:
            _loc4_ = DotMap(i)
            creator.write_int(_loc4_.id)
            creator.write_int(_loc4_.role)
            creator.write_utf(_loc4_.name)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def teamList(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TEAM_LIST
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.TEAM_LIST))
        _loc4_ = None  # : PlayerInfoData
        data = []
        cnt_player_team = len(data)  #
        creator.write_int(cnt_player_team)
        if cnt_player_team > 0:
            Player = DotMap()
            Player.team = DotMap()
            creator.write_int(Player.team.leaderID)
            creator.write_int(Player.team.maxMembers)
            for i in data:
                _loc4_ = DotMap(i)
                creator.write_int(_loc4_.shipId)
                creator.write_int(_loc4_.id)
                creator.write_utf(_loc4_.name)
        data = []
        creator.write_int(len(data))
        for i in data:
            _loc4_ = DotMap(i)
            creator.write_int(_loc4_.shipId)
            creator.write_int(_loc4_.id)
            creator.write_utf(_loc4_.name)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def checkValueResult(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CHECK_VALUE_RESULT
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.CHECK_VALUE_RESULT))
        _loc2_ = 5
        _loc3_ = True
        creator.write_int(_loc2_)
        creator.write_bool(_loc3_)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def acceptedClanInfo(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ACCEPTED_CLAN_INFO
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.ACCEPTED_CLAN_INFO))
        _loc2_: int = 0
        _loc3_: str = ''
        _loc4_: str = ''
        _loc5_: str = ''
        _loc6_: int = 0
        creator.write_int(_loc2_)
        creator.write_utf(_loc3_)
        creator.write_utf(_loc4_)
        creator.write_utf(_loc5_)
        creator.write_int(_loc6_)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def clanId(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CLAN_ID
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.CLAN_ID))
        player = DotMap()
        creator.write_int(player.clanId)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def clansLetters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CLANS_LETTERS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.CLANS_LETTERS))
        data = []
        for i in data:
            creator.write_utf(i)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def clansList(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CLANS_LIST
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.CLANS_LIST))
        data = []
        _loc3_ = 's'
        creator.write_utf(_loc3_)
        for i in data:
            creator.write_int(i)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def clanJoinRequests(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CLAN_JOIN_REQUESTS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.CLAN_JOIN_REQUESTS))
        _loc2_ = None  # ClanJoinRequest
        data = []
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.playerID)
            creator.write_utf(_loc2_.playerName)
            creator.write_utf(_loc2_.message)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def logged(self):
        from ..cfg.cfg_const import cfg_const
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOGGED

        creator.write_int(cfg_const['stateLoop'])
        creator.write_unsigned_byte(cfg_const['bankSendOperationFee'])
        creator.write_int(cfg_const['clanJoinCost'])
        creator.write_unsigned_byte(cfg_const['clanCreateLevelNeed'])
        creator.write_int(cfg_const['bonuses'])

        creator.write_int(self.Player.id)
        creator.write_utf(self.Player.login)
        creator.write_short(self.Player.classNumber)  #
        creator.write_short(self.Player.ship['cpu'])
        creator.write_unsigned_byte(self.Player.race)
        creator.write_unsigned_byte(self.Player.aliance)
        creator.write_unsigned_byte(self.Player.status)
        creator.write_unsigned_byte(self.Player.level)
        creator.write_int(self.Player.clanId)
        creator.write_bool(self.Player.deleteEnqueued)
        creator.write_bool(self.Player.canDelete)
        creator.write_bool(True)  # Отвечает за вход
        self.write_skills(creator, self.Player.skills)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def playerInfo(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_INFO  # PlayerInfoData
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.PLAYER_INFO))
        _loc2_ = DotMap({
            'id': 0,
            'name': 'max',
            'level': 10,
            'status': 10,
            'shipClass': 3,
            'clanId': 10,
            'aliance': 10,
            'race': 10,
            'clanPoints': 10,
            'role': 10
        })
        print('PLAYER INFO STATIC SEND')
        creator.write_int(_loc2_.id)
        creator.write_utf(_loc2_.name)
        creator.write_unsigned_byte(_loc2_.level)
        creator.write_unsigned_byte(_loc2_.status)
        creator.write_short(_loc2_.shipClass)
        creator.write_int(_loc2_.clanId)
        creator.write_unsigned_byte(_loc2_.aliance)
        creator.write_unsigned_byte(_loc2_.race)
        creator.write_int(_loc2_.clanPoints)
        creator.write_int(_loc2_.role)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def playerLoggedOn(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_LOGGED_ON
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.PLAYER_LOGGED_ON))
        _loc2_ = DotMap()
        creator.write_int(_loc2_.id)
        creator.write_utf(_loc2_.name)
        creator.write_int(_loc2_.clanId)
        creator.write_int(_loc2_.level)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def playerLoggedOff(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_LOGGED_OFF
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.PLAYER_LOGGED_OFF))
        _loc2_ = DotMap()
        creator.write_int(_loc2_.id)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def friendClans(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.FRIEND_CLANS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.FRIEND_CLANS))
        data = []
        for i in data:
            ClanData = DotMap(i)
            creator.write_int(ClanData.id)
            creator.write_int(ClanData.leaderID)
            creator.write_utf(ClanData.leaderName)
            creator.write_utf(ClanData.logoFileName)
            creator.write_utf(ClanData.name)
            creator.write_utf(ClanData.shortName)
            creator.write_unsigned_byte(ClanData.aliace)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def enemyClans(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ENEMY_CLANS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.ENEMY_CLANS))
        data = []
        for i in data:
            ClanData = DotMap(i)
            creator.write_int(ClanData.id)
            creator.write_int(ClanData.leaderID)
            creator.write_utf(ClanData.leaderName)
            creator.write_utf(ClanData.logoFileName)
            creator.write_utf(ClanData.name)
            creator.write_utf(ClanData.shortName)
            creator.write_unsigned_byte(ClanData.aliace)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def friendRequests(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.FRIEND_REQUESTS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.FRIEND_REQUESTS))
        data = []
        for i in data:  # clanId Data
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.id)
            creator.write_int(_loc2_.leaderID)
            creator.write_utf(_loc2_.leaderName)
            creator.write_utf(_loc2_.logoFileName)
            creator.write_utf(_loc2_.name)
            creator.write_utf(_loc2_.shortName)
            creator.write_unsigned_byte(_loc2_.aliace)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def droidEvent(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.DROID_EVENT
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.DROID_EVENT))
        _loc2_ = DotMap()
        _loc3_ = 5
        _loc4_ = 5
        creator.write_unsigned_byte(_loc2_.id)
        creator.write_short(_loc2_.type)
        creator.write_short(_loc2_.weaponClass)
        creator.write_int(_loc3_)
        creator.write_unsigned_byte(_loc4_)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def updateValue(self, num_pack, value=0):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.UPDATE_VALUE
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.UPDATE_VALUE))
        creator.write_unsigned_byte(num_pack)
        match num_pack:
            case 1:
                 value = self.Player.Clan.cash #clan Cash
            case 2:
                value = clanPoints
            case 3:
                value = PlayerClanPoint
            case 4:
                value = ClanFriendRequests
            case 5:
                value = ClanLevel
            case 6:
                value = ClanNextLevelPoints
            case 7:
                value = ClanMaxMembers
            case 8:
                value = ClanJoinRequestStatus
            case 9:
                value = self.Player.cash
            case 10:
                value = self.Player.ControlUsed
            case 11:
                value = self.Player.ControlLeft
            case 12:
                value = self.Player.clanId
            case 13:
                value = self.Player.bonus
            case 14:
                value = 20#self.Player.HyperRadius
            case 15:
                value = 20#self.Player.HyperCost
            case 16:
                value = self.Player.ClanLeader
            case 17:
                value = self.Player.ClanBonuses
        creator.write_int(value)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def missions(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.MISSIONS
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.MISSIONS))
        _loc5_ = DotMap()
        creator.write_int(_loc5_.id)
        _loc5_.current = True
        _loc6_ = 6
        _loc7_ = 7
        creator.write_unsigned_byte(_loc6_)
        creator.write_unsigned_byte(_loc7_)
        data_reachable_system = []
        creator.write_unsigned_byte(len(data_reachable_system))
        for i in data_reachable_system:
            _loc5_ = DotMap(i)
            creator.write_int(_loc5_.id)
        data = []  # PlanetData
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.id)
            creator.write_bytes(_loc2_.classNumber)
            creator.write_unsigned_byte(_loc2_.aliance)
            creator.write_unsigned_byte(_loc2_.race)
            creator.write_int(_loc2_.starId)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def tradeInvitation(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TRADE_INVITATION
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.TRADE_INVITATION))
        _loc2_: int = 0
        _loc3_: int = 0
        _loc4_: str = ''
        creator.write_int(_loc2_)
        creator.write_int(_loc3_)
        creator.write_utf(_loc4_)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def showTrading(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHOW_TRADING
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.SHOW_TRADING))
        _loc2_: int = 0
        _loc3_: int = 0
        _loc4_: str = ''
        _loc5_: list = []
        creator.write_int(_loc2_)
        creator.write_int(_loc3_)
        creator.write_utf(_loc4_)
        self._write_items(creator, True, True)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def toGame(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TO_GAME
        PacStr = ServerRequestStr()
        print('Пакет отправлен', PacStr.get_str(ServerRequest.TO_GAME))
        self.Game.id_to_conn[self.id].send(creator.get_package())
