from python.Game._Component.Utils import DotMap
from python.Static.Type.Package.T_ServerRequest import T_ServerRequest


class ReadPackagesClient:
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
    # def isValidPackageLength(self, decoder: int) -> bool:
    #     return 0 <= decoder < 60000

    # def _parsePackages(self) -> list:
    #     _loc1_: BasePackage = None
    #     _loc2_: int = 0
    #     _loc3_: int = 0
    #     _loc4_: BasePackage = None
    #
    #     if self._iLastPackageLength > 0 and self._aBuffer.bytesAvailable >= self._iLastPackageLength:
    #         if T_ServerRequest.isValid(self._iLastServerRequest) and isValidPackageLength(self._iLastPackageLength):
    #             _loc1_ = BasePackage()
    #             _loc1_.type = self._iLastServerRequest
    #             self._aBuffer.read_bytes(_loc1_, 0, self._iLastPackageLength)
    #             self._aAvailablePackages.append(_loc1_)
    #         else:
    #             self.resetBuffer()
    #
    #     _loc5_: bool = False
    #     while self._aBuffer.bytesAvailable >= 8 and not _loc5_:
    #         _loc2_ = self._iLastServerRequest = self._aBuffer.read_int()
    #         _loc3_ = self._iLastPackageLength = self._aBuffer.read_int()
    #         if self._iLastServerRequest == T_ServerRequest.ASTEROIDS:
    #             self._iLastServerRequest.tostr()
    #         if not T_ServerRequest.isValid(self._iLastServerRequest) or not self.isValidPackageLength(self._iLastPackageLength):
    #             self.resetBuffer()
    #             _loc5_ = True
    #         else:
    #             if self._aBuffer.bytesAvailable >= self._iLastPackageLength:
    #                 _loc4_ = BasePackage()
    #                 _loc4_.type = self._iLastServerRequest
    #             if self._iLastPackageLength > 0:
    #                 self._aBuffer.read_bytes(_loc4_, 0, self._iLastPackageLength)
    #             self._aAvailablePackages.append(_loc4_)
    #     else:
    #         _loc5_ = True

    # def process(self, decoder: socket) -> list:
    #     if decoder.bytesAvailable == 0:
    #         return
    #     self._Traffic.input(decoder.bytesAvailable)
    #     decoder.read_bytes(self._aBuffer, len(self._aBuffer), decoder.bytesAvailable)
    #     self._parsePackages()
    #     if self._aBuffer.bytesAvailable == 0:
    #         self.resetBuffer()
    #     try:
    #         processPackages()
    #         return
    #     except:
    #         (oError:Error)
    #     return

    def processPackages(self, _loc1_: int, decoder) -> list:
        match _loc1_:
            case T_ServerRequest.SHIPS_POSITION:
                return self.ships_position(decoder)
            case T_ServerRequest.SHIPS_STASE:
                return self.shipsState(decoder)
            #     case T_ServerRequest.MESSAGE:
            #         return self.message()
            #     case T_ServerRequest.PLAYER_SHIP_UPDATE:
            #         return self.playerShipUpdate()
            #     case T_ServerRequest.PLANETS_STATE:
            #         return self.planetsState()
            #     case T_ServerRequest.PLANETS_UPDATE:
            #         return self.planetsUpdate()
            #     case T_ServerRequest.REPOSITORY:
            #         return self.player_repository()
            #     case T_ServerRequest.CLAN_REPOSITORY:
            #         return self.clanrepository()
            #     case T_ServerRequest.WEAPON_TROUBLES:
            #         return self.weaponTroubles()
            #     case T_ServerRequest.SHIP:
            #         return self.ship()
            #     case T_ServerRequest.SHOOTS:
            #         return self.shoots()
            #     case T_ServerRequest.ITEMS:
            #         return self.items()
            case T_ServerRequest.ACTIVE_DEVICES:
                return self.activeDevices(decoder)
            case T_ServerRequest.ACTIVE_WEPONS:
                return self.activeWeapons(decoder)
            case T_ServerRequest.HIDE_SHIP:
                return self.hideShip(decoder)
            #     case T_ServerRequest.SHIP_DESTROYED:
            #         return self.shipDestroyed()
            #     case T_ServerRequest.SHIP_JUMPED:
            #         return self.shipJumped()
            #     case T_ServerRequest.PLANET:
            #         return self.SpaceObjectItems()
            #     case T_ServerRequest.INVENTORY:
            #         return self.inventory()
            case T_ServerRequest.TRADING_ITEMS:
                return self.tradingItems(decoder)
            #     case T_ServerRequest.RESOURCE_UPDATE_INFO:
            #         return self.resourceUpdate()
            #     case T_ServerRequest.ASTEROIDS:
            #         return self.asteroids()
            #     case T_ServerRequest.EFFECT_CREATED:
            #         return self.effectCreated()
            #     case T_ServerRequest.LOCATION_PLANET:
            #         return self.locationPlanet()
            case T_ServerRequest.LOCATION_SYSTEM:
                return self.locationSystem(decoder)
            #     case T_ServerRequest.LOCATION_BATTLE:
            #         return self.locationBattle()
            case T_ServerRequest.PLAYER:
                return self.player(decoder)
            #     case T_ServerRequest.QUEST_MESSAGE:
            #         return self.questMessage()
            #     case T_ServerRequest.PLAYER_SKILLS:
            #         return self.playerSkills()
            case T_ServerRequest.PLAYER_SKILLS_DATA:
                return self.playerSkillsData(decoder)
            case T_ServerRequest.PLAYER_SHIP:
                return self.playerShip(decoder)
            #     case T_ServerRequest.DROID_BUILDING_DIALOG:
            #         return self.droidBuildingDialog()
            case T_ServerRequest.TRADING_SHIPS:
                return self.tradingShips(decoder)
            case T_ServerRequest.WEAPONS_PARAMETERS:
                return self.weaponsParameters(decoder)
            case T_ServerRequest.ENGINES_PARAMETERS:
                return self.engineParameters(decoder)
            case T_ServerRequest.AMMOS_PARAMETERS:
                return self.ammoParameters(decoder)
            case T_ServerRequest.RESOURCE_PARAMETERS:
                return self.resourceParameters(decoder)
            case T_ServerRequest.DEVICE_PARAMETERS:
                return self.deviceParameters(decoder)
            case T_ServerRequest.DROID_PARAMETERS:
                return self.droidParameters(decoder)
            case T_ServerRequest.SHIP_PARAMETERS:
                return self.shipParameters(decoder)
            case T_ServerRequest.LOGGED:
                return self.logged(decoder)
            case T_ServerRequest.REACHABLE_SYSTEMS:
                return self.reachableSystems(decoder)
            #     case T_ServerRequest.SYSTEM_MESSAGE:
            #         return self.systemMessage()
            #     case T_ServerRequest.LOG_MESSAGE:
            #         return self.logMessage()
            #     case T_ServerRequest.LOG_MESSAGE_STRING:
            #         return self.logMessagestr()
            #     case T_ServerRequest.SYSTEM_MESSAGE_STRING:
            #         return self.systemMessagestr()
            case T_ServerRequest.MAP:
                return self.map(decoder)
            #     case T_ServerRequest.QUESTS_JOURNAL:
            #         return self.questsJournal()
            #     case T_ServerRequest.ARENA_REQUESTS:
            #         return self.arenaRequests()
            #     case T_ServerRequest.PLANET_QUESTS:
            #         return self.planetQuests()
            #     case T_ServerRequest.ADDITIONAL_QUEST_MESSAGE:
            #         return self.additionalQuestMessage()
            #     case T_ServerRequest.BATTLE_REQUEST_CHANGED:
            #         return self.battleRequestChanged()
            case T_ServerRequest.TOP_LIST:
                return self.topList(decoder)
            case T_ServerRequest.TOP_RATING_LIST:
                return self.topRatingList(decoder)
            case T_ServerRequest.TOP_CLANS_LIST:
                return self.topClansList(decoder)
            #     case T_ServerRequest.NEWS_LIST:
            #         return self.sList()
            # case T_ServerRequest.FLASH_CONNECT_REQUEST:
            #     return self.flash_connect()
            case T_ServerRequest.ONLINE:
                return self.online(decoder)
            case T_ServerRequest.VERSION:
                return self.version(decoder)
            #     case T_ServerRequest.SHIP_HEALTH:
            #         return self.shipHealth()
            #     case T_ServerRequest.NPC_MESSAGE:
            #         return self.npcMessage()
            #     case T_ServerRequest.UPDATE_HOLD:
            #         return self.updateHold()
            #     case T_ServerRequest.GINETIC_LAB_OPTIONS:
            #         return self.gineticLabOptions()
            case T_ServerRequest.CLAN:
                return self.clan(decoder)
            #     case T_ServerRequest.CHECK_VALUE_RESULT:
            #         return self.checkValueResult()
            #     case T_ServerRequest.ACCEPTED_CLAN_INFO:
            #         return self.acceptedClanInfo()
            #     case T_ServerRequest.clanId:
            #         return self.clanId()
            #     case T_ServerRequest.CLANS_LETTERS:
            #         return self.clansLetters()
            #     case T_ServerRequest.CLANS_LIST:
            #         return self.clansList()
            #     case T_ServerRequest.CLAN_JOIN_REQUESTS:
            #         return self.clanJoinRequests()
            # case T_ServerRequest.PLAYER_INFO:
            #     return self.playerInfo()

            case T_ServerRequest.PLAYER_LOGGED_ON:
                return self.playerLoggedOn(decoder)
            #     case T_ServerRequest.PLAYER_LOGGED_OFF:
            #         return self.playerLoggedOff()
            case T_ServerRequest.PLAYER_CLAN:
                return self.playerClan(decoder)
            #     case T_ServerRequest.FRIEND_CLANS:
            #         return self.friendClans()
            #     case T_ServerRequest.ENEMY_CLANS:
            #         return self.enemyClans()
            case T_ServerRequest.UPDATE_VALUE:
                return self.updateValue(decoder)
            #     case T_ServerRequest.FRIEND_REQUESTS:
            #         return self.friendRequests()
            #     case T_ServerRequest.DROID_EVENT:
            #         return self.droidEvent()
            #     case T_ServerRequest.EFFECT_REMOVED:
            #         return self.effectRemoved()
            #     case T_ServerRequest.MISSIONS:
            #         return self.missions()
            case T_ServerRequest.TO_GAME:
                return self.toGame(decoder)
        #     case T_ServerRequest.PLAYER_ANGAR:
        #         return self.playerAngar()
        #     case T_ServerRequest.TRADE_INVITATION:
        #         return self.tradeInvitation()
        #     case T_ServerRequest.SHOW_TRADING:
        #         return self.showTrading()
        #     case T_ServerRequest.TRADING_CASH:
        #         return self.GameEngine.tradingCash(.read_int())
        #     case T_ServerRequest.TRADE_SELL_ITEMS:
        #         return self.tradeSellItems()
        #     case T_ServerRequest.EVIL:
        #         return self.Evil()
        #     case T_ServerRequest.TRADE_ACCEPTED:
        #         return self.GameEngine.changeTradingAccepted(.read_bool())
        #     case T_ServerRequest.TRADE_BUY_ITEMS:
        #         return self.tradeBuyItems()
        #     case T_ServerRequest.FINISH_TRADING:
        #         return self.finishTrading()
        #     case T_ServerRequest.SHIP_UPDATE_INFO:
        #         return self.shipUpdateInfo()
        #     case T_ServerRequest.TEAM_LIST:
        #         return self.teamList()
        #     case _:
                # print('НЕИЗВЕСТНЫЙ ПАКЕТ')

    # def flash_connect(self):
    #     decoder = PackageDecoder
    #
    #     def read_f():
    #         with open('test.txt', 'r') as f:
    #             return f.read()
    #
    #     # return PackageDecoder().converter(read_f())
    #     return decoder.read_package()
    #
    # def shipUpdateInfo(self) -> list:
    #     
    #     _loc2_: Restriction = None
    #     _loc3_: ShipFeature = None
    #     _loc4_: int = 0
    #     _loc5_: ResourceCost = None
    #     _loc6_: ShipForSale
    #     _loc6_ = ShipForSale()
    #     decoder.read_short(_loc6_.classfloat)
    #     decoder.read_short(_loc6_.size)
    #     decoder.read_unsigned_byte(_loc6_.weaponSlots)
    #     decoder.read_unsigned_byte(_loc6_.deviceSlots)
    #     decoder.read_unsigned_byte(_loc6_.armor)
    #     decoder.read_unsigned_byte(_loc6_.shields)
    #     decoder.read_short(_loc6_.maxEnergy)
    #     decoder.read_short(_loc6_.maxHealth)
    #     decoder.read_short(_loc6_.cpu)
    #     decoder.read_short(_loc6_.radar)
    #     decoder.read_unsigned_byte(_loc6_.maxSpeed)
    #     _loc7_ = 0
    #     decoder.read_unsigned_byte(_loc7_)
    #     _loc4_ = 0
    #     while _loc4_ < _loc7_:
    #         _loc2_ = Restriction()
    #         decoder.read_unsigned_byte(_loc2_.type)
    #         decoder.read_unsigned_byte(_loc2_.valueType)
    #         decoder.read_int(_loc2_.value)
    #     _loc4_ += 1
    #
    #     _loc8_ = 0
    #     decoder.read_unsigned_byte(_loc8_)
    #     _loc4_ = 0
    #     while _loc4_ < _loc8_:
    #         _loc3_ = ShipFeature()
    #         decoder.read_unsigned_byte(_loc3_.type)
    #         decoder.read_int(_loc3_.value)
    #         _loc4_ += 1
    #     _loc9_: ShipForSale
    #     _loc9_ = ShipForSale()
    #     decoder.read_short(_loc9_.classfloat)
    #     decoder.read_short(_loc9_.size)
    #     decoder.read_unsigned_byte(_loc9_.weaponSlots)
    #     decoder.read_unsigned_byte(_loc9_.deviceSlots)
    #     decoder.read_unsigned_byte(_loc9_.armor)
    #     decoder.read_unsigned_byte(_loc9_.shields)
    #     decoder.read_short(_loc9_.maxEnergy)
    #     decoder.read_short(_loc9_.maxHealth)
    #     decoder.read_short(_loc9_.cpu)
    #     decoder.read_short(_loc9_.radar)
    #     decoder.read_unsigned_byte(_loc9_.maxSpeed)
    #     _loc7_ = 0
    #     decoder.read_unsigned_byte(_loc7_)
    #     _loc4_ = 0
    #     while _loc4_ < _loc7_:
    #         _loc2_ = Restriction()
    #         decoder.read_unsigned_byte(_loc2_.type)
    #         decoder.read_unsigned_byte(_loc2_.valueType)
    #         decoder.read_int(_loc2_.value)
    #         _loc4_ += 1
    #     _loc8_ = 0
    #     decoder.read_unsigned_byte(_loc8_)
    #     _loc4_ = 0
    #     while _loc4_ < _loc8_:
    #         _loc3_ = ShipFeature()
    #         decoder.read_unsigned_byte(_loc3_.type)
    #         decoder.read_int(_loc3_.value)
    #         _loc4_ += 1
    #     decoder.read_bool(_loc9_.satisfying)
    #     _loc10_: UpdateCost
    #     _loc10_ = UpdateCost()
    #     decoder.read_int(_loc10_.cash)
    #     while decoder.bytesAvailable > 0:
    #         _loc5_ = ResourceCost()
    #         decoder.read_short(_loc5_.classfloat)
    #         decoder.read_int(_loc5_.count)
    #         decoder.read_bool(_loc5_.enough)
    #     return decoder.read_package()
    #
    # def finishTrading(self) -> list:
    #     
    #     _loc2_ = 0
    #     decoder.read_int(_loc2_)
    #     _loc3_: list = read_items(decoder, True, False, False)
    #     _loc4_: int = 0
    #     decoder.read_int(_loc4_)
    #     _loc5_: list = read_items(decoder, True, False, False)
    #     return decoder.read_package()
    #
    # def tradeSellItems(self) -> list:
    #     
    #     _loc2_: list = self.read_items(decoder, True, True)
    #     return decoder.read_package()
    #
    # def tradeBuyItems(self) -> list:
    #     
    #     _loc2_: list = self.read_items(decoder, True, True)
    #     return decoder.read_package()

    def playerAngar(self) -> list:
        
        _loc2_: int = 0
        _loc3_: int = 0
        _loc4_ = None  # Restriction
        _loc5_ = None  # ShipFeature
        _loc6_ = None  # ShipForSale
        _loc7_: int = 0
        _loc8_: int = 0
        _loc10_ = 0
        decoder.read_unsigned_byte(_loc10_)
        _loc11_: int = 0
        while _loc11_ < _loc10_:
            # _loc6_ = ShipForSale()
            decoder.read_short(_loc6_.classfloat)
            decoder.read_int(_loc6_.cost)
            decoder.read_short(_loc6_.size)
            decoder.read_bytes(_loc6_.weaponSlots)
            decoder.read_bytes(_loc6_.deviceSlots)
            decoder.read_bytes(_loc6_.armor)
            decoder.read_bytes(_loc6_.shields)
            decoder.read_short(_loc6_.maxEnergy)
            decoder.read_short(_loc6_.maxHealth)
            decoder.read_short(_loc6_.cpu)
            decoder.read_short(_loc6_.radar)
            decoder.read_unsigned_byte(_loc6_.maxSpeed)
            _loc2_ = 0
            decoder.read_unsigned_byte(_loc2_)
            _loc7_ = 0
            while _loc7_ < _loc2_:
                # _loc4_ = Restriction()
                decoder.read_unsigned_byte(_loc4_.type)
                decoder.read_unsigned_byte(_loc4_.valueType)
                decoder.read_int(_loc4_.value)
                _loc7_ += 1
                decoder.read_unsigned_byte(_loc3_)
                _loc8_ = 0
                while _loc8_ < _loc3_:
                    decoder.read_unsigned_byte(_loc5_.type)
                    decoder.read_int(_loc5_.value)
                    _loc8_ += 1
                    decoder.read_bool(_loc6_.satisfying)
                    _loc11_ += 1
        return decoder.read_package()

    #
    #     # def updateHold(self) -> list:
    #     #     
    #     #     _loc2_ = False
    #     #     decoder.read_bool(_loc2_)
    #     #     _loc3_: list = self.read_items(decoder, True, True, True, _loc2_)
    #     #     _loc4_: list
    #     #     _loc4_ = self.read_items(decoder, True, True, True, len(_loc2_))
    #     #     return decoder.read_package()
    #     #
    #     # def gineticLabOptions(self) -> list:
    #     #     
    #     #     _loc2_: GineticLabOption = None
    #     #     _loc3_: int = 0
    #     #     decoder.read_unsigned_byte(_loc3_)
    #     #     _loc4_: list = list()
    #     #     _loc5_: int = 0
    #     #     while _loc5_ < _loc3:
    #     #         _loc2_ = GineticLabOption()
    #     #         decoder.read_unsigned_byte(_loc2_.option)
    #     #         decoder.read_int(_loc2_.cost)
    #     #         _loc5_ += 1
    #     #     return decoder.read_package()
    #     #
    #     # def npcMessage(self) -> list:
    #     #     
    #     #     _loc2_: int = 0
    #     #     decoder.read_int(_loc2_)
    #     #     _loc3_: int = 0
    #     #     decoder.read_int(_loc3_)
    #     #     return decoder.read_package()
    #     #
    #     # def additionalQuestMessage(self) -> list:
    #     #     
    #     #     _loc2_: int = 0
    #     #     decoder.read_int(_loc2_)
    #     #     _loc3_: int = 0
    #     #     decoder.read_int(_loc3_)
    #     #     return decoder.read_package()
    #     #
    #     # def arenaRequests(self) -> list:
    #     #     
    #     #     _loc2_: BattleRequest = None
    #     #     _loc3_: list = list()
    #     #     _loc4_: int = 0
    #     #     decoder.read_int(_loc4_)
    #     #     _loc5_: int = 0
    #     #     while _loc5_ < _loc4_:
    #     #         _loc2_ = BattleRequest()
    #     #         decoder.read_int(_loc2_.id)
    #     #         decoder.read_int(_loc2_.playersCount)
    #     #         decoder.read_int(_loc2_.maxPlayers)
    #     #         decoder.read_int(_loc2_.maxShipType)
    #     #         decoder.read_int(_loc2_.minShipType)
    #     #         decoder.read_unsigned_byte(_loc2_.type)
    #     #         _loc5_ += 1
    #     #     return decoder.read_package()
    #     #
    #     # def battleRequestChanged(self) -> list:
    #     #     
    #     #     _loc2_: BattleRequestPlayer = None
    #     #     _loc3_: BattleRequest = BattleRequest()
    #     #     decoder.read_int(_loc3_.id)
    #     #     decoder.read_int(_loc3_.playersCount)
    #     #     decoder.read_int(_loc3_.maxPlayers)
    #     #     decoder.read_int(_loc3_.maxShipType)
    #     #     decoder.read_int(_loc3_.minShipType)
    #     #     decoder.read_unsigned_byte(_loc3_.type)
    #     #     decoder.read_int(_loc3_.award)
    #     #     _loc3_.cost = (_loc3_.type - 1) * 2000
    #     #     _loc4_: int = 0
    #     #     while _loc4_ < _loc3_.playersCoun:
    #     #         _loc2_ = BattleRequestPlayer()
    #     #         decoder.read_bool(_loc2_.isReady)
    #     #         decoder.read_int(_loc2_.id)
    #     #         decoder.read_utf(_loc2_.login)
    #     #         decoder.read_int(_loc2_.level)
    #     #         decoder.read_int(_loc2_.shipClass)
    #     #         decoder.read_int(_loc2_.race)
    #     #         _loc3_.players.append(_loc2_)
    #     #         _loc4_ += 1
    #     #     return decoder.read_package()
    #     #
    #     # def questsJournal(self) -> list:
    #     #     
    #     #     _loc2_: QuestPackage = None
    #     #     _loc3_: list = list()
    #     #     _loc4_: int = decoder.read_int()
    #     #     _loc5_: int = 0
    #     #     while _loc5_ < _loc4_:
    #     #         _loc2_ = QuestPackage()
    #     #         decoder.read_int(_loc2_.questId)
    #     #         decoder.read_int(_loc2_.giverType)
    #     #         decoder.read_utf(_loc2_.giverName)
    #     #         decoder.read_utf(_loc2_.Name)
    #     #         _loc3_.append(_loc2_)
    #     #         _loc5_ += 1
    #     #     return decoder.read_package()
    #     #
    def activeDevices(self, decoder):
        data = []
        decoder.read_int()
        _loc5_ = decoder.read_unsigned_byte()
        _loc6_: int = 0
        while _loc6_ < _loc5_:
            _loc3_ = DotMap()
            _loc3_.id = decoder.read_short()
            _loc3_.guid = decoder.read_bytes(16)
            _loc3_.reloadedTime = decoder.read_float()
            data.append(_loc3_)
            _loc6_ += 1
        return data

    def activeWeapons(self, decoder) -> list:
        data = []
        decoder.read_int()
        _loc4_ = decoder.read_unsigned_byte()
        _loc5_: int = 0
        while _loc5_ < _loc4_:
            _loc2_ = DotMap()
            _loc2_.classfloat = decoder.read_short()
            _loc2_.index = decoder.read_unsigned_byte()

            data.append(_loc2_)
            _loc5_ += 1
        return data
    #     #
    #     # def playerShipUpdate(self) -> list:
    #     #     
    #     #     _loc2_: PlayerShip = PlayerShip()
    #     #     decoder.read_short(_loc2_.energy)
    #     #     decoder.read_short(_loc2_.health)
    #     #     decoder.read_unsigned_byte(_loc2_.controlLeft)
    #     #     decoder.read_unsigned_byte(_loc2_.controlUsed)
    #     #     return decoder.read_package()
    #     #
    def tradingShips(self, decoder) -> DotMap:
        w = decoder.read_int()
        _loc9_ = decoder.read_int()
        _loc10_ = decoder.read_int()
        _loc11_ = decoder.read_float()
        _loc12_ = decoder.read_float()
        _loc13_ = decoder.read_int()
        _loc15_ = 0
        _loc0_ = DotMap()
        _loc0_.value = []
        _loc0_.one = _loc9_
        _loc0_.two = _loc10_
        _loc0_.free = _loc11_
        _loc0_.foo = _loc12_
        _loc0_.five = _loc13_
        while _loc15_ < _loc13_:
            _loc6_ = DotMap()
            _loc6_.guid = self.read_guid(decoder)
            _loc6_.classfloat = decoder.read_short()
            _loc6_.cost = decoder.read_int()
            _loc6_.size = decoder.read_short()
            _loc6_.weaponSlots = decoder.read_unsigned_byte()
            _loc6_.deviceSlots = decoder.read_unsigned_byte()
            _loc6_.armor = decoder.read_unsigned_byte()
            _loc6_.shields = decoder.read_unsigned_byte()
            _loc6_.maxEnergy = decoder.read_short()
            _loc6_.maxHealth = decoder.read_short()
            _loc6_.cpu = decoder.read_short()
            _loc6_.radar = decoder.read_short()
            _loc6_.maxSpeed = decoder.read_unsigned_byte()
            _loc2_ = decoder.read_unsigned_byte()
            _loc7_ = 0
            _loc6_.rest = []
            while _loc7_ < _loc2_:
                _loc4_ = DotMap()
                _loc4_.type = decoder.read_unsigned_byte()
                _loc4_.valueType = decoder.read_unsigned_byte()
                _loc4_.value = decoder.read_int()
                _loc7_ += 1
                _loc6_.rest.append(_loc4_)
            _loc3_ = decoder.read_unsigned_byte()
            _loc8_ = 0
            _loc6_.feat = []
            while _loc8_ < _loc3_:
                _loc5_ = DotMap()
                _loc5_.type = decoder.read_unsigned_byte()
                _loc5_.value = decoder.read_int()
                _loc8_ += 1
                _loc6_.feat.append(_loc5_)
            _loc6_.satisfying = decoder.read_bool()
            _loc15_ += 1
            _loc0_.value.append(_loc6_)
        return _loc0_
    #     #
    def tradingItems(self, decoder) -> list:
        decoder.read_int()
        _loc2_: int = decoder.read_int()
        _loc3_: float = decoder.read_float()
        _loc4_: float = decoder.read_float()
        print(_loc2_, _loc3_, _loc4_)
        _loc5_ = self.read_items(decoder, True, True, True, True)
        _loc6_ = self.read_items(decoder, True, True, True, True)
        return _loc2_, _loc3_, _loc4_, _loc5_, _loc6_

    #     # def resourceUpdate(self) -> list:
    #     #     
    #     #     _loc2_: int = 0
    #     #     decoder.read_int(_loc2_)
    #     #     _loc3_: float = 1
    #     #     _loc4_: float = 1
    #     #     _loc5_: list = self.read_items(decoder, True, True)
    #     #     _loc6_: list = self.read_items(decoder, True, True)
    #     #     return decoder.read_package()
    #     #
    def read_items(self, decoder, param2: bool, param3: bool, param4: bool = True, param5: bool = False):

        _loc8_ = decoder.read_int()
        _loc9_: int = 0
        e = []
        print(_loc8_)
        while _loc9_ < _loc8_:
            i = DotMap()
            i.classfloat = decoder.read_int()
            i.guid = self.read_guid(decoder)
            i.wear = decoder.read_int()
            print(f'{i.wear=}, {i.classfloat=}, {i.guid=}')
            if param4:
                # print(i)
                i.level = decoder.read_int()
            else:
                i.level = 1
            if param2:
                zeroCost = 0
                i.zeroCost = decoder.read_bool()
            if param5:
                i.hz = decoder.read_int()
            if param3:
                satisfying = False
                i.satisfying = decoder.read_bool()
            _loc9_ += 1
            e.append(i)
        return e

    def ships_position(self, decoder) -> list:
        data = []
        hz = decoder.read_int()
        _loc3_ = decoder.read_int()
        if hz == 16:
            _loc3_ = 1
        if hz != 16 and hz != 4:
            print(hz)
            print('\n\n\n\n\n EROOOOOOOOOOOOOOOOOOOOR')
        cnt = 0
        while cnt != _loc3_:
            _loc2_ = DotMap()
            _loc2_.id = decoder.read_int()
            _loc2_.x = decoder.read_short()
            _loc2_.y = decoder.read_short()
            _loc2_.targetX = decoder.read_short()
            _loc2_.targetY = decoder.read_short()
            data.append(_loc2_)
            cnt += 1
        return data
    #     #
    def shipsState(self, decoder) -> list:
        data = []
        cnt_ship = decoder.read_int()
        cnt = 0
        # while cnt != cnt_ship:
        _loc2_ = DotMap()
        _loc2_.id = decoder.read_int()
        _loc2_.speed = decoder.read_unsigned_byte() # * 1000
        _loc2_.health = decoder.read_short()
        _loc2_.energy = decoder.read_short()
        _loc2_.PlayerRelation = decoder.read_short()
        data.append(_loc2_)
        cnt += 1
        return data
    #     #
    #     # def weaponTroubles(self) -> list:
    #     #     
    #     #     _loc2_: WeaponTrouble = None
    #     #     _loc3_: int = 0
    #     #     decoder.read_unsigned_byte(_loc3_)
    #     #     _loc4_: list = list()
    #     #     _loc5_: int = 0
    #     #     while _loc5_ < _loc3_:
    #     #         _loc2_ = WeaponTrouble()
    #     #         decoder.read_unsigned_byte(_loc2_.trouble)
    #     #         decoder.read_unsigned_byte(_loc2_.index)
    #     #         _loc5_ += 1
    #     #     return decoder.read_package()
    #     #
    #     # def player_repository(self) -> list:
    #     #     
    #     #     _loc2_: ItemPackage = None
    #     #     # _loc3_: list = read_items(decoder, False, False)
    #     #     _loc4_: float = decoder.read_float()
    #     #     _loc5_: list = list()
    #     #     _loc6_: int = decoder.read_int()
    #     #     _loc7_: int = 0
    #     #     while _loc7_ < _loc6_:
    #     #         _loc2_ = ItemPackage()
    #     #         decoder.read_int(_loc2_.classfloat)
    #     #         # _loc2_.guid = read_guid(decoder)
    #     #         decoder.read_int(_loc2_.wear)
    #     #         decoder.read_int(_loc2_.level)
    #     #         # decoder.read_int()
    #     #         _loc7_ += 1
    #     #     return decoder.read_package()
    #     #
    #     # def clanrepository(self) -> list:
    #     #     
    #     #     _loc2_: ItemPackage = None
    #     #     # _loc3_: list = read_items(decoder, False, False)
    #     #     _loc4_: float = decoder.read_float()
    #     #     _loc5_: list = list()
    #     #     _loc6_: int = decoder.read_int()
    #     #     _loc7_: int = 0
    #     #     while _loc7_ < _loc6_:
    #     #         _loc2_ = ItemPackage()
    #     #         decoder.read_int(_loc2_.classfloat)
    #     #         # _loc2_.guid = read_guid(decoder)
    #     #         decoder.read_int(_loc2_.wear)
    #     #         decoder.read_int(_loc2_.level)
    #     #         # decoder.read_int()
    #     #         _loc7_ += 1
    #     #
    #     #     return decoder.read_package()
    #     #
    #     # def planetsState(self) -> list:
    #     #     
    #     #     _loc2_: int = 0
    #     #     _loc3_: float = None
    #     #     _loc4_: int = 0
    #     #     decoder.read_unsigned_byte(_loc4_)
    #     #     _loc5_: int = 0
    #     #     while _loc5_ < _loc4_:
    #     #         _loc2_ = 0
    #     #         decoder.read_int(_loc2_)
    #     #         _loc3_ = 0
    #     #         decoder.read_float(_loc3_)
    #     #     return decoder.read_package()
    #     #
    #     # def planetsUpdate(self) -> list:
    #     #     
    #     #     _loc2_: int = 0
    #     #     _loc3_: float = None
    #     #     _loc4_: int = 0
    #     #     _loc5_: int = 0
    #     #     _loc6_: int = 0
    #     #     _loc7_: int = 0
    #     #     decoder.read_unsigned_byte(_loc7_)
    #     #     _loc8_: int = 0
    #     #     while _loc8_ < _loc7_:
    #     #         _loc2_ = 0
    #     #         decoder.read_int(_loc2_)
    #     #         _loc3_ = 0
    #     #         decoder.read_float(_loc3_)
    #     #         _loc4_ = 0
    #     #         decoder.read_bytes(_loc4_)
    #     #         _loc5_ = 0
    #     #         decoder.read_bytes(_loc5_)
    #     #         _loc6_ = 0
    #     #         decoder.read_int(_loc6_)
    #     #     return decoder.read_package()
    #     #
    #     # def ship(self) -> list:
    #     #     
    #     #     _loc2_: DroidData = None
    #     #     # _loc3_: Owner = ShipsManager.createInstance(decoder.read_short())
    #     #     decoder.read_int(_loc3_.id)
    #     #     decoder.read_utf(_loc3_.Name)
    #     #     decoder.read_short(_loc3_.size)
    #     #     # _loc3_.setPosition = decoder.read_float(), decoder.read_float())
    #     #     decoder.read_int(_loc3_.player.level)
    #     #     decoder.read_short(_loc3_.maxHealth)
    #     #     decoder.read_short(_loc3_.maxEnergy)
    #     #     decoder.read_int(_loc3_.player.avatar)
    #     #     decoder.read_unsigned_byte(_loc3_.maxSpeed) / 1000
    #     #     # _loc3_.setMovePoint(decoder.read_float(), decoder.read_float())
    #     #     decoder.read_unsigned_byte(_loc3_.player.aliance)
    #     #     decoder.read_unsigned_byte(_loc3_.player.status)
    #     #     decoder.read_int(_loc3_.player.clanId)
    #     #     _loc4_: int = 0
    #     #     decoder.read_unsigned_byte(_loc4_)
    #     #     _loc5_: int = 0
    #     #     while _loc5_ < _loc4_:
    #     #         _loc2_ = DroidData()
    #     #         decoder.read_unsigned_byte(_loc2_.id)
    #     #         decoder.read_short(_loc2_.type)
    #     #         decoder.read_short(_loc2_.weaponClass)
    #     #         decoder.read_short(_loc2_.health)
    #     #         _loc5_ += 1
    #     #     return decoder.read_package()
    #     #
    #     # def SpaceObjectItems(self) -> list:
    #     #     
    #     #     # _loc2_: DB_Planet = PlanetsManager.createInstance(decoder.read_bytes())
    #     #     decoder.read_int(_loc2_.id)
    #     #     T_Race.defineById(self, decoder.read_unsigned_byte(_loc2_.race))
    #     #     decoder.read_int(_loc2_.RADIUS_BETWEEN_PLANET)
    #     #     decoder.read_int(_loc2_.size)
    #     #     decoder.read_float(_loc2_.serverAngle)
    #     #     decoder.read_bool(_loc2_.landable)
    #     #     return decoder.read_package()
    #     #
    #     # def inventory(self) -> list:
    #     #     
    #     #     _loc2_: I_Item = None
    #     #     _loc3_: bytearray = None
    #     #     _loc4_: list = list()
    #     #     _loc5_: int = decoder.read_short()
    #     #     _loc6_: int = 0
    #     #     while _loc6_ < _loc5_:
    #     #         _loc2_ = ItemsManager.createInstance(decoder.read_short())
    #     #         _loc3_ = bytearray()
    #     #         decoder.read_bytes(_loc3_, 0, 16)
    #     #         _loc2_.guid = _loc3_
    #     #         decoder.read_short(_loc2_.wear)
    #     #         decoder.read_bool(_loc2_.inUsing)
    #     #         decoder.read_unsigned_byte(_loc2_.level)
    #     #         decoder.read_bool(_loc2_.satisfying)
    #     #         _loc6_ += 1
    #     #     _loc7_: ShipParametersPackage
    #     #     _loc7_ = ShipParametersPackage()
    #     #     decoder.read_unsigned_byte(_loc7_.armor)
    #     #     decoder.read_unsigned_byte(_loc7_.shields)
    #     #     decoder.read_short(_loc7_.usedSpace)
    #     #     decoder.read_short(_loc7_.cpu)
    #     #     decoder.read_short(_loc7_.cpuUsed)
    #     #     decoder.read_unsigned_byte(_loc7_.level)
    #     #     decoder.read_unsigned_byte(_loc7_.maxDroids)
    #     #     _loc8_: list = list()
    #     #     while decoder.bytesAvailable > 0:
    #     #         _loc2_ = ItemsManager.createInstance(decoder.read_short())
    #     #         decoder.read_bytes(_loc2_.id)
    #     #     return decoder.read_package()
    #     #
    def player(self, decoder) -> list:
        data = []
        hz = decoder.read_int()
        Player = DotMap()
        Player.id = decoder.read_int()
        Player.login = decoder.read_utf()
        Player.level = decoder.read_int()
        Player.cash = decoder.read_int()
        Player.race = decoder.read_unsigned_byte()
        Player.avatar = decoder.read_int()
        Player.aliance = decoder.read_unsigned_byte()
        Player.clanId = decoder.read_int()
        Player.role = decoder.read_int()
        Player.clanRequestStatus = decoder.read_unsigned_byte()
        Player.clanJoinRequestStatus = decoder.read_unsigned_byte()
        Player.PlayerRelation = decoder.read_int()
        data.append(Player)
        return data

    #     #
    #     # def questMessage(self) -> list:
    #     #     
    #     #     _loc2_: str = None
    #     #     _loc3_: QuestAward = None
    #     #     _loc4_: QuestTarget = None
    #     #     _loc5_: QuestPackage
    #     #     _loc5_ = QuestPackage()
    #     #     decoder.read_int(_loc5_.questId)
    #     #     decoder.read_int(_loc5_.nextQuestId)
    #     #     decoder.read_int(_loc5_.giverType)
    #     #     decoder.read_int(_loc5_.status)
    #     #     decoder.read_utf(_loc5_.giverName)
    #     #     _loc6_ = 0
    #     #     decoder.read_int(_loc6_)
    #     #     _loc7_: int = 0
    #     #     while _loc7_ < _loc6_:
    #     #         _loc2_ = ''
    #     #         decoder.read_utf(_loc2_)
    #     #         _loc7_ += 1
    #     #     decoder.read_int(_loc5_.ParentSystemID)
    #     #     decoder.read_unsigned_byte(_loc5_.LocationType)
    #     #     decoder.read_int(_loc5_.LocationID)
    #     #     _loc8_ = 0
    #     #     decoder.read_int(_loc8_)
    #     #     _loc9_: int = 0
    #     #     while _loc9_ < _loc8_:
    #     #         # _loc3_ = QuestAward()
    #     #         decoder.read_int(_loc3_.classfloat)
    #     #         decoder.read_int(_loc3_.level)
    #     #         decoder.read_int(_loc3_.type)
    #     #         decoder.read_int(_loc3_.value)
    #     #         _loc9_ += 1
    #     #     _loc10_ = 0
    #     #     decoder.read_int(_loc10_)
    #     #     _loc11_: int = 0
    #     #     while _loc11_ < _loc10_:
    #     #         # _loc4_ = QuestTarget()
    #     #         decoder.read_int(_loc4_.targetId)
    #     #         decoder.read_int(_loc4_.targetSystemId)
    #     #         decoder.read_int(_loc4_.targetPlanetId)
    #     #         decoder.read_int(_loc4_.type)
    #     #         decoder.read_int(_loc4_.value)
    #     #         _loc5_.targets.append(_loc4_)
    #     #         _loc11_ += 1
    #     #     return decoder.read_package()
    #     #
    #     # def playerSkills(self) -> list:
    #     #     
    #     #     _loc2_: PlayerSkills = PlayerSkills()
    #     #     decoder.read_unsigned_byte(_loc2_.level)
    #     #     decoder.read_int(_loc2_.experience)
    #     #     decoder.read_int(_loc2_.expForNext)
    #     #     # read_skills(decoder, _loc2_)
    #     #     decoder.read_int(_loc2_.freeSkills)
    #     #     decoder.read_int(_loc2_.expForFirstSkillLevel)
    #     #     decoder.read_float(_loc2_.expSkillGrowCoef)
    #     #     decoder.read_float(_loc2_.expSkillReduserCoef)
    #     #     decoder.read_unsigned_byte(_loc2_.maxSkill)
    #     #     # _loc3_: PlayerStatistics = PlayerStatistics()
    #     #     decoder.read_unsigned_byte(_loc3_.status)
    #     #     decoder.read_unsigned_byte(_loc3_.level)
    #     #     decoder.read_int(_loc3_.pirateStatus)
    #     #     decoder.read_int(_loc3_.policeStatus)
    #     #     decoder.read_int(_loc3_.forNextLevel)
    #     #     return decoder.read_package()
    #     #
    def read_skills(self, decoder) -> DotMap:
        param2 = DotMap()
        param2.Control = decoder.read_unsigned_byte()
        param2.Defending = decoder.read_unsigned_byte()
        param2.EnergyWeapons = decoder.read_unsigned_byte()
        param2.KineticWeapons = decoder.read_unsigned_byte()
        param2.Mining = decoder.read_unsigned_byte()
        param2.Piloting = decoder.read_unsigned_byte()
        param2.Repairing = decoder.read_unsigned_byte()
        param2.RocketWeapons = decoder.read_unsigned_byte()
        param2.Trading = decoder.read_unsigned_byte()
        param2.Attacking = decoder.read_unsigned_byte()
        param2.Tactics = decoder.read_unsigned_byte()
        param2.Targeting = decoder.read_unsigned_byte()
        param2.Electronics = decoder.read_unsigned_byte()
        param2.Biocemistry = decoder.read_unsigned_byte()
        param2.Mechanics = decoder.read_unsigned_byte()
        param2.Cybernetics = decoder.read_unsigned_byte()
        return param2
    #     #
    def playerSkillsData(self, decoder) -> list:
        data = []
        decoder.read_int()

        _loc2_ = DotMap()
        _loc2_.level = decoder.read_unsigned_byte()
        _loc2_.experience = decoder.read_int()
        _loc2_.expForNext = decoder.read_int()

        _loc2_.skills = self.read_skills(decoder)
        _loc2_.freeSkills = decoder.read_int()
        _loc2_.expForFirstSkillLevel = decoder.read_int()
        _loc2_.expSkillGrowCoef = decoder.read_float()
        _loc2_.expSkillReduserCoef = decoder.read_float()
        _loc2_.maxSkill = decoder.read_unsigned_byte()
        data.append(_loc2_)

        _loc3_ = DotMap() #PlayerStatistics
        _loc3_.status = decoder.read_unsigned_byte()
        _loc3_.level = decoder.read_unsigned_byte()
        _loc3_.pirateStatus = decoder.read_int()
        _loc3_.policeStatus = decoder.read_int()
        data.append(_loc3_)
        return data
    #     #
    def playerShip(self, decoder) -> list:
        data = []
        _loc2_ = decoder.read_int()
        _loc2_ = decoder.read_int()
        Player = DotMap()
        Player.ship = DotMap()

        Player.ship.id = decoder.read_int()
        Player.ship.Name = decoder.read_utf()
        Player.ship.size = decoder.read_int()
        Player.ship.energy = decoder.read_int()
        Player.ship.maxEnergy = decoder.read_int()
        Player.ship.setPosition = decoder.read_float(), decoder.read_float()
        Player.ship.team = decoder.read_int()
        Player.ship.maxSpeed = decoder.read_unsigned_byte() * 1000
        Player.ship.weaponSlots = decoder.read_unsigned_byte()
        Player.ship.deviceSlots = decoder.read_unsigned_byte()
        Player.ship.maxHealth = decoder.read_int()
        Player.ship.radarRadius = decoder.read_short()
        Player.ship.cpu = decoder.read_short()
        data.append(Player)
        return data
    #     #
    def weaponsParameters(self, decoder) -> list:
        _loc2_ = None  # WeaponParameters
        _loc3_: int = 0
        _loc4_: int = 0
        _loc5_ = None  # Restriction
        cnt_weapon = decoder.read_int()
        cnt_weapon = decoder.read_int()
        _loc8_: int = 0
        data = []
        while _loc8_ < cnt_weapon:
            _loc2_ = DotMap()  # WeaponParameters()
            _loc2_.classfloat = decoder.read_int()
            _loc2_.autoShots = decoder.read_int()
            _loc2_.radius = decoder.read_int()
            _loc2_.reloadTime = decoder.read_int()
            _loc2_.energyCost = decoder.read_int()
            _loc2_.size = decoder.read_float()
            _loc2_.cost = decoder.read_int()
            _loc2_.needAmmo = decoder.read_bool()
            _loc2_.ammoClass = decoder.read_int()
            _loc2_.minDamage = decoder.read_int()
            _loc2_.maxDamage = decoder.read_int()
            _loc2_.type = decoder.read_unsigned_byte()
            _loc2_.effect = decoder.read_unsigned_byte()
            _loc2_.maxWear = decoder.read_int()
            addition = decoder.read_unsigned_byte()
            _loc4_ = 0
            all_addition = []
            while _loc4_ < addition:
                _loc5_ = DotMap()
                _loc5_.type = decoder.read_unsigned_byte()
                _loc5_.valueType = decoder.read_unsigned_byte()
                _loc5_.value = decoder.read_int()

                all_addition.append(_loc5_)
                _loc4_ += 1

            _loc2_.addition = all_addition
            data.append(_loc2_)
            _loc8_ += 1
        return data

    #     #
    def ammoParameters(self, decoder) -> list:
        data = []
        hz = decoder.read_int()
        cnt_ammo = decoder.read_int()
        _loc5_: int = 0
        while _loc5_ < cnt_ammo:
            _loc2_ = DotMap()  # AmmoParameters()
            _loc2_.classfloat = decoder.read_int()
            _loc2_.size = decoder.read_float()
            _loc2_.cost = decoder.read_int()
            _loc2_.damage = decoder.read_int()

            data.append(_loc2_)
            _loc5_ += 1
        return data

    def resourceParameters(self, decoder) -> list:
        data = []
        cnt_res: int = 0
        cnt_res = decoder.read_int()
        cnt_res = decoder.read_int()
        _loc5_: int = 0
        while _loc5_ < cnt_res:
            _loc2_ = DotMap()  # ResourceParameters()
            _loc2_.classfloat = decoder.read_int()
            _loc2_.size = decoder.read_float()
            _loc2_.cost = decoder.read_int()

            data.append(_loc2_)
            _loc5_ += 1
        return data

    def deviceParameters(self, decoder) -> list:
        data = []
        _loc2_: int = 0
        # _loc3_: DeviceEffect = None
        # _loc4_: DeviceParameters = None
        _loc5_: int = 0
        _loc6_: int = 0
        _loc7_: int = 0
        # _loc8_: Restriction = None
        cnt_device = decoder.read_int()
        cnt_device = decoder.read_int()
        _loc11_: int = 0
        while _loc11_ < cnt_device:
            _loc4_ = DotMap()
            _loc4_.classfloat = decoder.read_int()
            _loc4_.size = decoder.read_float()
            _loc4_.cost = decoder.read_int()
            _loc4_.energyCost = decoder.read_int()
            _loc4_.reloadTime = decoder.read_int()
            _loc4_.maxWear = decoder.read_int()
            cnt_dev_eff = decoder.read_unsigned_byte()
            data_dev_eff = []
            _loc5_ = 0
            while _loc5_ < cnt_dev_eff:
                _loc3_ = DotMap()
                _loc3_.targetType = decoder.read_unsigned_byte()
                _loc3_.value = decoder.read_int()
                _loc3_.effectTime = decoder.read_int()
                _loc3_.effectType = decoder.read_unsigned_byte()

                data_dev_eff.append(_loc3_)
                _loc5_ += 1
            _loc4_.cnt_dev_eff = cnt_dev_eff

            cnt_restr = decoder.read_unsigned_byte()
            restr = []
            _loc7_ = 0
            while _loc7_ < cnt_restr:
                _loc8_ = DotMap()
                _loc8_.type = decoder.read_unsigned_byte()
                _loc8_.valueType = decoder.read_unsigned_byte()
                _loc8_.value = decoder.read_int()

                restr.append(_loc8_)
                _loc7_ += 1

            _loc4_.restr = restr
            data.append(_loc4_)
            _loc11_ += 1
        return data

    def droidParameters(self, decoder) -> list:
        data = []
        # _loc2_: DroidParameters = None
        _loc3_: int = 0
        _loc4_: int = 0
        # _loc5_: Restriction = None
        cnt_droid = decoder.read_int()
        cnt_droid = decoder.read_int()
        _loc8_: int = 0
        while _loc8_ < cnt_droid:
            _loc2_ = DotMap()
            _loc2_.classfloat = decoder.read_short()
            _loc2_.size = decoder.read_float()
            _loc2_.cost = decoder.read_int()
            _loc2_.energyCost = decoder.read_unsigned_byte()
            _loc2_.armor = decoder.read_unsigned_byte()
            _loc2_.droidType = decoder.read_short()
            _loc2_.weaponClass = decoder.read_short()
            _loc2_.health = decoder.read_short()

            cnt_restr = decoder.read_unsigned_byte()
            restr = []
            _loc4_ = 0
            while _loc4_ < cnt_restr:
                _loc5_ = DotMap()  # Restriction()
                _loc5_.type = decoder.read_unsigned_byte()
                _loc5_.valueType = decoder.read_unsigned_byte()
                _loc5_.value = decoder.read_int()

                restr.append(_loc5_)
                _loc4_ += 1

            _loc2_.restr = restr
            data.append(_loc2_)
            _loc8_ += 1
        return data

    #     #
    def shipParameters(self, decoder) -> list:
        data = []
        decoder.read_int()
        cnt_ship = decoder.read_int()
        _loc11_: int = 0
        while _loc11_ < cnt_ship:
            _loc2_ = DotMap()
            _loc2_.classfloat = decoder.read_short()
            _loc2_.cost = decoder.read_int()
            _loc2_.size = decoder.read_short()
            _loc2_.weaponSlots = decoder.read_unsigned_byte()
            _loc2_.deviceSlots = decoder.read_unsigned_byte()
            _loc2_.armor = decoder.read_unsigned_byte()
            _loc2_.shields = decoder.read_unsigned_byte()
            _loc2_.maxEnergy = decoder.read_short()
            _loc2_.maxHealth = decoder.read_short()
            _loc2_.cpu = decoder.read_short()
            _loc2_.radar = decoder.read_short()
            _loc2_.maxSpeed = decoder.read_unsigned_byte()

            cnt_restr = decoder.read_unsigned_byte()
            restr = []
            _loc4_ = 0
            while _loc4_ < cnt_restr:
                _loc7_ = DotMap()
                _loc7_.type = decoder.read_unsigned_byte()
                _loc7_.valueType = decoder.read_unsigned_byte()
                _loc7_.value = decoder.read_int()

                restr.append(_loc7_)
                _loc4_ += 1

            _loc2_.restr = restr
            cnt_ship_feat = decoder.read_unsigned_byte()
            ship_feat = []
            _loc6_ = 0
            while _loc6_ < cnt_ship_feat:
                _loc8_ = DotMap()
                _loc8_.type = decoder.read_unsigned_byte()
                _loc8_.value = decoder.read_int()

                ship_feat.append(_loc8_)
                _loc6_ += 1

            _loc2_.ship_feat = ship_feat
            data.append(_loc2_)
            _loc11_ += 1
        return data

    def engineParameters(self, decoder) -> list:
        data = []
        cnt_engine = decoder.read_int()
        cnt_engine = decoder.read_int()
        _loc5_: int = 0
        while _loc5_ < cnt_engine:
            _loc2_ = DotMap()
            _loc2_.classfloat = decoder.read_short()
            _loc2_.size = decoder.read_float()
            _loc2_.cost = decoder.read_int()
            _loc2_.hyperjumpRadius = decoder.read_unsigned_byte()
            _loc2_.maxWear = decoder.read_int()
            _loc2_.energyCost = decoder.read_unsigned_byte()

            data.append(_loc2_)
            _loc5_ += 1
        return data

    #     #
    def map(self, decoder) -> list:
        data = []
        _loc2_ = None  # ReachableSystem
        _loc4_: int = 0
        _loc6_: int = 0
        _loc7_ = None  # PlanetData
        _loc8_ = None  # StaticObjectData
        cnt_system = decoder.read_short()
        cnt_system = decoder.read_short()
        cnt_system = decoder.read_short()
        _loc11_: int = 0
        while _loc11_ < cnt_system:
            _loc2_ = DotMap()  # ReachableSystem()
            _loc2_.id = decoder.read_unsigned_byte()
            _loc2_.classfloat = decoder.read_unsigned_byte()
            _loc2_.x = decoder.read_short()
            _loc2_.y = decoder.read_short()
            _loc2_.sector = decoder.read_unsigned_byte()
            _loc2_.lineTo = decoder.read_unsigned_byte()
            cnt_planet = decoder.read_unsigned_byte()
            planet = []
            _loc4_ = 0
            while _loc4_ < cnt_planet:
                _loc7_ = DotMap()  # PlanetData()
                _loc7_.id = decoder.read_short()
                _loc7_.race = decoder.read_unsigned_byte()
                _loc7_.classfloat = decoder.read_unsigned_byte()
                _loc7_.aliance = decoder.read_unsigned_byte()

                planet.append(_loc7_)
                _loc4_ += 1

            _loc2_.planet = planet
            cnt_static_object = decoder.read_unsigned_byte()
            static_object = []
            _loc6_ = 0
            while _loc6_ < cnt_static_object:
                _loc8_ = DotMap()  # StaticObjectData()
                _loc8_.type = decoder.read_unsigned_byte()
                _loc8_.aliance = decoder.read_unsigned_byte()
                _loc8_.race = decoder.read_unsigned_byte()

                static_object.append(_loc8_)
                _loc6_ += 1

            _loc2_.static_object = static_object
            data.append(_loc2_)
            _loc11_ += 1
        return data

    #     #
    def reachableSystems(self, decoder) -> list:
        d = DotMap()
        _loc3_= decoder.read_unsigned_byte()
        _loc5_: int = 0
        while _loc5_ < _loc3_:
            _loc2_ = ReachableSystem()
            decoder.read_unsigned_byte(_loc2_.id)
            decoder.read_bool(_loc2_.current)
            decoder.read_short(_loc2_.energyForJump)
            _loc5_ += 1
        _loc6_: int = 0
        decoder.read_unsigned_byte(_loc6_)
        _loc7_: int = 0
        decoder.read_unsigned_byte(_loc7_)
        return decoder.read_package()
    #     #
    def version(self, decoder):
        decoder.read_int()
        return decoder.read_utf()


    #     #
    #     # def shipHealth(self) -> list:
    #     #     
    #     #     _loc2_ = 0
    #     #     _loc3_ = 0
    #     #     decoder.read_int(_loc2_)
    #     #     decoder.read_int(_loc3_)
    #     #     return decoder.read_package()
    #     #
    def online(self, decoder):
        decoder.read_int()
        decoder.read_int()
        return decoder.read_int()


    def topList(self, decoder) -> DotMap:
        hz = decoder.read_int()
        cnt = decoder.read_int()
        _loc5_: int = 0
        all_player = []
        while _loc5_ < cnt:
            _loc2_ = DotMap()
            _loc2_.login = decoder.read_utf()
            _loc2_.level = decoder.read_int()
            _loc2_.experience = decoder.read_int()
            _loc2_.clanId = decoder.read_int()
            _loc2_.race = decoder.read_unsigned_byte()
            _loc2_.shipClass = decoder.read_short()
            _loc5_ += 1
            all_player.append(_loc2_)
        return all_player

    def topRatingList(self, decoder) -> list:
        cnt = decoder.read_int()
        cnt = decoder.read_int()
        all_player = []
        _loc5_: int = 0
        while _loc5_ < cnt:
            _loc2_ = DotMap()  # PlayerData()
            _loc2_.login = decoder.read_utf()
            _loc2_.level = decoder.read_int()
            _loc2_.points = decoder.read_int()
            _loc2_.clanId = decoder.read_int()
            _loc2_.race = decoder.read_unsigned_byte()
            _loc2_.shipClass = decoder.read_short()
            _loc5_ += 1
            all_player.append(_loc2_)
        return all_player

    def topClansList(self, decoder) -> list:
        decoder.read_int()
        cnt = decoder.read_int()
        all_player = []
        _loc5_: int = 0
        while _loc5_ < cnt:
            _loc2_ = DotMap()  # ClanData()
            _loc2_.id = decoder.read_int()
            _loc2_.points = decoder.read_int()
            _loc2_.leaderID = decoder.read_int()
            _loc2_.aliace = decoder.read_unsigned_byte()
            _loc2_.level = decoder.read_unsigned_byte()
            _loc2_.name = decoder.read_utf()
            _loc2_.shortName = decoder.read_utf()
            _loc2_.logoFileName = decoder.read_utf()
            _loc5_ += 1
            all_player.append(_loc2_)
        return all_player

    #     #
    #     # def auctionList(self) -> list:
    #     #     
    #     #     _loc2_: int = 0
    #     #     _loc3_: I_Item = None
    #     #     _loc4_ = 0
    #     #     decoder.read_int(_loc4_)
    #     #     _loc5_: list = list()
    #     #     _loc6_: int = 0
    #     #     while _loc6_ < _loc4_:
    #     #         decoder.read_int(_loc2_)
    #     #         # _loc3_ = ItemsManager.createInstance(_loc2_)
    #     #         # decoder.read_guid(_loc3_.guid)
    #     #         decoder.read_int(_loc3_.wear)
    #     #         decoder.read_int(_loc3_.ownerid)
    #     #         decoder.read_int(_loc3_.price)
    #     #         decoder.read_int(_loc3_.ransom)
    #     #         decoder.read_int(_loc3_.lastPlayerID)
    #     #         decoder.read_utf(_loc3_.ownerName)
    #     #         decoder.read_utf(_loc3_.lastPlayerName)
    #     #         _loc6_ += 1
    #     #     return decoder.read_package()
    #     #
    #     # def sList(self) -> list:
    #     #     
    #     #     _loc3_ = 0
    #     #     decoder.read_int(_loc3_)
    #     #     _loc5_: int = 0
    #     #     while _loc5_ < _loc3_:
    #     #         _loc2_ = ''
    #     #         decoder.read_utf(_loc2_)
    #     #         _loc5_ += 1
    #     #     return decoder.read_package()
    #     #
    #     # def Evil(self) -> list:
    #     #     
    #     #     _loc2_ = ''
    #     #     decoder.read_utf(_loc2_)
    #     #     return decoder.read_package()
    #     #
    #     # def locationPlanet(self) -> list:
    #     #     
    #     #     _loc2_: PlayerInfoData = None
    #     #     _loc3_: Shop = None
    #     #     _loc4_: DB_Planet
    #     #     _loc4_ = PlanetsManager.createInstance(decoder.read_bytes())
    #     #     _loc4_.id = decoder.read
    #     #     _int()
    #     #     _loc4_.race = T_Race.defineById(self, decoder.read_unsigned_byte())
    #     #     
    #     #     decoder.read_int(_loc4_.RADIUS_BETWEEN_PLANET)
    #     #     decoder.read_int(_loc4_.size)
    #     #     decoder.read_unsigned_byte(_loc4_.aliance)
    #     #     decoder.read_int(_loc4_.clanId)
    #     #     decoder.read_float(_loc4_.angle)
    #     #     decoder.read_unsigned_byte(_loc4_.QCount)
    #     #     _loc5_: int = 0
    #     #     decoder.read_short(_loc5_)
    #     #     _loc6_: int = 0
    #     #     while _loc6_ < _loc5_:
    #     #         _loc3_ = Shop()
    #     #         decoder.read_int(_loc3_.id)
    #     #         decoder.read_unsigned_byte(_loc3_.type)
    #     #         _loc6_ += 1
    #     #     _loc7_: list = []
    #     #     while decoder.bytesAvailable > 0:
    #     #         _loc2_ = PlayerInfoData()
    #     #         decoder.read_int(_loc2_.id)
    #     #         decoder.read_utf(_loc2_.name)
    #     #         decoder.read_int(_loc2_.clanId)
    #     #         decoder.read_int(_loc2_.level)
    #     #     return decoder.read_package()
    #     #
    #     # def planetQuests(self) -> list:
    #     #     
    #     #     _loc2_: QuestPackage = None
    #     #     _loc3_: list = list()
    #     #     _loc4_: int = decoder.read_short()
    #     #     _loc5_: int = 0
    #     #     while _loc5_ < _loc4_:
    #     #         _loc2_ = QuestPackage()
    #     #         decoder.read_int(_loc2_.questId)
    #     #         decoder.read_int(_loc2_.giverType)
    #     #         decoder.read_utf(_loc2_.giverName)
    #     #         decoder.read_utf(_loc2_.Name)
    #     #         _loc5_ += 1
    #     #     return decoder.read_package()
    #     #
    def locationSystem(self, decoder) -> list:
        data = []
        decoder.read_int()
        _loc8_ = DotMap()
        _loc8_.id = decoder.read_int()
        _loc8_.x = decoder.read_float()
        _loc8_.y = decoder.read_float()
        _loc8_.sector = decoder.read_unsigned_byte()
        data.append(_loc8_)
        cnt_ship: int = decoder.read_short()
        ship = []
        _loc10_: int = 0
        while _loc10_ < cnt_ship:
            _loc2_ = DotMap()
            _loc2_.player = DotMap()
            _loc2_.race = decoder.read_short()
            _loc2_.id = decoder.read_int()
            # if _loc2_.id == Owner.ship.id:
            #     _loc2_ = Owner.ship
            _loc2_.Name = decoder.read_utf()
            _loc2_.size = decoder.read_short()
            _loc2_.set_x = decoder.read_float()  # setPosition
            _loc2_.set_y = decoder.read_float()
            _loc2_.player.level = decoder.read_int()
            _loc2_.maxHealth = decoder.read_short()
            _loc2_.maxEnergy = decoder.read_short()
            _loc2_.player.avatar = decoder.read_int()
            _loc2_.maxSpeed = decoder.read_unsigned_byte() / 1000
            _loc2_.mov_x = decoder.read_float()
            _loc2_.mov_y = decoder.read_float()  # setMovePoint
            _loc2_.player.aliance = decoder.read_unsigned_byte()
            _loc2_.player.status = decoder.read_unsigned_byte()
            _loc2_.player.clanId = decoder.read_int()

            cnt_droid_data = decoder.read_unsigned_byte()
            droid = []
            _loc5_ = 0
            while _loc5_ < cnt_droid_data:
                _loc4_ = DotMap()
                _loc4_.id = decoder.read_unsigned_byte()
                _loc4_.type = decoder.read_short()
                _loc4_.weaponClass = decoder.read_short()
                _loc4_.health = decoder.read_short()

                droid.append(_loc4_)
                _loc5_ += 1

            _loc2_.droid = droid
            ship.append(_loc2_)
            _loc10_ += 1
        data.append(ship)
        cnt_planet: int = decoder.read_short()
        planet = []
        _loc12_: int = 0
        while _loc12_ < cnt_planet:
            _loc6_ = DotMap()
            _loc6_.PlanetClass = decoder.read_unsigned_byte()
            _loc6_.id = decoder.read_int()
            _loc6_.race = decoder.read_unsigned_byte()
            _loc6_.radius = decoder.read_int()
            _loc6_.size = decoder.read_int()
            _loc6_.angle = decoder.read_float()
            _loc6_.landable = decoder.read_bool()
            _loc6_.aliance = decoder.read_unsigned_byte()
            _loc6_.clanId = decoder.read_int()

            planet.append(_loc6_)
            _loc12_ += 1

        data.append(planet)
        cnt_stat_space_obj: int = decoder.read_short()
        stat_space_obj = []
        _loc14_: int = 0
        while _loc14_ < cnt_stat_space_obj:
            _loc7_ = DotMap()
            _loc7_.StaticSpaceObjectType = decoder.read_int()
            _loc7_.id = decoder.read_int()
            _loc7_.x = decoder.read_float()
            _loc7_.y = decoder.read_float()
            _loc7_.landable = decoder.read_bool()
            stat_space_obj.append(_loc7_)
            _loc14_ += 1
        data.append(stat_space_obj)
        return data

    #     # def locationBattle(self) -> list:
    #     #     
    #     #     _loc2_: Owner = None
    #     #     _loc3_: int = 0
    #     #     _loc4_: DroidData = None
    #     #     _loc5_: int = 0
    #     #     _loc6_: Battle
    #     #     _loc6_ = Battle()
    #     #     decoder.read_int(_loc6_.id)
    #     #     decoder.read_float(_loc6_.x)
    #     #     decoder.read_float(_loc6_.y)
    #     #     _loc7_ = 0
    #     #     decoder.read_short(_loc7_)
    #     #     _loc8_: int = 0
    #     #     while _loc8_ < _loc7_:
    #     #         decoder.read_short(_loc2_)
    #     #         decoder.read_int(_loc2_.id)
    #     #         if _loc2_.id == Owner.ship.id:
    #     #             _loc2_ = Owner.ship
    #     #         decoder.read_utf(_loc2_.Name)
    #     #         decoder.read_short(_loc2_.size)
    #     #         # _loc2_.setPosition = eator.read_float(), decoder.read_float())
    #     #         decoder.read_int(_loc2_.player)
    #     #         decoder.read_short(_loc2_.maxHealth)
    #     #         decoder.read_short(_loc2_.maxEnergy)
    #     #         decoder.read_int(_loc2_.player)
    #     #         iance = decoder.read_unsigned_byte(_loc2_.player)
    #     #         atus = decoder.read_unsigned_byte(_loc2_.player)
    #     #         anId = decoder.read_int(_loc2_.player)
    #     #         decoder.read_unsigned_byte(_loc3_)
    #     #         _loc5_ = 0
    #     #         while _loc5_ < _loc3_:
    #     #             _loc4_ = DroidData()
    #     #             decoder.read_unsigned_byte(_loc4_.id)
    #     #             decoder.read_short(_loc4_.type)
    #     #             decoder.read_short(_loc4_.weaponClass)
    #     #             decoder.read_short(_loc4_.health)
    #     #             _loc5_ += 1
    #     #         _loc8_ += 1
    #     #     return decoder.read_package()
    #     #
    #     # def shoots(self) -> list:
    #     #     
    #     #     _loc2_ = None  # ShipShoots
    #     #     _loc3_: int = 0
    #     #     _loc4_: int = 0
    #     #     _loc5_ = None  # Shoot
    #     #     _loc7_ = 0
    #     #     decoder.read_short(_loc7_)
    #     #     _loc8_: int = 0
    #     #     while _loc8_ < _loc7_:
    #     #         _loc2_ = ShipShoots()
    #     #         decoder.read_int(_loc2_.id)
    #     #         decoder.read_short(_loc3_)
    #     #         _loc4_ = 0
    #     #         while _loc4_ < _loc3_:
    #     #             _loc5_ = Shoot()
    #     #             decoder.read_short(_loc5_.classfloat)
    #     #             decoder.read_short(_loc5_.damage)
    #     #             decoder.read_unsigned_byte(_loc5_.destroyedTarget)
    #     #             decoder.read_int(_loc5_.targetId)
    #     #             decoder.read_unsigned_byte(_loc5_.targetType)
    #     #             decoder.read_unsigned_byte(_loc5_.muzzleIndex)
    #     #             _loc4_ += 1
    #     #         _loc8_ += 1
    #     #     return decoder.read_package()
    #     #
    #     # def items(self) -> list:
    #     #     
    #     #     _loc2_: BattleItem = None
    #     #     _loc3_: list = list()
    #     #     if decoder.bytesAvailable / 10 - int(decoder.bytesAvailable / 10) == 0:
    #     #         while decoder.bytesAvailable >= 10:
    #     #             _loc2_ = BattleItem()
    #     #             decoder.read_int(_loc2_.id)
    #     #             decoder.read_short(_loc2_.classfloat)
    #     #             decoder.read_short(_loc2_.x)
    #     #             decoder.read_short(_loc2_.y)
    #     #             _loc3_.append(_loc2_)
    #     #     return decoder.read_package()
    #     #
    #     # def message(self) -> list:
    #     #     
    #     #     _loc2_: T_Message = T_Message()
    #     #     _loc2_ = ''
    #     #     decoder.read_utf(_loc2_)
    #     #     decoder.read_utf(_loc2_.text)
    #     #     decoder.read_unsigned_byte(_loc2_.type)
    #     #     decoder.read_bool(_loc2_.isPrivate)
    #     #     decoder.read_bool(_loc2_.isAdmin)
    #     #     return decoder.read_package()
    #     #
    #     # def asteroids(self) -> list:
    #     #     
    #     #     _loc2_: AsteroidPackage = None
    #     #     _loc3_: list = list()
    #     #     if decoder.bytesAvailable / 25 - int(decoder.bytesAvailable / 25) == 0:
    #     #         while decoder.bytesAvailable >= 25:
    #     #             _loc2_ = AsteroidPackage()
    #     #             decoder.read_int(_loc2_.id)
    #     #             decoder.read_float(_loc2_.x)
    #     #             decoder.read_float(_loc2_.y)
    #     #             decoder.read_float(_loc2_.targetX)
    #     #             decoder.read_float(_loc2_.targetY)
    #     #             decoder.read_unsigned_byte(_loc2_.speed) / 1000
    #     #             decoder.read_int(_loc2_.size)
    #     #             _loc3_.append(_loc2_)
    #     #     return decoder.read_package()
    #     #
    #     # def effectCreated(self) -> list:
    #     #     
    #     #     _loc2_: EffectTarget = None
    #     #     _loc3_: int = 0
    #     #     decoder.read_int(_loc3_)
    #     #     _loc4_: int = 0
    #     #     decoder.read_unsigned_byte(_loc4_)
    #     #     _loc5_: list = []
    #     #     _loc6_: int = 0
    #     #     while _loc6_ < _loc4_:
    #     #         _loc2_ = EffectTarget()
    #     #         decoder.read_int(_loc2_.targetId)
    #     #         decoder.read_unsigned_byte(_loc2_.destroyedTarget)
    #     #         decoder.read_bool(_loc2_.effectFailed)
    #     #         _loc6_ += 1
    #     #     _loc7_: int = 0
    #     #     decoder.read_unsigned_byte(_loc7_)
    #     #     _loc8_: float = 0
    #     #     decoder.read_float(_loc8_)
    #     #     _loc9_: int = 0
    #     #     decoder.read_int(_loc9_)
    #     #     return decoder.read_package()
    #     #
    #     # def effectRemoved(self) -> list:
    #     #     
    #     #     _loc2_: int = 0
    #     #     decoder.read_int(_loc2_)
    #     #     _loc3_: int = 0
    #     #     decoder.read_unsigned_byte(_loc3_)
    #     #     return decoder.read_package()
    #     #
    #     # def logMessage(self) -> list:
    #     #     
    #     #     _loc2_: int = 0
    #     #     decoder.read_int(_loc2_)
    #     #     _loc3_: int = 0
    #     #     decoder.read_int(_loc3_)
    #     #     return decoder.read_package()
    #     #
    #     # def logMessagestr(self) -> list:
    #     #     
    #     #     _loc2_: str = ''
    #     #     decoder.read_utf(_loc2_)
    #     #     return decoder.read_package()
    #     #
    #     # def systemMessage(self) -> list:
    #     #     
    #     #     _loc2_: int = 0
    #     #     decoder.read_int(_loc2_)
    #     #     _loc3_: int = 0
    #     #     decoder.read_int(_loc3_)
    #     #     return decoder.read_package()
    #     #
    #     # def systemMessagestr(self) -> list:
    #     #     
    #     #     _loc2_: str = ''
    #     #     decoder.read_utf(_loc2_)
    #     #     return decoder.read_package()
    #     #
    #     # def droidBuildingDialog(self) -> list:
    #     #     
    #     #     _loc2_: DroidPackage = None
    #     #     _loc3_: DroidBuildingDialogPackage = DroidBuildingDialogPackage()
    #     #     _loc3_.deviceGuid = self.read_guid(decoder)
    #     #     _loc4_: int = 0
    #     #     decoder.read_int(_loc4_)
    #     #     _loc3_.droids = list()
    #     #     _loc5_: int = 0
    #     #     while _loc5_ < _loc4_:
    #     #         _loc2_ = DroidPackage()
    #     #         _loc2_.guid = read_guid(decoder)
    #     #         decoder.read_int(_loc2_.classfloat)
    #     #         decoder.read_int(_loc2_.level)
    #     #         decoder.read_int(_loc2_.energyCost)
    #     #     _loc5_ += 1
    #     #
    #     #     return decoder.read_package()
    #     #
    def read_guid(self, decoder) -> list:
        guid = decoder.read_bytes(16)
        return guid
    #     #
    def hideShip(self, decoder) -> list:
        data = []
        decoder.read_int()
        _loc2_ = decoder.read_int()
        data.append(_loc2_)
        return data
    #     #
    #     # def shipDestroyed(self) -> list:
    #     #     
    #     #     _loc2_: int = 0
    #     #     decoder.read_int(_loc2_)
    #     #     return decoder.read_package()
    #     #
    #     # def shipJumped(self) -> list:
    #     #     
    #     #     _loc2_: int = 0
    #     #     decoder.read_int(_loc2_)  # findShip
    #     #     return decoder.read_package()
    #     #
    def clan(self, decoder) -> list:
        data = []
        decoder.read_int()
        _loc2_= DotMap()
        _loc2_.id = decoder.read_int()
        _loc2_.leaderID = decoder.read_int()
        _loc2_.leaderName = decoder.read_utf()
        _loc2_.logoFileName = decoder.read_utf()
        _loc2_.name = decoder.read_utf()
        _loc2_.shortName = decoder.read_utf()
        _loc2_.aliace = decoder.read_unsigned_byte()
        data.append(_loc2_)
        return data

    def playerClan(self, decoder) -> DotMap:
        _loc5_ = DotMap()
        _loc5_.hz = decoder.read_int()
        _loc5_.id = decoder.read_int()
        _loc5_.leaderID = decoder.read_int()
        _loc5_.leaderName = decoder.read_utf()
        _loc5_.logoFileName = decoder.read_utf()
        _loc5_.name = decoder.read_utf()
        _loc5_.shortName = decoder.read_utf()
        _loc5_.aliace = decoder.read_unsigned_byte()
        _loc5_.description = decoder.read_utf()
        _loc5_.joinRequestsCount = decoder.read_short()
        _loc5_.points = decoder.read_int()
        _loc5_.cash = decoder.read_int()
        _loc5_.level = decoder.read_unsigned_byte()
        _loc5_.maxMembers = decoder.read_unsigned_byte()
        _loc5_.maxFriends = decoder.read_unsigned_byte()
        _loc5_.friendRequests = decoder.read_short()
        _loc5_.currentLevelPoints = decoder.read_int()
        _loc5_.nextLevelPoints = decoder.read_int()
        _loc5_.nextLevelCash = decoder.read_int()
        _loc5_.bonuses = decoder.read_int()
        _loc2_ = decoder.read_int()
        _loc3_ = 0
        _loc5_.enemyClans = []
        while _loc3_ < _loc2_:
            _loc5_.enemyClans.append(decoder.read_int())
            _loc3_ += 1

        _loc2_ = decoder.read_int()
        _loc3_ = 0
        _loc5_.friendClans = []
        while _loc3_ < _loc2_:
            _loc5_.friendClans.append(decoder.read_int())
            _loc3_ += 1
        _loc2_ = decoder.read_int()
        _loc3_ = 0
        _loc5_.member = []
        while _loc3_ < _loc2_:
            _loc4_ = DotMap()
            _loc4_.id = decoder.read_int()
            _loc4_.role = decoder.read_int()
            _loc4_.name = decoder.read_utf()
            _loc5_.member.append(_loc4_)
            _loc3_ += 1
        return _loc5_
    #     #
    #     # def teamList(self) -> list:
    #     #     
    #     #     _loc2_: int = 0
    #     #     _loc3_: int = 0
    #     #     _loc4_ = None  # : PlayerInfoData
    #     #     cnt_player_team = 0
    #     #     decoder.read_int(cnt_player_team)
    #     #     if cnt_player_team > 0:
    #     #         Owner.team = TeamList()
    #     #         decoder.read_int(Owner.team.leaderID)
    #     #         decoder.read_int(Owner.team.maxMembers)
    #     #         _loc2_ = 0
    #     #         while _loc2_ < cnt_player_team:
    #     #             _loc4_ = PlayerInfoData()
    #     #             _loc4_.role = 0
    #     #             decoder.read_int(_loc4_.shipId)
    #     #             decoder.read_int(_loc4_.id)
    #     #             decoder.read_utf(_loc4_.name)
    #     #             _loc2_ += 1
    #     #     cnt_player_team = 0
    #     #     decoder.read_int(cnt_player_team)
    #     #     if cnt_player_team >= 0:
    #     #         _loc2_ = 0
    #     #     while _loc2_ < cnt_player_team:
    #     #         _loc4_ = PlayerInfoData()
    #     #         _loc4_.role = -1
    #     #         decoder.read_int(_loc4_.shipId)
    #     #         decoder.read_int(_loc4_.id)
    #     #         decoder.read_utf(_loc4_.name)
    #     #         _loc2_ += 1
    #     #     return decoder.read_package()
    #     #
    #     # def checkValueResult(self) -> list:
    #     #     
    #     #     _loc2_: int = 0
    #     #     decoder.read_int(_loc2_)
    #     #     _loc3_: bool = False
    #     #     decoder.read_bool(_loc3_)
    #     #     return decoder.read_package()
    #     #
    #     # def acceptedClanInfo(self) -> list:
    #     #     
    #     #     _loc2_: int = 0
    #     #     decoder.read_int(_loc2_)
    #     #     _loc3_: str = ''
    #     #     decoder.read_utf(_loc3_)
    #     #     _loc4_: str = ''
    #     #     decoder.read_utf(_loc4_)
    #     #     _loc5_: str = ''
    #     #     decoder.read_utf(_loc5_)
    #     #     _loc6_: int = 0
    #     #     decoder.read_int(_loc6_)
    #     #     return decoder.read_package()
    #     #
    #     # def clanId(self) -> list:
    #     #     
    #     #     decoder.read_int(Owner.clanId)
    #     #     return decoder.read_package()
    #     #
    #     # def clansLetters(self) -> list:
    #     #     
    #     #     _loc2_: list = None
    #     #     _loc2_ = list()
    #     #     while decoder.bytesAvailable > 0:
    #     #         _loc2_[len(_loc2_)] = decoder.read_utf()
    #     #     return decoder.read_package()
    #     #
    #     # def clansList(self) -> list:
    #     #     
    #     #     _loc2_: list = None
    #     #     _loc3_: str = None
    #     #     _loc2_ = list()
    #     #     _loc3_ = decoder.read_utf()
    #     #     while decoder.bytesAvailable > 0:
    #     #         _loc2_[len(_loc2_)] = decoder.read_int()
    #     #     return decoder.read_package()
    #     #
    #     # def clanJoinRequests(self) -> list:
    #     #     
    #     #     _loc2_ = None  # ClanJoinRequest
    #     #     _loc3_: list = None
    #     #     _loc2_ = None
    #     #     _loc3_ = list()
    #     #     while decoder.bytesAvailable > 0:
    #     #         _loc2_ = ClanJoinRequest()
    #     #         decoder.read_int(_loc2_.playerID)
    #     #         decoder.read_utf(_loc2_.playerName)
    #     #         decoder.read_utf(_loc2_.message)
    #     #     return decoder.read_package()
    #     #

    def logged(self, decoder):
        data = []
        hz = decoder.read_int()
        _loc0_ = DotMap()
        _loc0_.stateLoop = decoder.read_int()
        _loc0_.bankSendOperationFee = decoder.read_unsigned_byte()
        _loc0_.clanJoinCost = decoder.read_int()
        _loc0_.clanCreateLevelNeed = decoder.read_unsigned_byte()
        _loc0_.bonuses = decoder.read_int()
        data.append(_loc0_)
        # while True:
        _loc2_ = DotMap()
        _loc2_.id = decoder.read_int()
        _loc2_.name = decoder.read_utf()
        _loc2_.shipClass = decoder.read_short()
        _loc2_.shipCPU = decoder.read_short()
        _loc2_.race = decoder.read_unsigned_byte()
        _loc2_.aliance = decoder.read_unsigned_byte()
        _loc2_.status = decoder.read_unsigned_byte()
        _loc2_.level = decoder.read_unsigned_byte()
        _loc2_.clanId = decoder.read_int()
        _loc2_.deleteEnqueued = decoder.read_bool()
        _loc2_.canDelete = decoder.read_bool()
        _loc2_.logged = decoder.read_bool()
        _loc2_.skills = self.read_skills(decoder)
        data.append(_loc2_)
        return data

    #     #
    #     # def playerInfo(self) -> list:
    #     #     
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
    #     #     decoder.read_int(_loc2_.id)
    #     #     decoder.read_utf(_loc2_.name)
    #     #     decoder.read_unsigned_byte(_loc2_.level)
    #     #     decoder.read_unsigned_byte(_loc2_.status)
    #     #     decoder.read_short(_loc2_.shipClass)
    #     #     decoder.read_int(_loc2_.clanId)
    #     #     decoder.read_unsigned_byte(_loc2_.aliance)
    #     #     decoder.read_unsigned_byte(_loc2_.race)
    #     #     decoder.read_int(_loc2_.clanPoints)
    #     #     decoder.read_int(_loc2_.role)
    #     #     return decoder.read_package()
    #     #
    def playerLoggedOn(self, decoder) -> dict:
        _loc2_ = {}
        _loc2_['hz'] = decoder.read_int()
        _loc2_['id'] = decoder.read_int()
        _loc2_['name'] = decoder.read_utf()
        _loc2_['clanId'] = decoder.read_int()
        _loc2_['level'] = decoder.read_int()
        _loc2_['bool'] = decoder.read_bool()
        return _loc2_
        #
    #     # def playerLoggedOff(self) -> list:
    #     #     
    #     #     _loc2_: PlayerInfoData = None
    #     #     _loc2_ = PlayerInfoData()
    #     #     decoder.read_int(_loc2_.id)
    #     #     return decoder.read_package()
    #     #
    #     # def friendClans(self) -> list:
    #     #     
    #     #     _loc2_: ClanData = None
    #     #     _loc3_: list = None
    #     #     _loc2_ = None
    #     #     _loc3_ = list()
    #     #     while decoder.bytesAvailable > 0:
    #     #         _loc2_ = ClanData()
    #     #         decoder.read_int(_loc2_.id)
    #     #         decoder.read_int(_loc2_.leaderID)
    #     #         decoder.read_utf(_loc2_.leaderName)
    #     #         decoder.read_utf(_loc2_.logoFileName)
    #     #         decoder.read_utf(_loc2_.name)
    #     #         decoder.read_utf(_loc2_.shortName)
    #     #         decoder.read_unsigned_byte(_loc2_.aliace)
    #     #     return decoder.read_package()
    #     #
    #     # def enemyClans(self) -> list:
    #     #     
    #     #     _loc2_: ClanData = None
    #     #     _loc3_: list = None
    #     #     _loc2_ = None
    #     #     _loc3_ = list()
    #     #     while decoder.bytesAvailable > 0:
    #     #         _loc2_ = ClanData()
    #     #         decoder.read_int(_loc2_.id)
    #     #         decoder.read_int(_loc2_.leaderID)
    #     #         decoder.read_utf(_loc2_.leaderName)
    #     #         decoder.read_utf(_loc2_.logoFileName)
    #     #         decoder.read_utf(_loc2_.name)
    #     #         decoder.read_utf(_loc2_.shortName)
    #     #         decoder.read_unsigned_byte(_loc2_.aliace)
    #     #     return decoder.read_package()
    #     #
    #     # def friendRequests(self) -> list:
    #     #     
    #     #     _loc2_: ClanData = None
    #     #     _loc3_: list = None
    #     #     _loc2_ = None
    #     #     _loc3_ = list()
    #     #     while decoder.bytesAvailable > 0:
    #     #         _loc2_ = ClanData()
    #     #         decoder.read_int(_loc2_.id)
    #     #         decoder.read_int(_loc2_.leaderID)
    #     #         decoder.read_utf(_loc2_.leaderName)
    #     #         decoder.read_utf(_loc2_.logoFileName)
    #     #         decoder.read_utf(_loc2_.name)
    #     #         decoder.read_utf(_loc2_.shortName)
    #     #         decoder.read_unsigned_byte(_loc2_.aliace)
    #     #     return decoder.read_package()
    #     #
    #     # def droidEvent(self) -> list:
    #     #     
    #     #     _loc2_: DroidData = None
    #     #     _loc3_: int = 0
    #     #     _loc4_: int = 0
    #     #     _loc2_ = DroidData()
    #     #     decoder.read_unsigned_byte(_loc2_.id)
    #     #     decoder.read_short(_loc2_.type)
    #     #     decoder.read_short(_loc2_.weaponClass)
    #     #     decoder.read_int(_loc3_)
    #     #     decoder.read_unsigned_byte(_loc4_)
    #     #     return decoder.read_package()
    #     #
    def updateValue(self, decoder) -> list:
        data = []
        decoder.read_int()
        _loc2_ = decoder.read_unsigned_byte()
        _loc3_ = decoder.read_int()
        data.append(_loc2_)
        data.append(_loc3_)
        return data
    #     #
    #     # def missions(self) -> list:
    #     #     
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
    #     #     decoder.read_int(_loc5_.id)
    #     #     _loc5_.current = True
    #     #     _loc4_.append(_loc5_)
    #     #     decoder.read_unsigned_byte(_loc6_)
    #     #     decoder.read_unsigned_byte(_loc7_)
    #     #     decoder.read_unsigned_byte(_loc8_)
    #     #     _loc9_ = 0
    #     #     while _loc9_ < _loc8_:
    #     #         _loc5_ = ReachableSystem()
    #     #         decoder.read_int(_loc5_.id)
    #     #         _loc9_ += 1
    #     #     while decoder.bytesAvailable > 0:
    #     #         # _loc2_ = PlanetData()
    #     #         decoder.read_int(_loc2_.id)
    #     #         decoder.read_bytes(_loc2_.classfloat)
    #     #         decoder.read_unsigned_byte(_loc2_.aliance)
    #     #         decoder.read_unsigned_byte(_loc2_.race)
    #     #         decoder.read_int(_loc2_.starId)
    #     #     return decoder.read_package()
    #     #
    #     # def tradeInvitation(self) -> list:
    #     #     
    #     #     _loc2_: int = 0
    #     #     _loc3_: int = 0
    #     #     _loc4_: str = ''
    #     #     decoder.read_int(_loc2_)
    #     #     decoder.read_int(_loc3_)
    #     #     decoder.read_utf(_loc4_)
    #     #     return decoder.read_package()
    #     #
    #     # def showTrading(self) -> list:
    #     #     
    #     #     _loc2_: int = 0
    #     #     _loc3_: int = 0
    #     #     _loc4_: str = ''
    #     #     _loc5_: list = []
    #     #     decoder.read_int(_loc2_)
    #     #     decoder.read_int(_loc3_)
    #     #     decoder.read_utf(_loc4_)
    #     #     _loc5_ = self.read_items(decoder, True, True)
    #     #     return decoder.read_package()
    #     #
    def toGame(self, decoder):
        data = []
        decoder.read_int()
        return data
