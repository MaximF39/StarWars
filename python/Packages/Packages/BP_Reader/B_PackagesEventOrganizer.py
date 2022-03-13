from python.Packages.Packages.BP_Reader.B_PackagesChecker import B_PackagesChecker
from python.Static.Type.Keys import Keys
from python.Static.Type.Package.T_ClientRequest import T_ClientRequest
from python.Static.Type.Package.T_ServerRequest import T_ServerRequest
from python.Static.Type.Package.T_UpdateValue import T_UpdateValue


class B_PackagesEventOrganizer(B_PackagesChecker):
    
    def __init__(self, Game, Player, command_type, data):
        B_PackagesChecker.__init__(self, Game, Player, command_type, data)

    def droidCommand(self, data) -> None:
        data = B_PackagesChecker.droidCommand(self, data)
        if data['type_command'] == 4:
            self.Player.unuse_droid_all()

    @staticmethod
    def login(data):
        data = B_PackagesChecker.login(data)
        return data[Keys.login], data[Keys.password]

    def registration(self, data) -> None:
        data = B_PackagesChecker.registration(self, data)

    def move(self, data) -> None:
        data = B_PackagesChecker.move(self, data)
        self.Player.move(data[Keys.x], data[Keys.y])

    def leaveLocation(self, data):
        data = B_PackagesChecker.leaveLocation(self, data)
        self.Player.remove_space_object()

    def evil(self, data) -> None:
        data = B_PackagesChecker.evil(self, data)

    def planetRequest(self, data) -> None:
        data = B_PackagesChecker.planetRequest(self, data)

    def shipRequest(self, data) -> None:
        data = B_PackagesChecker.shipRequest(self, data)

    def addObjectToTeam(self, data) -> None:
        data = B_PackagesChecker.addObjectToTeam(self, data)

    def ObjectToAttack(self, data) -> None:
        data = B_PackagesChecker.ObjectToAttack(self, data)
        self.Player.attack(data)

    def objectToReach(self, data):
        data = B_PackagesChecker.objectToReach(self, data)
        self.Player.set_object_to_reach(data)

    def useItem(self, data) -> None:
        data = B_PackagesChecker.useItem(self, data)
        self.Player.use_item(data)

    def unuseItem(self, data) -> None:
        data = B_PackagesChecker.unuseItem(self, data)
        self.Player.unuse_item(data)

    def buy_item(self, data) -> None:
        data = B_PackagesChecker.buy_item(self, data)
        self.Player.buy_item(data)

    def sell_item(self, data) -> None:
        data = B_PackagesChecker.sell_item(self, data)
        self.Player.sell_item(data)

    def updatedataource(self, data) -> None:
        data = B_PackagesChecker.updatedataource(self, data)

    def clanCreate(self, data) -> None:
        data = B_PackagesChecker.clanCreate(self, data)

    def dropItem(self, data, ) -> None:
        data = B_PackagesChecker.dropItem(self, data)
        self.Player.drop_item(data)

    def repairItem(self, data) -> None:
        data = B_PackagesChecker.repairItem(self, data)

    def openShop(self, data, ) -> None:
        data = B_PackagesChecker.openShop(self, data)
        self.Player.open_shop(data)

    def inventory(self, data) -> None:
        data = B_PackagesChecker.inventory(self, data)
        self.Player.SendPacMan(T_ServerRequest.INVENTORY)

    def reachableSystems(self, data) -> None:
        data = B_PackagesChecker.reachableSystems(self, data)

    def jumpTo(self, data) -> None:
        data = B_PackagesChecker.jumpTo(self, data)
        self.Player.move_hyper_jump(data[Keys.id])

    def sendMessage(self, data) -> None:
        data = B_PackagesChecker.sendMessage(self, data)
        self.Game.Chat.send_message(self.Player, data)

    def sendBan(self, data) -> None:
        data = B_PackagesChecker.sendBan(self, data)

    def repair(self, data):
        data = B_PackagesChecker.repair(self, data)
        self.Player.repair()
        self.Player.SendPacMan.shipHealth()


    def Auction(self, data) -> None:
        data = B_PackagesChecker.Auction(self, data)

    def restoreEnergy(self, data):
        data = B_PackagesChecker.restoreEnergy(self, data)
        # getattr(self.StarWars, f'Player_{self.id}').datatoreEnergy()
        # PackagesManager(self.id, self.StarWars).()

    def playerSkills(self, data):
        data = B_PackagesChecker.playerSkills(self, data)
        self.Player.SendPacMan(T_ServerRequest.PLAYER_SKILLS)

    def ClickedTime(self, data) -> None:
        data = B_PackagesChecker.ClickedTime(self, data)

    def deviceClicked(self, data) -> None:
        data = B_PackagesChecker.deviceClicked(self, data)
        self.Player.device_clicked(data)

    def droidClicked(self, data) -> None:
        data = B_PackagesChecker.droidClicked(self, data)
        self.Player.use_item(data)

    def buyShip(self, data) -> None:
        data = B_PackagesChecker.buyShip(self, data)
        self.Player.buyShip(data)

    def showQuest(self, data) -> None:
        data = B_PackagesChecker.showQuest(self, data)

    def Quest(self, data) -> None:
        data = B_PackagesChecker.Quest(self, data)

    def questsJournal(self, data) -> None:
        data = B_PackagesChecker.questsJournal(self, data)

    def showPlanetQuests(self, data) -> None:
        data = B_PackagesChecker.showPlanetQuests(self, data)

    def training(self, data) -> None:
        data = B_PackagesChecker.training(self, data)

    def arenaRequests(self, data) -> None:
        data = B_PackagesChecker.arenaRequests(self, data)

    def joinToRequest(self, data) -> None:
        data = B_PackagesChecker.joinToRequest(self, data)

    def battleRequestWindowClosed(self, data) -> None:
        data = B_PackagesChecker.battleRequestWindowClosed(self, data)

    def readyToBattle(self, data) -> None:
        data = B_PackagesChecker.readyToBattle(self, data)

    def droidsMode(self, data) -> None:
        data = B_PackagesChecker.droidsMode(self, data)

    def buildDroid(self, data) -> None:
        data = B_PackagesChecker.buildDroid(self, data)
        self.Player.SendPacMan.droidBuildingDialog(self)

    def crearTargets(self, data) -> None:  # убрать дройдов всех
        data = B_PackagesChecker.crearTargets(self, data)
        self.Player.move(stop=True)

    def syncronizeHealth(self, data) -> None:
        data = B_PackagesChecker.syncronizeHealth(self, data)

    def createArenaRequest(self, data) -> None:
        data = B_PackagesChecker.createArenaRequest(self, data)

    def commitSkills(self, data):
        data = B_PackagesChecker.commitSkills(self, data)
        self.Player.commitSkills(data)
        self.Player.SendPacMan(T_ServerRequest.PLAYER_SKILLS)

    def applyGineticLabOption(self, data) -> None:
        data = B_PackagesChecker.applyGineticLabOption(self, data)
        self.Player.reset_skills()

    def sendCredits(self, data) -> None:
        data = B_PackagesChecker.sendCredits(self, data)

    def sendBonuses(self, data) -> None:
        data = B_PackagesChecker.sendBonuses(self, data)

    def toRepository(self, data) -> None:
        data = B_PackagesChecker.toRepository(self, data)

    def returnItem(self, data) -> None:
        data = B_PackagesChecker.returnItem(self, data)

    def toClanRepository(self, data) -> None:
        data = B_PackagesChecker.toClanRepository(self, data)

    def returnItemClan(self, data) -> None:
        data = B_PackagesChecker.returnItemClan(self, data)

    def loadClan(self, data) -> None:
        data = B_PackagesChecker.loadClan(self, data)

    def clanLoad(self, data) -> None:
        data = B_PackagesChecker.clanLoad(self, data)

    def checkValue(self, data) -> None:
        data = B_PackagesChecker.checkValue(self, data)

    def AcceptedClanInfo(self, data) -> None:
        data = B_PackagesChecker.AcceptedClanInfo(self, data)

    def createClan(self, data) -> None:
        data = B_PackagesChecker.createClan(self, data)

    def ClansLetters(self, data) -> None:
        data = B_PackagesChecker.ClansLetters(self, data)

    def ClansList(self, data) -> None:
        data = B_PackagesChecker.ClansList(self, data)

    def joinToClanRequest(self, data) -> None:
        data = B_PackagesChecker.joinToClanRequest(self, data)

    def bodylessCommand(self, data) -> None:
        data = B_PackagesChecker.bodylessCommand(self, data)

    def guidValueCommand(self, data) -> None:
        data = B_PackagesChecker.guidValueCommand(self, data)

    def tradeItemToSell(self, data) -> None:
        data = B_PackagesChecker.tradeItemToSell(self, data)

    def intValueCommand(self, data, command_type) -> None:
        data = B_PackagesChecker.intValueCommand(self, data)
        match command_type:
            case T_ClientRequest.PLAYER_INFO:
                self.Player.SendPacMan.playerInfo(data[Keys.id])
            # case T_ClientRequest.REMOVE_CLAN_RELATION:
            #     self.PlayerItems.
            # case T_ClientRequest.ADD_CLAN_TO_ENEMIES:
            #     self.PlayerItems.
            # case T_ClientRequest.ADD_CLAN_FRIEND_REQUEST:
            #     self.PlayerItems.
            # case T_ClientRequest.REMOVE_PLAYER_FROM_CLAN:
            #     self.PlayerItems.
            case T_ClientRequest.TO_GAME:
                self.Player.SendPacMan.toGame()
            # case T_ClientRequest.EXCHANGE_VOTES:
            #     self.PlayerItems.
            case T_ClientRequest.CHANGE_SHIP:
                self.Player.change_ship(data[Keys.id])
            # case T_ClientRequest.DELETE_PILOT:
            #     self.PlayerItems.
            # case T_ClientRequest.CANCEL_DELETE_PILOT:
            #     self.PlayerItems.
            # case T_ClientRequest.EXCHANGE_VOTES_TO_BONUSES:
            #     self.PlayerItems.
            # case T_ClientRequest.TRADE_INVITATION:
            #     self.PlayerItems.
            # case T_ClientRequest.TRADE_CASH:
            #     self.PlayerItems.
            # case T_ClientRequest.CHANGE_LEADER:
            #     self.PlayerItems.
            # case T_ClientRequest.GET_UPDATE_VALUE:
            #     self.PlayerItems.
            # case T_ClientRequest.REMOVE_PLAYER_FROM_TEAM:
            #     self.PlayerItems.
            # case _:
            #     print("error")

    def floatValueCommand(self, data) -> None:
        data = B_PackagesChecker.floatValueCommand(self, data)

    def boolValueCommand(self, data) -> None:
        data = B_PackagesChecker.boolValueCommand(self, data)

    def submitClanFriendRequests(self, data) -> None:
        data = B_PackagesChecker.submitClanFriendRequests(self, data)

    def createPilot(self, data) -> None:
        data = B_PackagesChecker.createPilot(self, data)

    def saveClanJoinRequests(self, data) -> None:
        data = B_PackagesChecker.saveClanJoinRequests(self, data)

    def buyItemByBonuses(self, data) -> None:
        data = B_PackagesChecker.buyItemByBonuses(self, data)
        self.Player.buyItemByBonuses(data)
        self.Player.SendPacMan(T_ServerRequest.INVENTORY)
        self.Player.updateValues(T_UpdateValue.Bonuses)

    def buyShipByBonuses(self, data) -> None:
        data = B_PackagesChecker.buyShipByBonuses(self, data)

    def tradeInvitationdatault(self, data) -> None:
        data = B_PackagesChecker.tradeInvitationResult(self, data)

    def PlayerRole(self, data) -> None:
        data = B_PackagesChecker.PlayerRole(self, data)

    def renamePilot(self, data) -> None:
        data = B_PackagesChecker.renamePilot(self, data)
        