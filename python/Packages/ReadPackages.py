from ..Packages.PackagesManager import PackagesManager
from .PackageDecoder import PackageDecoder
from python.Static.Type.ClientRequest import ClientRequest
import os, pathlib
from loguru import logger

from ..Static.Type.ObjectToReachType import ObjectToReachType

if False:
    from python.Player.Player import Player


class ReadPackages:
    def __write_logger(self):
        path = pathlib.Path(__file__).parent.parent.joinpath('DataBase').joinpath("PlayerLog")
        if os.path.exists(path):
            os.chdir(path)
        else:
            os.mkdir(path)
            os.chdir(path)

        logger.add(f'Player_{self.id}.log', format="{time:YYYY-MM-DD HH:mm:ss.SSS}, {level}, {message}",
                   rotation="5 MB",
                   compression='zip', encoding='cp1251')  #

    def __init__(self, Game, Player: "Player", command_type, data):
        self.id = Player.id
        self.Game = Game
        self.Player = Player
        self.__write_logger()
        self.PacMan = PackagesManager(self.Player)

        match command_type:
            case ClientRequest.LOGIN:
                self.login(data)
            case ClientRequest.MOVE:
                self.move(data)
            case ClientRequest.LEAVE_LOCATION:
                self.leaveLocation(data)
            case ClientRequest.PLANET_REQUEST:
                self.planetRequest(data)
            case ClientRequest.SHIP_REQUEST:
                self.shipRequest(data)
            #     # case ClientRequest.ALREADY_LOGGED: # don't use
            #         return self.
            #     # case ClientRequest.SESSION_ID: # don't use
            #         return self.
            case ClientRequest.OBJECT_TO_REACH:
                self.objectToReach(data)
            case ClientRequest.OBJECT_EVIL:
                self.evil(data)
            case ClientRequest.USE_ITEM:
                self.useItem(data)
            case ClientRequest.UNUSE_ITEM:
                self.unuseItem(data)
            case ClientRequest.OPEN_SHOP:
                self.openShop(data)
            # case ClientRequest.FAILED: # use i don't find it
            #         return self.
            #
            #
            #     # case ClientRequest.LOCATION_CHANGED: # don't use
            #         return self.
            #
            #
            case ClientRequest.INVENTORY:
                self.inventory(data)
            case ClientRequest.HYPERJUMP:
                self.jumpTo(data)
            case ClientRequest.REACHABLE_SYSTEMS:
                self.reachableSystems(data)
            case ClientRequest.MESSAGE:
                self.sendMessage(data)
            case ClientRequest.REPAIR:
                self.repair(data)
            case ClientRequest.MAP:  # don't use
                print('sssssssssssss ERROR ')
            #     return self.bodylessCommand(data)
            case ClientRequest.REGISTER:
                self.registration(data)
            case ClientRequest.PLAYER_SKILLS:
                self.playerSkills(data)
            case ClientRequest.DEVICE_CLICKED:
                self.deviceClicked(data)
            case ClientRequest.DROID_CLICKED:
                self.droidClicked(data)
            case ClientRequest.RESTORE_ENERGY:
                self.restoreEnergy(data)
            case ClientRequest.USE_FREE_PARAMETERS:  # don't use
                print('sssssssssss ERROR')
            #     return self.
            case ClientRequest.DROID_COMMAND:
                self.droidCommand(data)
            case ClientRequest.BUY_SHIP:
                self.buyShip(data)
            case ClientRequest.SHOW_QUEST:
                self.showQuest(data)
            case ClientRequest.GET_QUEST:
                self.Quest(data)
            case ClientRequest.QUESTS_JOURNAL:
                self.questsJournal(data)
            case ClientRequest.PLANET_QUESTS:
                self.showPlanetQuests(data)
            case ClientRequest.TRAINING:
                self.training(data)
            case ClientRequest.ARENA_REQUESTS:
                self.arenaRequests(data)
            case ClientRequest.JOIN_TO_REQUEST:
                self.joinToRequest(data)
            case ClientRequest.BATTLE_REQUEST_WINDOW_CLOSED:
                self.battleRequestWindowClosed(data)
            case ClientRequest.READY_TO_BATTLE:
                self.readyToBattle(data)
            case ClientRequest.DROIDS_MODE:
                self.droidsMode(data)
            case ClientRequest.BUILD_DROID:
                self.buildDroid(data)
            case ClientRequest.SYNCRONIZE_HEALTH:
                self.syncronizeHealth(data)
            case ClientRequest.CREATE_ARENA_REQUEST:
                self.createArenaRequest(data)
            case ClientRequest.BUY_ITEM:
                self.buy_item(data)
            case ClientRequest.SELL_ITEM:
                self.sell_item(data)
            case ClientRequest.DROP_ITEM:
                self.dropItem(data)
            case ClientRequest.OBJECT_TO_ATTACK:
                self.ObjectToAttack(data)
            case ClientRequest.COMMIT_SKILLS:
                self.commitSkills(data)
            case ClientRequest.APPLY_GINETIC_LAB_OPTION:
                self.applyGineticLabOption(data)
            case ClientRequest.CREAR_TARGETS:
                self.crearTargets(data)
            case ClientRequest.SEND_CREDITS:
                self.sendCredits(data)
            case ClientRequest.TO_REPOSITORY:
                self.toRepository(data)
            case ClientRequest.RETURN_ITEM:
                self.returnItem(data)
            case ClientRequest.LOAD_CLAN:
                self.loadClan(data)
            case ClientRequest.CLAN_LOAD:
                self.clanLoad(data)
            case ClientRequest.CHECK_VALUE:
                self.checkValue(data)
            case ClientRequest.ACCEPTED_CLAN_INFO:
                self.AcceptedClanInfo(data)
            case ClientRequest.CREATE_CLAN:
                self.createClan(data)
            case ClientRequest.GET_CLANS_LETTERS:
                self.ClansLetters(data)
            case ClientRequest.GET_CLANS_LIST:
                self.ClansList(data)
            case ClientRequest.JOIN_TO_CLAN_REQUEST:
                self.joinToClanRequest(data)
            case ClientRequest.GET_CLAN_REQUESTS:
                self.bodylessCommand(data)
            case ClientRequest.PLAYER_INFO:
                self.intValueCommand(data, command_type)
            case ClientRequest.SAVE_CLAN_JOIN_REQUESTS:
                self.saveClanJoinRequests(data)
            case ClientRequest.JOIN_TO_CLAN:
                self.boolValueCommand(data)
            case ClientRequest.CANCEL_CLAN_CREATE_REQUEST:
                self.bodylessCommand(data)
            case ClientRequest.GET_FRIEND_CLANS:
                self.bodylessCommand(data)
            case ClientRequest.GET_ENEMY_CLANS:
                self.bodylessCommand(data)
            case ClientRequest.REMOVE_CLAN_RELATION:
                self.intValueCommand(data, command_type)
            case ClientRequest.ADD_CLAN_TO_ENEMIES:
                self.intValueCommand(data, command_type)
            case ClientRequest.ADD_CLAN_FRIEND_REQUEST:
                self.intValueCommand(data, command_type)
            case ClientRequest.GET_FRIEND_REQUESTS:
                self.bodylessCommand(data)
            case ClientRequest.SUBMIT_CLAN_FRIEND_REQUESTS:
                self.submitClanFriendRequests(data)
            case ClientRequest.MOVE_CLAN_TO_NEXT_LEVEL:
                self.bodylessCommand(data)
            case ClientRequest.REMOVE_PLAYER_FROM_CLAN:
                self.intValueCommand(data, command_type)
            case ClientRequest.GET_MISSIONS:
                self.bodylessCommand(data)
            case ClientRequest.CREATE_PILOT:
                self.createPilot(data)
            case ClientRequest.TO_GAME:
                self.intValueCommand(data, command_type)
            case ClientRequest.EXCHANGE_VOTES:
                self.intValueCommand(data, command_type)
            case ClientRequest.CHANGE_SHIP:
                self.intValueCommand(data, command_type)
            case ClientRequest.DELETE_PILOT:
                self.intValueCommand(data, command_type)
            case ClientRequest.CANCEL_DELETE_PILOT:
                self.intValueCommand(data, command_type)
            case ClientRequest.GET_MAP:
                self.bodylessCommand(data)
            case ClientRequest.LEAVE_CLAN:
                self.bodylessCommand(data)
            case ClientRequest.EXCHANGE_VOTES_TO_BONUSES:
                self.intValueCommand(data, command_type)
            case ClientRequest.BUY_ITEM_BY_BONUSES:
                self.buyItemByBonuses(data)
            case ClientRequest.TRADE_INVITATION:
                self.intValueCommand(data, command_type)
            case ClientRequest.TRADE_INVITATION_RESULT:
                self.tradeInvitationResult(data)
            case ClientRequest.TRADE_CASH:
                self.intValueCommand(data, command_type)
            case ClientRequest.TRADE_ITEM_TO_SELL:
                self.tradeItemToSell(data)
            case ClientRequest.TRADE_ITEM_TO_HOLD:
                self.guidValueCommand(data)
            case ClientRequest.TRADE_ACCEPTED:
                self.boolValueCommand(data)
            case ClientRequest.FINISH_TRADING_RESULT:
                self.boolValueCommand(data)
            case ClientRequest.TRADE_DENIED:
                self.bodylessCommand(data)
            case ClientRequest.UPDATE_HOLD:
                self.bodylessCommand(data)
            case ClientRequest.UPDATE_SHIP:
                self.bodylessCommand(data)
            case ClientRequest.LOST_ITEMS:
                self.bodylessCommand(data)
            case ClientRequest.CHANGE_LEADER:
                self.intValueCommand(data, command_type)
            case ClientRequest.UPDATE_RESOURCE:
                self.updateresource(data)
            case ClientRequest.CLAN_CREATE:
                self.clanCreate(data)
            case ClientRequest.TO_CLAN_REPOSITORY:
                self.toClanRepository(data)
            case ClientRequest.RETURN_ITEM_CLAN:
                self.returnItemClan(data)
            case ClientRequest.SET_PLAYER_ROLE:
                self.PlayerRole(data)
            case ClientRequest.SEND_BONUSES:
                self.sendBonuses(data)
            case ClientRequest.RENAME_PILOT:
                self.renamePilot(data)
            case ClientRequest.RESERV4:
                self.ClickedTime(data)
            case ClientRequest.REPAIR_ITEM:
                self.repairItem(data)
            case ClientRequest.GETAUCTION:
                self.Auction(data)
            case ClientRequest.GET_UPDATE_VALUE:
                self.intValueCommand(data, command_type)
            case ClientRequest.OBJECT_TO_TEAM:
                self.addObjectToTeam(data)
            case ClientRequest.REMOVE_PLAYER_FROM_TEAM:
                self.intValueCommand(data, command_type)
            case ClientRequest.SEND_BAN:
                self.sendBan(data)
            case ClientRequest.RESERV11:  # don't use
                print('ssssssss ERROR')
            #     return self.
            case ClientRequest.RESERV12:  # don't use
                print('sssssssss ERROR')
            #     return self.
            case ClientRequest.BUY_SHIP_BY_BONUSES:
                self.buyShipByBonuses(data)
            case _:
                print('Error unknow Packages')

    def droidCommand(self, data) -> None:
        _loc5_ = PackageDecoder()
        _loc5_.data = data
        data = {
            'hz': _loc5_.read_bytes(16),  # 16 или 1
            'type_command': _loc5_.read_int(),
            'hz3': _loc5_.read_int(),
            'hz4': _loc5_.read_int(),
        }
        logger.info(f'droidCommand {data}')
        if data['type_command'] == 4:
            self.Player.unuse_droid_all()

    def login(self, data):
        _loc5_ = PackageDecoder()
        _loc5_.data = data
        data = {
            'id': _loc5_.read_utf(),  # Vk_user_id
            "_": _loc5_.read_utf(),  # don't use
            'AuthKey': _loc5_.read_utf(),  # Vk_auth_key
            'Domain': _loc5_.read_utf()}  # domain
        logger.critical(f'login {data}')

    def registration(self, data) -> None:
        _loc5_ = PackageDecoder()
        _loc5_.data = data
        data = {
            'id': _loc5_.read_utf(),  # Vk_user_id
            "_": _loc5_.read_utf(),  # don't use
            'AuthKey': _loc5_.read_utf(),  # Vk_auth_key
            'Domain': _loc5_.read_utf()}  # domain
        logger.critical(f'registration {data}')

    def move(self, data) -> None:
        _loc4_ = PackageDecoder()
        _loc4_.data = data

        x = _loc4_.read_float()  # x
        y = _loc4_.read_float()  # y
        _ = _loc4_.read_int()  # count
        logger.info(f'move {x}, {y}')
        self.Player.move(x, y)

    def leaveLocation(self, data):
        logger.info(f'leaveLocation')
        self.Player.leaveLocation()

    def evil(self, data) -> None:
        oWriter = PackageDecoder()
        oWriter.data = data
        info = oWriter.read_utf()
        logger.info(f'evil {info}')

    def planetRequest(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        id_ = _loc2_.read_int()
        logger.info(f'Planet request {id_}')

    def shipRequest(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        id_ = _loc2_.read_int()
        logger.info(f'Planet request', id_)

    def addObjectToTeam(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            'ObjectToReachType': _loc2_.read_int(),
            'id': _loc2_.read_int()}
        logger.info(f'addObjectToTeam {data}')

    def ObjectToAttack(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            'type': _loc2_.read_int(),  # ObjectToReachType
            'id': _loc2_.read_int(), }  # id
        logger.info(data)
        self.Player.attack(data)

    def objectToReach(self, data):
        _loc4_ = PackageDecoder()
        _loc4_.data = data
        data = {
            'type': _loc4_.read_int(),
            'id': _loc4_.read_int(),
            'aliance': _loc4_.read_int()
        }
        _loc4_.read_int()  # count
        logger.info(f'objectToReach {data}')
        self.Player.set_object_to_reach(data)

    def useItem(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            'guid': _loc2_.read_bytes(16), }
        self.Player.use_item(data)
        logger.info(f'useItem {data}')

    def unuseItem(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            'guid': _loc2_.read_bytes(16), }
        self.Player.unuse_item(data)
        logger.info(f'unuseItem {data}')

    def buy_item(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            'guid': _loc2_.read_bytes(16),
            'wear': _loc2_.read_int(), }
        logger.info(f'buy_item {data}')
        self.Player.buy_item(data)

    def sell_item(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            'guid': _loc2_.read_bytes(16),
            'wear': _loc2_.read_int(), }
        logger.info(f'sell_item {data}')
        self.Player.sell_item(data)

    def updateresource(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            'guid': _loc2_.read_bytes(16),
            'count': _loc2_.read_int(), }
        logger.info(f'updateresource {data}')

    def clanCreate(self, data) -> None:
        _loc4_ = PackageDecoder()
        _loc4_.data = data
        data = {
            'name': _loc4_.read_utf(),
            'description': _loc4_.read_utf(),
            'name_short': _loc4_.read_utf(), }
        logger.info(f'clanCreate {data}')

    def dropItem(self, data, ) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            'guid': _loc2_.read_bytes(16),
            'count': _loc2_.read_int(), }
        self.Player.drop_item(data)
        logger.info(f'dropItem {data}')

    def repairItem(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            'guid': _loc2_.read_bytes(),
            'count': _loc2_.read_int(), }
        logger.info(f'repairItem {data}')

    def openShop(self, data, ) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            "type": _loc2_.read_int()}
        logger.info(f'openShop {data}')
        self.Player.OpenShop(data)

    def inventory(self, data) -> None:
        _loc1_ = PackageDecoder()
        _loc1_.data = data
        data = {
            _loc1_.read_utf(), }  # domain ?!
        self.PacMan.inventory()
        logger.info(f'inventory {data}')

    def reachableSystems(self, data) -> None:
        _loc1_: PackageDecoder = PackageDecoder()
        _loc1_.data = data
        data = {}
        logger.info(f'reachableSystems {data}')

    def jumpTo(self, data) -> None:
        _loc4_ = PackageDecoder()
        _loc4_.data = data
        data = {
            "id": _loc4_.read_int()}  # id Location
        logger.info(f'jumpTo {data}')
        _loc4_.read_int()  # clicked count
        _loc4_.read_utf()  # domain
        self.Player.hyper_jump(data["id"])

    def sendMessage(self, data) -> None:
        _loc4_: PackageDecoder
        _loc4_ = PackageDecoder()
        _loc4_.data = data
        data = {
            'private_id': _loc4_.read_int(),
            'text': _loc4_.read_utf(),
            'type_chat': _loc4_.read_unsigned_byte(), }  # 1 - global  2 - local 3 - clanId 4 - trade 5 - client chat
        logger.info(f'sendMessage {data}')
        self.Game.Chat.send_message(self.Player, data)


    def sendBan(self, data) -> None:
        _loc4_: PackageDecoder
        _loc4_ = PackageDecoder()
        _loc4_.data = data
        data = {
            'text1': _loc4_.read_utf(),
            'text2': _loc4_.read_utf(),
            'bool': _loc4_.read_bytes(), }
        logger.info(f'sendBan {data}')

    def repair(self, data):
        logger.info(f'repair {data}')
        self.Player.repair()
        self.Player.PacMan.shipHealth()

    def Auction(self, data) -> None:
        _loc1_: PackageDecoder = PackageDecoder()
        _loc1_.data = data
        data = {}
        logger.info(f'Auction {data}')

    def restoreEnergy(self, data):
        logger.info(f'restoreEnergy {data}')
        # getattr(self.Game, f'Player_{self.id}').restoreEnergy()
        # PackagesManager(self.id, self.Game).()

    def playerSkills(self, data):
        self.PacMan.playerSkills()
        logger.info(f'playerSkills {data}')

    def ClickedTime(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            'hz': _loc2_.read_int()}
        logger.info(f'ClickedTime {data}')

    def deviceClicked(self, data) -> None:
        _loc5_ = PackageDecoder()
        _loc5_.data = data
        data = {
            'guid': _loc5_.read_bytes(),
            'targetId': _loc5_.read_int(),  # id цели если 0 то исползуется сам на себя
            'id_droid': _loc5_.read_unsigned_byte(),  # id использовавшего
            'effectType': _loc5_.read_unsigned_byte(), }
        logger.info(f'deviceClicked {data}')
        self.Player.device_clicked(data)

    def droidClicked(self, data) -> None:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = {
            'hz1': _loc3_.read_bytes(),
            'guid': _loc3_.read_bytes(), }
        self.Player.use_item(data)
        logger.info(f'droidClicked {data}')

    def buyShip(self, data) -> None:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = {
            'guid': _loc3_.read_bytes(),
            'Yes or No': _loc3_.read_bool(), }
        logger.info(f'buyShip {data}')

    def showQuest(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            'id': _loc2_.read_int(), }
        logger.info(f'showQuest {data}')

    def Quest(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            'id': _loc2_.read_int(), }  # id quest
        logger.info(f'Quest {data}')

    def questsJournal(self, data) -> None:
        logger.info(f'questsJournal {data}')

    def showPlanetQuests(self, data) -> None:
        logger.info(f'showPlanetQuests {data}')

    def training(self, data) -> None:
        _loc7_ = PackageDecoder()
        _loc7_.data = data
        data = {
            'hz1': _loc7_.read_int(),
            'hz2': _loc7_.read_int(),
            'hz3': _loc7_.read_int(),
            'hz4': _loc7_.read_int(),
            'hz5': _loc7_.read_int(),
            'hz6': _loc7_.read_int(), }
        logger.info(f'training {data}')

    def arenaRequests(self, data) -> None:
        logger.info(f'arenaRequests {data}')

    def joinToRequest(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            'id': _loc2_.read_int(), }
        logger.info(f'joinToRequest {data}')

    def battleRequestWindowClosed(self, data) -> None:
        logger.info(f'battleRequestWindowClosed {data}')

    def readyToBattle(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            'id': _loc2_.read_int(), }
        logger.info(f'readyToBattle {data}')

    def droidsMode(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            'id': _loc2_.read_int(), }
        logger.info(f'droidsMode {data}')

    def buildDroid(self, data) -> None:
        logger.info(f'buildDroid {data}')
        self.Player.PacMan.droidBuildingDialog(self)

    def crearTargets(self, data) -> None:  # убрать дройдов всех
        logger.info(f'crearTargets {data}')
        self.Player.move(stop=True)

    def syncronizeHealth(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            'id': _loc2_.read_int(), }
        logger.info(f'syncronizeHealth {data}')

    def createArenaRequest(self, data) -> None:
        _loc4_ = PackageDecoder()
        _loc4_.data = data
        data = {
            'type': _loc4_.read_unsigned_byte(),  # read_bytes()
            'id': _loc4_.read_int(),
            'yes_or_no': _loc4_.read_bool(), }
        logger.info(f'createArenaRequest {data}')

    def commitSkills(self, data):
        decoder: PackageDecoder = PackageDecoder()
        decoder.data = data
        data = {}
        while len(decoder.data) > decoder.Position:
            self.read_skill(data, decoder)
        logger.info(f'commitSkills {data}')
        self.Player.commitSkills(data)
        self.PacMan.playerSkills()
        logger.info(f'commitSkills {data}')

    def read_skill(self, data, decoder):
        from ..Static.TypeStr.PlayerSkillTypeStr import PlayerSkillTypeStr
        type_ = decoder.read_unsigned_byte()
        count = decoder.read_unsigned_byte()
        data[PlayerSkillTypeStr().get_str(type_)] = count  # player skill type

    def applyGineticLabOption(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            'id': _loc2_.read_int(), }
        logger.info(f'applyGineticLabOption {data}')
        self.Player.reset_skills()

    def sendCredits(self, data) -> None:
        _loc5_ = PackageDecoder()
        _loc5_.data = data
        data = {
            'id': _loc5_.read_int(),  # id
            'count': _loc5_.read_int(),  # count credits
            'bool1': _loc5_.read_bool(),
            'bool2': _loc5_.read_bool(), }
        logger.info(f'sendCredits {data}')

    def sendBonuses(self, data) -> None:
        _loc5_ = PackageDecoder()
        _loc5_.data = data
        data = {
            'id': _loc5_.read_int(),
            'count': _loc5_.read_int(),
            'bool1': _loc5_.read_bool(),
            'bool2': _loc5_.read_bool(), }
        logger.info(f'sendBonuses {data}')

    def toRepository(self, data) -> None:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = {
            'guid': _loc3_.read_bytes(),
            'count': _loc3_.read_int(), }
        logger.info(f'toRepository {data}')

    def returnItem(self, data) -> None:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = {
            'guid': _loc3_.read_bytes(),
            'count': _loc3_.read_int(), }
        logger.info(f'returnItem {data}')

    def toClanRepository(self, data) -> None:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = {
            'guid': _loc3_.read_bytes(),
            'count': _loc3_.read_int(), }
        logger.info(f'toClanRepository {data}')

    def returnItemClan(self, data) -> None:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = {
            'guid': _loc3_.read_bytes(),
            'count': _loc3_.read_int(), }
        logger.info(f'returnItemClan {data}')

    def loadClan(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            'id_clan': _loc2_.read_int(), }
        logger.info(f'loadClan {data}')

    def clanLoad(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            'id_clan': _loc2_.read_int(), }
        logger.info(f'clanLoad {data}')

    def checkValue(self, data) -> None:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = {
            'id': _loc3_.read_int(),
            'text?': _loc3_.read_utf(), }
        logger.info(f'checkValue {data}')

    def AcceptedClanInfo(self, data) -> None:
        logger.info(f'AcceptedClanInfo {data}')

    def createClan(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            'id': _loc2_.read_int(), }
        logger.info(f'createClan {data}')

    def ClansLetters(self, data) -> None:
        logger.info(f'ClansLetters {data}')

    def ClansList(self, data) -> None:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = {
            'text': _loc3_.read_utf(),
            'id': _loc3_.read_int(), }
        logger.info(f'ClansList {data}')

    def joinToClanRequest(self, data) -> None:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = {
            'id': _loc3_.read_int(),
            'text?': _loc3_.read_utf(), }
        logger.info(f'joinToClanRequest {data}')

    def bodylessCommand(self, data) -> None:
        logger.info(f'bodylessCommand {data}')

    def guidValueCommand(self, data) -> None:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = {
            'guid': _loc3_.read_bytes(), }
        logger.info(f'guidValueCommand {data}')

    def tradeItemToSell(self, data) -> None:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = {
            'guid': _loc3_.read_bytes(),
            'count?': _loc3_.read_short(), }
        logger.info(f'tradeItemToSell {data}')

    def intValueCommand(self, data, command_type) -> None:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = {
            'id': _loc3_.read_int(), }
        logger.info(f'intValueCommand {data}')
        match command_type:
            case ClientRequest.PLAYER_INFO:
                self.Player.PacMan.playerInfo(data['id'])
            # case ClientRequest.REMOVE_CLAN_RELATION:
            #     self.Player.
            # case ClientRequest.ADD_CLAN_TO_ENEMIES:
            #     self.Player.
            # case ClientRequest.ADD_CLAN_FRIEND_REQUEST:
            #     self.Player.
            # case ClientRequest.REMOVE_PLAYER_FROM_CLAN:
            #     self.Player.
            case ClientRequest.TO_GAME:
                self.Player.PacMan.toGame()
            # case ClientRequest.EXCHANGE_VOTES:
            #     self.Player.
            case ClientRequest.CHANGE_SHIP:
                self.Player.change_ship(data['id'])
            # case ClientRequest.DELETE_PILOT:
            #     self.Player.
            # case ClientRequest.CANCEL_DELETE_PILOT:
            #     self.Player.
            # case ClientRequest.EXCHANGE_VOTES_TO_BONUSES:
            #     self.Player.
            # case ClientRequest.TRADE_INVITATION:
            #     self.Player.
            # case ClientRequest.TRADE_CASH:
            #     self.Player.
            # case ClientRequest.CHANGE_LEADER:
            #     self.Player.
            # case ClientRequest.GET_UPDATE_VALUE:
            #     self.Player.
            # case ClientRequest.REMOVE_PLAYER_FROM_TEAM:
            #     self.Player.

    def floatValueCommand(self, data) -> None:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = {
            'float': _loc3_.read_float(), }
        logger.info(f'floatValueCommand {data}')

    def boolValueCommand(self, data) -> None:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = {
            'bool': _loc3_.read_bool(), }
        logger.info(f'boolValueCommand {data}')

    def submitClanFriendRequests(self, data) -> None:
        _loc4_ = PackageDecoder()
        _loc4_.data = data
        data = {}
        for i in range(_loc4_.read_int()):
            data[f'id_{i}'] = _loc4_.read_int(),
            data[f'count_{i}'] = _loc4_.read_int(),

        for i in range(_loc4_.read_int()):
            data['i'] = _loc4_.read_int(),
        logger.info(f'submitClanFriendRequests {data}')

    def createPilot(self, data) -> None:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {
            'id?': _loc2_.read_short(),
            'authKey': _loc2_.read_utf(), }
        logger.info(f'createPilot {data}')

    def saveClanJoinRequests(self, data) -> None:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = {}
        i = 0
        while True:
            i += 1
            if len(_loc3_.data):
                data[f'id_{i}'] = _loc3_.read_int(),  # playerID)
                data[f'result_{i}'] = _loc3_.read_bytes(1),  # result)
            else:
                break
        logger.info(f'saveClanJoinRequests {data}')

    def buyItemByBonuses(self, data) -> None:
        _loc5_ = PackageDecoder()
        _loc5_.data = data
        data = {
            'classNumber': _loc5_.read_short(),
            'wear': _loc5_.read_short(),  # 1000 количество
            'id': _loc5_.read_int(),  # 255
            'hz': _loc5_.read_short(), }  # 0
        logger.info(f'buyItemByBonuses {data}')

        self.Player.buyItemByBonuses(data)
        self.PacMan.inventory()
        self.PacMan.updateValue(13)

    def buyShipByBonuses(self, data) -> None:
        _loc4_ = PackageDecoder()
        _loc4_.data = data
        data = {
            'id_ship': _loc4_.read_short(),
            'player_id': _loc4_.read_int(),
            'hz3': _loc4_.read_short(), }  # 0
        logger.info(f'buyShipByBonuses {data}')
        self.Player.buyShip(data)

    def tradeInvitationResult(self, data) -> None:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = {
            'id': _loc3_.read_int(),
            'bool': _loc3_.read_bool(), }
        logger.info(f'tradeInvitationResult {data}')

    def PlayerRole(self, data) -> None:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = {
            'id': _loc3_.read_int(),
            'role': _loc3_.read_int(), }
        logger.info(f'PlayerRole {data}')

    def renamePilot(self, data) -> None:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = {
            'id': _loc3_.read_int(),
            'role': _loc3_.read_utf(), }
        logger.info(f'renamePilot {data}')
