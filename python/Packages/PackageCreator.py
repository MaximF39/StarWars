from . import PackageWriter
from . import SpaceObject
from . import PlayerInfoData, PlayerSkillType, ClientRequest


class PackageCreator(PackageWriter):
    local: str = 'self.local_TRUSTED'
    domain: str = 'serverstarwars.com'

    def droidCommand(self, param1: int, param2: int, param3: int, param4: int) -> bytearray:
        _loc5_: PackageWriter()
        _loc5_ = PackageWriter().commandType = ClientRequest.DROID_COMMAND
        _loc5_.write_bytes(param1)
        _loc5_.write_int(param2)
        _loc5_.write_int(param3)
        _loc5_.write_int(param4)
        return _loc5_.getPackage()

    # def login(self, param1: str, param2: str, param3: str) -> bytearray:
    #     # _loc4_: localConnection = localConnection()
    #     _loc5_: PackageWriter
    #     _loc5_ = PackageWriter().commandType = ClientRequest.LOGIN
    #     _loc5_.write_utf(param1)
    #     _loc5_.write_utf(param2)
    #     _loc5_.write_utf(param3)
    #     _loc5_.write_utf(self.domain)
    #     return _loc5_.getPackage()

    def registration(self, param1: str, param2: str, param3: str, param4: int) -> bytearray:
        _loc5_: PackageWriter
        _loc5_ = PackageWriter().commandType = ClientRequest.REGISTER
        _loc5_.write_utf(param1)
        _loc5_.write_utf(param2)
        _loc5_.write_utf(param3)
        _loc5_.write_int(param4)
        return _loc5_.getPackage()

    def move(self, param1: float, param2: float, param3: int) -> bytearray:
        _loc4_: PackageWriter
        _loc4_ = PackageWriter().commandType = ClientRequest.MOVE
        _loc4_.write_float(param1)
        _loc4_.write_float(param2)
        _loc4_.write_int(param3)
        return _loc4_.getPackage()

    def leaveLocation(self) -> bytearray:
        _loc1_: PackageWriter = PackageWriter()
        _loc1_.commandType = ClientRequest.LEAVE_LOCATION
        return _loc1_.getPackage()

    # def evil(self, param1: str) -> bytearray:
    # oWriter: PackageWriter = None
    # oWriter = None
    # ev: str = param1
    # oWriter = PackageWriter()
    # oWriter.commandType = ClientRequest.OBJECT_EVIL
    # try:
    #     pass
    # oWriter.write_utf(":" + ExternalInterface.call("eval", ev))
    # except:
    #     oWriter.write_utf("null")
    # return oWriter.getPackage()

    def planetRequest(self, param1: int) -> bytearray:
        _loc2_: PackageWriter = PackageWriter()
        _loc2_.commandType = ClientRequest.PLANET_REQUEST
        _loc2_.write_int(param1)
        return _loc2_.getPackage()

    def shipRequest(self, param1: int) -> bytearray:
        _loc2_: PackageWriter = PackageWriter()
        _loc2_.commandType = ClientRequest.SHIP_REQUEST
        _loc2_.write_int(param1)
        return _loc2_.getPackage()

    def addObjectToTeam(self, param1: int) -> bytearray:
        _loc2_: PackageWriter = PackageWriter()
        _loc2_.commandType = ClientRequest.OBJECT_TO_TEAM
        # _loc2_.write_int(int(ObjectToReachType.SHIP))
        _loc2_.write_int(param1)
        return _loc2_.getPackage()

    def setObjectToAttack(self, param1: SpaceObject) -> bytearray:
        _loc2_: PackageWriter = PackageWriter()
        _loc2_.commandType = ClientRequest.OBJECT_TO_ATTACK
        _loc2_.write_int(param1.typeOfObject)
        _loc2_.write_int(param1.id)
        return _loc2_.getPackage()

    def objectToReach(self, param1: SpaceObject, param2: int, param3: int) -> bytearray:
        _loc4_: PackageWriter
        _loc4_ = PackageWriter().commandType = ClientRequest.OBJECT_TO_REACH
        _loc4_.write_int(param1.typeOfObject)
        _loc4_.write_int(param1.id)
        _loc4_.write_int(param2)
        _loc4_.write_int(param3)
        return _loc4_.getPackage()

    def useItem(self, param1: bytearray) -> bytearray:
        _loc2_: PackageWriter = PackageWriter()
        _loc2_.commandType = ClientRequest.USE_ITEM
        _loc2_.write_bytes(param1, 0, 16)
        return _loc2_.getPackage()

    def unuseItem(self, param1: bytearray) -> bytearray:
        _loc2_: PackageWriter = PackageWriter()
        _loc2_.commandType = ClientRequest.UNUSED_ITEM
        _loc2_.write_bytes(param1, 0, 16)
        return _loc2_.getPackage()

    # def buyItem(self, param1: Item) -> bytearray:
    #     _loc2_: PackageWriter = PackageWriter()
    #     _loc2_.commandType = ClientRequest.BUY_ITEM
    #     _loc2_.write_bytes(param1.guid, 0, 16)
    #     _loc2_.write_int(param1.wear)
    #     return _loc2_.getPackage()
    #
    # def sellItem(self, param1: Item) -> bytearray:
    #     _loc2_: PackageWriter = PackageWriter()
    #     _loc2_.commandType = ClientRequest.SELL_ITEM
    #     _loc2_.write_bytes(param1.guid, 0, 16)
    #     _loc2_.write_int(param1.wear)
    #     return _loc2_.getPackage()

    # def updateresource(self, param1: Item) -> bytearray:
    #     _loc2_: PackageWriter = PackageWriter()
    #     _loc2_.commandType = ClientRequest.UPDATE_RESOURCE
    #     _loc2_.write_bytes(param1.guid, 0, 16)
    #     _loc2_.write_int(param1.wear)
    #     return _loc2_.getPackage()

    def clanCreate(self, param1: str, param2: str, param3: str) -> bytearray:
        _loc4_: PackageWriter
        _loc4_ = PackageWriter()
        _loc4_.commandType = ClientRequest.CLAN_CREATE
        _loc4_.write_utf(param1)
        _loc4_.write_utf(param2)
        _loc4_.write_utf(param3)
        return _loc4_.getPackage()

    # def dropItem(self, param1: Item) -> bytearray:
    #     _loc2_: PackageWriter = PackageWriter()
    #     _loc2_.commandType = ClientRequest.DROP_ITEM
    #     _loc2_.write_bytes(param1.guid, 0, 16)
    #     _loc2_.write_int(param1.wear)
    #     return _loc2_.getPackage()
    #
    # def repairItem(self, param1: Item) -> bytearray:
    #     _loc2_: PackageWriter = PackageWriter()
    #     _loc2_.commandType = ClientRequest.REPAIR_ITEM
    #     _loc2_.write_bytes(param1.guid, 0, 16)
    #     _loc2_.write_int(param1.wear)
    #     return _loc2_.getPackage()

    def openShop(self, param1: int) -> bytearray:
        _loc2_: PackageWriter = PackageWriter()
        _loc2_.commandType = ClientRequest.OPEN_SHOP
        _loc2_.write_int(param1)
        return _loc2_.getPackage()

    def boolToInt(self, param1: bool) -> int:
        if param1:
            return 1
        return 0

    # def inventory(self) -> bytearray:
    #     _loc1_: localConnection = localConnection()
    #     _loc2_: PackageWriter = PackageWriter()
    #     _loc2_.commandType = ClientRequest.INVENTORY
    #     _loc2_.write_utf(self.domain)
    #     return _loc2_.getPackage()

    def reachableSystems(self) -> bytearray:
        _loc1_: PackageWriter = PackageWriter()
        _loc1_.commandType = ClientRequest.REACHABLE_SYSTEMS
        return _loc1_.getPackage()

    # def jumpTo(self, param1: ReachableSystem, param2: int) -> bytearray:
    #     _loc3_: localConnection = localConnection()
    #     _loc4_: PackageWriter
    #     _loc4_ = PackageWriter().commandType = ClientRequest.HYPER_JUMP
    #     _loc4_.write_int(param1.id)
    #     _loc4_.write_int(param2)
    #     _loc4_.write_utf(self.domain)
    #     return _loc4_.getPackage()

    # def sendMesage(self, param1: str, param2: int, param3: int) -> bytearray:
    #     _loc4_: PackageWriter
    #     _loc4_ = PackageWriter().commandType = ClientRequest.MEsAGE
    #     _loc4_.write_int(param2)
    #     _loc4_.write_utf(param1)
    #     _loc4_.write_bytes(param3)
    #     return _loc4_.getPackage()

    def sendBan(self, param1: str, param2: str, param3: int) -> bytearray:
        _loc4_: PackageWriter
        _loc4_ = PackageWriter().commandType = ClientRequest.SEND_BAN
        _loc4_.write_utf(param1)
        _loc4_.write_utf(param2)
        _loc4_.write_bytes(param3)
        return _loc4_.getPackage()

    def repair(self) -> bytearray:
        _loc1_: PackageWriter = PackageWriter()
        _loc1_.commandType = ClientRequest.REPAIR
        return _loc1_.getPackage()

    def getAuction(self) -> bytearray:
        _loc1_: PackageWriter = PackageWriter()
        _loc1_.commandType = ClientRequest.GET_AUCTION
        return _loc1_.getPackage()

    def restoreEnergy(self) -> bytearray:
        _loc1_: PackageWriter = PackageWriter()
        _loc1_.commandType = ClientRequest.RESTORE_ENERGY
        return _loc1_.getPackage()

    def playerSkills(self) -> bytearray:
        _loc1_: PackageWriter = PackageWriter()
        _loc1_.commandType = ClientRequest.PLAYER_SKILLS
        return _loc1_.getPackage()

    def ClickedTime(self, param1: int) -> bytearray:
        _loc2_: PackageWriter = PackageWriter()
        _loc2_.commandType = ClientRequest.RESERVE4
        _loc2_.write_int(param1)
        return _loc2_.getPackage()

    def deviceClicked(self, param1: bytearray, param2: int, param3: int, param4: int) -> bytearray:
        _loc5_: PackageWriter
        _loc5_ = PackageWriter().commandType = ClientRequest.DEVICE_CLICKED
        _loc5_.write_bytes(param1, 0, len(param1))
        _loc5_.write_int(param2)
        _loc5_.write_bytes(param3)
        _loc5_.write_bytes(param4)
        return _loc5_.getPackage()

    def droidClicked(self, param1: bytearray, param2: bytearray) -> bytearray:
        _loc3_: PackageWriter = PackageWriter()
        _loc3_.commandType = ClientRequest.DROID_CLICKED
        _loc3_.write_bytes(param1, 0, len(param1))
        _loc3_.write_bytes(param2, 0, len(param2))
        return _loc3_.getPackage()

    # def buyShip(self, param1: ShipForSale, param2: bool) -> bytearray:
    #     _loc3_: PackageWriter = PackageWriter()
    #     _loc3_.commandType = ClientRequest.BUY_SHIP
    #     _loc3_.write_bytes(param1.id, 0, param1.len(id))
    #     _loc3_.write_bool(param2)
    #     return _loc3_.getPackage()

    def showQuest(self, param1: int) -> bytearray:
        _loc2_: PackageWriter = PackageWriter()
        _loc2_.commandType = ClientRequest.SHOW_QUEST
        _loc2_.write_int(param1)
        return _loc2_.getPackage()

    def getQuest(self, param1: int) -> bytearray:
        _loc2_: PackageWriter = PackageWriter()
        _loc2_.commandType = ClientRequest.GET_QUEST
        _loc2_.write_int(param1)
        return _loc2_.getPackage()

    def questsJournal(self) -> bytearray:
        _loc1_: PackageWriter = PackageWriter()
        _loc1_.commandType = ClientRequest.QUESTS_JOURNAL
        return _loc1_.getPackage()

    def showPlanetQuests(self) -> bytearray:
        _loc1_: PackageWriter = PackageWriter()
        _loc1_.commandType = ClientRequest.PLANET_QUESTS
        return _loc1_.getPackage()

    def training(self, param1: int, param2: int, param3: int, param4: int, param5: int, param6: int) -> bytearray:
        _loc7_: PackageWriter
        _loc7_ = PackageWriter().commandType = ClientRequest.TRAINING
        _loc7_.write_int(param1)
        _loc7_.write_int(param2)
        _loc7_.write_int(param3)
        _loc7_.write_int(param4)
        _loc7_.write_int(param5)
        _loc7_.write_int(param6)
        return _loc7_.getPackage()

    def arenaRequests(self) -> bytearray:
        _loc1_: PackageWriter = PackageWriter()
        _loc1_.commandType = ClientRequest.ARENA_REQUESTS
        return _loc1_.getPackage()

    # def joinToRequest(self, param1: BattleRequest) -> bytearray:
    #     _loc2_: PackageWriter = PackageWriter()
    #     _loc2_.commandType = ClientRequest.JOIN_TO_REQUEST
    #     _loc2_.write_int(param1.id)
    #     return _loc2_.getPackage()

    def battleRequestWindowClosed(self) -> bytearray:
        _loc1_: PackageWriter = PackageWriter()
        _loc1_.commandType = ClientRequest.BATTLE_REQUEST_WINDOW_CLOSED
        return _loc1_.getPackage()

    # def readyToBattle(self, param1: BattleRequest) -> bytearray:
    #     _loc2_: PackageWriter = PackageWriter()
    #     _loc2_.commandType = ClientRequest.READY_TO_BATTLE
    #     _loc2_.write_int(param1.id)
    #     return _loc2_.getPackage()

    def droidsMode(self, param1: int) -> bytearray:
        _loc2_: PackageWriter = PackageWriter()
        _loc2_.commandType = ClientRequest.DROIDS_MODE
        _loc2_.write_int(param1)
        return _loc2_.getPackage()

    def buildDroid(self) -> bytearray:
        _loc1_: PackageWriter = PackageWriter()
        _loc1_.commandType = ClientRequest.BUILD_DROID
        return _loc1_.getPackage()

    def crearTargets(self) -> bytearray:
        _loc1_: PackageWriter = PackageWriter()
        _loc1_.commandType = ClientRequest.CREATE_TARGETS
        return _loc1_.getPackage()

    def syncronizeHealth(self, param1: int) -> bytearray:
        _loc2_: PackageWriter = PackageWriter()
        _loc2_.commandType = ClientRequest.SYNCHRONIZE_HEALTH
        _loc2_.write_int(param1)
        return _loc2_.getPackage()

    def createArenaRequest(self, param1: int, param2: int, param3: bool) -> bytearray:
        _loc4_: PackageWriter
        _loc4_ = PackageWriter()
        _loc4_.commandType = ClientRequest.CREATE_ARENA_REQUEST
        _loc4_.write_bytes(param1)
        _loc4_.write_int(param2)
        _loc4_.write_bool(param3)
        return _loc4_.getPackage()

    # def commitSkills(self, param1: dict) -> bytearray:
    #     _loc2_: PackageWriter = PackageWriter()
    #     _loc2_.commandType = ClientRequest.COMMIT_SKILLS
    #     writeSkill(PlayerSkillType.Atacking, param1, _loc2_)
    #     writeSkill(PlayerSkillType.Control, param1, _loc2_)
    #     writeSkill(PlayerSkillType.Defending, param1, _loc2_)
    #     writeSkill(PlayerSkillType.EnergyWeapons, param1, _loc2_)
    #     writeSkill(PlayerSkillType.KineticWeapons, param1, _loc2_)
    #     writeSkill(PlayerSkillType.Mining, param1, _loc2_)
    #     writeSkill(PlayerSkillType.Piloting, param1, _loc2_)
    #     writeSkill(PlayerSkillType.Repairing, param1, _loc2_)
    #     writeSkill(PlayerSkillType.RocketWeapons, param1, _loc2_)
    #     writeSkill(PlayerSkillType.Tactics, param1, _loc2_)
    #     writeSkill(PlayerSkillType.Trading, param1, _loc2_)
    #     writeSkill(PlayerSkillType.Targeting, param1, _loc2_)
    #     writeSkill(PlayerSkillType.Electronics, param1, _loc2_)
    #     writeSkill(PlayerSkillType.Mechanics, param1, _loc2_)
    #     writeSkill(PlayerSkillType.Biocemistry, param1, _loc2_)
    #     writeSkill(PlayerSkillType.Cybernetics, param1, _loc2_)
    #     return _loc2_.getPackage()

    # def writeSkill(self, param1: int, param2: dict, param3: PackageWriter):
    #     _loc4_: int
    #     if _loc4_ = param2[param1] as int > 0:
    #         param3.write_bytes(param1)
    #         param3.write_bytes(_loc4_)

    def applyGineticLabOption(self, param1: int) -> bytearray:
        _loc2_: PackageWriter = PackageWriter()
        _loc2_.commandType = ClientRequest.APPLY_GENETIC_LAB_OPTION
        _loc2_.write_int(param1)
        return _loc2_.getPackage()

    def sendCredits(self, param1: int, param2: int, param3: bool, param4: bool) -> bytearray:
        _loc5_: PackageWriter
        _loc5_ = PackageWriter().commandType = ClientRequest.SEND_CREDITS
        _loc5_.write_int(param1)
        _loc5_.write_int(param2)
        _loc5_.write_bool(param3)
        _loc5_.write_bool(param4)
        return _loc5_.getPackage()

    def sendBonuses(self, param1: int, param2: int, param3: bool, param4: bool) -> bytearray:
        _loc5_: PackageWriter
        _loc5_ = PackageWriter().commandType = ClientRequest.SEND_BONUSES
        _loc5_.write_int(param1)
        _loc5_.write_int(param2)
        _loc5_.write_bool(param3)
        _loc5_.write_bool(param4)
        return _loc5_.getPackage()

    def toRepository(self, param1: bytearray, param2: int) -> bytearray:
        _loc3_: PackageWriter = PackageWriter()
        _loc3_.commandType = ClientRequest.TO_REPOSITORY
        _loc3_.write_bytes(param1, 0, len(param1))
        _loc3_.write_int(param2)
        return _loc3_.getPackage()

    def returnItem(self, param1: bytearray, param2: int) -> bytearray:
        _loc3_: PackageWriter = PackageWriter()
        _loc3_.commandType = ClientRequest.RETURN_ITEM
        _loc3_.write_bytes(param1, 0, len(param1))
        _loc3_.write_int(param2)
        return _loc3_.getPackage()

    def toClanRepository(self, param1: bytearray, param2: int) -> bytearray:
        _loc3_: PackageWriter = PackageWriter()
        _loc3_.commandType = ClientRequest.TO_CLAN_REPOSITORY
        _loc3_.write_bytes(param1, 0, len(param1))
        _loc3_.write_int(param2)
        return _loc3_.getPackage()

    def returnItemClan(self, param1: bytearray, param2: int) -> bytearray:
        _loc3_: PackageWriter = PackageWriter()
        _loc3_.commandType = ClientRequest.RETURN_ITEM_CLAN
        _loc3_.write_bytes(param1, 0, len(param1))
        _loc3_.write_int(param2)
        return _loc3_.getPackage()

    def loadClan(self, param1: int) -> bytearray:
        _loc2_: PackageWriter = PackageWriter()
        _loc2_.commandType = ClientRequest.LOAD_CLAN
        _loc2_.write_int(param1)
        return _loc2_.getPackage()

    def clanLoad(self, param1: int) -> bytearray:
        _loc2_: PackageWriter = PackageWriter()
        _loc2_.commandType = ClientRequest.CLAN_LOAD
        _loc2_.write_int(param1)
        return _loc2_.getPackage()

    def checkValue(self, param1: str, param2: int) -> bytearray:
        _loc3_: PackageWriter = PackageWriter()
        _loc3_.commandType = ClientRequest.CHECK_VALUE
        _loc3_.write_int(param2)
        _loc3_.write_utf(param1)
        return _loc3_.getPackage()

    def getAcceptedClanInfo(self) -> bytearray:
        _loc1_: PackageWriter = PackageWriter()
        _loc1_.commandType = ClientRequest.ACCEPTED_CLAN_INFO
        return _loc1_.getPackage()

    def createClan(self, param1: int) -> bytearray:
        _loc2_: PackageWriter = PackageWriter()
        _loc2_.commandType = ClientRequest.CREATE_CLAN
        _loc2_.write_int(param1)
        return _loc2_.getPackage()

    def getClansLetters(self) -> bytearray:
        _loc1_: PackageWriter = PackageWriter()
        _loc1_.commandType = ClientRequest.GET_CLANS_LETTERS
        return _loc1_.getPackage()

    def getClansList(self, param1: str, param2: bool) -> bytearray:
        _loc3_: PackageWriter = PackageWriter()
        _loc3_.commandType = ClientRequest.GET_CLANS_LIST
        _loc4_: int = 0
        if param2:
            _loc4_ = 1
            _loc3_.write_utf(param1)
            _loc3_.write_int(_loc4_)
        return _loc3_.getPackage()

    def joinToClanRequest(self, param1: int, param2: str) -> bytearray:
        _loc3_: PackageWriter = PackageWriter()
        _loc3_.commandType = ClientRequest.JOIN_TO_CLAN_REQUEST
        _loc3_.write_int(param1)
        _loc3_.write_utf(param2)
        return _loc3_.getPackage()

    def bodylesCommand(self, param1: int) -> bytearray:
        _loc2_: PackageWriter = PackageWriter()
        _loc2_.commandType = param1
        return _loc2_.getPackage()

    def guidValueCommand(self, param1: int, param2: bytearray) -> bytearray:
        _loc3_: PackageWriter = PackageWriter()
        _loc3_.commandType = param1
        _loc3_.write_bytes(param2, 0, 16)
        return _loc3_.getPackage()

    def tradeItemToSell(self, param1: bytearray, param2: int) -> bytearray:
        _loc3_: PackageWriter = PackageWriter()
        _loc3_.commandType = ClientRequest.TRADE_ITEM_TO_SELL
        _loc3_.write_bytes(param1, 0, 16)
        _loc3_.write_short(param2)
        return _loc3_.getPackage()

    def intValueCommand(self, param1: int, param2: int) -> bytearray:
        _loc3_: PackageWriter = PackageWriter()
        _loc3_.commandType = param1
        _loc3_.write_int(param2)
        return _loc3_.getPackage()

    def floatValueCommand(self, param1: int, param2: float) -> bytearray:
        _loc3_: PackageWriter = PackageWriter()
        _loc3_.commandType = param1
        _loc3_.write_float(param2)
        return _loc3_.getPackage()

    def boolValueCommand(self, param1: int, param2: bool) -> bytearray:
        _loc3_: PackageWriter = PackageWriter()
        _loc3_.commandType = param1
        _loc3_.write_bool(param2)
        return _loc3_.getPackage()

    def submitClanFriendRequests(self, param1: list, param2: list) -> bytearray:
        _loc3_: int = 0
        _loc4_: PackageWriter
        _loc4_ = PackageWriter().commandType = ClientRequest.SUBMIT_CLAN_FRIEND_REQUESTS
        _loc4_.write_int(len(param1))
        _loc3_ = 0
        while _loc3_ < len(param1):
            _loc4_.write_int(param1[_loc3_])
            _loc3_ += 1
            _loc4_.write_int(len(param2))
            _loc3_ = 0
        while _loc3_ < len(param2):
            _loc4_.write_int(param2[_loc3_])
            _loc3_ += 1
        return _loc4_.getPackage()

    def createPilot(self, param1: PlayerInfoData) -> bytearray:
        _loc2_: PackageWriter = PackageWriter()
        _loc2_.commandType = ClientRequest.CREATE_PILOT
        _loc2_.write_short(param1.race)
        _loc2_.write_utf(param1.name)
        return _loc2_.getPackage()

    # def saveClanJoinRequests(self, param1: list) -> bytearray:
    #     _loc2_: ClanJoinRequest = None
    #     _loc3_: PackageWriter = PackageWriter()
    #     _loc3_.commandType = ClientRequest.SAVE_CLAN_JOIN_REQUESTS
    #     _loc4_: int = 0
    #     while _loc4_ < len(param1):
    #         _loc2_ = param1[_loc4_] as ClanJoinRequest
    #     if _loc2_ != None:
    #         _loc3_.write_int(_loc2_.playerID)
    #         _loc3_.write_bytes(_loc2_.result)
    #     _loc4_ += 1
    #     return _loc3_.getPackage()

    def buyItemByBonuses(self, param1: int, param2: int, param3: int, param4: int) -> bytearray:
        _loc5_: PackageWriter
        _loc5_ = PackageWriter().commandType = ClientRequest.BUY_ITEM_BY_BONUSES
        _loc5_.write_short(param1)
        _loc5_.write_short(param2)
        _loc5_.write_int(param3)
        _loc5_.write_short(param4)
        return _loc5_.getPackage()

    def buyShipByBonuses(self, param1: int, param2: int, param3: int) -> bytearray:
        _loc4_: PackageWriter
        _loc4_ = PackageWriter().commandType = ClientRequest.BUY_SHIP_BY_BONUSES
        _loc4_.write_short(param1)
        _loc4_.write_int(param2)
        _loc4_.write_short(param3)
        return _loc4_.getPackage()

    def tradeInvitationResult(self, param1: int, param2: bool) -> bytearray:
        _loc3_: PackageWriter = PackageWriter()
        _loc3_.commandType = ClientRequest.TRADE_INVITATION_RESULT
        _loc3_.write_int(param1)
        _loc3_.write_bool(param2)
        return _loc3_.getPackage()

    def setPlayerRole(self, param1: int, param2: int) -> bytearray:
        _loc3_: PackageWriter = PackageWriter()
        _loc3_.commandType = ClientRequest.SET_PLAYER_ROLE
        _loc3_.write_int(param1)
        _loc3_.write_int(param2)
        return _loc3_.getPackage()

    def renamePilot(self, param1: int, param2: str) -> bytearray:
        _loc3_: PackageWriter = PackageWriter()
        _loc3_.commandType = ClientRequest.RENAME_PILOT
        _loc3_.write_int(param1)
        _loc3_.write_utf(param2)
        return _loc3_.getPackage()
