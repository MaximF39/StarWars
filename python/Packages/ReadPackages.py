from PackageDecoder import PackageDecoder
from python.Static.ClientRequest import ClientRequest

class ReadPackages:
    IocaI: str = "LOCAL_TRUSTED"
    Domain: str = "serverstarwars.com"

    def main(self, command_type: int, *args):
        match command_type:
            case ClientRequest.LOGIN:
                return self.login(*args)
            # case ClientRequest.MOVE:
            #     return self.move()
            # case ClientRequest.LEAVE_LOCATION:
            #     return self.leaveLocation()
            # case ClientRequest.PLANET_REQUEST:
            #     return self.planetRequest()
            # case ClientRequest.SHIP_REQUEST:
            #     return self.shipRequest()
            # case ClientRequest.ALREADY_LOGGED:
            #     return self.
            # case ClientRequest.SESSION_ID:
            #     return self.
            # case ClientRequest.OBJECT_TO_REACH:
            #     return self.objectToReach()
            # # case ClientRequest.OBJECT_EVIL:
            # #     return self.
            # case ClientRequest.USE_ITEM:
            #     return self.useItem()
            # case ClientRequest.UNUSE_ITEM:
            #     return self.
            # case ClientRequest.OPEN_SHOP:
            #     return self.
            # case ClientRequest.FAILED:
            #     return self.
            # case ClientRequest.LOCATION_CHANGED:
            #     return self.
            # case ClientRequest.INVENTORY:
            #     return self.
            # case ClientRequest.HYPERJUMP:
            #     return self.
            # case ClientRequest.REACHABLE_SYSTEMS:
            #     return self.
            # case ClientRequest.MESSAGE:
            #     return self.
            # case ClientRequest.REPAIR:
            #     return self.
            # case ClientRequest.MAP:
            #     return self.
            # case ClientRequest.REGISTER:
            #     return self.
            # case ClientRequest.PLAYER_SKILLS:
            #     return self.
            # case ClientRequest.DEVICE_CLICKED:
            #     return self.
            # case ClientRequest.DROID_CLICKED:
            #     return self.
            # case ClientRequest.RESTORE_ENERGY:
            #     return self.
            # case ClientRequest.USE_FREE_PARAMETERS:
            #     return self.
            # case ClientRequest.DROID_COMMAND:
            #     return self.
            # case ClientRequest.BUY_SHIP:
            #     return self.
            # case ClientRequest.SHOW_QUEST:
            #     return self.
            # case ClientRequest.GET_QUEST:
            #     return self.
            # case ClientRequest.QUESTS_JOURNAL:
            #     return self.
            # case ClientRequest.PLANET_QUESTS:
            #     return self.
            # case ClientRequest.TRAINING:
            #     return self.
            # case ClientRequest.ARENA_REQUESTS:
            #     return self.
            # case ClientRequest.JOIN_TO_REQUEST:
            #     return self.
            # case ClientRequest.BATTLE_REQUEST_WINDOW_CLOSED:
            #     return self.
            # case ClientRequest.READY_TO_BATTLE:
            #     return self.
            # case ClientRequest.DROIDS_MODE:
            #     return self.
            # case ClientRequest.BUILD_DROID:
            #     return self.
            # case ClientRequest.SYNCRONIZE_HEALTH:
            #     return self.
            # case ClientRequest.CREATE_ARENA_REQUEST:
            #     return self.
            # case ClientRequest.BUY_ITEM:
            #     return self.
            # case ClientRequest.SELL_ITEM:
            #     return self.
            # case ClientRequest.DROP_ITEM:
            #     return self.
            # case ClientRequest.OBJECT_TO_ATTACK:
            #     return self.
            # case ClientRequest.COMMIT_SKILLS:
            #     return self.
            # case ClientRequest.APPLY_GINETIC_LAB_OPTION:
            #     return self.
            # case ClientRequest.CREAR_TARGETS:
            #     return self.
            # case ClientRequest.SEND_CREDITS:
            #     return self.
            # case ClientRequest.TO_REPOSITORY:
            #     return self.
            # case ClientRequest.RETURN_ITEM:
            #     return self.
            # case ClientRequest.LOAD_CLAN:
            #     return self.
            # case ClientRequest.CLAN_LOAD:
            #     return self.
            # case ClientRequest.CHECK_VALUE:
            #     return self.
            # case ClientRequest.ACCEPTED_CLAN_INFO:
            #     return self.
            # case ClientRequest.CREATE_CLAN:
            #     return self.
            # case ClientRequest.GET_CLANS_LETTERS:
            #     return self.
            # case ClientRequest.GET_CLANS_LIST:
            #     return self.
            # case ClientRequest.JOIN_TO_CLAN_REQUEST:
            #     return self.
            # case ClientRequest.GET_CLAN_REQUESTS:
            #     return self.
            # case ClientRequest.PLAYER_INFO:
            #     return self.
            # case ClientRequest.SAVE_CLAN_JOIN_REQUESTS:
            #     return self.
            # case ClientRequest.JOIN_TO_CLAN:
            #     return self.
            # case ClientRequest.CANCEL_CLAN_CREATE_REQUEST:
            #     return self.
            # case ClientRequest.GET_FRIEND_CLANS:
            #     return self.
            # case ClientRequest.GET_ENEMY_CLANS:
            #     return self.
            # case ClientRequest.REMOVE_CLAN_RELATION:
            #     return self.
            # case ClientRequest.ADD_CLAN_TO_ENEMIES:
            #     return self.
            # case ClientRequest.ADD_CLAN_FRIEND_REQUEST:
            #     return self.
            # case ClientRequest.GET_FRIEND_REQUESTS:
            #     return self.
            # case ClientRequest.SUBMIT_CLAN_FRIEND_REQUESTS:
            #     return self.
            # case ClientRequest.MOVE_CLAN_TO_NEXT_LEVEL:
            #     return self.
            # case ClientRequest.REMOVE_PLAYER_FROM_CLAN:
            #     return self.
            # case ClientRequest.GET_MISSIONS:
            #     return self.
            # case ClientRequest.CREATE_PILOT:
            #     return self.
            # case ClientRequest.TO_GAME:
            #     return self.
            # case ClientRequest.EXCHANGE_VOTES:
            #     return self.
            # case ClientRequest.CHANGE_SHIP:
            #     return self.
            # case ClientRequest.DELETE_PILOT:
            #     return self.
            # case ClientRequest.CANCEL_DELETE_PILOT:
            #     return self.
            # case ClientRequest.GET_MAP:
            #     return self.
            # case ClientRequest.LEAVE_CLAN:
            #     return self.
            # case ClientRequest.EXCHANGE_VOTES_TO_BONUSES:
            #     return self.
            # case ClientRequest.BUY_ITEM_BY_BONUSES:
            #     return self.
            # case ClientRequest.TRADE_INVITATION:
            #     return self.
            # case ClientRequest.TRADE_INVITATION_RESULT:
            #     return self.
            # case ClientRequest.TRADE_CASH:
            #     return self.
            # case ClientRequest.TRADE_ITEM_TO_SELL:
            #     return self.
            # case ClientRequest.TRADE_ITEM_TO_HOLD:
            #     return self.
            # case ClientRequest.TRADE_ACCEPTED:
            #     return self.
            # case ClientRequest.FINISH_TRADING_RESULT:
            #     return self.
            # case ClientRequest.TRADE_DENIED:
            #     return self.
            # case ClientRequest.UPDATE_HOLD:
            #     return self.
            # case ClientRequest.UPDATE_SHIP:
            #     return self.
            # case ClientRequest.LOST_ITEMS:
            #     return self.
            # case ClientRequest.CHANGE_LEADER:
            #     return self.
            # case ClientRequest.UPDATE_RESOURCE:
            #     return self.
            # case ClientRequest.CLAN_CREATE:
            #     return self.
            # case ClientRequest.TO_CLAN_REPOSITORY:
            #     return self.
            # case ClientRequest.RETURN_ITEM_CLAN:
            #     return self.
            # case ClientRequest.SET_PLAYER_ROLE:
            #     return self.
            # case ClientRequest.SEND_BONUSES:
            #     return self.
            # case ClientRequest.RENAME_PILOT:
            #     return self.
            # case ClientRequest.RESERV4:
            #     return self.
            # case ClientRequest.REPAIR_ITEM:
            #     return self.
            # case ClientRequest.GETAUCTION:
            #     return self.
            # case ClientRequest.GET_UPDATE_VALUE:
            #     return self.
            # case ClientRequest.OBJECT_TO_TEAM:
            #     return self.
            # case ClientRequest.REMOVE_PLAYER_FROM_TEAM:
            #     return self.
            # case ClientRequest.SEND_BAN:
            #     return self.sendBan()
            # case ClientRequest.RESERV11:
            #     return self.
            # case ClientRequest.RESERV12:
            #     return self.
            # case ClientRequest.BUY_SHIP_BY_BONUSES:
            #     return self.buyShipByBonuses()
            case _:
                return print('Error unknow Packages')
    #
    # def droidCommand(self) -> None:
    #     _loc5_: PackageDecoder
    #     _loc5_ = PackageDecoder()
    #     _loc5_.read_bytes()
    #     _loc5_.read_int()
    #     _loc5_.read_int()
    #     _loc5_.read_int()


    def login(self, data) -> None:
        _loc5_: PackageDecoder
        _loc5_ = PackageDecoder()
        _loc5_.data = data
        data = []
        data.append(_loc5_.read_utf())
        data.append(_loc5_.read_utf())
        data.append(_loc5_.read_utf())
        data.append(_loc5_.read_utf())
        return data
    #
    # def registration(self) -> None:
    #     _loc5_: PackageDecoder
    #     _loc5_ = PackageDecoder()
    #     _loc5_.read_utf()
    #     _loc5_.read_utf()
    #     _loc5_.read_utf()
    #     _loc5_.read_int()
    #
    # def move(self) -> None:
    #     _loc4_: PackageDecoder
    #     _loc4_ = PackageDecoder()
    #     _loc4_.read_float()
    #     _loc4_.read_float()
    #     _loc4_.read_int()
    #
    # def leaveLocation(self) -> None:
    #     _loc1_: PackageDecoder = PackageDecoder()
    #
    # # def evil(self) -> None:
    # #     oWriter: PackageDecoder = None
    # #     oWriter = None
    # #     ev: str =
    # #     oWriter = PackageDecoder(
    #     # try:
    #     #     oWriter.read_utf(":" + ExternalInterface.call("eval",ev))
    #     #
    #     # except:(ex:*)
    #     #
    #     # oWriter.read_utf("None")
    #
    # def planetRequest(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_int()
    #
    # def shipRequest(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_int()
    #
    # def addObjectToTeam(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_int()
    #     _loc2_.read_int()
    #
    # def ObjectToAttack(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_int()
    #     _loc2_.read_int()
    #
    # def objectToReach(self) -> None:
    #     _loc4_: PackageDecoder
    #     _loc4_ = PackageDecoder()
    #     _loc4_.read_int()
    #     _loc4_.read_int()
    #     _loc4_.read_int()
    #     _loc4_.read_int()
    #
    # def useItem(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_bytes()
    #
    # def unuseItem(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_bytes()
    #
    # def buyItem(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_bytes()
    #     _loc2_.read_int()
    #
    # def sellItem(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_bytes()
    #     _loc2_.read_int()
    #
    # def updateresource(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_bytes()
    #     _loc2_.read_int()
    #
    # def clanCreate(self) -> None:
    #     _loc4_: PackageDecoder
    #     _loc4_ = PackageDecoder()
    #     _loc4_.read_utf()
    #     _loc4_.read_utf()
    #     _loc4_.read_utf()
    #
    # def dropItem(self, ) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_bytes()
    #     _loc2_.read_int()
    #
    # def repairItem(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_bytes()
    #     _loc2_.read_int()
    #
    # def openShop(self,) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_int()
    #
    # def inventory(self) -> None:
    #     # _loc1_: LocalConnection = LocalConnection()
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_utf()
    #
    # def reachableSystems() -> None:
    #     _loc1_: PackageDecoder = PackageDecoder()
    #
    # def jumpTo(self) -> None:
    #     # _loc3_: LocalConnection = LocalConnection()
    #     _loc4_: PackageDecoder
    #     _loc4_ = PackageDecoder()
    #     _loc4_.read_int()
    #     _loc4_.read_int()
    #     _loc4_.read_utf()
    #
    # def sendMessage(self) -> None:
    #     _loc4_: PackageDecoder
    #     _loc4_ = PackageDecoder()
    #     _loc4_.read_int()
    #     _loc4_.read_utf()
    #     _loc4_.read_bytes()
    #
    # def sendBan(self) -> None:
    #     _loc4_: PackageDecoder
    #     _loc4_ = PackageDecoder()
    #     _loc4_.read_utf()
    #     _loc4_.read_utf()
    #     _loc4_.read_bytes()
    #
    # def repair(self) -> None:
    #     _loc1_: PackageDecoder = PackageDecoder()
    #
    # def Auction(self) -> None:
    #     _loc1_: PackageDecoder = PackageDecoder()
    #
    # def restoreEnergy(self) -> None:
    #     _loc1_: PackageDecoder = PackageDecoder()
    #
    # def playerSkills(self) -> None:
    #     _loc1_: PackageDecoder = PackageDecoder()
    #
    # def ClickedTime(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_int()
    #
    # def deviceClicked(self) -> None:
    #     _loc5_: PackageDecoder
    #     _loc5_ = PackageDecoder()
    #     _loc5_.read_bytes()
    #     _loc5_.read_int()
    #     _loc5_.read_bytes()
    #     _loc5_.read_bytes()
    #
    # def droidClicked(self,) -> None:
    #     _loc3_: PackageDecoder = PackageDecoder()
    #     _loc3_.read_bytes()
    #     _loc3_.read_bytes()
    #
    # def buyShip(self) -> None:
    #     _loc3_: PackageDecoder = PackageDecoder()
    #     _loc3_.read_bytes()
    #     _loc3_.read_bool()
    #
    # def showQuest(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_int()
    #
    # def Quest(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_int()
    #
    # def questsJournal(self) -> None:
    #     _loc1_: PackageDecoder = PackageDecoder()
    #
    # def showPlanetQuests(self) -> None:
    #     _loc1_: PackageDecoder = PackageDecoder()
    #
    # def training(self) -> None:
    #     _loc7_: PackageDecoder
    #     _loc7_ = PackageDecoder()
    #     _loc7_.read_int()
    #     _loc7_.read_int()
    #     _loc7_.read_int()
    #     _loc7_.read_int()
    #     _loc7_.read_int()
    #     _loc7_.read_int()
    #
    # def arenaRequests(self) -> None:
    #     _loc1_: PackageDecoder = PackageDecoder()
    #
    # def joinToRequest(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_int()
    #
    # def battleRequestWindowClosed(self) -> None:
    #     _loc1_: PackageDecoder = PackageDecoder()
    #
    # def readyToBattle(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_int()
    #
    # def droidsMode(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_int()
    #
    # def buildDroid(self) -> None:
    #     _loc1_: PackageDecoder = PackageDecoder()
    #
    # def crearTargets(self) -> None:
    #     _loc1_: PackageDecoder = PackageDecoder()
    #
    # def syncronizeHealth(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_int()
    #
    # def createArenaRequest(self) -> None:
    #     _loc4_: PackageDecoder
    #     _loc4_ = PackageDecoder()
    #     _loc4_.read_bytes()
    #     _loc4_.read_int()
    #     _loc4_.read_bool()
    #
    # # def commitSkills(self) -> None:
    # #     _loc2_: PackageDecoder = PackageDecoder()
    # #     self.writeSkill(PlayerSkillType.Atacking, , _loc2_)
    # #     self.writeSkill(PlayerSkillType.Control, , _loc2_)
    # #     self.writeSkill(PlayerSkillType.Defending, , _loc2_)
    # #     self.writeSkill(PlayerSkillType.EnergyWeapons, , _loc2_)
    # #     self.writeSkill(PlayerSkillType.KineticWeapons, , _loc2_)
    # #     self.writeSkill(PlayerSkillType.Mining, , _loc2_)
    # #     self.writeSkill(PlayerSkillType.Piloting, , _loc2_)
    # #     self.writeSkill(PlayerSkillType.Repairing, , _loc2_)
    # #     self.writeSkill(PlayerSkillType.RocketWeapons, , _loc2_)
    # #     self.writeSkill(PlayerSkillType.Tactics, , _loc2_)
    # #     self.writeSkill(PlayerSkillType.Trading, , _loc2_)
    # #     self.writeSkill(PlayerSkillType.Targeting, , _loc2_)
    # #     self.writeSkill(PlayerSkillType.Electronics, , _loc2_)
    # #     self.writeSkill(PlayerSkillType.Mechanics, , _loc2_)
    # #     self.writeSkill(PlayerSkillType.Biocemistry, , _loc2_)
    # #     self.writeSkill(PlayerSkillType.Cybernetics, , _loc2_)
    #
    # # def writeSkill() -> None:
    # #     _loc4_: int
    # #     _loc4_ = []
    # #     if int(_loc4_) > 0:
    # #         .read_bytes()
    # #     .read_bytes(_loc4_)
    #
    # def applyGineticLabOption(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_int()
    #
    # def sendCredits(self) -> None:
    #     _loc5_: PackageDecoder
    #     _loc5_ = PackageDecoder()
    #     _loc5_.read_int()
    #     _loc5_.read_int()
    #     _loc5_.read_bool()
    #     _loc5_.read_bool()
    #
    # def sendBonuses(self) -> None:
    #     _loc5_: PackageDecoder
    #     _loc5_ = PackageDecoder()
    #     _loc5_.read_int()
    #     _loc5_.read_int()
    #     _loc5_.read_bool()
    #     _loc5_.read_bool()
    #
    # def toRepository(self) -> None:
    #     _loc3_: PackageDecoder = PackageDecoder()
    #     _loc3_.read_bytes()
    #     _loc3_.read_int()
    #
    # def returnItem(self) -> None:
    #     _loc3_: PackageDecoder = PackageDecoder()
    #     _loc3_.read_bytes()
    #     _loc3_.read_int()
    #
    # def toClanRepository(self) -> None:
    #     _loc3_: PackageDecoder = PackageDecoder()
    #     _loc3_.read_bytes()
    #     _loc3_.read_int()
    #
    # def returnItemClan(self) -> None:
    #     _loc3_: PackageDecoder = PackageDecoder()
    #     _loc3_.read_bytes()
    #     _loc3_.read_int()
    #
    # def loadClan(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_int()
    #
    # def clanLoad(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_int()
    #
    # def checkValue(self) -> None:
    #     _loc3_: PackageDecoder = PackageDecoder()
    #     _loc3_.read_int()
    #     _loc3_.read_utf()
    #
    # def AcceptedClanInfo(self) -> None:
    #     _loc1_: PackageDecoder = PackageDecoder()
    #
    # def createClan(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_int()
    #
    # def ClansLetters(self) -> None:
    #     _loc1_: PackageDecoder = PackageDecoder()
    #
    # # def ClansList(self) -> None:
    # #     _loc3_: PackageDecoder = PackageDecoder()
    # #     _loc4_: int = 0
    # #     if :
    # #         _loc4_ = 1
    # #     _loc3_.read_utf()
    # #     _loc3_.read_int(_loc4_)
    #
    # def joinToClanRequest(self) -> None:
    #     _loc3_: PackageDecoder = PackageDecoder()
    #     _loc3_.read_int()
    #     _loc3_.read_utf()
    #
    # def bodylessCommand(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #
    # def guidValueCommand(self) -> None:
    #     _loc3_: PackageDecoder = PackageDecoder()
    #     _loc3_.read_bytes()
    #
    # def tradeItemToSell(self) -> None:
    #     _loc3_: PackageDecoder = PackageDecoder()
    #     _loc3_.read_bytes()
    #     _loc3_.read_short()
    #
    # def intValueCommand(self) -> None:
    #     _loc3_: PackageDecoder = PackageDecoder()
    #     _loc3_.read_int()
    #
    # def floatValueCommand(self) -> None:
    #     _loc3_: PackageDecoder = PackageDecoder()
    #     _loc3_.read_float()
    #
    # def boolValueCommand(self) -> None:
    #     _loc3_: PackageDecoder = PackageDecoder()
    #     _loc3_.read_bool()
    #
    # # def submitClanFriendRequests(self) -> None:
    # #     _loc3_: int = 0
    # #     _loc4_: PackageDecoder
    # #     _loc4_ = PackageDecoder()
    # #     _loc4_.read_int()
    # #     _loc3_ = 0
    # #     while _loc3_ < len():
    # #         _loc4_.read_int()
    # #         _loc3_ += 1
    # #         _loc4_.read_int()
    # #         _loc3_ = 0
    # #     while _loc3_ < len():
    # #         _loc4_.read_int()
    # #         _loc3_ += 1
    #
    # def createPilot(self) -> None:
    #     _loc2_: PackageDecoder = PackageDecoder()
    #     _loc2_.read_short()
    #     _loc2_.read_utf()
    #
    # # def saveClanJoinRequests(self) -> None:
    # #     _loc2_: None = None #ClanJoinRequest
    # #     _loc3_: PackageDecoder = PackageDecoder()
    # #     _loc4_: int = 0
    # #     while (_loc4_ < len()):
    # #         _loc2_ = [_loc4_]  # as
    # #         if _loc2_ is not None:
    # #             _loc3_.read_int() # playerID
    # #             _loc3_.read_bytes() #result
    # #         _loc4_ += 1
    #
    # def buyItemByBonuses(self) -> None:
    #     _loc5_: PackageDecoder
    #     _loc5_ = PackageDecoder()
    #     _loc5_.read_short()
    #     _loc5_.read_short()
    #     _loc5_.read_int()
    #     _loc5_.read_short()
    #
    # def buyShipByBonuses(self) -> None:
    #     _loc4_: PackageDecoder
    #     _loc4_ = PackageDecoder()
    #     _loc4_.read_short()
    #     _loc4_.read_int()
    #     _loc4_.read_short()
    #
    # def tradeInvitationResult(self) -> None:
    #     _loc3_: PackageDecoder = PackageDecoder()
    #     _loc3_.read_int()
    #     _loc3_.read_bool()
    #
    # def PlayerRole(self) -> None:
    #     _loc3_: PackageDecoder = PackageDecoder()
    #     _loc3_.read_int()
    #     _loc3_.read_int()
    #
    # def renamePilot(self) -> None:
    #     _loc3_: PackageDecoder = PackageDecoder()
    #     _loc3_.read_int()
    #     _loc3_.read_utf()
