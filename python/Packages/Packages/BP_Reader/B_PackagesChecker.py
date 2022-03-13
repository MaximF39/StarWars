from python.Packages.Packages.BP_Reader.B_PackagesReader import B_PackagesReader

class B_PackagesChecker(B_PackagesReader):
    def __init__(self, Game, Player, command_type, data):
        B_PackagesReader.__init__(self, Game, Player, command_type, data)

    def droidCommand(self, data) -> dict:
        data = B_PackagesReader.droidCommand(self, data)
        return data

    @staticmethod
    def login(data):
        data = B_PackagesReader.login(data)
        return data

    def registration(self, data) -> dict:
        data = B_PackagesReader.registration(self, data)
        return data

    def move(self, data) -> dict:
        data = B_PackagesReader.move(self, data)
        return data

    def leaveLocation(self, data):
        data = B_PackagesReader.leaveLocation(self, data)
        return data

    def evil(self, data) -> dict:
        data = B_PackagesReader.evil(self, data)
        return data

    def planetRequest(self, data) -> dict:
        data = B_PackagesReader.planetRequest(self, data)
        return data

    def shipRequest(self, data) -> dict:
        data = B_PackagesReader.shipRequest(self, data)
        return data

    def addObjectToTeam(self, data) -> dict:
        data = B_PackagesReader.addObjectToTeam(self, data)
        return data

    def ObjectToAttack(self, data) -> dict:
        data = B_PackagesReader.ObjectToAttack(self, data)
        return data

    def objectToReach(self, data):
        data = B_PackagesReader.objectToReach(self, data)
        return data

    def useItem(self, data) -> dict:
        data = B_PackagesReader.useItem(self, data)
        return data

    def unuseItem(self, data) -> dict:
        data = B_PackagesReader.unuseItem(self, data)
        return data

    def buy_item(self, data) -> dict:
        data = B_PackagesReader.buy_item(self, data)
        return data

    def sell_item(self, data) -> dict:
        data = B_PackagesReader.sell_item(self, data)
        return data

    def updateResource(self, data) -> dict:
        data = B_PackagesReader.updateResource(self, data)
        return data

    def clanCreate(self, data) -> dict:
        data = B_PackagesReader.clanCreate(self, data)
        return data

    def dropItem(self, data, ) -> dict:
        data = B_PackagesReader.dropItem(self, data)
        return data

    def repairItem(self, data) -> dict:
        data = B_PackagesReader.repairItem(self, data)
        return data

    def openShop(self, data, ) -> dict:
        data = B_PackagesReader.openShop(self, data)
        return data

    def inventory(self, data) -> dict:
        data = B_PackagesReader.inventory(self, data)
        return data

    def reachableSystems(self, data) -> dict:
        data = B_PackagesReader.reachableSystems(self, data)
        return data

    def jumpTo(self, data) -> dict:
        data = B_PackagesReader.jumpTo(self, data)
        return data

    def sendMessage(self, data) -> dict:
        data = B_PackagesReader.sendMessage(self, data)
        return data

    def sendBan(self, data) -> dict:
        data = B_PackagesReader.sendBan(self, data)
        return data

    def repair(self, data):
        data = B_PackagesReader.repair(self, data)
        return data

    def Auction(self, data) -> dict:
        data = B_PackagesReader.Auction(self, data)
        return data

    def restoreEnergy(self, data):
        data = B_PackagesReader.restoreEnergy(self, data)
        return data

    def playerSkills(self, data):
        data = B_PackagesReader.playerSkills(self, data)
        return data

    def ClickedTime(self, data) -> dict:
        data = B_PackagesReader.ClickedTime(self, data)
        return data

    def deviceClicked(self, data) -> dict:
        data = B_PackagesReader.deviceClicked(self, data)
        return data

    def droidClicked(self, data) -> dict:
        data = B_PackagesReader.droidClicked(self, data)
        return data

    def buyShip(self, data) -> dict:
        data = B_PackagesReader.buyShip(self, data)
        return data

    def showQuest(self, data) -> dict:
        data = B_PackagesReader.showQuest(self, data)
        return data

    def Quest(self, data) -> dict:
        data = B_PackagesReader.Quest(self, data)
        return data

    def questsJournal(self, data) -> dict:
        data = B_PackagesReader.questsJournal(self, data)
        return data

    def showPlanetQuests(self, data) -> dict:
        data = B_PackagesReader.showPlanetQuests(self, data)
        return data

    def training(self, data) -> dict:
        data = B_PackagesReader.training(self, data)
        return data

    def arenaRequests(self, data) -> dict:
        data = B_PackagesReader.arenaRequests(self, data)
        return data

    def joinToRequest(self, data) -> dict:
        data = B_PackagesReader.joinToRequest(self, data)
        return data

    def battleRequestWindowClosed(self, data) -> dict:
        data = B_PackagesReader.battleRequestWindowClosed(self, data)
        return data

    def readyToBattle(self, data) -> dict:
        data = B_PackagesReader.readyToBattle(self, data)
        return data

    def droidsMode(self, data) -> dict:
        data = B_PackagesReader.droidsMode(self, data)
        return data

    def buildDroid(self, data) -> dict:
        data = B_PackagesReader.buildDroid(self, data)
        return data

    def crearTargets(self, data) -> dict:  # убрать дройдов всех
        data = B_PackagesReader.crearTargets(self, data)
        return data

    def syncronizeHealth(self, data) -> dict:
        data = B_PackagesReader.syncronizeHealth(self, data)
        return data

    def createArenaRequest(self, data) -> dict:
        data = B_PackagesReader.createArenaRequest(self, data)
        return data

    def commitSkills(self, data):
        data = B_PackagesReader.commitSkills(self, data)
        return data

    def applyGineticLabOption(self, data) -> dict:
        data = B_PackagesReader.applyGineticLabOption(self, data)
        return data

    def sendCredits(self, data) -> dict:
        data = B_PackagesReader.sendCredits(self, data)
        return data

    def sendBonuses(self, data) -> dict:
        data = B_PackagesReader.sendBonuses(self, data)
        return data

    def toRepository(self, data) -> dict:
        data = B_PackagesReader.toRepository(self, data)
        return data

    def returnItem(self, data) -> dict:
        data = B_PackagesReader.returnItem(self, data)
        return data

    def toClanRepository(self, data) -> dict:
        data = B_PackagesReader.toClanRepository(self, data)
        return data

    def returnItemClan(self, data) -> dict:
        data = B_PackagesReader.returnItemClan(self, data)
        return data

    def loadClan(self, data) -> dict:
        data = B_PackagesReader.loadClan(self, data)
        return data

    def clanLoad(self, data) -> dict:
        data = B_PackagesReader.clanLoad(self, data)
        return data

    def checkValue(self, data) -> dict:
        data = B_PackagesReader.checkValue(self, data)
        return data

    def AcceptedClanInfo(self, data) -> dict:
        data = B_PackagesReader.AcceptedClanInfo(self, data)
        return data

    def createClan(self, data) -> dict:
        data = B_PackagesReader.createClan(self, data)
        return data

    def ClansLetters(self, data) -> dict:
        data = B_PackagesReader.ClansLetters(self, data)
        return data

    def ClansList(self, data) -> dict:
        data = B_PackagesReader.ClansList(self, data)
        return data

    def joinToClanRequest(self, data) -> dict:
        data = B_PackagesReader.joinToClanRequest(self, data)
        return data

    def bodylessCommand(self, data) -> dict:
        data = B_PackagesReader.bodylessCommand(self, data)
        return data

    def guidValueCommand(self, data) -> dict:
        data = B_PackagesReader.guidValueCommand(self, data)
        return data

    def tradeItemToSell(self, data) -> dict:
        data = B_PackagesReader.tradeItemToSell(self, data)
        return data

    def intValueCommand(self, data, command_type) -> dict:
        data = B_PackagesReader.intValueCommand(self, data)
        return data

    def floatValueCommand(self, data) -> dict:
        data = B_PackagesReader.floatValueCommand(self, data)
        return data

    def boolValueCommand(self, data) -> dict:
        data = B_PackagesReader.boolValueCommand(self, data)
        return data

    def submitClanFriendRequests(self, data) -> dict:
        data = B_PackagesReader.submitClanFriendRequests(self, data)
        return data

    def createPilot(self, data) -> dict:
        data = B_PackagesReader.createPilot(self, data)
        return data

    def saveClanJoinRequests(self, data) -> dict:
        data = B_PackagesReader.saveClanJoinRequests(self, data)
        return data

    def buyItemByBonuses(self, data) -> dict:
        data = B_PackagesReader.buyItemByBonuses(self, data)
        return data

    def buyShipByBonuses(self, data) -> dict:
        data = B_PackagesReader.buyShipByBonuses(self, data)
        return data

    def tradeInvitationResult(self, data) -> dict:
        data = B_PackagesReader.tradeInvitationResult(self, data)
        return data

    def PlayerRole(self, data) -> dict:
        data = B_PackagesReader.PlayerRole(self, data)
        return data

    def renamePilot(self, data) -> dict:
        data = B_PackagesReader.renamePilot(self, data)
        return data