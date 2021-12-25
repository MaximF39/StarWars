from python.Packages.PackagesEntry import *
from python.Static.ParseXml import parse_xml
from python.MyUtils.DotMap import DotMap
from python.Static.Type.ServerRequest import ServerRequest
from python.Packages.PackageCreator import PackageCreator


class ssssssssssss:
    count_guid = 0
    _aAvailablePackages: list = list()
    _iStateKey: int
    _iLastPackageLength: int
    _iLastServerRequest: int
    _aBuffer: bytearray
    # _iLastTime: int = getTimer()
    lastFiveStateKeys: list = list()
    stateLoop: int
    Game: StarWarsClass

    def __init__(self, id_, StarWars: StarWarsClass):
        self.id = id_
        self.Game = StarWars

    @staticmethod
    def isValidPackageLength(creator: int) -> bool:
        return 0 <= creator < 60000

    # def _parsePackages(self) -> bytearray:
    #     _loc1_: BasePackage = None
    #     _loc2_: int = 0
    #     _loc3_: int = 0
    #     _loc4_: BasePackage = None
    #
    #     if self._iLastPackageLength > 0 and self._aBuffer.bytesAvailable >= self._iLastPackageLength:
    #         if ServerRequest.isValid(self._iLastServerRequest) and isValidPackageLength(self._iLastPackageLength):
    #             _loc1_ = BasePackage()
    #             _loc1_.type = self._iLastServerRequest
    #             self._aBuffer.write_bytes(_loc1_, 0, self._iLastPackageLength)
    #             self._aAvailablePackages.append(_loc1_)
    #         else:
    #             self.resetBuffer()
    #
    #     _loc5_: bool = False
    #     while self._aBuffer.bytesAvailable >= 8 and not _loc5_:
    #         _loc2_ = self._iLastServerRequest = self._aBuffer.write_int()
    #         _loc3_ = self._iLastPackageLength = self._aBuffer.write_int()
    #         if self._iLastServerRequest == ServerRequest.ASTEROIDS:
    #             self._iLastServerRequest.tostr()
    #         if not ServerRequest.isValid(self._iLastServerRequest) or not self.isValidPackageLength(self._iLastPackageLength):
    #             self.resetBuffer()
    #             _loc5_ = True
    #         else:
    #             if self._aBuffer.bytesAvailable >= self._iLastPackageLength:
    #                 _loc4_ = BasePackage()
    #                 _loc4_.type = self._iLastServerRequest
    #             if self._iLastPackageLength > 0:
    #                 self._aBuffer.write_bytes(_loc4_, 0, self._iLastPackageLength)
    #             self._aAvailablePackages.append(_loc4_)
    #     else:
    #         _loc5_ = True

    # def process(self, creator: socket) -> bytearray:
    #     if creator.bytesAvailable == 0:
    #         return
    #     self._Traffic.input(creator.bytesAvailable)
    #     creator.write_bytes(self._aBuffer, len(self._aBuffer), creator.bytesAvailable)
    #     self._parsePackages()
    #     if self._aBuffer.bytesAvailable == 0:
    #         self.resetBuffer()
    #     try:
    #         processPackages()
    #         return
    #     except:
    #         (oError:Error)
    #     return

    def processPackages(self, _loc1_: ServerRequest, *args) -> bytearray:
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
                return self.online(*args)
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

    def tradingCash(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TRADING_CASH
        creator.write_int(5)
        return creator.get_package()

    def tradeAccept(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TRADE_ACCEPTED
        creator.write_bool(bool())
        return creator.get_package()

    # def flash_connect(self) -> bytearray:
    #     creator = PackageCreator
    #
    #     def read_f():
    #         with open('test.txt', 'r') as f:
    #             return f.read()
    #
    #     # return PackageCreator().converter(read_f())
    #     return creator.get_package()
    #

    def shipUpdateInfo(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIP_UPDATE_INFO
        # _loc2_: Restriction = None
        # _loc3_: ShipFeature = None
        # _loc4_: int = 0
        # _loc5_: ResourceCost = None
        # _loc6_: ShipForSale
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
        return creator.get_package()

    def finishTrading(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.FINISH_TRADING
        _loc2_ = 0
        creator.write_int(_loc2_)
        self._write_items(creator, True, False, False)
        _loc4_: int = 0
        creator.write_int(_loc4_)
        self._write_items(creator, True, False, False)
        return creator.get_package()

    def tradeSellItems(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TRADE_SELL_ITEMS
        self._write_items(creator, True, True)
        return creator.get_package()

    def tradeBuyItems(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TRADE_BUY_ITEMS
        self._write_items(creator, True, True)
        return creator.get_package()

    def playerAngar(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_ANGAR
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
        return creator.get_package()

    #
    def updateHold(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.UPDATE_HOLD
        update_hold = bool()
        creator.write_bool(update_hold)
        self._write_items(creator, True, True, True, update_hold)
        self._write_items(creator, True, True, True, update_hold)
        return creator.get_package()

    def gineticLabOptions(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.GINETIC_LAB_OPTIONS
        data = []
        creator.write_unsigned_byte(len(data))
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_unsigned_byte(_loc2_.option)
            creator.write_int(_loc2_.cost)
        return creator.get_package()

    def npcMessage(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.NPC_MESSAGE
        npc_message = DotMap()
        creator.write_int(npc_message.message)  # message SystemMessageType
        creator.write_int(npc_message.avatar)  # avatar
        return creator.get_package()

    def additionalQuestMessage(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ADDITIONAL_QUEST_MESSAGE
        _loc2_: int = 0
        _loc3_: int = 0
        creator.write_int(_loc2_)
        creator.write_int(_loc3_)
        return creator.get_package()

    def arenaRequests(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ARENA_REQUESTS
        # _loc2_: BattleRequest = None
        # _loc3_: list = list()
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
        return creator.get_package()

    #     #
    def battleRequestChanged(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.BATTLE_REQUEST_CHANGED
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
        return creator.get_package()

    def questsJournal(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.QUESTS_JOURNAL
        data = []
        creator.write_int(len(data))
        _loc5_: int = 0
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.questId)
            creator.write_int(_loc2_.giverType)
            creator.write_utf(_loc2_.giverName)
            creator.write_utf(_loc2_.Name)
        return creator.get_package()

    def activeDevices(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ACTIVE_DEVICES
        data_active_device = active_device(self.Game, self.id)
        print(data_active_device)
        creator.write_unsigned_byte(len(data_active_device))
        for i in data_active_device:
            _loc3_ = DotMap(i)
            creator.write_short(_loc3_.id)
            creator.write_bytes(_loc3_.guid)
            creator.write_float(_loc3_.reloadedTime)

        return creator.get_package()

    #     #
    def activeWeapons(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ACTIVE_WEPONS
        data_active_weapons = active_weapons(self.Game, self.id)
        creator.write_unsigned_byte(len(data_active_weapons))
        for i in data_active_weapons:
            _loc2_ = i
            creator.write_short(_loc2_['classfloat'])
            creator.write_unsigned_byte(_loc2_["index"])
        return creator.get_package()

    #     #
    def playerShipUpdate(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_SHIP_UPDATE
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
        return creator.get_package()

    #     #
    def tradingShips(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TRADING_SHIPS

        ship = DotMap()

        creator.write_int(ship.id)  # id
        creator.write_int(ship.cost)  # ship cost
        creator.write_float(ship.buy_coef)  # buyCoeficient
        creator.write_float(ship.sell_coef)  # sellCoeficient

        data = []
        creator.write_int(len(data))
        _loc14_: list = list()
        _loc15_: int = 0
        for i in data:
            _loc6_ = DotMap(i)
            creator.write_bytes(_loc6_.id)
            creator.write_short(_loc6_.classNumber)
            creator.write_int(_loc6_.cost)
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
            data_restr = []
            creator.write_unsigned_byte(len(data_restr))
            for i in data_restr:
                _loc4_ = DotMap(i)
                creator.write_unsigned_byte(_loc4_.type)
                creator.write_unsigned_byte(_loc4_.valueType)
                creator.write_int(_loc4_.value)
            data_ship_feature = []
            creator.write_unsigned_byte(len(data_ship_feature))
            for i in data_ship_feature:
                _loc5_ = DotMap(i)
                creator.write_unsigned_byte(_loc5_.type)
                creator.write_int(_loc5_.value)

            creator.write_bool(_loc6_.satisfying)
            return creator.get_package()

    def tradingItems(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TRADING_ITEMS
        _loc2_ = DotMap()
        _loc3_ = DotMap()
        _loc4_ = DotMap()
        creator.write_int(_loc2_)  # id
        creator.write_float(_loc3_)  # buyCoeficient
        creator.write_float(_loc4_)  # sellCoeficient
        self._write_items(creator, True, True, True, True)
        self._write_items(creator, True, True, True, True)
        return creator.get_package()

    #     #
    def resourceUpdate(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.RESOURCE_UPDATE_INFO
        ss = 22
        creator.write_int(ss)  # id
        self._write_items(creator, True, True)
        self._write_items(creator, True, True)
        return creator.get_package()

    def _write_items(self, creator, param2: bool, param3: bool, param4: bool = True,
                     param5: bool = False) -> None:
        data = []
        creator.write_int(len(data))
        for i in data:
            _loc6_ = DotMap(i)
            creator.write_int(_loc6_.classNumber)
            creator.write_bytes(_loc6_.guid)
            creator.write_int(_loc6_.wear)
            if param4:
                _loc6_.level = 0
                creator.write_int(_loc6_.level)
            else:
                _loc6_.level = 1
            if param2:
                _loc6_.zeroCost = 0
                creator.write_bool(_loc6_.zeroCost)
            if param5:
                creator.write_int(12)  # random don't use
            if param3:
                _loc6_.satisfying = False
                creator.write_bool(_loc6_.satisfying)

    def shipsPosition(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIPS_POSITION
        data_ship_position = ship_position(self.Game, self.id)
        creator.write_int(len(data_ship_position))
        for i in data_ship_position:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.id)
            creator.write_short(_loc2_.x)
            creator.write_short(_loc2_.y)
            creator.write_short(_loc2_.targetX)
            creator.write_short(_loc2_.targetY)
        return creator.get_package()

    #     #
    def shipsState(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIPS_STASE
        data_ship_state = ship_state(self.Game, self.id)
        for i in data_ship_state:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.id)
            creator.write_unsigned_byte(_loc2_.speed)
            creator.write_short(_loc2_.health)
            creator.write_short(_loc2_.energy)
            creator.write_short(_loc2_.PlayerRelation)
        return creator.get_package()

    def weaponTroubles(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.WEAPON_TROUBLES
        data = []
        creator.write_unsigned_byte(len(data))
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_unsigned_byte(_loc2_.trouble)
            creator.write_unsigned_byte(_loc2_.index)
        return creator.get_package()

    def repository(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.REPOSITORY
        _loc2_ = DotMap()
        data = []
        self._write_items(creator, False, False)
        _loc4_ = DotMap()
        creator.write_float(_loc4_.costCoef)  # costCoef
        creator.write_int(len(data))
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.classNumber)
            creator.write_bytes(_loc2_.guid)
            creator.write_int(_loc2_.wear)
            creator.write_int(_loc2_.level)
            creator.write_int(12)  # random don't use
        return creator.get_package()

    def clanrepository(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CLAN_REPOSITORY
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
        return creator.get_package()

    def planetsState(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLANETS_STATE
        data = []
        creator.write_unsigned_byte(len(data))
        for i in data:
            _loc1_ = DotMap(i)
            creator.write_int(_loc1_.id)  # id planet
            creator.write_float(_loc1_.angel)  # angel
        return creator.get_package()

    def planetsUpdate(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLANETS_UPDATE
        data = []
        creator.write_unsigned_byte(len(data))
        for i in data:
            _loc1_ = DotMap(i)
            creator.write_int(_loc1_.id)
            creator.write_float(_loc1_.angel)
            creator.write_bytes(_loc1_.race)
            creator.write_bytes(_loc1_.aliance)
            creator.write_int(_loc1_.clanID)
        return creator.get_package()

    #     #
    def ship(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIP
        _loc3_ = DotMap()
        creator.write_short(_loc3_.race)
        creator.write_int(_loc3_.id)
        creator.write_utf(_loc3_.Name)
        creator.write_short(_loc3_.size)
        creator.write_float(_loc3_.setPosition[0])
        creator.write_float(_loc3_.setPosition[1])
        creator.write_int(_loc3_.player.level)
        creator.write_short(_loc3_.maxHealth)
        creator.write_short(_loc3_.maxEnergy)
        creator.write_int(_loc3_.player.avatar)
        creator.write_unsigned_byte(_loc3_.maxSpeed)
        creator.write_float(_loc3_.setMovePoint[0])
        creator.write_float(_loc3_.setMovePoint[1])
        creator.write_unsigned_byte(_loc3_.player.aliance)
        creator.write_unsigned_byte(_loc3_.player.status)
        creator.write_int(_loc3_.player.clanId)
        drodata = _loc3_.droid
        creator.write_unsigned_byte(len(drodata))
        for i in drodata:
            _loc2_ = DotMap(i)
            creator.write_unsigned_byte(_loc2_.id)
            creator.write_short(_loc2_.type)
            creator.write_short(_loc2_.weaponClass)
            creator.write_short(_loc2_.health)
        return creator.get_package()

    #     #
    def planet(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLANET
        _loc2_ = DotMap()
        creator.write_bytes(_loc2_.classNumber)
        creator.write_int(_loc2_.id)
        creator.write_unsigned_byte(_loc2_.race)
        creator.write_int(_loc2_.radius)
        creator.write_int(_loc2_.size)
        creator.write_float(_loc2_.serverAngle)
        creator.write_bool(_loc2_.landable)
        return creator.get_package()

    def inventory(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.INVENTORY
        data = []
        _loc5_: int = creator.write_short(len(data))
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_short(_loc2_.ItemClass)
            creator.write_bytes(_loc2_.guid)
            creator.write_short(_loc2_.wear)
            creator.write_bool(_loc2_.inUsing)
            creator.write_unsigned_byte(_loc2_.level)
            creator.write_bool(_loc2_.satisfying)
        ship = DotMap()
        creator.write_unsigned_byte(ship.armor)
        creator.write_unsigned_byte(ship.shields)
        creator.write_short(ship.usedSpace)
        creator.write_short(ship.cpu)
        creator.write_short(ship.cpuUsed)
        creator.write_unsigned_byte(ship.level)
        creator.write_unsigned_byte(ship.maxDroids)
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_short(_loc2_.ItemClass)
            creator.write_bytes(_loc2_.id)
        return creator.get_package()

    def player(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER
        Player = player(self.Game, self.id)
        creator.write_int(Player.id)
        creator.write_utf(Player.login)
        creator.write_int(Player.level)
        creator.write_int(Player.cash)
        creator.write_unsigned_byte(Player.race)
        creator.write_int(Player.avatar)
        creator.write_unsigned_byte(Player.aliance)
        creator.write_int(Player.clanId)
        creator.write_int(Player.role)
        creator.write_unsigned_byte(Player.clanRequestStatus)
        creator.write_unsigned_byte(Player.clanJoinRequestStatus)
        creator.write_int(Player.PlayerRelation)
        return creator.get_package()

    #     #
    def questMessage(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.QUEST_MESSAGE
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
        return creator.get_package()

    def playerSkills(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_SKILLS_DATA
        player_skills_data = player_skills(self.Game, self.id)
        creator.write_unsigned_byte(player_skills_data.level)
        creator.write_int(player_skills_data.experience)
        creator.write_int(player_skills_data.expForNext)
        self.write_skills(creator, player_skills_data)
        creator.write_int(player_skills_data.freeSkills)
        creator.write_int(player_skills_data.expForFirstSkillLevel)
        creator.write_float(player_skills_data.expSkillGrowCoef)
        creator.write_float(player_skills_data.expSkillReduserCoef)
        creator.write_unsigned_byte(player_skills_data.maxSkill)

        player_statistics = DotMap()
        creator.write_unsigned_byte(player_statistics.status)
        creator.write_unsigned_byte(player_statistics.level)
        creator.write_int(player_statistics.pirateStatus)
        creator.write_int(player_statistics.policeStatus)
        creator.write_int(player_statistics.forNextLevel)
        return creator.get_package()

    @staticmethod
    def write_skills(creator, param2) -> None:
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

    def playerSkillsData(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_SKILLS_DATA
        data_player_skills = player_skills_data(self.Game, self.id)
        creator.write_unsigned_byte(data_player_skills[0]["level"])
        creator.write_int(data_player_skills[0]["experience"])
        creator.write_int(data_player_skills[0]["expForNext"])
        self.write_skills(creator, DotMap(data_player_skills[0]['skills']))
        creator.write_int(data_player_skills[0]["freeSkills"])
        creator.write_int(data_player_skills[0]["expForFirstSkillLevel"])
        creator.write_float(data_player_skills[0]["expSkillGrowCoef"])
        creator.write_float(data_player_skills[0]["expSkillReduserCoef"])
        creator.write_unsigned_byte(data_player_skills[0]["maxSkill"])

        creator.write_unsigned_byte(data_player_skills[1]['status'])
        creator.write_unsigned_byte(data_player_skills[1]['level'])
        creator.write_int(data_player_skills[1]['pirateStatus'])
        creator.write_int(data_player_skills[1]['policeStatus'])
        return creator.get_package()

    def playerShip(self) -> bytearray:
        ship = player_ship(self.Game, self.id)
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_SHIP
        creator.write_int(3) # raca
        # creator.write_int(1) #
        creator.write_int(ship.id)
        creator.write_utf(ship.login)
        creator.write_int(ship.size)
        creator.write_int(ship.energy)
        creator.write_int(ship.maxEnergy)
        creator.write_float(ship.setPosition[0])
        creator.write_float(ship.setPosition[1])
        creator.write_int(ship.team)
        creator.write_unsigned_byte(ship.maxSpeed)
        creator.write_unsigned_byte(ship.weaponSlots)
        creator.write_unsigned_byte(ship.deviceSlots)
        creator.write_int(ship.maxHealth)
        creator.write_short(ship.radarRadius)
        creator.write_short(ship.cpu)
        return creator.get_package()

    def weaponsParameters(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.WEAPONS_PARAMETERS
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
        return creator.get_package()

    #     #
    def ammoParameters(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.AMMOS_PARAMETERS
        data_ammo = parse_xml("AmmoParameters")
        cnt_ammo: int = len(data_ammo)
        creator.write_int(cnt_ammo)
        for i in data_ammo:
            _loc2_ = DotMap(i)  # AmmoParameters()
            creator.write_int(_loc2_.classNumber)
            creator.write_float(_loc2_.size)
            creator.write_int(_loc2_.cost)
            creator.write_int(_loc2_.damage)
        return creator.get_package()

    def resourceParameters(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.RESOURCE_PARAMETERS
        data_resourse = parse_xml('ResourseParameters')
        creator.write_int(len(data_resourse))
        for i in data_resourse:
            _loc2_ = DotMap(i)  # ResourceParameters()
            creator.write_int(_loc2_.classNumber)
            creator.write_float(_loc2_.size)
            creator.write_int(_loc2_.cost)
        return creator.get_package()

    def deviceParameters(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.DEVICE_PARAMETERS
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
        return creator.get_package()

    def droidParameters(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.DROID_PARAMETERS
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
        return creator.get_package()

    #     #
    def shipParameters(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIP_PARAMETERS
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
        return creator.get_package()

    def engineParameters(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ENGINES_PARAMETERS
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
        return creator.get_package()

    #     #
    def map(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.MAP
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
        return creator.get_package()

    def reachableSystems(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.REACHABLE_SYSTEMS
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
        return creator.get_package()

    #     #
    def version(self) -> bytearray:
        creator = PackageCreator()
        version = '0.9.0.1'
        creator.PackageNumber = ServerRequest.VERSION
        creator.write_utf(version)
        return creator.get_package()

    def shipHealth(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIP_HEALTH
        ship = DotMap
        creator.write_int(ship.id)
        creator.write_int(ship.health)
        return creator.get_package()

    def online(self, cnt_online) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ONLINE
        creator.write_int(1)
        creator.write_int(cnt_online)
        return creator.get_package()

    def topList(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TOP_LIST
        all_player = top_list()
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
        return creator.get_package()

    def topRatingList(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TOP_RATING_LIST
        top_players = top_rating_list()
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
        return creator.get_package()

    def topClansList(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TOP_CLANS_LIST
        players = top_clan_list()
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
        return creator.get_package()

        #
        # def auctionList(self) -> bytearray:
        #     creator = PackageCreator()
        #     creator.PackageNumber = ServerRequest.AUCTION_SHOP_PACKAGE
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
        #     return creator.get_package()

    def newsList(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.NEWS_LIST
        data = []
        creator.write_int(len(data))
        for i in data:
            creator.write_utf(i)  # text
        return creator.get_package()

    def Evil(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.EVIL
        _loc2_ = ''
        creator.write_utf(_loc2_)
        return creator.get_package()

    def locationPlanet(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOCATION_PLANET

        _loc4_ = DotMap()
        creator.write_bytes(_loc4_.classNumber)
        creator.write_int(_loc4_.id)
        creator.write_unsigned_byte(_loc4_.race)
        creator.write_int(_loc4_.radius)
        creator.write_int(_loc4_.size)
        creator.write_unsigned_byte(_loc4_.aliance)
        creator.write_int(_loc4_.clanID)
        creator.write_float(_loc4_.angle)
        creator.write_unsigned_byte(_loc4_.QCount)
        shop_data = _loc4_.shop
        creator.write_short(len(shop_data))
        for i in shop_data:
            _loc3_ = DotMap(i)
            creator.write_int(_loc3_.id)
            creator.write_unsigned_byte(_loc3_.type)

        player_info_data = []
        for i in player_info_data:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.id)
            creator.write_utf(_loc2_.name)
            creator.write_int(_loc2_.clanId)
            creator.write_int(_loc2_.level)

        return creator.get_package()

    def planetQuests(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLANET_QUESTS
        data = []
        creator.write_short(len(data))
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.questId)
            creator.write_int(_loc2_.giverType)
            creator.write_utf(_loc2_.giverName)
            creator.write_utf(_loc2_.Name)
        return creator.get_package()

    def locationSystem(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOCATION_SYSTEM
        location, players, planets, static_space_objects = location_system(self.Game, self.id)
        creator.write_int(location[0]) # id
        creator.write_float(location[1])  # location.x
        creator.write_float(location[2])  # location.y
        creator.write_unsigned_byte(location[3])  # location.sector
        creator.write_short(len(players))
        for i in players:
            _loc2_ = DotMap(i)
            creator.write_short(_loc2_.race)
            creator.write_int(_loc2_.id)
            creator.write_utf(_loc2_.Name)
            creator.write_short(_loc2_.size)
            creator.write_float(_loc2_.set_x)  # setPosition
            creator.write_float(_loc2_.set_y)
            creator.write_int(_loc2_.player.level)
            creator.write_short(_loc2_.maxHealth)
            creator.write_short(_loc2_.maxEnergy)
            creator.write_int(_loc2_.player.avatar)
            creator.write_unsigned_byte(int(_loc2_.maxSpeed))
            creator.write_float(_loc2_.mov_x)
            creator.write_float(_loc2_.mov_y)  # setMovePoint
            creator.write_unsigned_byte(_loc2_.player.aliance)
            creator.write_unsigned_byte(_loc2_.player.status)
            creator.write_int(_loc2_.player.clanId)

            creator.write_unsigned_byte(len(_loc2_.droid))

            for droid in _loc2_.droid:
                _loc4_ = DotMap(droid)
                creator.write_unsigned_byte(_loc4_.id)
                creator.write_short(_loc4_.type)
                creator.write_short(_loc4_.weaponClass)
                creator.write_short(_loc4_.health)

        creator.write_short(len(planets))
        for planet in planets:
            _loc6_ = DotMap(planet)
            creator.write_unsigned_byte(_loc6_.PlanetClass)
            creator.write_int(_loc6_.id)
            creator.write_unsigned_byte(_loc6_.race)
            creator.write_int(_loc6_.radius)
            creator.write_int(_loc6_.size)
            creator.write_float(_loc6_.angle)
            creator.write_bool(_loc6_.landable)
            creator.write_unsigned_byte(_loc6_.aliance)
            creator.write_int(_loc6_.clanID)

        creator.write_short(len(static_space_objects))
        for static_space_object in static_space_objects:
            _loc7_ = DotMap(static_space_object)
            creator.write_int(_loc7_.StaticSpaceObjectType)
            creator.write_int(_loc7_.id)
            creator.write_float(_loc7_.x)
            creator.write_float(_loc7_.y)
            creator.write_bool(_loc7_.landable)

        return creator.get_package()

    def locationBattle(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOCATION_BATTLE
        _loc6_ = DotMap()
        creator.write_int(_loc6_.id)
        creator.write_float(_loc6_.x)
        creator.write_float(_loc6_.y)
        player_info_data = []
        creator.write_short(len(player_info_data))
        for i in player_info_data:
            ship_data = DotMap(i)
            creator.write_short(ship_data.race)
            creator.write_int(ship_data.id)
            creator.write_utf(ship_data.Name)
            creator.write_short(ship_data.size)
            creator.write_float(ship_data.setPosition[0])
            creator.write_float(ship_data.setPosition[1])
            creator.write_int(ship_data.player)
            creator.write_short(ship_data.maxHealth)
            creator.write_short(ship_data.maxEnergy)
            creator.write_int(ship_data.player)
            creator.write_unsigned_byte(ship_data.player.aliance)
            creator.write_unsigned_byte(ship_data.player.status)
            creator.write_int(ship_data.player.clanID)
            drodata = []
            creator.write_unsigned_byte(len(drodata))
            for i in drodata:
                _loc4_ = DotMap(i)
                creator.write_unsigned_byte(_loc4_.id)
                creator.write_short(_loc4_.type)
                creator.write_short(_loc4_.weaponClass)
                creator.write_short(_loc4_.health)
        return creator.get_package()

    def shoots(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHOOTS
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
        return creator.get_package()

    #     #
    def items(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ITEMS
        data = []
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.id)
            creator.write_short(_loc2_.classNumber)
            creator.write_short(_loc2_.x)
            creator.write_short(_loc2_.y)
        return creator.get_package()

    def message(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.MESSAGE
        _loc2_ = DotMap({
            "from_player": 'Max223',
            "text": "Hello",
            "type": 1,
            "isPrivate": False,
            "isAdmin": False,
        })
        creator.write_utf(_loc2_.from_player)  # name player
        creator.write_utf(_loc2_.text)
        creator.write_unsigned_byte(_loc2_.type)  # 1 - global  2 - local 3 - clan 4 - trade 5 - client chat
        creator.write_bool(_loc2_.isPrivate)
        creator.write_bool(_loc2_.isAdmin)
        return creator.get_package()

    #     #
    def asteroids(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ASTEROIDS
        data = []
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.id)
            creator.write_float(_loc2_.x)
            creator.write_float(_loc2_.y)
            creator.write_float(_loc2_.targetX)
            creator.write_float(_loc2_.targetY)
            creator.write_unsigned_byte(_loc2_.speed)
            creator.write_int(_loc2_.size)
        return creator.get_package()

    def effectCreated(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.EFFECT_CREATED
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
        return creator.get_package()

    def effectRemoved(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.EFFECT_REMOVED
        _loc2_: int = 0
        _loc3_: int = 0
        creator.write_int(_loc2_)
        creator.write_unsigned_byte(_loc3_)
        return creator.get_package()

    def logMessage(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOG_MESSAGE
        _loc2_: int = 0
        _loc3_: int = 0
        creator.write_int(_loc2_)
        creator.write_int(_loc3_)
        return creator.get_package()

    def logMessagestr(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOG_MESSAGE_STRING
        _loc2_: str = ''
        creator.write_utf(_loc2_)
        return creator.get_package()

    def systemMessage(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SYSTEM_MESSAGE
        _loc2_ = 6
        _loc3_ = 5
        creator.write_int(_loc2_)  # SystemMessageType
        creator.write_int(_loc3_)  # hz
        return creator.get_package()

    def systemMessagestr(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SYSTEM_MESSAGE_STRING
        _loc2_: str = ''
        creator.write_utf(_loc2_)
        return creator.get_package()

    def droidBuildingDialog(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.DROID_BUILDING_DIALOG
        _loc3_ = DotMap()
        creator.write_bytes(_loc3_.deviceGuid)
        data = []
        creator.write_int(len(data))
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_bytes(_loc2_.guid)
            creator.write_int(_loc2_.classNumber)
            creator.write_int(_loc2_.level)
            creator.write_int(_loc2_.energyCost)
        return creator.get_package()

    def hideShip(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.HIDE_SHIP
        _loc2_ = hide_ship(self.Game, self.id)
        creator.write_int(_loc2_)
        return creator.get_package()

    #     #
    def shipDestroyed(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIP_DESTROYED
        ship_destroyed = DotMap()
        creator.write_int(ship_destroyed.id)
        return creator.get_package()

    #     #
    def shipJumped(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIP_JUMPED
        location = DotMap()
        creator.write_int(location.id)  # findShip
        return creator.get_package()

    #     #
    def clan(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CLAN
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
        return creator.get_package()

    def playerClan(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_CLAN
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
        return creator.get_package()

    def teamList(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TEAM_LIST
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
        return creator.get_package()

    def checkValueResult(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CHECK_VALUE_RESULT
        _loc2_ = 5
        _loc3_ = True
        creator.write_int(_loc2_)
        creator.write_bool(_loc3_)
        return creator.get_package()

    def acceptedClanInfo(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ACCEPTED_CLAN_INFO
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
        return creator.get_package()

    def clanId(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CLAN_ID
        player = DotMap()
        creator.write_int(player.clanId)
        return creator.get_package()

    def clansLetters(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CLANS_LETTERS
        data = []
        for i in data:
            creator.write_utf(i)
        return creator.get_package()

    def clansList(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CLANS_LIST
        data = []
        _loc3_ = 's'
        creator.write_utf(_loc3_)
        for i in data:
            creator.write_int(i)
        return creator.get_package()

    def clanJoinRequests(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CLAN_JOIN_REQUESTS
        _loc2_ = None  # ClanJoinRequest
        data = []
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.playerID)
            creator.write_utf(_loc2_.playerName)
            creator.write_utf(_loc2_.message)
        return creator.get_package()

    def logged(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOGGED
        _logged = logged()
        creator.write_int(_logged.stateLoop)
        creator.write_unsigned_byte(_logged.bankSendOperationFee)
        creator.write_int(_logged.clanJoinCost)
        creator.write_unsigned_byte(_logged.clanCreateLevelNeed)
        creator.write_int(_logged.bonuses)
        # while True:
        _loc2_ = logged2(self.Game, self.id)
        creator.write_int(_loc2_.id)
        creator.write_utf(_loc2_.name)
        creator.write_short(_loc2_.shipClass)
        creator.write_short(_loc2_.shipCPU)
        creator.write_unsigned_byte(_loc2_.race)
        creator.write_unsigned_byte(_loc2_.aliance)
        creator.write_unsigned_byte(_loc2_.status)
        creator.write_unsigned_byte(_loc2_.level)
        creator.write_int(_loc2_.clanId)
        creator.write_bool(_loc2_.deleteEnqueued)
        creator.write_bool(_loc2_.canDelete)
        creator.write_bool(_loc2_.logged)
        self.write_skills(creator, _loc2_.skills)
        return creator.get_package()

    def playerInfo(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_INFO  # PlayerInfoData
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
        return creator.get_package()

    def playerLoggedOn(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_LOGGED_ON
        _loc2_ = DotMap()
        creator.write_int(_loc2_.id)
        creator.write_utf(_loc2_.name)
        creator.write_int(_loc2_.clanId)
        creator.write_int(_loc2_.level)
        return creator.get_package()

    def playerLoggedOff(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_LOGGED_OFF
        _loc2_ = DotMap()
        creator.write_int(_loc2_.id)
        return creator.get_package()

    def friendClans(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.FRIEND_CLANS
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
        return creator.get_package()

    def enemyClans(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ENEMY_CLANS
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
        return creator.get_package()

    def friendRequests(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.FRIEND_REQUESTS
        data = []
        for i in data:  # clan Data
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.id)
            creator.write_int(_loc2_.leaderID)
            creator.write_utf(_loc2_.leaderName)
            creator.write_utf(_loc2_.logoFileName)
            creator.write_utf(_loc2_.name)
            creator.write_utf(_loc2_.shortName)
            creator.write_unsigned_byte(_loc2_.aliace)
        return creator.get_package()

    def droidEvent(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.DROID_EVENT
        _loc2_ = DotMap()
        _loc3_ = 5
        _loc4_ = 5
        creator.write_unsigned_byte(_loc2_.id)
        creator.write_short(_loc2_.type)
        creator.write_short(_loc2_.weaponClass)
        creator.write_int(_loc3_)
        creator.write_unsigned_byte(_loc4_)
        return creator.get_package()

    def updateValue(self, num_pack, value=0) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.UPDATE_VALUE
        creator.write_unsigned_byte(num_pack)
        creator.write_int(value)
        return creator.get_package()

    def missions(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.MISSIONS
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
        return creator.get_package()

    def tradeInvitation(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TRADE_INVITATION
        _loc2_: int = 0
        _loc3_: int = 0
        _loc4_: str = ''
        creator.write_int(_loc2_)
        creator.write_int(_loc3_)
        creator.write_utf(_loc4_)
        return creator.get_package()

    def showTrading(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHOW_TRADING
        _loc2_: int = 0
        _loc3_: int = 0
        _loc4_: str = ''
        _loc5_: list = []
        creator.write_int(_loc2_)
        creator.write_int(_loc3_)
        creator.write_utf(_loc4_)
        self._write_items(creator, True, True)
        return creator.get_package()

    @staticmethod
    def toGame() -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TO_GAME
        return creator.get_package()
