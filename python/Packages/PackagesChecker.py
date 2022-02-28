from python.Static.Type.Package.T_ClientRequest import T_ClientRequest
class PackagesChecker:
    def __init__(self, PackageNumber, data):
        self.__procesPackage(PackageNumber, data)

    def __procesPackage(self, PackageNumber, data):
        match PackageNumber:
            case T_ClientRequest.LOGIN:
                return self.login(data)
            case T_ClientRequest.MOVE:
                return self.move(data)
            case T_ClientRequest.LEAVE_LOCATION:
                return #self.leave(data)
            case T_ClientRequest.PLANET_REQUEST:
                return self.planetRequest(data)
            case T_ClientRequest.SHIP_REQUEST:
                return self.shipRequest(data)
            case T_ClientRequest.ALREADY_LOGGED:
                return
            case T_ClientRequest.SESSION_ID:
                return
            case T_ClientRequest.OBJECT_TO_REACH:
                return self.objectToReach(data)
            case T_ClientRequest.OBJECT_EVIL:
                return self.evil(data)
            case T_ClientRequest.USE_ITEM:
                return self.useItem(data)
            case T_ClientRequest.UNUSE_ITEM:
                return self.unuseItem(data)
            case T_ClientRequest.OPEN_SHOP:
                return self.openShop(data)
            case T_ClientRequest.FAILED:
                return
            case T_ClientRequest.LOCATION_CHANGED:
                return
            case T_ClientRequest.INVENTORY:
                return self.inventory(data)
            case T_ClientRequest.HYPERJUMP:
                return
            case T_ClientRequest.REACHABLE_SYSTEMS:
                return self.reachableSystems(data)
            case T_ClientRequest.MESSAGE:
                return self.sendMessage(data)
            case T_ClientRequest.REPAIR:
                return self.repair(data)
            case T_ClientRequest.MAP:
                return
            case T_ClientRequest.REGISTER:
                return self.registration(data)
            case T_ClientRequest.PLAYER_SKILLS:
                return self.playerSkills(data)
            case T_ClientRequest.DEVICE_CLICKED:
                return self.deviceClicked(data)
            case T_ClientRequest.DROID_CLICKED:
                return self.droidClicked(data)
            case T_ClientRequest.RESTORE_ENERGY:
                return self.restoreEnergy(data)
            case T_ClientRequest.USE_FREE_PARAMETERS:
                return
            case T_ClientRequest.DROID_COMMAND:
                return self.droidCommand(data)
            case T_ClientRequest.BUY_SHIP:
                return self.buyShip(data)
            case T_ClientRequest.SHOW_QUEST:
                return self.showQuest(data)
            case T_ClientRequest.GET_QUEST:
                return
            case T_ClientRequest.QUESTS_JOURNAL:
                return self.questsJournal(data)
            case T_ClientRequest.PLANET_QUESTS:
                return self.showPlanetQuests(data)
            case T_ClientRequest.TRAINING:
                return self.training(data)
            case T_ClientRequest.ARENA_REQUESTS:
                return self.arenaRequests(data)
            case T_ClientRequest.JOIN_TO_REQUEST:
                return self.joinToRequest(data)
            case T_ClientRequest.BATTLE_REQUEST_WINDOW_CLOSED:
                return self.battleRequestWindowClosed(data)
            case T_ClientRequest.READY_TO_BATTLE:
                return self.readyToBattle(data)
            case T_ClientRequest.DROIDS_MODE:
                return self.droidsMode(data)
            case T_ClientRequest.BUILD_DROID:
                return self.buildDroid(data)
            case T_ClientRequest.SYNCRONIZE_HEALTH:
                return self.syncronizeHealth(data)
            case T_ClientRequest.CREATE_ARENA_REQUEST:
                return self.createArenaRequest(data)
            case T_ClientRequest.BUY_ITEM:
                return self.buy_item(data)
            case T_ClientRequest.SELL_ITEM:
                return self.sell_item(data)
            case T_ClientRequest.DROP_ITEM:
                return self.dropItem(data)
            case T_ClientRequest.OBJECT_TO_ATTACK:
                return self.ObjectToAttack(data)
            case T_ClientRequest.COMMIT_SKILLS:
                return self.commitSkills(data)
            case T_ClientRequest.APPLY_GINETIC_LAB_OPTION:
                return self.applyGineticLabOption(data)
            case T_ClientRequest.CREAR_TARGETS:
                return self.crearTargets(data)
            case T_ClientRequest.SEND_CREDITS:
                return self.sendCredits(data)
            case T_ClientRequest.TO_REPOSITORY:
                return self.toRepository(data)
            case T_ClientRequest.RETURN_ITEM:
                return self.returnItem(self)
            case T_ClientRequest.LOAD_CLAN:
                return self.loadClan(data)
            case T_ClientRequest.CLAN_LOAD:
                return self.clanLoad(data)
            case T_ClientRequest.CHECK_VALUE:
                return self.checkValue(data)
            case T_ClientRequest.ACCEPTED_CLAN_INFO:
                return self.AcceptedClanInfo(data)
            case T_ClientRequest.CREATE_CLAN:
                return self.createClan(data)
            case T_ClientRequest.GET_CLANS_LETTERS:
                return self.ClansLetters(data)
            case T_ClientRequest.GET_CLANS_LIST:
                return self.ClansList(data)
            case T_ClientRequest.JOIN_TO_CLAN_REQUEST:
                return self.joinToClanRequest(data)
            case T_ClientRequest.GET_CLAN_REQUESTS:
                return
            case T_ClientRequest.PLAYER_INFO:
                return
            case T_ClientRequest.SAVE_CLAN_JOIN_REQUESTS:
                return self.saveClanJoinRequests(data)
            case T_ClientRequest.JOIN_TO_CLAN:
                return
            case T_ClientRequest.CANCEL_CLAN_CREATE_REQUEST:
                return
            case T_ClientRequest.GET_FRIEND_CLANS:
                return
            case T_ClientRequest.GET_ENEMY_CLANS:
                return
            case T_ClientRequest.REMOVE_CLAN_RELATION:
                return
            case T_ClientRequest.ADD_CLAN_TO_ENEMIES:
                return
            case T_ClientRequest.ADD_CLAN_FRIEND_REQUEST:
                return
            case T_ClientRequest.GET_FRIEND_REQUESTS:
                return
            case T_ClientRequest.SUBMIT_CLAN_FRIEND_REQUESTS:
                return
            case T_ClientRequest.MOVE_CLAN_TO_NEXT_LEVEL:
                return
            case T_ClientRequest.REMOVE_PLAYER_FROM_CLAN:
                return
            case T_ClientRequest.GET_MISSIONS:
                return
            case T_ClientRequest.CREATE_PILOT:
                return self.createPilot(data)
            case T_ClientRequest.TO_GAME:
                return
            case T_ClientRequest.EXCHANGE_VOTES:
                return
            case T_ClientRequest.CHANGE_SHIP:
                return
            case T_ClientRequest.DELETE_PILOT:
                return
            case T_ClientRequest.CANCEL_DELETE_PILOT:
                return
            case T_ClientRequest.GET_MAP:
                return
            case T_ClientRequest.LEAVE_CLAN:
                return #self.leave
            case T_ClientRequest.EXCHANGE_VOTES_TO_BONUSES:
                return
            case T_ClientRequest.BUY_ITEM_BY_BONUSES:
                return
            case T_ClientRequest.TRADE_INVITATION:
                return
            case T_ClientRequest.TRADE_INVITATION_RESULT:
                return
            case T_ClientRequest.TRADE_CASH:
                return
            case T_ClientRequest.TRADE_ITEM_TO_SELL:
                return
            case T_ClientRequest.TRADE_ITEM_TO_HOLD:
                return
            case T_ClientRequest.TRADE_ACCEPTED:
                return
            case T_ClientRequest.FINISH_TRADING_RESULT:
                return
            case T_ClientRequest.TRADE_DENIED:
                return
            case T_ClientRequest.UPDATE_HOLD:
                return
            case T_ClientRequest.UPDATE_SHIP:
                return
            case T_ClientRequest.LOST_ITEMS:
                return
            case T_ClientRequest.CHANGE_LEADER:
                return
            case T_ClientRequest.UPDATE_RESOURCE:
                return self.updateresource(data)
            case T_ClientRequest.CLAN_CREATE:
                return self.createClan(data)
            case T_ClientRequest.TO_CLAN_REPOSITORY:
                return self.toClanRepository(data)
            case T_ClientRequest.RETURN_ITEM_CLAN:
                return self.returnItemClan(data)
            case T_ClientRequest.SET_PLAYER_ROLE:
                return self.PlayerRole(data)
            case T_ClientRequest.SEND_BONUSES:
                return self.sendBonuses(data)
            case T_ClientRequest.RENAME_PILOT:
                return self.renamePilot(data)
            case T_ClientRequest.RESERV4:
                return
            case T_ClientRequest.REPAIR_ITEM:
                return self.returnItem(data)
            case T_ClientRequest.GETAUCTION:
                return self.Auction(data)
            case T_ClientRequest.GET_UPDATE_VALUE:
                return
            case T_ClientRequest.OBJECT_TO_TEAM:
                return self.addObjectToTeam(data)
            case T_ClientRequest.REMOVE_PLAYER_FROM_TEAM:
                return
            case T_ClientRequest.SEND_BAN:
                return
            case T_ClientRequest.RESERV11:
                return
            case T_ClientRequest.RESERV12:
                return
            case T_ClientRequest.BUY_SHIP_BY_BONUSES:
                return self.buyShipByBonuses(data)
            case _:
                pass

    def droidCommand(self, data) -> None:
        pass

    def login(self, data):
        pass

    def registration(self, data) -> None:
        pass

    def move(self, data) -> None:
        pass

    def leave(self, data):
        pass

    def evil(self, data) -> None:
        pass

    def planetRequest(self, data) -> None:
        pass

    def shipRequest(self, data) -> None:
        pass

    def addObjectToTeam(self, data) -> None:
        pass

    def ObjectToAttack(self, data) -> None:
        pass

    def objectToReach(self, data):
        pass

    def useItem(self, data) -> None:
        pass

    def unuseItem(self, data) -> None:
        pass

    def buy_item(self, data) -> None:
        pass

    def sell_item(self, data) -> None:
        pass

    def updateresource(self, data) -> None:
        pass

    def clanCreate(self, data) -> None:
        pass

    def dropItem(self, data, ) -> None:
        pass

    def repairItem(self, data) -> None:
        pass

    def openShop(self, data, ) -> None:
        pass

    def inventory(self, data) -> None:
        pass

    def reachableSystems(self, data) -> None:
        pass

    def jumpTo(self, data) -> None:
        pass

    def sendMessage(self, data) -> None:
        pass

    def sendBan(self, data) -> None:
        pass

    def repair(self, data):
        pass

    def Auction(self, data) -> None:
        pass

    def restoreEnergy(self, data):
        pass

    def playerSkills(self, data):
        pass

    def ClickedTime(self, data) -> None:
        pass

    def deviceClicked(self, data) -> None:
        pass

    def droidClicked(self, data) -> None:
        pass

    def buyShip(self, data) -> None:
        pass

    def showQuest(self, data) -> None:
        pass

    def Quest(self, data) -> None:
        pass

    def questsJournal(self, data) -> None:
        pass

    def showPlanetQuests(self, data) -> None:
        pass

    def training(self, data) -> None:
        pass

    def arenaRequests(self, data) -> None:
        pass

    def joinToRequest(self, data) -> None:
        pass

    def battleRequestWindowClosed(self, data) -> None:
        pass

    def readyToBattle(self, data) -> None:
        pass

    def droidsMode(self, data) -> None:
        pass

    def buildDroid(self, data) -> None:
        pass

    def crearTargets(self, data) -> None:  # убрать дройдов всех
        pass

    def syncronizeHealth(self, data) -> None:
        pass

    def createArenaRequest(self, data) -> None:
        pass

    def commitSkills(self, data):
        pass

    def read_skill(self, data, decoder):
        pass

    def applyGineticLabOption(self, data) -> None:
        pass

    def sendCredits(self, data) -> None:
        pass

    def sendBonuses(self, data) -> None:
        pass

    def toRepository(self, data) -> None:
        pass

    def returnItem(self, data) -> None:
        pass

    def toClanRepository(self, data) -> None:
        pass

    def returnItemClan(self, data) -> None:
        pass

    def loadClan(self, data) -> None:
        pass

    def clanLoad(self, data) -> None:
        pass

    def checkValue(self, data) -> None:
        pass

    def AcceptedClanInfo(self, data) -> None:
        pass

    def createClan(self, data) -> None:
        pass

    def ClansLetters(self, data) -> None:
        pass

    def ClansList(self, data) -> None:
        pass

    def joinToClanRequest(self, data) -> None:
        pass

    def bodylessCommand(self, data) -> None:
        pass

    def guidValueCommand(self, data) -> None:
        pass

    def tradeItemToSell(self, data) -> None:
        pass

    def intValueCommand(self, data, command_type) -> None:
        pass

    def floatValueCommand(self, data) -> None:
        pass

    def boolValueCommand(self, data) -> None:
        pass

    def submitClanFriendRequests(self, data) -> None:
        pass

    def createPilot(self, data) -> None:
        pass

    def saveClanJoinRequests(self, data) -> None:
        pass

    def buyItemByBonuses(self, data) -> None:
        pass

    def buyShipByBonuses(self, data) -> None:
        pass

    def tradeInvitationResult(self, data) -> None:
        pass

    def PlayerRole(self, data) -> None:
        pass

    def renamePilot(self, data) -> None:
        pass