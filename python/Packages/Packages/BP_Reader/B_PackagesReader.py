from python.Static.Type.Keys import Keys
from python.Static.Type.Package.T_ServerRequest import T_ServerRequest
from python.Packages.PackagesManager import PackagesManager
from python.Packages.PackageDecoder import PackageDecoder
from python.Static.Type.Package.T_ClientRequest import T_ClientRequest
import os, pathlib
from loguru import logger

from python.Static.Type.Package.T_UpdateValue import T_UpdateValue


class B_PackagesReader:
    def __write_logger(self):
        path = pathlib.Path(__file__)
        while path.name != 'python':
            path = path.parent
        path = path.joinpath('Database').joinpath("PlayerLog")

        if os.path.exists(path):
            os.chdir(path)
        else:
            os.mkdir(path)
            os.chdir(path)
        logger.add(f'Player_{self.id}.log', format="{time:YYYY-MM-DD HH:mm:ss.SSS}, {level}, {message}",
                   rotation="5 MB",
                   compression='zip', encoding='cp1251')  #

    def __init__(self, Game, Player, command_type, data):
        self.id = Player.id
        self.Game = Game
        self.Player = Player
        self.__write_logger()
        self._process(command_type, data)

    def _process(self, command_type, data):
        match command_type:
            case T_ClientRequest.LOGIN:
                self.login(data)
            case T_ClientRequest.MOVE:
                self.move(data)
            case T_ClientRequest.LEAVE_LOCATION:
                self.leaveLocation(data)
            case T_ClientRequest.PLANET_REQUEST:
                self.planetRequest(data)
            case T_ClientRequest.SHIP_REQUEST:
                self.shipRequest(data)
            #     # case T_ClientRequest.ALREADY_LOGGED: # don't use
            #         return self.
            #     # case T_ClientRequest.SESSION_ID: # don't use
            #         return self.
            case T_ClientRequest.OBJECT_TO_REACH:
                self.objectToReach(data)
            case T_ClientRequest.OBJECT_EVIL:
                self.evil(data)
            case T_ClientRequest.USE_ITEM:
                self.useItem(data)
            case T_ClientRequest.UNUSE_ITEM:
                self.unuseItem(data)
            case T_ClientRequest.OPEN_SHOP:
                self.openShop(data)
            # case T_ClientRequest.FAILED: # use i don't find it
            #         return self.
            #
            #
            #     # case T_ClientRequest.LOCATION_CHANGED: # don't use
            #         return self.
            #
            #
            case T_ClientRequest.INVENTORY:
                self.inventory(data)
            case T_ClientRequest.HYPERJUMP:
                self.jumpTo(data)
            case T_ClientRequest.REACHABLE_SYSTEMS:
                self.reachableSystems(data)
            case T_ClientRequest.MESSAGE:
                self.sendMessage(data)
            case T_ClientRequest.REPAIR:
                self.repair(data)
            case T_ClientRequest.MAP:  # don't use
                # print('sssssssssssss ERROR ')
                pass
            #     return self.bodylessCommand(data)
            case T_ClientRequest.REGISTER:
                self.registration(data)
            case T_ClientRequest.PLAYER_SKILLS:
                self.playerSkills(data)
            case T_ClientRequest.DEVICE_CLICKED:
                self.deviceClicked(data)
            case T_ClientRequest.DROID_CLICKED:
                self.droidClicked(data)
            case T_ClientRequest.RESTORE_ENERGY:
                self.restoreEnergy(data)
            case T_ClientRequest.USE_FREE_PARAMETERS:  # don't use
                # print('sssssssssss ERROR')
                pass
            case T_ClientRequest.DROID_COMMAND:
                self.droidCommand(data)
            case T_ClientRequest.BUY_SHIP:
                self.buyShip(data)
            case T_ClientRequest.SHOW_QUEST:
                self.showQuest(data)
            case T_ClientRequest.GET_QUEST:
                self.Quest(data)
            case T_ClientRequest.QUESTS_JOURNAL:
                self.questsJournal(data)
            case T_ClientRequest.PLANET_QUESTS:
                self.showPlanetQuests(data)
            case T_ClientRequest.TRAINING:
                self.training(data)
            case T_ClientRequest.ARENA_REQUESTS:
                self.arenaRequests(data)
            case T_ClientRequest.JOIN_TO_REQUEST:
                self.joinToRequest(data)
            case T_ClientRequest.BATTLE_REQUEST_WINDOW_CLOSED:
                self.battleRequestWindowClosed(data)
            case T_ClientRequest.READY_TO_BATTLE:
                self.readyToBattle(data)
            case T_ClientRequest.DROIDS_MODE:
                self.droidsMode(data)
            case T_ClientRequest.BUILD_DROID:
                self.buildDroid(data)
            case T_ClientRequest.SYNCRONIZE_HEALTH:
                self.syncronizeHealth(data)
            case T_ClientRequest.CREATE_ARENA_REQUEST:
                self.createArenaRequest(data)
            case T_ClientRequest.BUY_ITEM:
                self.buy_item(data)
            case T_ClientRequest.SELL_ITEM:
                self.sell_item(data)
            case T_ClientRequest.DROP_ITEM:
                self.dropItem(data)
            case T_ClientRequest.OBJECT_TO_ATTACK:
                self.ObjectToAttack(data)
            case T_ClientRequest.COMMIT_SKILLS:
                self.commitSkills(data)
            case T_ClientRequest.APPLY_GINETIC_LAB_OPTION:
                self.applyGineticLabOption(data)
            case T_ClientRequest.CREAR_TARGETS:
                self.crearTargets(data)
            case T_ClientRequest.SEND_CREDITS:
                self.sendCredits(data)
            case T_ClientRequest.TO_REPOSITORY:
                self.toRepository(data)
            case T_ClientRequest.RETURN_ITEM:
                self.returnItem(data)
            case T_ClientRequest.LOAD_CLAN:
                self.loadClan(data)
            case T_ClientRequest.CLAN_LOAD:
                self.clanLoad(data)
            case T_ClientRequest.CHECK_VALUE:
                self.checkValue(data)
            case T_ClientRequest.ACCEPTED_CLAN_INFO:
                self.AcceptedClanInfo(data)
            case T_ClientRequest.CREATE_CLAN:
                self.createClan(data)
            case T_ClientRequest.GET_CLANS_LETTERS:
                self.ClansLetters(data)
            case T_ClientRequest.GET_CLANS_LIST:
                self.ClansList(data)
            case T_ClientRequest.JOIN_TO_CLAN_REQUEST:
                self.joinToClanRequest(data)
            case T_ClientRequest.GET_CLAN_REQUESTS:
                self.bodylessCommand(data)
            case T_ClientRequest.PLAYER_INFO:
                self.intValueCommand(data, command_type)
            case T_ClientRequest.SAVE_CLAN_JOIN_REQUESTS:
                self.saveClanJoinRequests(data)
            case T_ClientRequest.JOIN_TO_CLAN:
                self.boolValueCommand(data)
            case T_ClientRequest.CANCEL_CLAN_CREATE_REQUEST:
                self.bodylessCommand(data)
            case T_ClientRequest.GET_FRIEND_CLANS:
                self.bodylessCommand(data)
            case T_ClientRequest.GET_ENEMY_CLANS:
                self.bodylessCommand(data)
            case T_ClientRequest.REMOVE_CLAN_RELATION:
                self.intValueCommand(data, command_type)
            case T_ClientRequest.ADD_CLAN_TO_ENEMIES:
                self.intValueCommand(data, command_type)
            case T_ClientRequest.ADD_CLAN_FRIEND_REQUEST:
                self.intValueCommand(data, command_type)
            case T_ClientRequest.GET_FRIEND_REQUESTS:
                self.bodylessCommand(data)
            case T_ClientRequest.SUBMIT_CLAN_FRIEND_REQUESTS:
                self.submitClanFriendRequests(data)
            case T_ClientRequest.MOVE_CLAN_TO_NEXT_LEVEL:
                self.bodylessCommand(data)
            case T_ClientRequest.REMOVE_PLAYER_FROM_CLAN:
                self.intValueCommand(data, command_type)
            case T_ClientRequest.GET_MISSIONS:
                self.bodylessCommand(data)
            case T_ClientRequest.CREATE_PILOT:
                self.createPilot(data)
            case T_ClientRequest.TO_GAME:
                self.intValueCommand(data, command_type)
            case T_ClientRequest.EXCHANGE_VOTES:
                self.intValueCommand(data, command_type)
            case T_ClientRequest.CHANGE_SHIP:
                self.intValueCommand(data, command_type)
            case T_ClientRequest.DELETE_PILOT:
                self.intValueCommand(data, command_type)
            case T_ClientRequest.CANCEL_DELETE_PILOT:
                self.intValueCommand(data, command_type)
            case T_ClientRequest.GET_MAP:
                self.bodylessCommand(data)
            case T_ClientRequest.LEAVE_CLAN:
                self.bodylessCommand(data)
            case T_ClientRequest.EXCHANGE_VOTES_TO_BONUSES:
                self.intValueCommand(data, command_type)
            case T_ClientRequest.BUY_ITEM_BY_BONUSES:
                self.buyItemByBonuses(data)
            case T_ClientRequest.TRADE_INVITATION:
                self.intValueCommand(data, command_type)
            case T_ClientRequest.TRADE_INVITATION_RESULT:
                self.tradeInvitationResult(data)
            case T_ClientRequest.TRADE_CASH:
                self.intValueCommand(data, command_type)
            case T_ClientRequest.TRADE_ITEM_TO_SELL:
                self.tradeItemToSell(data)
            case T_ClientRequest.TRADE_ITEM_TO_HOLD:
                self.guidValueCommand(data)
            case T_ClientRequest.TRADE_ACCEPTED:
                self.boolValueCommand(data)
            case T_ClientRequest.FINISH_TRADING_RESULT:
                self.boolValueCommand(data)
            case T_ClientRequest.TRADE_DENIED:
                self.bodylessCommand(data)
            case T_ClientRequest.UPDATE_HOLD:
                self.bodylessCommand(data)
            case T_ClientRequest.UPDATE_SHIP:
                self.bodylessCommand(data)
            case T_ClientRequest.LOST_ITEMS:
                self.bodylessCommand(data)
            case T_ClientRequest.CHANGE_LEADER:
                self.intValueCommand(data, command_type)
            case T_ClientRequest.UPDATE_RESOURCE:
                self.updateResource(data)
            case T_ClientRequest.CLAN_CREATE:
                self.clanCreate(data)
            case T_ClientRequest.TO_CLAN_REPOSITORY:
                self.toClanRepository(data)
            case T_ClientRequest.RETURN_ITEM_CLAN:
                self.returnItemClan(data)
            case T_ClientRequest.SET_PLAYER_ROLE:
                self.PlayerRole(data)
            case T_ClientRequest.SEND_BONUSES:
                self.sendBonuses(data)
            case T_ClientRequest.RENAME_PILOT:
                self.renamePilot(data)
            case T_ClientRequest.RESERV4:
                self.ClickedTime(data)
            case T_ClientRequest.REPAIR_ITEM:
                self.repairItem(data)
            case T_ClientRequest.GETAUCTION:
                self.Auction(data)
            case T_ClientRequest.GET_UPDATE_VALUE:
                self.intValueCommand(data, command_type)
            case T_ClientRequest.OBJECT_TO_TEAM:
                self.addObjectToTeam(data)
            case T_ClientRequest.REMOVE_PLAYER_FROM_TEAM:
                self.intValueCommand(data, command_type)
            case T_ClientRequest.SEND_BAN:
                self.sendBan(data)
            case T_ClientRequest.RESERV11:  # don't use
                pass
            #     return self.
            case T_ClientRequest.RESERV12:  # don't use
                pass
            #     return self.
            case T_ClientRequest.BUY_SHIP_BY_BONUSES:
                self.buyShipByBonuses(data)
            case _:
                pass

    @staticmethod
    def _myLogger(func):
        def print_(*args, **kwargs):
            res = func(*args, **kwargs)
            logger.info(func.__name__ + res.__str__())
            return res
        return print_

    @_myLogger
    def droidCommand(self, data) -> dict:
        _loc5_ = PackageDecoder(data)
        return {
            Keys.hz: _loc5_.read_bytes(16),  # 16 или 1
            Keys.type_command: _loc5_.read_int(),
            Keys.hz3: _loc5_.read_int(),
            Keys.hz4: _loc5_.read_int(),
        }

    @staticmethod
    @_myLogger
    def login(data):
        _loc5_ = PackageDecoder(data)
        return {
            Keys.login: _loc5_.read_utf(),  # Vk_user_id
            Keys.authkey: _loc5_.read_utf(),  # don't use
            Keys.password: _loc5_.read_utf(),  # Vk_auth_key
            Keys.domain: _loc5_.read_utf()}  # domain

    @_myLogger
    def registration(self, data) -> dict:
        _loc5_ = PackageDecoder(data)
        return {
            Keys.id: _loc5_.read_utf(),  # Vk_user_id
            Keys.count_click: _loc5_.read_utf(),  # don't use
            Keys.authkey: _loc5_.read_utf(),  # Vk_auth_key
            Keys.domain: _loc5_.read_utf()}  # domain

    @_myLogger
    def move(self, data) -> dict:
        _loc4_ = PackageDecoder(data)

        return {Keys.x: _loc4_.read_float(),  # count_click
                Keys.y: _loc4_.read_float(),  # y
                Keys.count_click: _loc4_.read_int()}  # count

    @_myLogger
    def leaveLocation(self, data):
        return {}

    @_myLogger
    def evil(self, data) -> dict:
        oWriter = PackageDecoder(data)
        info = oWriter.read_utf()
        return {}

    @_myLogger
    def planetRequest(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {Keys.id: _loc2_.read_int()}

    @_myLogger
    def shipRequest(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {Keys.id: _loc2_.read_int()}

    @_myLogger
    def addObjectToTeam(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.t_object_to_reach: _loc2_.read_int(),
            Keys.id: _loc2_.read_int()}

    @_myLogger
    def ObjectToAttack(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.type: _loc2_.read_int(),  # t_object_to_reach
            Keys.id: _loc2_.read_int(), }  # id

    @_myLogger
    def objectToReach(self, data):
        _loc4_ = PackageDecoder(data)
        return {
            Keys.type: _loc4_.read_int(),
            Keys.id: _loc4_.read_int(),
            Keys.aliance: _loc4_.read_int(),
            Keys.count_click: _loc4_.read_int()  # count
        }

    @_myLogger
    def useItem(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.guid: _loc2_.read_bytes(16), }

    @_myLogger
    def unuseItem(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {Keys.guid: _loc2_.read_bytes(16)}

    @_myLogger
    def buy_item(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.guid: _loc2_.read_bytes(16),
            Keys.wear: _loc2_.read_int(), }

    @_myLogger
    def sell_item(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.guid: _loc2_.read_bytes(16),
            Keys.wear: _loc2_.read_int(), }

    @_myLogger
    def updateResource(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.guid: _loc2_.read_bytes(16),
            Keys.wear: _loc2_.read_int(), }

    @_myLogger
    def clanCreate(self, data) -> dict:
        _loc4_ = PackageDecoder(data)
        return {
            Keys.name: _loc4_.read_utf(),
            Keys.description: _loc4_.read_utf(),
            Keys.name_short: _loc4_.read_utf(), }

    @_myLogger
    def dropItem(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.guid: _loc2_.read_bytes(16),
            Keys.wear: _loc2_.read_int(), }

    @_myLogger
    def repairItem(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.guid: _loc2_.read_bytes(),
            Keys.wear: _loc2_.read_int(), }

    @_myLogger
    def openShop(self, data, ) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {Keys.type: _loc2_.read_int()}

    @_myLogger
    def inventory(self, data) -> dict:
        _loc1_ = PackageDecoder(data)
        return {Keys.domain: _loc1_.read_utf()}  # domain ?!

    @_myLogger
    def reachableSystems(self, data) -> dict:
        # _loc1_: PackageDecoder = PackageDecoder(data)
        return {}

    @_myLogger
    def jumpTo(self, data) -> dict:
        _loc4_ = PackageDecoder(data)
        return {
            Keys.id: _loc4_.read_int(),
            Keys.count_click: _loc4_.read_int(),  # clicked count
            Keys.domain: _loc4_.read_utf()  # domain
        }  # id Location

    @_myLogger
    def sendMessage(self, data) -> dict:
        _loc4_ = PackageDecoder(data)
        return {
            Keys.private_id: _loc4_.read_int(),
            Keys.text: _loc4_.read_utf(),
            Keys.type_chat: _loc4_.read_unsigned_byte(), }  # 1 - global  2 - local 3 - clan_id 4 - trade 5 - client chat

    @_myLogger
    def sendBan(self, data) -> dict:
        _loc4_ = PackageDecoder(data)
        return {
            Keys.text1: _loc4_.read_utf(),
            Keys.text2: _loc4_.read_utf(),
            Keys.bool: _loc4_.read_bytes(), }

    @_myLogger
    def repair(self, data):
        return {}

    @_myLogger
    def Auction(self, data) -> dict:
        _loc1_: PackageDecoder = PackageDecoder(data)
        return {}

    @_myLogger
    def restoreEnergy(self, data) -> dict:
        return {}

    @_myLogger
    def playerSkills(self, data):
        return {}

    @_myLogger
    def ClickedTime(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {Keys.hz: _loc2_.read_int()}

    @_myLogger
    def deviceClicked(self, data) -> dict:
        _loc5_ = PackageDecoder(data)
        return {
            Keys.guid: _loc5_.read_bytes(),
            Keys.target_id: _loc5_.read_int(),  # id цели если 0 то исползуется сам на себя
            Keys.id_droid: _loc5_.read_unsigned_byte(),  # id использовавшего
            Keys.effect_type: _loc5_.read_unsigned_byte(), }

    @_myLogger
    def droidClicked(self, data) -> dict:
        _loc3_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.hz: _loc3_.read_bytes(),
            Keys.guid: _loc3_.read_bytes(), }

    @_myLogger
    def buyShip(self, data) -> dict:
        _loc3_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.guid: _loc3_.read_bytes(),
            Keys.bool: _loc3_.read_bool(), }

    @_myLogger
    def showQuest(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {Keys.id: _loc2_.read_int(), }

    @_myLogger
    def Quest(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {Keys.id: _loc2_.read_int(), }  # id quest

    @_myLogger
    def questsJournal(self, data) -> dict:
        return {}

    @_myLogger
    def showPlanetQuests(self, data) -> dict:
        return {}

    @_myLogger
    def training(self, data) -> dict:
        _loc7_ = PackageDecoder(data)
        return {
            Keys.hz1: _loc7_.read_int(),
            Keys.hz2: _loc7_.read_int(),
            Keys.hz3: _loc7_.read_int(),
            Keys.hz4: _loc7_.read_int(),
            Keys.hz5: _loc7_.read_int(),
            Keys.hz6: _loc7_.read_int(), }

    @_myLogger
    def arenaRequests(self, data) -> dict:
        return {}

    @_myLogger
    def joinToRequest(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {Keys.id: _loc2_.read_int()}

    @_myLogger
    def battleRequestWindowClosed(self, data) -> dict:
        return {}

    @_myLogger
    def readyToBattle(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {Keys.id: _loc2_.read_int()}

    @_myLogger
    def droidsMode(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {Keys.id: _loc2_.read_int()}

    @_myLogger
    def buildDroid(self, data) -> dict:
        return {}

    @_myLogger
    def crearTargets(self, data) -> dict:  # убрать дройдов всех
        return {}

    @_myLogger
    def syncronizeHealth(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {Keys.id: _loc2_.read_int()}

    @_myLogger
    def createArenaRequest(self, data) -> dict:
        _loc4_ = PackageDecoder(data)
        return {
            Keys.type: _loc4_.read_unsigned_byte(),  # read_bytes()
            Keys.id: _loc4_.read_int(),
            Keys.bool: _loc4_.read_bool(), }

    @_myLogger
    def commitSkills(self, data):
        decoder: PackageDecoder = PackageDecoder(data)
        data_skills = {}
        while len(decoder.data) > decoder.Position:
            self._read_skill(data_skills, decoder)
        return data_skills

    def _read_skill(self, data, decoder):
        type_ = decoder.read_unsigned_byte()
        count = decoder.read_unsigned_byte()
        data[type_] = count  # player skill type

    @_myLogger
    def applyGineticLabOption(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {Keys.id: _loc2_.read_int()}

    @_myLogger
    def sendCredits(self, data) -> dict:
        _loc5_ = PackageDecoder(data)
        return {
            Keys.id: _loc5_.read_int(),  # id
            Keys.wear: _loc5_.read_int(),  # count credits
            Keys.bool1: _loc5_.read_bool(),
            Keys.bool2: _loc5_.read_bool(), }

    @_myLogger
    def sendBonuses(self, data) -> dict:
        _loc5_ = PackageDecoder(data)
        return {
            Keys.id: _loc5_.read_int(),
            Keys.wear: _loc5_.read_int(),
            Keys.bool1: _loc5_.read_bool(),
            Keys.bool2: _loc5_.read_bool(), }

    @_myLogger
    def toRepository(self, data) -> dict:
        _loc3_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.guid: _loc3_.read_bytes(),
            Keys.wear: _loc3_.read_int(), }

    @_myLogger
    def returnItem(self, data) -> dict:
        _loc3_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.guid: _loc3_.read_bytes(),
            Keys.wear: _loc3_.read_int(), }

    @_myLogger
    def toClanRepository(self, data) -> dict:
        _loc3_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.guid: _loc3_.read_bytes(),
            Keys.wear: _loc3_.read_int(), }

    @_myLogger
    def returnItemClan(self, data) -> dict:
        _loc3_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.guid: _loc3_.read_bytes(),
            Keys.wear: _loc3_.read_int(), }

    @_myLogger
    def loadClan(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {Keys.id_clan: _loc2_.read_int()}

    @_myLogger
    def clanLoad(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {Keys.id_clan: _loc2_.read_int()}

    @_myLogger
    def checkValue(self, data) -> dict:
        _loc3_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.id: _loc3_.read_int(),
            Keys.text: _loc3_.read_utf(), }

    @_myLogger
    def AcceptedClanInfo(self, data) -> dict:
        return {}
    
    @_myLogger
    def createClan(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {Keys.id: _loc2_.read_int()}

    @_myLogger
    def ClansLetters(self, data) -> dict:
        return {}
    
    @_myLogger
    def ClansList(self, data) -> dict:
        _loc3_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.text: _loc3_.read_utf(),
            Keys.id: _loc3_.read_int(), }

    @_myLogger
    def joinToClanRequest(self, data) -> dict:
        _loc3_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.id: _loc3_.read_int(),
            Keys.text: _loc3_.read_utf(), }

    @_myLogger
    def bodylessCommand(self, data) -> dict:
        return {}

    @_myLogger
    def guidValueCommand(self, data) -> dict:
        _loc3_: PackageDecoder = PackageDecoder(data)
        return {Keys.guid: _loc3_.read_bytes()}

    @_myLogger
    def tradeItemToSell(self, data) -> dict:
        _loc3_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.guid: _loc3_.read_bytes(),
            Keys.wear: _loc3_.read_short(), }

    @_myLogger
    def intValueCommand(self, data, command_type) -> dict:
        _loc3_: PackageDecoder = PackageDecoder(data)
        return {Keys.id: _loc3_.read_int()}

    @_myLogger
    def floatValueCommand(self, data) -> dict:
        _loc3_: PackageDecoder = PackageDecoder(data)
        return {Keys.float: _loc3_.read_float()}

    @_myLogger
    def boolValueCommand(self, data) -> dict:
        _loc3_: PackageDecoder = PackageDecoder(data)
        return {Keys.bool: _loc3_.read_bool()}

    @_myLogger
    def submitClanFriendRequests(self, data) -> dict:
        _loc4_ = PackageDecoder(data)
        data = {}
        for i in range(_loc4_.read_int()):
            data[f'id_{i}'] = _loc4_.read_int(),
            data[f'count_{i}'] = _loc4_.read_int(),
            
        for i in range(_loc4_.read_int()):
            data['i'] = _loc4_.read_int(),
            
        return data

    @_myLogger
    def createPilot(self, data) -> dict:
        _loc2_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.id: _loc2_.read_short(),
            Keys.authkey: _loc2_.read_utf(), }

    @_myLogger
    def saveClanJoinRequests(self, data) -> dict:
        _loc3_: PackageDecoder = PackageDecoder(data)
        data = {}
        i = 0
        while True:
            i += 1
            if len(_loc3_.data):
                data[f'id_{i}'] = _loc3_.read_int(),  # player_id)
                data[f'result_{i}'] = _loc3_.read_bytes(1),  # result)
            else:
                break
        return data
    
    @_myLogger
    def buyItemByBonuses(self, data) -> dict:
        _loc5_ = PackageDecoder(data)
        return {
            Keys.class_number: _loc5_.read_short(),
            Keys.wear: _loc5_.read_short(),  # 1000 количество
            Keys.id: _loc5_.read_int(),  # 255
            Keys.hz: _loc5_.read_short(), }  # 0

    @_myLogger
    def buyShipByBonuses(self, data) -> dict:
        _loc4_ = PackageDecoder(data)
        return {
            Keys.id_ship: _loc4_.read_short(),
            Keys.player_id: _loc4_.read_int(),
            Keys.hz3: _loc4_.read_short(), }  # 0

    @_myLogger
    def tradeInvitationResult(self, data) -> dict:
        _loc3_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.id: _loc3_.read_int(),
            Keys.bool: _loc3_.read_bool(), }

    @_myLogger
    def PlayerRole(self, data) -> dict:
        _loc3_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.id: _loc3_.read_int(),
            Keys.role: _loc3_.read_int(), }

    @_myLogger
    def renamePilot(self, data) -> dict:
        _loc3_: PackageDecoder = PackageDecoder(data)
        return {
            Keys.id: _loc3_.read_int(),
            Keys.role: _loc3_.read_utf(), }
