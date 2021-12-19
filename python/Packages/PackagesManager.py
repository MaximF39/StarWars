from python.Static.ParseXml import parse_xml
from python.MyUtils.DotMap import DotMap
from python.Static.PlanetClass import PlanetClass
from python.Static.Race import Race
from python.Static.ServerRequest import ServerRequest
from .PackageCreator import PackageCreator
from python.Static.StaticSpaceObjectType import StaticSpaceObjectType


class PackagesManager:
    _aAvailablePackages: list
    _iStateKey: int
    _iLastPackageLength: int
    _iLastServerRequest: int
    _aBuffer: bytearray
    # _iLastTime: int = getTimer()
    lastFiveStateKeys: list = list()
    stateLoop: int

    # def initialize(self):
    #     self._aAvailablePackages = list()
    #
    # def isValidPackageLength(self, creator: int) -> bool:
    #     return 0 <= creator < 60000

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
            # case
            case ServerRequest.SHIPS_POSITION:
                return self.shipsPosition()
            case ServerRequest.SHIPS_STASE:
                return self.shipsState()
            #     case ServerRequest.MESSAGE:
            #         return self.message()
            #     case ServerRequest.PLAYER_SHIP_UPDATE:
            #         return self.playerShipUpdate()
            #     case ServerRequest.PLANETS_STATE:
            #         return self.planetsState()
            #     case ServerRequest.PLANETS_UPDATE:
            #         return self.planetsUpdate()
            #     case ServerRequest.REPOSITORY:
            #         return self.repository()
            #     case ServerRequest.CLAN_REPOSITORY:
            #         return self.clanrepository()
            #     case ServerRequest.WEAPON_TROUBLES:
            #         return self.weaponTroubles()
            #     case ServerRequest.SHIP:
            #         return self.ship()
            #     case ServerRequest.SHOOTS:
            #         return self.shoots()
            #     case ServerRequest.ITEMS:
            #         return self.items()
            case ServerRequest.ACTIVE_DEVICES:
                return self.activeDevices()
            case ServerRequest.ACTIVE_WEPONS:
                return self.activeWeapons()
            case ServerRequest.HIDE_SHIP:
                return self.hideShip()
            #     case ServerRequest.SHIP_DESTROYED:
            #         return self.shipDestroyed()
            #     case ServerRequest.SHIP_JUMPED:
            #         return self.shipJumped()
            #     case ServerRequest.PLANET:
            #         return self.planet()
            #     case ServerRequest.INVENTORY:
            #         return self.inventory()
            #     case ServerRequest.TRADING_ITEMS:
            #         return self.tradingItems()
            #     case ServerRequest.RESOURCE_UPDATE_INFO:
            #         return self.resourceUpdate()
            #     case ServerRequest.ASTEROIDS:
            #         return self.asteroids()
            #     case ServerRequest.EFFECT_CREATED:
            #         return self.effectCreated()
            #     case ServerRequest.LOCATION_PLANET:
            #         return self.locationPlanet()
            case ServerRequest.LOCATION_SYSTEM:
                return self.locationSystem()
            #     case ServerRequest.LOCATION_BATTLE:
            #         return self.locationBattle()
            case ServerRequest.PLAYER:
                return self.player()
            #     case ServerRequest.QUEST_MESSAGE:
            #         return self.questMessage()
            #     case ServerRequest.PLAYER_SKILLS:
            #         return self.playerSkills()
            case ServerRequest.PLAYER_SKILLS_DATA:
                return self.playerSkillsData()
            case ServerRequest.PLAYER_SHIP:
                return self.playerShip()
            #     case ServerRequest.DROID_BUILDING_DIALOG:
            #         return self.droidBuildingDialog()
            #     case ServerRequest.TRADING_SHIPS:
            #         return self.tradingShips()
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
            #     case ServerRequest.REACHABLE_SYSTEMS:
            #         return self.reachableSystems()
            #     case ServerRequest.SYSTEM_MESSAGE:
            #         return self.systemMessage()
            #     case ServerRequest.LOG_MESSAGE:
            #         return self.logMessage()
            #     case ServerRequest.LOG_MESSAGE_STRING:
            #         return self.logMessagestr()
            #     case ServerRequest.SYSTEM_MESSAGE_STRING:
            #         return self.systemMessagestr()
            case ServerRequest.MAP:
                return self.map()
            #     case ServerRequest.QUESTS_JOURNAL:
            #         return self.questsJournal()
            #     case ServerRequest.ARENA_REQUESTS:
            #         return self.arenaRequests()
            #     case ServerRequest.PLANET_QUESTS:
            #         return self.planetQuests()
            #     case ServerRequest.ADDITIONAL_QUEST_MESSAGE:
            #         return self.additionalQuestMessage()
            #     case ServerRequest.BATTLE_REQUEST_CHANGED:
            #         return self.battleRequestChanged()
            case ServerRequest.TOP_LIST:
                return self.topList()
            case ServerRequest.TOP_RATING_LIST:
                return self.topRatingList()
            case ServerRequest.TOP_CLANS_LIST:
                return self.topClansList()
            #     case ServerRequest.NEWS_LIST:
            #         return self.sList()
            # case ServerRequest.FLASH_CONNECT_REQUEST:
            #     return self.flash_connect()
            case ServerRequest.ONLINE:
                return self.online()
            case ServerRequest.VERSION:
                return self.version()
            #     case ServerRequest.SHIP_HEALTH:
            #         return self.shipHealth()
            #     case ServerRequest.NPC_MESSAGE:
            #         return self.npcMessage()
            #     case ServerRequest.UPDATE_HOLD:
            #         return self.updateHold()
            #     case ServerRequest.GINETIC_LAB_OPTIONS:
            #         return self.gineticLabOptions()
            case ServerRequest.CLAN:
                return self.clan()
            #     case ServerRequest.CHECK_VALUE_RESULT:
            #         return self.checkValueResult()
            #     case ServerRequest.ACCEPTED_CLAN_INFO:
            #         return self.acceptedClanInfo()
            #     case ServerRequest.CLAN_ID:
            #         return self.clanId()
            #     case ServerRequest.CLANS_LETTERS:
            #         return self.clansLetters()
            #     case ServerRequest.CLANS_LIST:
            #         return self.clansList()
            #     case ServerRequest.CLAN_JOIN_REQUESTS:
            #         return self.clanJoinRequests()
            # case ServerRequest.PLAYER_INFO:
            #     return self.playerInfo()

            #     case ServerRequest.PLAYER_LOGGED_ON:
            #         return self.playerLoggedOn()
            #     case ServerRequest.PLAYER_LOGGED_OFF:
            #         return self.playerLoggedOff()
            #     case ServerRequest.PLAYER_CLAN:
            #         return self.playerClan()
            #     case ServerRequest.FRIEND_CLANS:
            #         return self.friendClans()
            #     case ServerRequest.ENEMY_CLANS:
            #         return self.enemyClans()
            case ServerRequest.UPDATE_VALUE:
                return self.updateValue(*args)
            #     case ServerRequest.FRIEND_REQUESTS:
            #         return self.friendRequests()
            #     case ServerRequest.DROID_EVENT:
            #         return self.droidEvent()
            #     case ServerRequest.EFFECT_REMOVED:
            #         return self.effectRemoved()
            #     case ServerRequest.MISSIONS:
            #         return self.missions()
            case ServerRequest.TO_GAME:
                return self.toGame()
        #     case ServerRequest.PLAYER_ANGAR:
        #         return self.playerAngar()
        #     case ServerRequest.TRADE_INVITATION:
        #         return self.tradeInvitation()
        #     case ServerRequest.SHOW_TRADING:
        #         return self.showTrading()
        #     case ServerRequest.TRADING_CASH:
        #         return self.GameEngine.tradingCash(.write_int())
        #     case ServerRequest.TRADE_SELL_ITEMS:
        #         return self.tradeSellItems()
        #     case ServerRequest.EVIL:
        #         return self.Evil()
        #     case ServerRequest.TRADE_ACCEPTED:
        #         return self.GameEngine.changeTradingAccepted(.write_bool())
        #     case ServerRequest.TRADE_BUY_ITEMS:
        #         return self.tradeBuyItems()
        #     case ServerRequest.FINISH_TRADING:
        #         return self.finishTrading()
        #     case ServerRequest.SHIP_UPDATE_INFO:
        #         return self.shipUpdateInfo()
        #     case ServerRequest.TEAM_LIST:
        #         return self.teamList()

    # def flash_connect(self):
    #     creator = PackageCreator
    #
    #     def read_f():
    #         with open('test.txt', 'r') as f:
    #             return f.read()
    #
    #     # return PackageCreator().converter(read_f())
    #     return creator.get_package()
    #
    # def shipUpdateInfo(self) -> bytearray:
    #     creator = PackageCreator()
    #     _loc2_: Restriction = None
    #     _loc3_: ShipFeature = None
    #     _loc4_: int = 0
    #     _loc5_: ResourceCost = None
    #     _loc6_: ShipForSale
    #     _loc6_ = ShipForSale()
    #     creator.write_short(_loc6_.classNumber)
    #     creator.write_short(_loc6_.size)
    #     creator.write_unsigned_byte(_loc6_.weaponSlots)
    #     creator.write_unsigned_byte(_loc6_.deviceSlots)
    #     creator.write_unsigned_byte(_loc6_.armor)
    #     creator.write_unsigned_byte(_loc6_.shields)
    #     creator.write_short(_loc6_.maxEnergy)
    #     creator.write_short(_loc6_.maxHealth)
    #     creator.write_short(_loc6_.cpu)
    #     creator.write_short(_loc6_.radar)
    #     creator.write_unsigned_byte(_loc6_.maxSpeed)
    #     _loc7_ = 0
    #     creator.write_unsigned_byte(_loc7_)
    #     _loc4_ = 0
    #     while _loc4_ < _loc7_:
    #         _loc2_ = Restriction()
    #         creator.write_unsigned_byte(_loc2_.type)
    #         creator.write_unsigned_byte(_loc2_.valueType)
    #         creator.write_int(_loc2_.value)
    #     _loc4_ += 1
    #
    #     _loc8_ = 0
    #     creator.write_unsigned_byte(_loc8_)
    #     _loc4_ = 0
    #     while _loc4_ < _loc8_:
    #         _loc3_ = ShipFeature()
    #         creator.write_unsigned_byte(_loc3_.type)
    #         creator.write_int(_loc3_.value)
    #         _loc4_ += 1
    #     _loc9_: ShipForSale
    #     _loc9_ = ShipForSale()
    #     creator.write_short(_loc9_.classNumber)
    #     creator.write_short(_loc9_.size)
    #     creator.write_unsigned_byte(_loc9_.weaponSlots)
    #     creator.write_unsigned_byte(_loc9_.deviceSlots)
    #     creator.write_unsigned_byte(_loc9_.armor)
    #     creator.write_unsigned_byte(_loc9_.shields)
    #     creator.write_short(_loc9_.maxEnergy)
    #     creator.write_short(_loc9_.maxHealth)
    #     creator.write_short(_loc9_.cpu)
    #     creator.write_short(_loc9_.radar)
    #     creator.write_unsigned_byte(_loc9_.maxSpeed)
    #     _loc7_ = 0
    #     creator.write_unsigned_byte(_loc7_)
    #     _loc4_ = 0
    #     while _loc4_ < _loc7_:
    #         _loc2_ = Restriction()
    #         creator.write_unsigned_byte(_loc2_.type)
    #         creator.write_unsigned_byte(_loc2_.valueType)
    #         creator.write_int(_loc2_.value)
    #         _loc4_ += 1
    #     _loc8_ = 0
    #     creator.write_unsigned_byte(_loc8_)
    #     _loc4_ = 0
    #     while _loc4_ < _loc8_:
    #         _loc3_ = ShipFeature()
    #         creator.write_unsigned_byte(_loc3_.type)
    #         creator.write_int(_loc3_.value)
    #         _loc4_ += 1
    #     creator.write_bool(_loc9_.satisfying)
    #     _loc10_: UpdateCost
    #     _loc10_ = UpdateCost()
    #     creator.write_int(_loc10_.cash)
    #     while creator.bytesAvailable > 0:
    #         _loc5_ = ResourceCost()
    #         creator.write_short(_loc5_.classNumber)
    #         creator.write_int(_loc5_.count)
    #         creator.write_bool(_loc5_.enough)
    #     return creator.get_package()
    #
    # def finishTrading(self) -> bytearray:
    #     creator = PackageCreator()
    #     _loc2_ = 0
    #     creator.write_int(_loc2_)
    #     _loc3_: list = write_items(creator, True, False, False)
    #     _loc4_: int = 0
    #     creator.write_int(_loc4_)
    #     _loc5_: list = write_items(creator, True, False, False)
    #     return creator.get_package()
    #
    # def tradeSellItems(self) -> bytearray:
    #     creator = PackageCreator()
    #     _loc2_: list = self.write_items(creator, True, True)
    #     return creator.get_package()
    #
    # def tradeBuyItems(self) -> bytearray:
    #     creator = PackageCreator()
    #     _loc2_: list = self.write_items(creator, True, True)
    #     return creator.get_package()

    def playerAngar(self) -> bytearray:
        creator = PackageCreator()
        _loc2_: int = 0
        _loc3_: int = 0
        _loc4_ = None  # Restriction
        _loc5_ = None  # ShipFeature
        _loc6_ = None  # ShipForSale
        _loc7_: int = 0
        _loc8_: int = 0
        _loc10_ = 0
        creator.write_unsigned_byte(_loc10_)
        _loc11_: int = 0
        while _loc11_ < _loc10_:
            # _loc6_ = ShipForSale()
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
            _loc2_ = 0
            creator.write_unsigned_byte(_loc2_)
            _loc7_ = 0
            while _loc7_ < _loc2_:
                # _loc4_ = Restriction()
                creator.write_unsigned_byte(_loc4_.type)
                creator.write_unsigned_byte(_loc4_.valueType)
                creator.write_int(_loc4_.value)
                _loc7_ += 1
                creator.write_unsigned_byte(_loc3_)
                _loc8_ = 0
                while _loc8_ < _loc3_:
                    creator.write_unsigned_byte(_loc5_.type)
                    creator.write_int(_loc5_.value)
                    _loc8_ += 1
                    creator.write_bool(_loc6_.satisfying)
                    _loc11_ += 1
        return creator.get_package()

    #
    #     # def updateHold(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_ = False
    #     #     creator.write_bool(_loc2_)
    #     #     _loc3_: list = self.write_items(creator, True, True, True, _loc2_)
    #     #     _loc4_: list
    #     #     _loc4_ = self.write_items(creator, True, True, True, len(_loc2_))
    #     #     return creator.get_package()
    #     #
    #     # def gineticLabOptions(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: GineticLabOption = None
    #     #     _loc3_: int = 0
    #     #     creator.write_unsigned_byte(_loc3_)
    #     #     _loc4_: list = list()
    #     #     _loc5_: int = 0
    #     #     while _loc5_ < _loc3:
    #     #         _loc2_ = GineticLabOption()
    #     #         creator.write_unsigned_byte(_loc2_.option)
    #     #         creator.write_int(_loc2_.cost)
    #     #         _loc5_ += 1
    #     #     return creator.get_package()
    #     #
    #     # def npcMessage(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: int = 0
    #     #     creator.write_int(_loc2_)
    #     #     _loc3_: int = 0
    #     #     creator.write_int(_loc3_)
    #     #     return creator.get_package()
    #     #
    #     # def additionalQuestMessage(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: int = 0
    #     #     creator.write_int(_loc2_)
    #     #     _loc3_: int = 0
    #     #     creator.write_int(_loc3_)
    #     #     return creator.get_package()
    #     #
    #     # def arenaRequests(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: BattleRequest = None
    #     #     _loc3_: list = list()
    #     #     _loc4_: int = 0
    #     #     creator.write_int(_loc4_)
    #     #     _loc5_: int = 0
    #     #     while _loc5_ < _loc4_:
    #     #         _loc2_ = BattleRequest()
    #     #         creator.write_int(_loc2_.id)
    #     #         creator.write_int(_loc2_.playersCount)
    #     #         creator.write_int(_loc2_.maxPlayers)
    #     #         creator.write_int(_loc2_.maxShipType)
    #     #         creator.write_int(_loc2_.minShipType)
    #     #         creator.write_unsigned_byte(_loc2_.type)
    #     #         _loc5_ += 1
    #     #     return creator.get_package()
    #     #
    #     # def battleRequestChanged(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: BattleRequestPlayer = None
    #     #     _loc3_: BattleRequest = BattleRequest()
    #     #     creator.write_int(_loc3_.id)
    #     #     creator.write_int(_loc3_.playersCount)
    #     #     creator.write_int(_loc3_.maxPlayers)
    #     #     creator.write_int(_loc3_.maxShipType)
    #     #     creator.write_int(_loc3_.minShipType)
    #     #     creator.write_unsigned_byte(_loc3_.type)
    #     #     creator.write_int(_loc3_.award)
    #     #     _loc3_.cost = (_loc3_.type - 1) * 2000
    #     #     _loc4_: int = 0
    #     #     while _loc4_ < _loc3_.playersCoun:
    #     #         _loc2_ = BattleRequestPlayer()
    #     #         creator.write_bool(_loc2_.isReady)
    #     #         creator.write_int(_loc2_.id)
    #     #         creator.write_utf(_loc2_.login)
    #     #         creator.write_int(_loc2_.level)
    #     #         creator.write_int(_loc2_.shipClass)
    #     #         creator.write_int(_loc2_.race)
    #     #         _loc3_.players.append(_loc2_)
    #     #         _loc4_ += 1
    #     #     return creator.get_package()
    #     #
    #     # def questsJournal(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: QuestPackage = None
    #     #     _loc3_: list = list()
    #     #     _loc4_: int = creator.write_int()
    #     #     _loc5_: int = 0
    #     #     while _loc5_ < _loc4_:
    #     #         _loc2_ = QuestPackage()
    #     #         creator.write_int(_loc2_.questId)
    #     #         creator.write_int(_loc2_.giverType)
    #     #         creator.write_utf(_loc2_.giverName)
    #     #         creator.write_utf(_loc2_.Name)
    #     #         _loc3_.append(_loc2_)
    #     #         _loc5_ += 1
    #     #     return creator.get_package()
    #     #
    def activeDevices(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ACTIVE_DEVICES
        data_active_device = [{'id': 122, 'guid': bytearray(b'P:\x1e+{mcN\x82j\x0cK\x7f4&\xd2'), 'reloadedTime': 0.0}, {'id': 122, 'guid': bytearray(b'5\xc6\xf5-\x84\xc5\xecH\xba\xd0\x89\xd1\tq\x1a\x1e'), 'reloadedTime': 0.0}, {'id': 122, 'guid': bytearray(b'\x84\xea\xc8\x87\xc4\xc8;E\x8f\x04@\xf7\xc5J\x86h'), 'reloadedTime': 0.0}, {'id': 122, 'guid': bytearray(b'@\x9a\x1f\x95\xb3\x13\xf5J\xbba\xe0\x03\x14<\x80b'), 'reloadedTime': 0.0}, {'id': 124, 'guid': bytearray(b',g\xc3\xe0\x16s\xc7M\x99\xdd\xa37\x8a\xa1\x85L'), 'reloadedTime': 0.0}]
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
        data_active_weapons = [{'classfloat': 61, 'index': 0}]
        creator.write_unsigned_byte(len(data_active_weapons))
        for i in data_active_weapons:
            _loc2_ = i
            creator.write_short(_loc2_['classfloat'])
            creator.write_unsigned_byte(_loc2_["index"])
        return creator.get_package()
    #     #
    #     # def playerShipUpdate(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: PlayerShip = PlayerShip()
    #     #     creator.write_short(_loc2_.energy)
    #     #     creator.write_short(_loc2_.health)
    #     #     creator.write_unsigned_byte(_loc2_.controlLeft)
    #     #     creator.write_unsigned_byte(_loc2_.controlUsed)
    #     #     return creator.get_package()
    #     #
    #     # def tradingShips(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: int = 0
    #     #     _loc3_: int = 0
    #     #     _loc4_: Restriction = None
    #     #     _loc5_: ShipFeature = None
    #     #     _loc6_: ShipForSale = None
    #     #     _loc7_: int = 0
    #     #     _loc8_: int = 0
    #     #     _loc9_: int = 0
    #     #     creator.write_int(_loc9_)
    #     #     _loc10_: int = 0
    #     #     creator.write_int(_loc10_)
    #     #     _loc11_: float = 0
    #     #     creator.write_float(_loc11_)
    #     #     _loc12_: float = 0
    #     #     creator.write_float(_loc12_)
    #     #     _loc13_: int = 0
    #     #     creator.write_int(_loc13_)
    #     #     _loc14_: list = list()
    #     #     _loc15_: int = 0
    #     #     while _loc15_ < _loc13:
    #     #         _loc6_ = ShipForSale()
    #     #         write_guid(creator_loc6_.id)
    #     #         creator.write_short(_loc6_.classNumber)
    #     #         creator.write_int(_loc6_.cost)
    #     #         creator.write_short(_loc6_.size)
    #     #         creator.write_unsigned_byte(_loc6_.weaponSlots)
    #     #         creator.write_unsigned_byte(_loc6_.deviceSlots)
    #     #         creator.write_unsigned_byte(_loc6_.armor)
    #     #         creator.write_unsigned_byte(_loc6_.shields)
    #     #         creator.write_short(_loc6_.maxEnergy)
    #     #         creator.write_short(_loc6_.maxHealth)
    #     #         creator.write_short(_loc6_.cpu)
    #     #         creator.write_short(_loc6_.radar)
    #     #         creator.write_unsigned_byte(_loc6_.maxSpeed)
    #     #         _loc2_ = 0
    #     #         creator.write_unsigned_byte(_loc2_)
    #     #         _loc7_ = 0
    #     #     while _loc7_ < _loc2:
    #     #         _loc4_ = Restriction()
    #     #         creator.write_unsigned_byte(_loc4_.type)
    #     #         creator.write_unsigned_byte(_loc4_.valueType)
    #     #         creator.write_int(_loc4_.value)
    #     #         _loc7_ += 1
    #     #
    #     #         _loc3_ = 0
    #     #         creator.write_unsigned_byte(_loc3_)
    #     #         _loc8_ = 0
    #     #     while _loc8_ < _loc3:
    #     #         _loc5_ = ShipFeature()
    #     #         creator.write_unsigned_byte(_loc5_.type)
    #     #         creator.write_int(_loc5_.value)
    #     #         _loc8_ += 1
    #     #
    #     #         creator.write_bool(_loc6_.satisfying)
    #     #         _loc14_.append(_loc6_)
    #     #         _loc15_ += 1
    #     #         return creator.get_package()
    #     #
    #     # def tradingItems(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: int = 0
    #     #     creator.write_int(_loc2_)
    #     #     _loc3_: float = 0
    #     #     creator.write_float(_loc3_)
    #     #     _loc4_: float = 0
    #     #     creator.write_float(_loc4_)
    #     #     _loc5_: list = write_items(creator, True, True, True, True)
    #     #     _loc6_: list = write_items(creator, True, True, True, True)
    #     #     return creator.get_package()
    #     #
    #     # def resourceUpdate(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: int = 0
    #     #     creator.write_int(_loc2_)
    #     #     _loc3_: float = 1
    #     #     _loc4_: float = 1
    #     #     _loc5_: list = self.write_items(creator, True, True)
    #     #     _loc6_: list = self.write_items(creator, True, True)
    #     #     return creator.get_package()
    #     #
    #     # def write_items(self, param2: bool, param3: bool, param4: bool = True, param5: bool = False):
    #     #     creator = PackageCreator()
    #     #     _loc6_: ItemPackage = None
    #     #     _loc7_: list = list()
    #     #     _loc8_: int = 0
    #     #     creator.write_int(_loc8_)
    #     #     _loc9_: int = 0
    #     #     while _loc9_ < _loc8_:
    #     #         _loc6_ = ItemPackage()
    #     #         creator.write_int(_loc6_.classNumber)
    #     #         # _loc6_.guid = write_guid(creator)
    #     #         creator.write_int(_loc6_.wear)
    #     #         if param4:
    #     #             _loc6_.level = 0
    #     #             creator.write_int(_loc6_.level)
    #     #         else:
    #     #             _loc6_.level = 1
    #     #         if param2:
    #     #             _loc6_.zeroCost = 0
    #     #             creator.write_bool(_loc6_.zeroCost)
    #     #         if param5:
    #     #             creator.write_int()
    #     #         if param3:
    #     #             _loc6_.satisfying = False
    #     #             creator.write_bool(_loc6_.satisfying)
    #     #         _loc9_ += 1
    #     #     return creator.get_package()
    #     #
    def shipsPosition(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIPS_POSITION
        data_ship_position = [{'id': 1656, 'x': 1308, 'y': 869, 'targetX': 1308, 'targetY': 869}]
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
        ship_state = [{'id': 1656, 'speed': 80, 'health': 850, 'energy': 350, 'PlayerRelation': 0}]
        for i in ship_state:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.id)
            creator.write_unsigned_byte(_loc2_.speed)
            creator.write_short(_loc2_.health)
            creator.write_short(_loc2_.energy)
            creator.write_short(_loc2_.PlayerRelation)
        return creator.get_package()
    #     #
    #     # def weaponTroubles(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: WeaponTrouble = None
    #     #     _loc3_: int = 0
    #     #     creator.write_unsigned_byte(_loc3_)
    #     #     _loc4_: list = list()
    #     #     _loc5_: int = 0
    #     #     while _loc5_ < _loc3_:
    #     #         _loc2_ = WeaponTrouble()
    #     #         creator.write_unsigned_byte(_loc2_.trouble)
    #     #         creator.write_unsigned_byte(_loc2_.index)
    #     #         _loc5_ += 1
    #     #     return creator.get_package()
    #     #
    #     # def repository(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: ItemPackage = None
    #     #     # _loc3_: list = write_items(creator, False, False)
    #     #     _loc4_: float = creator.write_float()
    #     #     _loc5_: list = list()
    #     #     _loc6_: int = creator.write_int()
    #     #     _loc7_: int = 0
    #     #     while _loc7_ < _loc6_:
    #     #         _loc2_ = ItemPackage()
    #     #         creator.write_int(_loc2_.classNumber)
    #     #         # _loc2_.guid = write_guid(creator)
    #     #         creator.write_int(_loc2_.wear)
    #     #         creator.write_int(_loc2_.level)
    #     #         # creator.write_int()
    #     #         _loc7_ += 1
    #     #     return creator.get_package()
    #     #
    #     # def clanrepository(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: ItemPackage = None
    #     #     # _loc3_: list = write_items(creator, False, False)
    #     #     _loc4_: float = creator.write_float()
    #     #     _loc5_: list = list()
    #     #     _loc6_: int = creator.write_int()
    #     #     _loc7_: int = 0
    #     #     while _loc7_ < _loc6_:
    #     #         _loc2_ = ItemPackage()
    #     #         creator.write_int(_loc2_.classNumber)
    #     #         # _loc2_.guid = write_guid(creator)
    #     #         creator.write_int(_loc2_.wear)
    #     #         creator.write_int(_loc2_.level)
    #     #         # creator.write_int()
    #     #         _loc7_ += 1
    #     #
    #     #     return creator.get_package()
    #     #
    #     # def planetsState(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: int = 0
    #     #     _loc3_: float = None
    #     #     _loc4_: int = 0
    #     #     creator.write_unsigned_byte(_loc4_)
    #     #     _loc5_: int = 0
    #     #     while _loc5_ < _loc4_:
    #     #         _loc2_ = 0
    #     #         creator.write_int(_loc2_)
    #     #         _loc3_ = 0
    #     #         creator.write_float(_loc3_)
    #     #     return creator.get_package()
    #     #
    #     # def planetsUpdate(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: int = 0
    #     #     _loc3_: float = None
    #     #     _loc4_: int = 0
    #     #     _loc5_: int = 0
    #     #     _loc6_: int = 0
    #     #     _loc7_: int = 0
    #     #     creator.write_unsigned_byte(_loc7_)
    #     #     _loc8_: int = 0
    #     #     while _loc8_ < _loc7_:
    #     #         _loc2_ = 0
    #     #         creator.write_int(_loc2_)
    #     #         _loc3_ = 0
    #     #         creator.write_float(_loc3_)
    #     #         _loc4_ = 0
    #     #         creator.write_bytes(_loc4_)
    #     #         _loc5_ = 0
    #     #         creator.write_bytes(_loc5_)
    #     #         _loc6_ = 0
    #     #         creator.write_int(_loc6_)
    #     #     return creator.get_package()
    #     #
    #     # def ship(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: DroidData = None
    #     #     # _loc3_: Ship = ShipsManager.createInstance(creator.write_short())
    #     #     creator.write_int(_loc3_.id)
    #     #     creator.write_utf(_loc3_.Name)
    #     #     creator.write_short(_loc3_.size)
    #     #     # _loc3_.setPosition = creator.write_float(), creator.write_float())
    #     #     creator.write_int(_loc3_.player.level)
    #     #     creator.write_short(_loc3_.maxHealth)
    #     #     creator.write_short(_loc3_.maxEnergy)
    #     #     creator.write_int(_loc3_.player.avatar)
    #     #     creator.write_unsigned_byte(_loc3_.maxSpeed) / 1000
    #     #     # _loc3_.setMovePoint(creator.write_float(), creator.write_float())
    #     #     creator.write_unsigned_byte(_loc3_.player.aliance)
    #     #     creator.write_unsigned_byte(_loc3_.player.status)
    #     #     creator.write_int(_loc3_.player.clanId)
    #     #     _loc4_: int = 0
    #     #     creator.write_unsigned_byte(_loc4_)
    #     #     _loc5_: int = 0
    #     #     while _loc5_ < _loc4_:
    #     #         _loc2_ = DroidData()
    #     #         creator.write_unsigned_byte(_loc2_.id)
    #     #         creator.write_short(_loc2_.type)
    #     #         creator.write_short(_loc2_.weaponClass)
    #     #         creator.write_short(_loc2_.health)
    #     #         _loc5_ += 1
    #     #     return creator.get_package()
    #     #
    #     # def planet(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     # _loc2_: Planet = PlanetsManager.createInstance(creator.write_bytes())
    #     #     creator.write_int(_loc2_.id)
    #     #     Race.defineById(self, creator.write_unsigned_byte(_loc2_.race))
    #     #     creator.write_int(_loc2_.radius)
    #     #     creator.write_int(_loc2_.size)
    #     #     creator.write_float(_loc2_.serverAngle)
    #     #     creator.write_bool(_loc2_.landable)
    #     #     return creator.get_package()
    #     #
    #     # def inventory(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: Item = None
    #     #     _loc3_: bytearray = None
    #     #     _loc4_: list = list()
    #     #     _loc5_: int = creator.write_short()
    #     #     _loc6_: int = 0
    #     #     while _loc6_ < _loc5_:
    #     #         _loc2_ = ItemsManager.createInstance(creator.write_short())
    #     #         _loc3_ = bytearray()
    #     #         creator.write_bytes(_loc3_, 0, 16)
    #     #         _loc2_.guid = _loc3_
    #     #         creator.write_short(_loc2_.wear)
    #     #         creator.write_bool(_loc2_.inUsing)
    #     #         creator.write_unsigned_byte(_loc2_.level)
    #     #         creator.write_bool(_loc2_.satisfying)
    #     #         _loc6_ += 1
    #     #     _loc7_: ShipParametersPackage
    #     #     _loc7_ = ShipParametersPackage()
    #     #     creator.write_unsigned_byte(_loc7_.armor)
    #     #     creator.write_unsigned_byte(_loc7_.shields)
    #     #     creator.write_short(_loc7_.usedSpace)
    #     #     creator.write_short(_loc7_.cpu)
    #     #     creator.write_short(_loc7_.cpuUsed)
    #     #     creator.write_unsigned_byte(_loc7_.level)
    #     #     creator.write_unsigned_byte(_loc7_.maxDroids)
    #     #     _loc8_: list = list()
    #     #     while creator.bytesAvailable > 0:
    #     #         _loc2_ = ItemsManager.createInstance(creator.write_short())
    #     #         creator.write_bytes(_loc2_.id)
    #     #     return creator.get_package()
    #     #
    def player(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER
        Player = DotMap({
            'id': 1656,
            'login': 'xxxCHELIKxxx',
            'level': 25,
            'cash': 28906,
            'race': 3,
            'avatar': 2001,
            'aliance': 2,
            'clanId': 0,
            'role': 0,
            'clanRequestStatus': 0,
            'clanJoinRequestStatus': 0,
            'PlayerRelation': 0
        })
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
    #     # def questMessage(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: str = None
    #     #     _loc3_: QuestAward = None
    #     #     _loc4_: QuestTarget = None
    #     #     _loc5_: QuestPackage
    #     #     _loc5_ = QuestPackage()
    #     #     creator.write_int(_loc5_.questId)
    #     #     creator.write_int(_loc5_.nextQuestId)
    #     #     creator.write_int(_loc5_.giverType)
    #     #     creator.write_int(_loc5_.status)
    #     #     creator.write_utf(_loc5_.giverName)
    #     #     _loc6_ = 0
    #     #     creator.write_int(_loc6_)
    #     #     _loc7_: int = 0
    #     #     while _loc7_ < _loc6_:
    #     #         _loc2_ = ''
    #     #         creator.write_utf(_loc2_)
    #     #         _loc7_ += 1
    #     #     creator.write_int(_loc5_.ParentSystemID)
    #     #     creator.write_unsigned_byte(_loc5_.LocationType)
    #     #     creator.write_int(_loc5_.LocationID)
    #     #     _loc8_ = 0
    #     #     creator.write_int(_loc8_)
    #     #     _loc9_: int = 0
    #     #     while _loc9_ < _loc8_:
    #     #         # _loc3_ = QuestAward()
    #     #         creator.write_int(_loc3_.classNumber)
    #     #         creator.write_int(_loc3_.level)
    #     #         creator.write_int(_loc3_.type)
    #     #         creator.write_int(_loc3_.value)
    #     #         _loc9_ += 1
    #     #     _loc10_ = 0
    #     #     creator.write_int(_loc10_)
    #     #     _loc11_: int = 0
    #     #     while _loc11_ < _loc10_:
    #     #         # _loc4_ = QuestTarget()
    #     #         creator.write_int(_loc4_.targetId)
    #     #         creator.write_int(_loc4_.targetSystemId)
    #     #         creator.write_int(_loc4_.targetPlanetId)
    #     #         creator.write_int(_loc4_.type)
    #     #         creator.write_int(_loc4_.value)
    #     #         _loc5_.targets.append(_loc4_)
    #     #         _loc11_ += 1
    #     #     return creator.get_package()
    #     #
    #     # def playerSkills(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: PlayerSkills = PlayerSkills()
    #     #     creator.write_unsigned_byte(_loc2_.level)
    #     #     creator.write_int(_loc2_.experience)
    #     #     creator.write_int(_loc2_.expForNext)
    #     #     # write_skills(creator, _loc2_)
    #     #     creator.write_int(_loc2_.freeSkills)
    #     #     creator.write_int(_loc2_.expForFirstSkillLevel)
    #     #     creator.write_float(_loc2_.expSkillGrowCoef)
    #     #     creator.write_float(_loc2_.expSkillReduserCoef)
    #     #     creator.write_unsigned_byte(_loc2_.maxSkill)
    #     #     # _loc3_: PlayerStatistics = PlayerStatistics()
    #     #     creator.write_unsigned_byte(_loc3_.status)
    #     #     creator.write_unsigned_byte(_loc3_.level)
    #     #     creator.write_int(_loc3_.pirateStatus)
    #     #     creator.write_int(_loc3_.policeStatus)
    #     #     creator.write_int(_loc3_.forNextLevel)
    #     #     return creator.get_package()
    #     #
    def write_skills(self, creator, param2):
        creator.write_unsigned_byte(param2.control)
        creator.write_unsigned_byte(param2.defending)
        creator.write_unsigned_byte(param2.energyWeapons)
        creator.write_unsigned_byte(param2.kineticWeapons)
        creator.write_unsigned_byte(param2.mining)
        creator.write_unsigned_byte(param2.piloting)
        creator.write_unsigned_byte(param2.repairing)
        creator.write_unsigned_byte(param2.rocketWeapons)
        creator.write_unsigned_byte(param2.trading)
        creator.write_unsigned_byte(param2.attacking)
        creator.write_unsigned_byte(param2.tactics)
        creator.write_unsigned_byte(param2.targeting)
        creator.write_unsigned_byte(param2.electronics)
        creator.write_unsigned_byte(param2.biocemistry)
        creator.write_unsigned_byte(param2.mechanics)
        creator.write_unsigned_byte(param2.cybernetics)

    def playerSkillsData(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_SKILLS_DATA
        data_player_skills = [{'level': 25, 'experience': 46877, 'expForNext': 49000, 'skills': {'control': 0, 'defending': 0, 'energyWeapons': 0, 'kineticWeapons': 0, 'mining': 0, 'piloting': 3, 'repairing': 6, 'rocketWeapons': 0, 'trading': 0, 'attacking': 0, 'tactics': 0, 'targeting': 0, 'electronics': 0, 'biocemistry': 0, 'mechanics': 8, 'cybernetics': 8}, 'freeSkills': 0, 'expForFirstSkillLevel': 2000, 'expSkillGrowCoef': 2.200000047683716, 'expSkillReduserCoef': 10.0, 'maxSkill': 12}, {'status': 0, 'level': 0, 'pirateStatus': 0, 'policeStatus': 11}]
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
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_SHIP
        creator.write_int(1)

        Player = DotMap({
            'ship': DotMap({
                'id': 1656,
                'Name': 'xxxCHELIKxxx',
                'size': 830,
                'energy': 350,
                'maxEnergy': 350,
                'setPosition': (1308.6500244140625, 869.5999755859375),
                'team': -1,
                'maxSpeed': 0,
                'weaponSlots': 1,
                'deviceSlots': 4,
                'maxHealth': 850,
                'radarRadius': 2200,
                'cpu': 1400})
        })
        creator.write_int(Player.ship.id)
        creator.write_utf(Player.ship.Name)
        creator.write_int(Player.ship.size)
        creator.write_int(Player.ship.energy)
        creator.write_int(Player.ship.maxEnergy)
        creator.write_float(Player.ship.setPosition[0])
        creator.write_float(Player.ship.setPosition[1])
        creator.write_int(Player.ship.team)
        creator.write_unsigned_byte(Player.ship.maxSpeed)  # / 1000
        creator.write_unsigned_byte(Player.ship.weaponSlots)
        creator.write_unsigned_byte(Player.ship.deviceSlots)
        creator.write_int(Player.ship.maxHealth)
        creator.write_short(Player.ship.radarRadius)
        creator.write_short(Player.ship.cpu)
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

    #     #
    #     # def reachableSystems(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: ReachableSystem = None
    #     #     cnt_system: int = 0
    #     #     creator.write_unsigned_byte(cnt_system)
    #     #     _loc5_: int = 0
    #     #     while _loc5_ < cnt_system:
    #     #         # _loc2_ = ReachableSystem()
    #     #         creator.write_unsigned_byte(_loc2_.id)
    #     #         creator.write_bool(_loc2_.current)
    #     #         creator.write_short(_loc2_.energyForJump)
    #     #         _loc5_ += 1
    #     #     _loc6_: int = 0
    #     #     creator.write_unsigned_byte(_loc6_)
    #     #     _loc7_: int = 0
    #     #     creator.write_unsigned_byte(_loc7_)
    #     #     return creator.get_package()
    #     #
    def version(self):
        creator = PackageCreator()
        version = '0.9.0.1'
        creator.PackageNumber = ServerRequest.VERSION
        creator.write_utf(version)
        return creator.get_package()

    #     #
    #     # def shipHealth(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_ = 0
    #     #     _loc3_ = 0
    #     #     creator.write_int(_loc2_)
    #     #     creator.write_int(_loc3_)
    #     #     return creator.get_package()
    #     #
    def online(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ONLINE
        creator.write_int(1)
        online = 4
        creator.write_int(online)
        return creator.get_package()

    def topList(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TOP_LIST
        _loc2_ = DotMap({
            'login': '___MiLkYwaY___',
            'level': 140,
            'experience': 39261643,
            'clanId': 87,
            'race': 1,
            'shipClass': 19
        })
        all_player = []
        all_player.append(_loc2_)
        cnt: int = len(all_player)
        creator.write_int(cnt)
        for i in all_player:
            _loc2_ = i
            creator.write_utf(_loc2_.login)
            creator.write_int(_loc2_.level)
            creator.write_int(_loc2_.experience)
            creator.write_int(_loc2_.clanId)
            creator.write_unsigned_byte(_loc2_.race)
            creator.write_short(_loc2_.shipClass)
        return creator.get_package()

    def topRatingList(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TOP_RATING_LIST
        top_players = []
        top_player = DotMap({
            'login': 'Anave',
            'level': 59,
            'points': 1846704,
            'clanId': 184,
            'race': 4,
            'shipClass': 3029})
        top_players.append(top_player)
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
        players = []
        player = DotMap({
            'id': 184,
            'points': 7343124,
            'leaderID': 1523,
            'aliace': 2,
            'level': 1,
            'name': 'Id 55maxik55 шмот дешего',
            'shortName': 'VK',
            'logoFileName': ''})
        players.append(player)
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

    #     #
    #     # def auctionList(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: int = 0
    #     #     _loc3_: Item = None
    #     #     _loc4_ = 0
    #     #     creator.write_int(_loc4_)
    #     #     _loc5_: list = list()
    #     #     _loc6_: int = 0
    #     #     while _loc6_ < _loc4_:
    #     #         creator.write_int(_loc2_)
    #     #         # _loc3_ = ItemsManager.createInstance(_loc2_)
    #     #         # creator.write_guid(_loc3_.guid)
    #     #         creator.write_int(_loc3_.wear)
    #     #         creator.write_int(_loc3_.ownerid)
    #     #         creator.write_int(_loc3_.price)
    #     #         creator.write_int(_loc3_.ransom)
    #     #         creator.write_int(_loc3_.lastPlayerID)
    #     #         creator.write_utf(_loc3_.ownerName)
    #     #         creator.write_utf(_loc3_.lastPlayerName)
    #     #         _loc6_ += 1
    #     #     return creator.get_package()
    #     #
    #     # def sList(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc3_ = 0
    #     #     creator.write_int(_loc3_)
    #     #     _loc5_: int = 0
    #     #     while _loc5_ < _loc3_:
    #     #         _loc2_ = ''
    #     #         creator.write_utf(_loc2_)
    #     #         _loc5_ += 1
    #     #     return creator.get_package()
    #     #
    #     # def Evil(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_ = ''
    #     #     creator.write_utf(_loc2_)
    #     #     return creator.get_package()
    #     #
    #     # def locationPlanet(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: PlayerInfoData = None
    #     #     _loc3_: Shop = None
    #     #     _loc4_: Planet
    #     #     _loc4_ = PlanetsManager.createInstance(creator.write_bytes())
    #     #     _loc4_.id = creator.write
    #     #     _int()
    #     #     _loc4_.race = Race.defineById(self, creator.write_unsigned_byte())
    #     #     creator = PackageCreator()
    #     #     creator.write_int(_loc4_.radius)
    #     #     creator.write_int(_loc4_.size)
    #     #     creator.write_unsigned_byte(_loc4_.aliance)
    #     #     creator.write_int(_loc4_.clanID)
    #     #     creator.write_float(_loc4_.angle)
    #     #     creator.write_unsigned_byte(_loc4_.QCount)
    #     #     _loc5_: int = 0
    #     #     creator.write_short(_loc5_)
    #     #     _loc6_: int = 0
    #     #     while _loc6_ < _loc5_:
    #     #         _loc3_ = Shop()
    #     #         creator.write_int(_loc3_.id)
    #     #         creator.write_unsigned_byte(_loc3_.type)
    #     #         _loc6_ += 1
    #     #     _loc7_: list = []
    #     #     while creator.bytesAvailable > 0:
    #     #         _loc2_ = PlayerInfoData()
    #     #         creator.write_int(_loc2_.id)
    #     #         creator.write_utf(_loc2_.name)
    #     #         creator.write_int(_loc2_.clanId)
    #     #         creator.write_int(_loc2_.level)
    #     #     return creator.get_package()
    #     #
    #     # def planetQuests(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: QuestPackage = None
    #     #     _loc3_: list = list()
    #     #     _loc4_: int = creator.write_short()
    #     #     _loc5_: int = 0
    #     #     while _loc5_ < _loc4_:
    #     #         _loc2_ = QuestPackage()
    #     #         creator.write_int(_loc2_.questId)
    #     #         creator.write_int(_loc2_.giverType)
    #     #         creator.write_utf(_loc2_.giverName)
    #     #         creator.write_utf(_loc2_.Name)
    #     #         _loc5_ += 1
    #     #     return creator.get_package()
    #     #
    def locationSystem(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOCATION_SYSTEM
        data_location_system = [{'id': 7, 'x': 9.0, 'y': 27.0, 'sector': 1}, [{'player': DotMap({'level': 25, 'avatar': 2001, 'aliance': 2, 'status': 0, 'clanId': 0}), 'race': 2003, 'id': 1656, 'Name': 'xxxCHELIKxxx', 'size': 830, 'set_x': 1308.6500244140625, 'set_y': 869.5999755859375, 'maxHealth': 850, 'maxEnergy': 350, 'maxSpeed': 0.0, 'mov_x': 1308.6500244140625, 'mov_y': 869.5999755859375, 'droid': []}], [{'PlanetClass': 1, 'id': 14, 'race': 0, 'radius': 0, 'size': 18232, 'angle': float("inf"), 'landable': False, 'aliance': 0, 'clanID': 0}, {'PlanetClass': 19, 'id': 15, 'race': 4, 'radius': 600, 'size': 10013, 'angle': 39801.8984375, 'landable': True, 'aliance': 2, 'clanID': 0}, {'PlanetClass': 14, 'id': 16, 'race': 4, 'radius': 1100, 'size': 12014, 'angle': 21710.126953125, 'landable': True, 'aliance': 2, 'clanID': 0}, {'PlanetClass': 11, 'id': 17, 'race': 4, 'radius': 2200, 'size': 9015, 'angle': 10855.0634765625, 'landable': True, 'aliance': 2, 'clanID': 0}], [{'StaticSpaceObjectType': 2, 'id': 25, 'x': 1300.0, 'y': 1000.0, 'landable': True}]]
        # {'PlanetClass': 1, 'id': 14, 'race': 0, 'radius': 0, 'size': 18232, 'angle': inf, 'landable': False, 'aliance': 0, 'clanID': 0}
        creator.write_int(data_location_system[0]['id'])
        creator.write_float(data_location_system[0]['x'])# Player.x
        creator.write_float(data_location_system[0]['y'])# Player.x
        creator.write_unsigned_byte(data_location_system[0]['sector']) # Player.sector

        creator.write_short(len(data_location_system[1]))

        for i in data_location_system[1]:
            _loc2_ = DotMap(i)
            creator.write_short(_loc2_.race)
            creator.write_int(_loc2_.id)
            # if _loc2_.id == Player.ship.id:
            #     _loc2_ = Player.ship
            creator.write_utf(_loc2_.Name)
            creator.write_short(_loc2_.size)
            creator.write_float(_loc2_.set_x)  # setPosition
            creator.write_float(_loc2_.set_y)
            creator.write_int(_loc2_.player.level)
            creator.write_short(_loc2_.maxHealth)
            creator.write_short(_loc2_.maxEnergy)
            creator.write_int(_loc2_.player.avatar)
            creator.write_unsigned_byte(int(_loc2_.maxSpeed * 1000))
            creator.write_float(_loc2_.mov_x)
            creator.write_float(_loc2_.mov_y)  # setMovePoint
            creator.write_unsigned_byte(_loc2_.player.aliance)
            creator.write_unsigned_byte(_loc2_.player.status)
            creator.write_int(_loc2_.player.clanId)

            creator.write_unsigned_byte(len(_loc2_.droid))

            for i in _loc2_.droid:
                _loc4_ = DotMap(i)
                creator.write_unsigned_byte(_loc4_.id)
                creator.write_short(_loc4_.type)
                creator.write_short(_loc4_.weaponClass)
                creator.write_short(_loc4_.health)

        creator.write_short(len(data_location_system[2]))
        for i in data_location_system[2]:
            _loc6_ = DotMap(i)
            creator.write_unsigned_byte(_loc6_.PlanetClass)
            creator.write_int(_loc6_.id)
            creator.write_unsigned_byte(_loc6_.race)
            creator.write_int(_loc6_.radius)
            creator.write_int(_loc6_.size)
            creator.write_float(_loc6_.angle)
            creator.write_bool(_loc6_.landable)
            creator.write_unsigned_byte(_loc6_.aliance)
            creator.write_int(_loc6_.clanID)

        creator.write_short(len(data_location_system[3]))
        for i in data_location_system[3]:
            _loc7_ = DotMap(i)
            creator.write_int(_loc7_.StaticSpaceObjectType)
            creator.write_int(_loc7_.id)
            creator.write_float(_loc7_.x)
            creator.write_float(_loc7_.y)
            creator.write_bool(_loc7_.landable)

        return creator.get_package()

    #     # def locationBattle(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: Ship = None
    #     #     _loc3_: int = 0
    #     #     _loc4_: DroidData = None
    #     #     _loc5_: int = 0
    #     #     _loc6_: Battle
    #     #     _loc6_ = Battle()
    #     #     creator.write_int(_loc6_.id)
    #     #     creator.write_float(_loc6_.x)
    #     #     creator.write_float(_loc6_.y)
    #     #     _loc7_ = 0
    #     #     creator.write_short(_loc7_)
    #     #     _loc8_: int = 0
    #     #     while _loc8_ < _loc7_:
    #     #         creator.write_short(_loc2_)
    #     #         creator.write_int(_loc2_.id)
    #     #         if _loc2_.id == Player.ship.id:
    #     #             _loc2_ = Player.ship
    #     #         creator.write_utf(_loc2_.Name)
    #     #         creator.write_short(_loc2_.size)
    #     #         # _loc2_.setPosition = eator.write_float(), creator.write_float())
    #     #         creator.write_int(_loc2_.player)
    #     #         creator.write_short(_loc2_.maxHealth)
    #     #         creator.write_short(_loc2_.maxEnergy)
    #     #         creator.write_int(_loc2_.player)
    #     #         iance = creator.write_unsigned_byte(_loc2_.player)
    #     #         atus = creator.write_unsigned_byte(_loc2_.player)
    #     #         anId = creator.write_int(_loc2_.player)
    #     #         creator.write_unsigned_byte(_loc3_)
    #     #         _loc5_ = 0
    #     #         while _loc5_ < _loc3_:
    #     #             _loc4_ = DroidData()
    #     #             creator.write_unsigned_byte(_loc4_.id)
    #     #             creator.write_short(_loc4_.type)
    #     #             creator.write_short(_loc4_.weaponClass)
    #     #             creator.write_short(_loc4_.health)
    #     #             _loc5_ += 1
    #     #         _loc8_ += 1
    #     #     return creator.get_package()
    #     #
    #     # def shoots(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_ = None  # ShipShoots
    #     #     _loc3_: int = 0
    #     #     _loc4_: int = 0
    #     #     _loc5_ = None  # Shoot
    #     #     _loc7_ = 0
    #     #     creator.write_short(_loc7_)
    #     #     _loc8_: int = 0
    #     #     while _loc8_ < _loc7_:
    #     #         _loc2_ = ShipShoots()
    #     #         creator.write_int(_loc2_.id)
    #     #         creator.write_short(_loc3_)
    #     #         _loc4_ = 0
    #     #         while _loc4_ < _loc3_:
    #     #             _loc5_ = Shoot()
    #     #             creator.write_short(_loc5_.classNumber)
    #     #             creator.write_short(_loc5_.damage)
    #     #             creator.write_unsigned_byte(_loc5_.destroyedTarget)
    #     #             creator.write_int(_loc5_.targetId)
    #     #             creator.write_unsigned_byte(_loc5_.targetType)
    #     #             creator.write_unsigned_byte(_loc5_.muzzleIndex)
    #     #             _loc4_ += 1
    #     #         _loc8_ += 1
    #     #     return creator.get_package()
    #     #
    #     # def items(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: BattleItem = None
    #     #     _loc3_: list = list()
    #     #     if creator.bytesAvailable / 10 - int(creator.bytesAvailable / 10) == 0:
    #     #         while creator.bytesAvailable >= 10:
    #     #             _loc2_ = BattleItem()
    #     #             creator.write_int(_loc2_.id)
    #     #             creator.write_short(_loc2_.classNumber)
    #     #             creator.write_short(_loc2_.x)
    #     #             creator.write_short(_loc2_.y)
    #     #             _loc3_.append(_loc2_)
    #     #     return creator.get_package()
    #     #
    #     # def message(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: Message = Message()
    #     #     _loc2_ = ''
    #     #     creator.write_utf(_loc2_)
    #     #     creator.write_utf(_loc2_.text)
    #     #     creator.write_unsigned_byte(_loc2_.type)
    #     #     creator.write_bool(_loc2_.isPrivate)
    #     #     creator.write_bool(_loc2_.isAdmin)
    #     #     return creator.get_package()
    #     #
    #     # def asteroids(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: AsteroidPackage = None
    #     #     _loc3_: list = list()
    #     #     if creator.bytesAvailable / 25 - int(creator.bytesAvailable / 25) == 0:
    #     #         while creator.bytesAvailable >= 25:
    #     #             _loc2_ = AsteroidPackage()
    #     #             creator.write_int(_loc2_.id)
    #     #             creator.write_float(_loc2_.x)
    #     #             creator.write_float(_loc2_.y)
    #     #             creator.write_float(_loc2_.targetX)
    #     #             creator.write_float(_loc2_.targetY)
    #     #             creator.write_unsigned_byte(_loc2_.speed) / 1000
    #     #             creator.write_int(_loc2_.size)
    #     #             _loc3_.append(_loc2_)
    #     #     return creator.get_package()
    #     #
    #     # def effectCreated(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: EffectTarget = None
    #     #     _loc3_: int = 0
    #     #     creator.write_int(_loc3_)
    #     #     _loc4_: int = 0
    #     #     creator.write_unsigned_byte(_loc4_)
    #     #     _loc5_: list = []
    #     #     _loc6_: int = 0
    #     #     while _loc6_ < _loc4_:
    #     #         _loc2_ = EffectTarget()
    #     #         creator.write_int(_loc2_.targetId)
    #     #         creator.write_unsigned_byte(_loc2_.destroyedTarget)
    #     #         creator.write_bool(_loc2_.effectFailed)
    #     #         _loc6_ += 1
    #     #     _loc7_: int = 0
    #     #     creator.write_unsigned_byte(_loc7_)
    #     #     _loc8_: float = 0
    #     #     creator.write_float(_loc8_)
    #     #     _loc9_: int = 0
    #     #     creator.write_int(_loc9_)
    #     #     return creator.get_package()
    #     #
    #     # def effectRemoved(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: int = 0
    #     #     creator.write_int(_loc2_)
    #     #     _loc3_: int = 0
    #     #     creator.write_unsigned_byte(_loc3_)
    #     #     return creator.get_package()
    #     #
    #     # def logMessage(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: int = 0
    #     #     creator.write_int(_loc2_)
    #     #     _loc3_: int = 0
    #     #     creator.write_int(_loc3_)
    #     #     return creator.get_package()
    #     #
    #     # def logMessagestr(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: str = ''
    #     #     creator.write_utf(_loc2_)
    #     #     return creator.get_package()
    #     #
    #     # def systemMessage(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: int = 0
    #     #     creator.write_int(_loc2_)
    #     #     _loc3_: int = 0
    #     #     creator.write_int(_loc3_)
    #     #     return creator.get_package()
    #     #
    #     # def systemMessagestr(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: str = ''
    #     #     creator.write_utf(_loc2_)
    #     #     return creator.get_package()
    #     #
    #     # def droidBuildingDialog(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: DroidPackage = None
    #     #     _loc3_: DroidBuildingDialogPackage = DroidBuildingDialogPackage()
    #     #     _loc3_.deviceGuid = self.write_guid(creator)
    #     #     _loc4_: int = 0
    #     #     creator.write_int(_loc4_)
    #     #     _loc3_.droids = list()
    #     #     _loc5_: int = 0
    #     #     while _loc5_ < _loc4_:
    #     #         _loc2_ = DroidPackage()
    #     #         _loc2_.guid = write_guid(creator)
    #     #         creator.write_int(_loc2_.classNumber)
    #     #         creator.write_int(_loc2_.level)
    #     #         creator.write_int(_loc2_.energyCost)
    #     #     _loc5_ += 1
    #     #
    #     #     return creator.get_package()
    #     #
    #     # def write_guid(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: bytearray = bytearray()
    #     #     creator.write_bytes(_loc2_, 0, 16)
    #     #     return _loc2_
    #     #
    def hideShip(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.HIDE_SHIP
        _loc2_ = -13
        creator.write_int(_loc2_)
        return creator.get_package()
    #     #
    #     # def shipDestroyed(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: int = 0
    #     #     creator.write_int(_loc2_)
    #     #     return creator.get_package()
    #     #
    #     # def shipJumped(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: int = 0
    #     #     creator.write_int(_loc2_)  # findShip
    #     #     return creator.get_package()
    #     #
    def clan(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CLAN
        data = parse_xml('Clans') # Если больше 1 клан, то сломается
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
    #     #
    #     # def playerClan(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: int = 0
    #     #     _loc3_: int = 0
    #     #     _loc4_ = None  # PlayerInfoData
    #     #     _loc5_: ClanData
    #     #     _loc5_ = ClanData()
    #     #     creator.write_int(_loc5_.id)
    #     #     creator.write_int(_loc5_.leaderID)
    #     #     creator.write_utf(_loc5_.leaderName)
    #     #     creator.write_utf(_loc5_.logoFileName)
    #     #     creator.write_utf(_loc5_.name)
    #     #     creator.write_utf(_loc5_.shortName)
    #     #     creator.write_unsigned_byte(_loc5_.aliace)
    #     #     creator.write_utf(_loc5_.description)
    #     #     creator.write_short(_loc5_.joinRequestsCount)
    #     #     creator.write_int(_loc5_.points)
    #     #     creator.write_int(_loc5_.cash)
    #     #     creator.write_unsigned_byte(_loc5_.level)
    #     #     creator.write_unsigned_byte(_loc5_.maxMembers)
    #     #     creator.write_unsigned_byte(_loc5_.maxFriends)
    #     #     creator.write_short(_loc5_.friendRequests)
    #     #     creator.write_int(_loc5_.currentLevelPoints)
    #     #     creator.write_int(_loc5_.nextLevelPoints)
    #     #     creator.write_int(_loc5_.nextLevelCash)
    #     #     creator.write_int(_loc5_.bonuses)
    #     #     # cnt = _loc2_
    #     #     creator.write_int(_loc2_)
    #     #     _loc3_ = 0
    #     #     while _loc3_ < _loc2_:
    #     #         # _loc5_.enemyClans.append(creator.write_int())
    #     #         _loc3_ += 1
    #     #     creator.write_int(_loc2_)
    #     #     _loc3_ = 0
    #     #     while _loc3_ < _loc2_:
    #     #         # _loc5_.friendClans.append(creator.write_int())
    #     #         _loc3_ += 1
    #     #     creator.write_int(_loc2_)
    #     #     _loc3_ = 0
    #     #     while _loc3_ < _loc2_:
    #     #         _loc4_ = PlayerInfoData()
    #     #         creator.write_int(_loc4_.id)
    #     #         creator.write_int(_loc4_.role)
    #     #         creator.write_utf(_loc4_.name)
    #     #         _loc5_.members.append(_loc4_)
    #     #         _loc3_ += 1
    #     #     return creator.get_package()
    #     #
    #     # def teamList(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: int = 0
    #     #     _loc3_: int = 0
    #     #     _loc4_ = None  # : PlayerInfoData
    #     #     cnt_player_team = 0
    #     #     creator.write_int(cnt_player_team)
    #     #     if cnt_player_team > 0:
    #     #         Player.team = TeamList()
    #     #         creator.write_int(Player.team.leaderID)
    #     #         creator.write_int(Player.team.maxMembers)
    #     #         _loc2_ = 0
    #     #         while _loc2_ < cnt_player_team:
    #     #             _loc4_ = PlayerInfoData()
    #     #             _loc4_.role = 0
    #     #             creator.write_int(_loc4_.shipId)
    #     #             creator.write_int(_loc4_.id)
    #     #             creator.write_utf(_loc4_.name)
    #     #             _loc2_ += 1
    #     #     cnt_player_team = 0
    #     #     creator.write_int(cnt_player_team)
    #     #     if cnt_player_team >= 0:
    #     #         _loc2_ = 0
    #     #     while _loc2_ < cnt_player_team:
    #     #         _loc4_ = PlayerInfoData()
    #     #         _loc4_.role = -1
    #     #         creator.write_int(_loc4_.shipId)
    #     #         creator.write_int(_loc4_.id)
    #     #         creator.write_utf(_loc4_.name)
    #     #         _loc2_ += 1
    #     #     return creator.get_package()
    #     #
    #     # def checkValueResult(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: int = 0
    #     #     creator.write_int(_loc2_)
    #     #     _loc3_: bool = False
    #     #     creator.write_bool(_loc3_)
    #     #     return creator.get_package()
    #     #
    #     # def acceptedClanInfo(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: int = 0
    #     #     creator.write_int(_loc2_)
    #     #     _loc3_: str = ''
    #     #     creator.write_utf(_loc3_)
    #     #     _loc4_: str = ''
    #     #     creator.write_utf(_loc4_)
    #     #     _loc5_: str = ''
    #     #     creator.write_utf(_loc5_)
    #     #     _loc6_: int = 0
    #     #     creator.write_int(_loc6_)
    #     #     return creator.get_package()
    #     #
    #     # def clanId(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     creator.write_int(Player.clanId)
    #     #     return creator.get_package()
    #     #
    #     # def clansLetters(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: list = None
    #     #     _loc2_ = list()
    #     #     while creator.bytesAvailable > 0:
    #     #         _loc2_[len(_loc2_)] = creator.write_utf()
    #     #     return creator.get_package()
    #     #
    #     # def clansList(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: list = None
    #     #     _loc3_: str = None
    #     #     _loc2_ = list()
    #     #     _loc3_ = creator.write_utf()
    #     #     while creator.bytesAvailable > 0:
    #     #         _loc2_[len(_loc2_)] = creator.write_int()
    #     #     return creator.get_package()
    #     #
    #     # def clanJoinRequests(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_ = None  # ClanJoinRequest
    #     #     _loc3_: list = None
    #     #     _loc2_ = None
    #     #     _loc3_ = list()
    #     #     while creator.bytesAvailable > 0:
    #     #         _loc2_ = ClanJoinRequest()
    #     #         creator.write_int(_loc2_.playerID)
    #     #         creator.write_utf(_loc2_.playerName)
    #     #         creator.write_utf(_loc2_.message)
    #     #     return creator.get_package()
    #     #

    def logged(self) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOGGED
        _logged = DotMap({
            'stateLoop': 500,
            'bankSendOperationFee': 2,
            'clanJoinCost': 5000,
            'clanCreateLevelNeed': 8,
            'bonuses': 0
        })
        creator.write_int(_logged.stateLoop)
        creator.write_unsigned_byte(_logged.bankSendOperationFee)
        creator.write_int(_logged.clanJoinCost)
        creator.write_unsigned_byte(_logged.clanCreateLevelNeed)
        creator.write_int(_logged.bonuses)
        # while True:
        _loc2_ = DotMap({
            'id': 1656,
            'name': 'xxxCHELIKxxx',
            'shipClass': 2003,
            'shipCPU': 1400,
            'race': 3,
            'aliance': 2,
            'status': 0,
            'level': 25,
            'clanId': 0,
            'deleteEnqueued': False,
            'canDelete': False,
            'logged': False,
            'skills': DotMap({
                'control': 0,
                'defending': 0,
                'energyWeapons': 0,
                'kineticWeapons': 0,
                'mining': 0,
                'piloting': 3,
                'repairing': 6,
                'rocketWeapons': 0,
                'trading': 0,
                'attacking': 0,
                'tactics': 0,
                'targeting': 0,
                'electronics': 0,
                'biocemistry': 0,
                'mechanics': 8,
                'cybernetics': 8
            })
        })
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

    #     #
    #     # def playerInfo(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     # _loc2_: PlayerInfoData = None
    #     #     _loc2_ = DotMap({
    #     #         'id': 0,
    #     #         'name': 'max',
    #     #         'level': 10,
    #     #         'status': 10,
    #     #         'shipClass': 3,
    #     #         'clanId': 10,
    #     #         'aliance': 10,
    #     #         'race': 10,
    #     #         'clanPoints': 10,
    #     #         'role': 10
    #     #     })
    #     #     _loc2_ = PlayerInfoData()
    #     #     creator.write_int(_loc2_.id)
    #     #     creator.write_utf(_loc2_.name)
    #     #     creator.write_unsigned_byte(_loc2_.level)
    #     #     creator.write_unsigned_byte(_loc2_.status)
    #     #     creator.write_short(_loc2_.shipClass)
    #     #     creator.write_int(_loc2_.clanId)
    #     #     creator.write_unsigned_byte(_loc2_.aliance)
    #     #     creator.write_unsigned_byte(_loc2_.race)
    #     #     creator.write_int(_loc2_.clanPoints)
    #     #     creator.write_int(_loc2_.role)
    #     #     return creator.get_package()
    #     #
    #     # def playerLoggedOn(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: PlayerInfoData = None
    #     #     _loc2_ = PlayerInfoData()
    #     #     creator.write_int(_loc2_.id)
    #     #     creator.write_utf(_loc2_.name)
    #     #     creator.write_int(_loc2_.clanId)
    #     #     creator.write_int(_loc2_.level)
    #     #     return creator.get_package()
    #     #
    #     # def playerLoggedOff(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: PlayerInfoData = None
    #     #     _loc2_ = PlayerInfoData()
    #     #     creator.write_int(_loc2_.id)
    #     #     return creator.get_package()
    #     #
    #     # def friendClans(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: ClanData = None
    #     #     _loc3_: list = None
    #     #     _loc2_ = None
    #     #     _loc3_ = list()
    #     #     while creator.bytesAvailable > 0:
    #     #         _loc2_ = ClanData()
    #     #         creator.write_int(_loc2_.id)
    #     #         creator.write_int(_loc2_.leaderID)
    #     #         creator.write_utf(_loc2_.leaderName)
    #     #         creator.write_utf(_loc2_.logoFileName)
    #     #         creator.write_utf(_loc2_.name)
    #     #         creator.write_utf(_loc2_.shortName)
    #     #         creator.write_unsigned_byte(_loc2_.aliace)
    #     #     return creator.get_package()
    #     #
    #     # def enemyClans(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: ClanData = None
    #     #     _loc3_: list = None
    #     #     _loc2_ = None
    #     #     _loc3_ = list()
    #     #     while creator.bytesAvailable > 0:
    #     #         _loc2_ = ClanData()
    #     #         creator.write_int(_loc2_.id)
    #     #         creator.write_int(_loc2_.leaderID)
    #     #         creator.write_utf(_loc2_.leaderName)
    #     #         creator.write_utf(_loc2_.logoFileName)
    #     #         creator.write_utf(_loc2_.name)
    #     #         creator.write_utf(_loc2_.shortName)
    #     #         creator.write_unsigned_byte(_loc2_.aliace)
    #     #     return creator.get_package()
    #     #
    #     # def friendRequests(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: ClanData = None
    #     #     _loc3_: list = None
    #     #     _loc2_ = None
    #     #     _loc3_ = list()
    #     #     while creator.bytesAvailable > 0:
    #     #         _loc2_ = ClanData()
    #     #         creator.write_int(_loc2_.id)
    #     #         creator.write_int(_loc2_.leaderID)
    #     #         creator.write_utf(_loc2_.leaderName)
    #     #         creator.write_utf(_loc2_.logoFileName)
    #     #         creator.write_utf(_loc2_.name)
    #     #         creator.write_utf(_loc2_.shortName)
    #     #         creator.write_unsigned_byte(_loc2_.aliace)
    #     #     return creator.get_package()
    #     #
    #     # def droidEvent(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: DroidData = None
    #     #     _loc3_: int = 0
    #     #     _loc4_: int = 0
    #     #     _loc2_ = DroidData()
    #     #     creator.write_unsigned_byte(_loc2_.id)
    #     #     creator.write_short(_loc2_.type)
    #     #     creator.write_short(_loc2_.weaponClass)
    #     #     creator.write_int(_loc3_)
    #     #     creator.write_unsigned_byte(_loc4_)
    #     #     return creator.get_package()
    #     #
    def updateValue(self, num_pack, value) -> bytearray:
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.UPDATE_VALUE
        creator.write_unsigned_byte(num_pack)
        creator.write_int(value)
        return creator.get_package()
    #     #
    #     # def missions(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: PlanetData = None
    #     #     _loc3_: list = None
    #     #     _loc4_: list = None
    #     #     _loc5_: ReachableSystem = None
    #     #     _loc6_: int = 0
    #     #     _loc7_: int = 0
    #     #     _loc8_: int = 0
    #     #     _loc9_: int = 0
    #     #     _loc2_ = None
    #     #     _loc3_ = []
    #     #     _loc4_ = []
    #     #     _loc5_ = ReachableSystem()
    #     #     creator.write_int(_loc5_.id)
    #     #     _loc5_.current = True
    #     #     _loc4_.append(_loc5_)
    #     #     creator.write_unsigned_byte(_loc6_)
    #     #     creator.write_unsigned_byte(_loc7_)
    #     #     creator.write_unsigned_byte(_loc8_)
    #     #     _loc9_ = 0
    #     #     while _loc9_ < _loc8_:
    #     #         _loc5_ = ReachableSystem()
    #     #         creator.write_int(_loc5_.id)
    #     #         _loc9_ += 1
    #     #     while creator.bytesAvailable > 0:
    #     #         # _loc2_ = PlanetData()
    #     #         creator.write_int(_loc2_.id)
    #     #         creator.write_bytes(_loc2_.classNumber)
    #     #         creator.write_unsigned_byte(_loc2_.aliance)
    #     #         creator.write_unsigned_byte(_loc2_.race)
    #     #         creator.write_int(_loc2_.starId)
    #     #     return creator.get_package()
    #     #
    #     # def tradeInvitation(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: int = 0
    #     #     _loc3_: int = 0
    #     #     _loc4_: str = ''
    #     #     creator.write_int(_loc2_)
    #     #     creator.write_int(_loc3_)
    #     #     creator.write_utf(_loc4_)
    #     #     return creator.get_package()
    #     #
    #     # def showTrading(self) -> bytearray:
    #     #     creator = PackageCreator()
    #     #     _loc2_: int = 0
    #     #     _loc3_: int = 0
    #     #     _loc4_: str = ''
    #     #     _loc5_: list = []
    #     #     creator.write_int(_loc2_)
    #     #     creator.write_int(_loc3_)
    #     #     creator.write_utf(_loc4_)
    #     #     _loc5_ = self.write_items(creator, True, True)
    #     #     return creator.get_package()
    #     #
    def toGame(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TO_GAME
        return creator.get_package()
