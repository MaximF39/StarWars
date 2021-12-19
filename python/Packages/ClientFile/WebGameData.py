class WebGameData:
    self: None  # WebGameData
    _b_manual_closed: bool = False

    _o_socket: None  # Socket
    login_data_received: None  # 
    system_state_received: None  # 
    trading_data: None  # 

    def on_socket_data(self):
        if self.system_state_received != None:
            self.system_state_received()
            self.system_state_received = None

    pass


class WebGameData:
    self: WebGameData
    _bManualClosed: bool = False
    # _oSocket: Socket
    loginDataReceived: None
    systemStateReceived: None
    tradingData: None

    def WebGameData(self):
        super().__init__()
        # PackagesManager.initialize()
        # this.connect()

    def initialize(self):
        # self = new
        WebGameData()

    def disconnect(self):
        _bManualClosed = True
        if self._oSocket.connected:
            self._oSocket.close()

    def toGame(self, param1: int) -> None:
        self.send(PackageCreator.intValueCommand(ClientCommands.TO_GAME, param1))

    def createPilot(self, param1: PlayerInfoData):
        self.send(PackageCreator.createPilot(param1))

    def changeShip(self, param1: int):
        self.send(PackageCreator.intValueCommand(ClientCommands.CHANGE_SHIP, param1))

    def exchangeVotesToBonuses(self, param1: int):
        self.send(PackageCreator.intValueCommand(ClientCommands.EXCHANGE_VOTES_TO_BONUSES, param1))

    def exchangeVotes(self, param1: int) -> None:
        self.send(PackageCreator.intValueCommand(ClientCommands.EXCHANGE_VOTES, param1))

    def RenamePilot(self, param1: int, param2: str) -> None:
        self.send(PackageCreator.renamePilot(param1, param2))

    def cancelDeletePilot(self, param1: int): 
        self.send(PackageCreator.intValueCommand(ClientCommands.CANCEL_DELETE_PILOT, param1))
    
    def changeLeader(self, param1: int): 
        self.send(PackageCreator.intValueCommand(ClientCommands.CHANGE_LEADER, param1))

    def leaveClan(self) -> None: 
        self.send(PackageCreator.bodylessCommand(ClientCommands.LEAVE_CLAN))

    def getMap(): 
        self.send(PackageCreator.bodylessCommand(ClientCommands.GET_MAP))
    
    def deletePilot(self, param1: int): 
        self.send(PackageCreator.intValueCommand(ClientCommands.DELETE_PILOT, param1))

    def getupdatevalue(self, param1: int): 
        self.send(PackageCreator.intValueCommand(ClientCommands.GET_UPDATE_VALUE, param1)) 

    def buyItemByBonuses(self, param1: int, param2: int, param3: int, param4: int): 
        self.send(PackageCreator.buyItemByBonuses(param1, param2, param3, param4))
    

    def buyShipByBonuses(self, param1: int, param2: int, param3: int): 
        self.send(PackageCreator.buyShipByBonuses(param1, param2, param3))
    
    def tradeInvitationResult(self, param1: int, param2: bool): 
        self.send(PackageCreator.tradeInvitationResult(param1, param2))

    def sendPlayerTradingCash(self, param1: int):
        self.send(PackageCreator.intValueCommand(ClientCommands.TRADE_CASH, param1))

    def tradeInvitation(param1: int):
        self.send(PackageCreator.intValueCommand(ClientCommands.TRADE_INVITATION, param1))
    

    def tradeItemToSell(self, param1: bytearray, param2: int):
        self.send(PackageCreator.tradeItemToSell(param1, param2))
    
    def tradeItemToHold(self, param1: bytearray):
        self.send(PackageCreator.guidValueCommand(ClientCommands.TRADE_ITEM_TO_HOLD, param1))

    def tradingDenied(self):
        self.send(PackageCreator.bodylessCommand(ClientCommands.TRADE_DENIED))
    
    def tradingAccepted(self, param1: bool):
        self.send(PackageCreator.boolValueCommand(ClientCommands.TRADE_ACCEPTED, param1))

    def updateHoldRequest():
        self.send(PackageCreator.bodylessCommand(ClientCommands.UPDATE_HOLD))

    def lostItems():
        self.send(PackageCreator.bodylessCommand(ClientCommands.LOST_ITEMS))

    def updateShip():
        self.send(PackageCreator.bodylessCommand(ClientCommands.UPDATE_SHIP))

    def finishTradingResult(self, param1: bool):
        self.send(PackageCreator.boolValueCommand(ClientCommands.FINISH_TRADING_RESULT, param1))

    def connect():
        _bManualClosed = False
        this._oSocket = new
        Socket()
        this._oSocket.addEventListener(ProgressEvent.SOCKET_DATA, this.onSocketData)
        this._oSocket.addEventListener(IOErrorEvent.IO_ERROR, this.onIOError)
        this._oSocket.addEventListener(SecurityErrorEvent.SECURITY_ERROR, this.onSecurityError)
        this._oSocket.addEventListener(Event.CLOSE, this.onClose)
        this._oSocket.connect(SocialCfg.GetIpAdress(), SocialCfg.GetPort())
    

    # get
    def connected(self) -> bool:
        return this._oSocket.connected

    def send(self, param1: bytearray):
        if !this.connected
            this.onClose(None)
        return
    
    Traffic.output(param1.length)
    this._oSocket.writeBytes(param1, 0, param1.length)
    this._oSocket.flush()

    onClose(param1: Event): 
    
    if (_bManualClosed)
    
    return


    if not GameEngine.self != None:
        GameEngine.self.connectionLost()

    def onSecurityError(param1: Event): 
        Console.write(ResourceStrings.SecurityErrorMessage)
    
    
    def onIOError(param1: IOErrorEvent):
        this.onClose(None)
    
    
    def move(param1: Number, param2: Number, param3: int): 
        _loc4_: bytearray = PackageCreator.move(param1, param2, param3)
    this.send(_loc4_)
    
    # get
    def battles(self) -> None: 
        return new
        Array()
    
    
    def login(self, param1: str, param2: str, param3: str): 
        _loc4_: bytearray = PackageCreator.login(param1, param2, param3)
        this.send(_loc4_)
    
    
    def registration(self, param1: str, param2: str, param3: str, param4: int): 
        if not GameEngine.checkVersion():
            return
        
        _loc5_: bytearray = PackageCreator.registration(param1, param2, param3, param4)
        this.send(_loc5_)


    def sendResponceForPlanet(param1: int): 
        _loc2_: bytearray = PackageCreator.planetRequest(param1)
        this.send(_loc2_)




    def sendResponceForShip(param1: int): 
        _loc2_: bytearray = PackageCreator.shipRequest(param1)
        this.send(_loc2_)


    def leaveLocation(): 
        _loc1_: bytearray = PackageCreator.leaveLocation()
        this.send(_loc1_)


    def onSocketData(param1: ProgressEvent): 
        PackagesManager.process(this._oSocket)
        if this.systemStateReceived != None:
            this.systemStateReceived()
            this.systemStateReceived = None


    def setObjectToReach(self, param1: SpaceObject, param2: int, param3: int):
        this.send(PackageCreator.objectToReach(param1, param2, param3))

    def addObjectToTeam(self, param1: int):
        this.send(PackageCreator.addObjectToTeam(param1))


    def setObjectToAttack(self, param1: SpaceObject):
        this.send(PackageCreator.setObjectToAttack(param1))

    def useItem(param1: bytearray):
        if (param1 == None):
            return
        _loc2_: bytearray = PackageCreator.useItem(param1)
        this.send(_loc2_)

    def unuseItem(param1: bytearray):
        if param1 == None:
            return
        this.send(PackageCreator.unuseItem(param1))


    def openShop(self, param1: int):
        this.send(PackageCreator.openShop(param1))


    def getInventoty(self):
        _loc1_: bytearray = PackageCreator.inventory()
        this.send(_loc1_)


    def getReachableSystems(self):
        _loc1_: bytearray = PackageCreator.reachableSystems()
        this.send(_loc1_)

    def jumpTo(self, param1: ReachableSystem, param2: int):
        _loc3_: bytearray = PackageCreator.jumpTo(param1, param2)
        this.send(_loc3_)

    def sendMessage(self, param1: str, param2: int, param3: int):
        _loc4_: bytearray = PackageCreator.sendMessage(param1, param2, param3)
        this.send(_loc4_)

    def sendBan(param1: str, param2: str, param3: int):
        _loc4_: bytearray = PackageCreator.sendBan(param1, param2, param3)
        this.send(_loc4_)
    
    def sendEvil(param1: str):
        _loc2_: bytearray = PackageCreator.evil(param1)
        this.send(_loc2_)

    def repair(self): 
        _loc1_: bytearray = PackageCreator.repair()
        this.send(_loc1_)

    def getAuction(self): 
        _loc1_: bytearray = PackageCreator.getAuction()
        this.send(_loc1_)

    def playerSkills(): 
        _loc1_: bytearray = PackageCreator.playerSkills()
        this.send(_loc1_)

    def deviceClicked(param1: bytearray, param2: int = 0, param3:int = 0, param4:int = 0): 
        _loc5_: bytearray = PackageCreator.deviceClicked(param1, param2, param3, param4)
    this.send(_loc5_)

    def droidClicked(param1: bytearray, param2: bytearray): 
        _loc3_: bytearray = PackageCreator.droidClicked(param1, param2)
        this.send(_loc3_)   

    def restoreEnergy(): 
        _loc1_: bytearray = PackageCreator.restoreEnergy()
        this.send(_loc1_)

    def droidBackCommand(self, param1: int):
        _loc2_: bytearray = PackageCreator.droidCommand(DroidCommand.BackToShip, param1, 0, 0)
        this.send(_loc2_)

    def droidsReturnAll(): 
        _loc1_: bytearray = PackageCreator.droidCommand(DroidCommand.ReturnAll, 0, 0, 0)
        this.send(_loc1_)

    def droidAttackCommand(self, param1: int, param2: int, param3: int): 
        _loc4_: bytearray = PackageCreator.droidCommand(DroidCommand.Attack, param1, param2, param3)
        this.send(_loc4_)

    def droidMoveCommand(self, param1: int, param2: int, param3: int): 
        _loc4_: bytearray = PackageCreator.droidCommand(DroidCommand.Move, param1, param2, param3)
        this.send(_loc4_)

    def buyShip(param1: FakeShip, param2: bool): 
        _loc3_: bytearray = PackageCreator.buyShip(param1.shipData, param2)
        this.send(_loc3_)

    def showQuest(param1: int):
        _loc2_: bytearray = PackageCreator.showQuest(param1)
        this.send(_loc2_)

    def getQuest(self, param1: int):
        _loc2_: bytearray = PackageCreator.getQuest(param1)
        this.send(_loc2_)

    def questsJournal():
        this.send(PackageCreator.questsJournal())


    def showPlanetQuests(): 
        this.send(PackageCreator.showPlanetQuests())

    def training(param1: int, param2: int, param3: int, param4: int, param5: int, param6: int): 
        this.send(PackageCreator.training(param1, param2, param3, param4, param5, param6))


    def getArenaRequests(): 
        this.send(PackageCreator.arenaRequests())

    def joinToRequest(param1: BattleRequest): 
        this.send(PackageCreator.joinToRequest(param1))

    def battleRequestWindowClosed(): 
        this.send(PackageCreator.battleRequestWindowClosed())

    def readyToBattle(param1: BattleRequest): 
        this.send(PackageCreator.readyToBattle(param1))

    def droidsMode(param1: int):
        this.send(PackageCreator.droidsMode(param1))

    def buildDroid():
        this.send(PackageCreator.buildDroid())

    def crearTargets():
        this.send(PackageCreator.crearTargets())

    def buyItem(param1: Item):
        this.send(PackageCreator.buyItem(param1))

    def sellItem(param1: Item):
        this.send(PackageCreator.sellItem(param1))

    def resUpdate(param1: Item):
        this.send(PackageCreator.updateresource(param1))

    def clanCreate(param1: str, param2: str, param3: str):
        this.send(PackageCreator.clanCreate(param1, param2, param3))

    def dropItem(param1: Item):
        this.send(PackageCreator.dropItem(param1))

    def repairItem(param1: Item):
        this.send(PackageCreator.repairItem(param1))

    def syncronizeHealth(param1: int):
        this.send(PackageCreator.syncronizeHealth(param1))

    def createArenaRequest(param1: int, param2: int, param3: *):
        this.send(PackageCreator.createArenaRequest(param1, param2, param3))

    def commitSkills(param1: Dictionary):
        this.send(PackageCreator.commitSkills(param1))

    def applyGineticLabOption(param1: int):
        this.send(PackageCreator.applyGineticLabOption(param1))

    def sendCredits(param1: int, param2: int, param3: bool, param4: bool):
        this.send(PackageCreator.sendCredits(param1, param2, param3, param4))

    def sendBonuses(param1: int, param2: int, param3: bool, param4: bool):
        this.send(PackageCreator.sendBonuses(param1, param2, param3, param4))

    def toRepository(param1: bytearray, param2: int):
        this.send(PackageCreator.toRepository(param1, param2))

    def returnItem(param1: bytearray, param2: int):
        this.send(PackageCreator.returnItem(param1, param2))

    def toClanRepository(param1: bytearray, param2: int):
        this.send(PackageCreator.toClanRepository(param1, param2))

    def returnItemClan(param1: bytearray, param2: int):
        this.send(PackageCreator.returnItemClan(param1, param2))

    def loadClan(param1: int):
        this.send(PackageCreator.loadClan(param1))

    def clanLoad(param1: int):
        this.send(PackageCreator.clanLoad(param1))

    def checkValue(param1: str, param2: int):
        this.send(PackageCreator.checkValue(param1, param2))

    def getAcceptedClanInfo():
        this.send(PackageCreator.getAcceptedClanInfo())

    def createClan(param1: int):
        this.send(PackageCreator.createClan(param1))

    def getClansLetters():
        this.send(PackageCreator.getClansLetters())

    def getClansList(param1: str, param2: bool):
        this.send(PackageCreator.getClansList(param1, param2))

    def joinToClanRequest(param1: int, param2: str):
        this.send(PackageCreator.joinToClanRequest(param1, param2))

    def getClanRequests():
        this.send(PackageCreator.bodylessCommand(ClientCommands.GET_CLAN_REQUESTS))

    def getPlayerInfo(param1: int):
        this.send(PackageCreator.intValueCommand(ClientCommands.PLAYER_INFO, param1))

    def saveClanJoinRequests(param1: Array):
        this.send(PackageCreator.saveClanJoinRequests(param1))

    def joinToClan(param1: bool):
        this.send(PackageCreator.boolValueCommand(ClientCommands.JOIN_TO_CLAN, param1))

    def def cancelClanCreateRequest():
        this.send(PackageCreator.bodylessCommand(ClientCommands.CANCEL_CLAN_CREATE_REQUEST))

    def getFriendClans():
        this.send(PackageCreator.bodylessCommand(ClientCommands.GET_FRIEND_CLANS))

    def getEnemyClans():
        this.send(PackageCreator.bodylessCommand(ClientCommands.GET_ENEMY_CLANS))

    def getFriendRequests():
        this.send(PackageCreator.bodylessCommand(ClientCommands.GET_FRIEND_REQUESTS))

    def addClanToEnemies(param1: int):
        this.send(PackageCreator.intValueCommand(ClientCommands.ADD_CLAN_TO_ENEMIES, param1))

    def addClanFriendRequest(param1: int):
        this.send(PackageCreator.intValueCommand(ClientCommands.ADD_CLAN_FRIEND_REQUEST, param1))

    def removePlayerFromClan(param1: int):
        this.send(PackageCreator.intValueCommand(ClientCommands.REMOVE_PLAYER_FROM_CLAN, param1))

    def removePlayerFromTeam(param1: int):
        this.send(PackageCreator.intValueCommand(ClientCommands.REMOVE_PLAYER_FROM_TEAM, param1))

    def setPlayerRole(param1: int, param2: int):
        this.send(PackageCreator.setPlayerRole(param1, param2))

    def removeClanRelation(param1: int):
        this.send(PackageCreator.intValueCommand(ClientCommands.REMOVE_CLAN_RELATION, param1))

    def moveClanToNextLevel():
        this.send(PackageCreator.bodylessCommand(ClientCommands.MOVE_CLAN_TO_NEXT_LEVEL))

    def submitClanFriendRequests(param1: Array, param2: Array):
        this.send(PackageCreator.submitClanFriendRequests(param1, param2))

    def getMissions():
        this.send(PackageCreator.bodylessCommand(ClientCommands.GET_MISSIONS))