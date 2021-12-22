from .PackageDecoder import PackageDecoder
from python.Static.Type.ClientRequest import ClientRequest


class ReadPackages:
    IocaI: str = "LOCAL_TRUSTED"
    Domain: str = "serverstarwars.com"

    def __init__(self, Game, id_):
        self.id = id_
        self.Game = Game

    def main(self, command_type: int, *args):
        match command_type:
            case ClientRequest.LOGIN:
                return self.login(*args)
            case ClientRequest.MOVE:
                return self.move(*args)
            case ClientRequest.LEAVE_LOCATION:
                return self.leaveLocation(*args)
            case ClientRequest.PLANET_REQUEST:
                return self.planetRequest(*args)
            case ClientRequest.SHIP_REQUEST:
                return self.shipRequest(*args)
            # case ClientRequest.ALREADY_LOGGED: # don't use
            #     return self.
            # case ClientRequest.SESSION_ID: # don't use
            #     return self.
            case ClientRequest.OBJECT_TO_REACH:
                return self.objectToReach(*args)
            case ClientRequest.OBJECT_EVIL:
                return self.evil(*args)
            case ClientRequest.USE_ITEM:
                return self.useItem(*args)
            case ClientRequest.UNUSE_ITEM:
                return self.unuseItem(*args)
            case ClientRequest.OPEN_SHOP:
                return self.openShop(*args)
            # case ClientRequest.FAILED: # use i don't find it
            #     return self.
            # case ClientRequest.LOCATION_CHANGED: # don't use
            #     return self.
            case ClientRequest.INVENTORY:
                return self.inventory(*args)
            case ClientRequest.HYPERJUMP:
                return self.jumpTo(*args)
            case ClientRequest.REACHABLE_SYSTEMS:
                return self.reachableSystems(*args)
            case ClientRequest.MESSAGE:
                return self.sendMessage(*args)
            case ClientRequest.REPAIR:
                return self.repair(*args)
            case ClientRequest.MAP:  # don't use
                print('sssssssssssss ERROR ')
            #     return self.bodylessCommand(*args)
            case ClientRequest.REGISTER:
                return self.registration(*args)
            case ClientRequest.PLAYER_SKILLS:
                return self.playerSkills(*args)
            case ClientRequest.DEVICE_CLICKED:
                return self.deviceClicked(*args)
            case ClientRequest.DROID_CLICKED:
                return self.droidClicked(*args)
            case ClientRequest.RESTORE_ENERGY:
                return self.restoreEnergy(*args)
            case ClientRequest.USE_FREE_PARAMETERS:  # don't use
                print('sssssssssss ERROR')
            #     return self.
            case ClientRequest.DROID_COMMAND:
                return self.droidCommand(*args)
            case ClientRequest.BUY_SHIP:
                return self.buyShip(*args)
            case ClientRequest.SHOW_QUEST:
                return self.showQuest(*args)
            case ClientRequest.GET_QUEST:
                return self.Quest(*args)
            case ClientRequest.QUESTS_JOURNAL:
                return self.questsJournal(*args)
            case ClientRequest.PLANET_QUESTS:
                return self.showPlanetQuests(*args)
            case ClientRequest.TRAINING:
                return self.training(*args)
            case ClientRequest.ARENA_REQUESTS:
                return self.arenaRequests(*args)
            case ClientRequest.JOIN_TO_REQUEST:
                return self.joinToRequest(*args)
            case ClientRequest.BATTLE_REQUEST_WINDOW_CLOSED:
                return self.battleRequestWindowClosed(*args)
            case ClientRequest.READY_TO_BATTLE:
                return self.readyToBattle(*args)
            case ClientRequest.DROIDS_MODE:
                return self.droidsMode(*args)
            case ClientRequest.BUILD_DROID:
                return self.buildDroid(*args)
            case ClientRequest.SYNCRONIZE_HEALTH:
                return self.syncronizeHealth(*args)
            case ClientRequest.CREATE_ARENA_REQUEST:
                return self.createArenaRequest(*args)
            case ClientRequest.BUY_ITEM:
                return self.buyItem(*args)
            case ClientRequest.SELL_ITEM:
                return self.sellItem(*args)
            case ClientRequest.DROP_ITEM:
                return self.dropItem(*args)
            case ClientRequest.OBJECT_TO_ATTACK:
                return self.ObjectToAttack(*args)
            case ClientRequest.COMMIT_SKILLS:
                return self.commitSkills(*args)
            case ClientRequest.APPLY_GINETIC_LAB_OPTION:
                return self.applyGineticLabOption(*args)
            case ClientRequest.CREAR_TARGETS:
                return self.crearTargets(*args)
            case ClientRequest.SEND_CREDITS:
                return self.sendCredits(*args)
            case ClientRequest.TO_REPOSITORY:
                return self.toRepository(*args)
            case ClientRequest.RETURN_ITEM:
                return self.returnItem(*args)
            case ClientRequest.LOAD_CLAN:
                return self.loadClan(*args)
            case ClientRequest.CLAN_LOAD:
                return self.clanLoad(*args)
            case ClientRequest.CHECK_VALUE:
                return self.checkValue(*args)
            case ClientRequest.ACCEPTED_CLAN_INFO:
                return self.AcceptedClanInfo(*args)
            case ClientRequest.CREATE_CLAN:
                return self.createClan(*args)
            case ClientRequest.GET_CLANS_LETTERS:
                return self.ClansLetters(*args)
            case ClientRequest.GET_CLANS_LIST:
                return self.ClansList(*args)
            case ClientRequest.JOIN_TO_CLAN_REQUEST:
                return self.joinToClanRequest(*args)
            case ClientRequest.GET_CLAN_REQUESTS:
                return self.bodylessCommand(*args)
            case ClientRequest.PLAYER_INFO:
                return self.intValueCommand(*args)
            case ClientRequest.SAVE_CLAN_JOIN_REQUESTS:
                return self.saveClanJoinRequests(*args)
            case ClientRequest.JOIN_TO_CLAN:
                return self.boolValueCommand(*args)
            case ClientRequest.CANCEL_CLAN_CREATE_REQUEST:
                return self.bodylessCommand(*args)
            case ClientRequest.GET_FRIEND_CLANS:
                return self.bodylessCommand(*args)
            case ClientRequest.GET_ENEMY_CLANS:
                return self.bodylessCommand(*args)
            case ClientRequest.REMOVE_CLAN_RELATION:
                return self.intValueCommand(*args)
            case ClientRequest.ADD_CLAN_TO_ENEMIES:
                return self.intValueCommand(*args)
            case ClientRequest.ADD_CLAN_FRIEND_REQUEST:
                return self.intValueCommand(*args)
            case ClientRequest.GET_FRIEND_REQUESTS:
                return self.bodylessCommand(*args)
            case ClientRequest.SUBMIT_CLAN_FRIEND_REQUESTS:
                return self.submitClanFriendRequests(*args)
            case ClientRequest.MOVE_CLAN_TO_NEXT_LEVEL:
                return self.bodylessCommand(*args)
            case ClientRequest.REMOVE_PLAYER_FROM_CLAN:
                return self.intValueCommand(*args)
            case ClientRequest.GET_MISSIONS:
                return self.bodylessCommand(*args)
            case ClientRequest.CREATE_PILOT:
                return self.createPilot(*args)
            case ClientRequest.TO_GAME:
                return self.intValueCommand(*args)
            case ClientRequest.EXCHANGE_VOTES:
                return self.intValueCommand(*args)
            case ClientRequest.CHANGE_SHIP:
                return self.intValueCommand(*args)
            case ClientRequest.DELETE_PILOT:
                return self.intValueCommand(*args)
            case ClientRequest.CANCEL_DELETE_PILOT:
                return self.intValueCommand(*args)
            case ClientRequest.GET_MAP:
                return self.bodylessCommand(*args)
            case ClientRequest.LEAVE_CLAN:
                return self.bodylessCommand(*args)
            case ClientRequest.EXCHANGE_VOTES_TO_BONUSES:
                return self.intValueCommand(*args)
            case ClientRequest.BUY_ITEM_BY_BONUSES:
                return self.buyItemByBonuses(*args)
            case ClientRequest.TRADE_INVITATION:
                return self.intValueCommand(*args)
            case ClientRequest.TRADE_INVITATION_RESULT:
                return self.tradeInvitationResult(*args)
            case ClientRequest.TRADE_CASH:
                return self.intValueCommand(*args)
            case ClientRequest.TRADE_ITEM_TO_SELL:
                return self.tradeItemToSell(*args)
            case ClientRequest.TRADE_ITEM_TO_HOLD:
                return self.guidValueCommand(*args)
            case ClientRequest.TRADE_ACCEPTED:
                return self.boolValueCommand(*args)
            case ClientRequest.FINISH_TRADING_RESULT:
                return self.boolValueCommand(*args)
            case ClientRequest.TRADE_DENIED:
                return self.bodylessCommand(*args)
            case ClientRequest.UPDATE_HOLD:
                return self.bodylessCommand(*args)
            case ClientRequest.UPDATE_SHIP:
                return self.bodylessCommand(*args)
            case ClientRequest.LOST_ITEMS:
                return self.bodylessCommand(*args)
            case ClientRequest.CHANGE_LEADER:
                return self.intValueCommand(*args)
            case ClientRequest.UPDATE_RESOURCE:
                return self.updateresource(*args)
            case ClientRequest.CLAN_CREATE:
                return self.clanCreate(*args)
            case ClientRequest.TO_CLAN_REPOSITORY:
                return self.toClanRepository(*args)
            case ClientRequest.RETURN_ITEM_CLAN:
                return self.returnItemClan(*args)
            case ClientRequest.SET_PLAYER_ROLE:
                return self.PlayerRole(*args)
            case ClientRequest.SEND_BONUSES:
                return self.sendBonuses(*args)
            case ClientRequest.RENAME_PILOT:
                return self.renamePilot(*args)
            case ClientRequest.RESERV4:
                return self.ClickedTime(*args)
            case ClientRequest.REPAIR_ITEM:
                return self.repairItem(*args)
            case ClientRequest.GETAUCTION:
                return self.Auction(*args)
            case ClientRequest.GET_UPDATE_VALUE:
                return self.intValueCommand(*args)
            case ClientRequest.OBJECT_TO_TEAM:
                return self.addObjectToTeam(*args)
            case ClientRequest.REMOVE_PLAYER_FROM_TEAM:
                return self.intValueCommand(*args)
            case ClientRequest.SEND_BAN:
                return self.sendBan(*args)
            case ClientRequest.RESERV11:  # don't use
                print('ssssssss ERROR')
            #     return self.
            case ClientRequest.RESERV12:  # don't use
                print('sssssssss ERROR')
            #     return self.
            case ClientRequest.BUY_SHIP_BY_BONUSES:
                return self.buyShipByBonuses(*args)
            case _:
                return print('Error unknow Packages')

    def droidCommand(self, data) -> list:
        _loc5_ = PackageDecoder()
        _loc5_.data = data
        data = []
        data.append(_loc5_.read_bytes(16))  # 16 или 1
        data.append(_loc5_.read_int())
        data.append(_loc5_.read_int())
        data.append(_loc5_.read_int())
        return data

    def login(self, data) -> list:
        _loc5_ = PackageDecoder()
        _loc5_.data = data
        data = []
        data.append(_loc5_.read_utf())  # Vk_user_id
        data.append(_loc5_.read_utf())  # don't use
        data.append(_loc5_.read_utf())  # Vk_auth_key
        data.append(_loc5_.read_utf())  # domain
        return data

    def registration(self, data) -> list:
        _loc5_ = PackageDecoder()
        _loc5_.data = data
        data = []
        data.append(_loc5_.read_utf())
        data.append(_loc5_.read_utf())
        data.append(_loc5_.read_utf())
        data.append(_loc5_.read_int())
        return data

    def move(self, data) -> list:
        _loc4_ = PackageDecoder()
        _loc4_.data = data
        data = []
        data.append(_loc4_.read_float())  # x
        data.append(_loc4_.read_float())  # y
        data.append(_loc4_.read_int())  # count
        return data

    def leaveLocation(self, data) -> list:
        _loc1_: PackageDecoder = PackageDecoder()
        _loc1_.data = data
        data = []
        return data

    def evil(self, data) -> list:
        oWriter = PackageDecoder()
        oWriter.data = data
        data = []
        data.append(oWriter.read_utf())
        return data

    def planetRequest(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_int())
        return data

    def shipRequest(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_int())
        return data

    def addObjectToTeam(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_int())  # ObjectToReachType
        data.append(_loc2_.read_int())  # id
        return data

    def ObjectToAttack(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_int())  # ObjectToReachType
        data.append(_loc2_.read_int())  # id
        return data

    def objectToReach(self, data) -> list:
        _loc4_ = PackageDecoder()
        _loc4_.data = data
        data = []
        data.append(_loc4_.read_int())  # ObjectToReachType
        data.append(_loc4_.read_int())  # id
        data.append(_loc4_.read_int())  # AlianceType ?
        data.append(_loc4_.read_int())  # count
        return data

    def useItem(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_bytes(16))
        return data

    def unuseItem(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_bytes(16))
        return data

    def buyItem(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_bytes(16))
        data.append(_loc2_.read_int())
        return data

    def sellItem(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_bytes(16))
        data.append(_loc2_.read_int())
        return data

    def updateresource(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_bytes(16))
        data.append(_loc2_.read_int())
        return data

    def clanCreate(self, data) -> list:
        _loc4_ = PackageDecoder()
        _loc4_.data = data
        data = []
        data.append(_loc4_.read_utf())
        data.append(_loc4_.read_utf())
        data.append(_loc4_.read_utf())
        return data

    def dropItem(self, data, ) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_bytes(16))
        data.append(_loc2_.read_int())
        return data

    def repairItem(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_bytes())
        data.append(_loc2_.read_int())
        return data

    def openShop(self, data, ) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_int())
        return data

    def inventory(self, data) -> list:
        _loc1_ = PackageDecoder()
        _loc1_.data = data
        data = []
        data.append(_loc1_.read_utf())  # domain ?!
        return data

    def reachableSystems(self, data) -> list:
        _loc1_: PackageDecoder = PackageDecoder()
        _loc1_.data = data
        data = []
        return data

    def jumpTo(self, data) -> list:
        _loc4_ = PackageDecoder()
        _loc4_.data = data
        data = []
        data.append(_loc4_.read_int())  # id location
        data.append(_loc4_.read_int())  # clicked count
        data.append(_loc4_.read_utf())  # domain
        return data

    def sendMessage(self, data) -> list:
        _loc4_: PackageDecoder
        _loc4_ = PackageDecoder()
        _loc4_.data = data
        data = []
        data.append(_loc4_.read_int())
        data.append(_loc4_.read_utf())
        data.append(_loc4_.read_bytes())
        return data

    def sendBan(self, data) -> list:
        _loc4_: PackageDecoder
        _loc4_ = PackageDecoder()
        _loc4_.data = data
        data = []
        data.append(_loc4_.read_utf())
        data.append(_loc4_.read_utf())
        data.append(_loc4_.read_bytes())
        return data

    def repair(self, data) -> list:
        _loc1_: PackageDecoder = PackageDecoder()
        _loc1_.data = data
        data = []
        return data

    def Auction(self, data) -> list:
        _loc1_: PackageDecoder = PackageDecoder()
        _loc1_.data = data
        data = []
        return data

    def restoreEnergy(self, data) -> list:
        _loc1_: PackageDecoder = PackageDecoder()
        _loc1_.data = data
        data = []
        return data

    def playerSkills(self, data) -> list:
        _loc1_: PackageDecoder = PackageDecoder()
        _loc1_.data = data
        data = []
        return data

    def ClickedTime(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        _loc2_.read_int()
        return data

    def deviceClicked(self, data) -> list:
        _loc5_ = PackageDecoder()
        _loc5_.data = data
        data = []
        data.append(_loc5_.read_bytes())
        data.append(_loc5_.read_int())  # id цели если 0 то не выбрана цель
        data.append(_loc5_.read_unsigned_byte())  # id использовавшего
        data.append(_loc5_.read_unsigned_byte())  # effect type
        return data

    def droidClicked(self, data) -> list:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = []
        data.append(_loc3_.read_bytes())
        data.append(_loc3_.read_bytes())
        return data

    def buyShip(self, data) -> list:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = []
        data.append(_loc3_.read_bytes())
        data.append(_loc3_.read_bool())
        return data

    def showQuest(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_int())
        return data

    def Quest(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_int())  # id quest
        return data

    def questsJournal(self, data) -> list:
        _loc1_: PackageDecoder = PackageDecoder()
        _loc1_.data = data
        data = []
        return data

    def showPlanetQuests(self, data) -> list:
        _loc1_: PackageDecoder = PackageDecoder()
        _loc1_.data = data
        data = []
        return data

    def training(self, data) -> list:
        _loc7_ = PackageDecoder()
        _loc7_.data = data
        data = []
        data.append(_loc7_.read_int())
        data.append(_loc7_.read_int())
        data.append(_loc7_.read_int())
        data.append(_loc7_.read_int())
        data.append(_loc7_.read_int())
        data.append(_loc7_.read_int())
        return data

    def arenaRequests(self, data) -> list:
        _loc1_: PackageDecoder = PackageDecoder()
        _loc1_.data = data
        data = []
        return data

    def joinToRequest(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_int())
        return data

    def battleRequestWindowClosed(self, data) -> list:
        _loc1_: PackageDecoder = PackageDecoder()
        _loc1_.data = data
        data = []
        return data

    def readyToBattle(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_int())
        return data

    def droidsMode(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_int())
        return data

    def buildDroid(self, data) -> list:
        _loc1_: PackageDecoder = PackageDecoder()
        _loc1_.data = data
        data = []
        return data

    def crearTargets(self, data) -> list:  # убрать дройдов всех
        _loc1_: PackageDecoder = PackageDecoder()
        _loc1_.data = data
        data = []
        return data

    def syncronizeHealth(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_int())
        return data

    def createArenaRequest(self, data) -> list:
        _loc4_ = PackageDecoder()
        _loc4_.data = data
        data = []
        data.append(_loc4_.read_bytes())
        data.append(_loc4_.read_int())
        data.append(_loc4_.read_bool())
        return data

    def commitSkills(self, data) -> dict:
        from python.Static.Type.PlayerSkillType import PlayerSkillType
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = {}
        self.read_skill(PlayerSkillType.Atacking, data, _loc2_)
        self.read_skill(PlayerSkillType.Control, data, _loc2_)
        self.read_skill(PlayerSkillType.Defending, data, _loc2_)
        self.read_skill(PlayerSkillType.EnergyWeapons, data, _loc2_)
        self.read_skill(PlayerSkillType.KineticWeapons, data, _loc2_)
        self.read_skill(PlayerSkillType.Mining, data, _loc2_)
        self.read_skill(PlayerSkillType.Piloting, data, _loc2_)
        self.read_skill(PlayerSkillType.Repairing, data, _loc2_)
        self.read_skill(PlayerSkillType.RocketWeapons, data, _loc2_)
        self.read_skill(PlayerSkillType.Tactics, data, _loc2_)
        self.read_skill(PlayerSkillType.Trading, data, _loc2_)
        self.read_skill(PlayerSkillType.Targeting, data, _loc2_)
        self.read_skill(PlayerSkillType.Electronics, data, _loc2_)
        self.read_skill(PlayerSkillType.Mechanics, data, _loc2_)
        self.read_skill(PlayerSkillType.Biocemistry, data, _loc2_)
        self.read_skill(PlayerSkillType.Cybernetics, data, _loc2_)
        return data

    def read_skill(self, player_skill_type, data, decoder):
        data[decoder.read_bytes()] = decoder.read_bytes()  # player skill type
        return data

    def applyGineticLabOption(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_int())
        return data

    def sendCredits(self, data) -> list:
        _loc5_ = PackageDecoder()
        _loc5_.data = data
        data = []
        data.append(_loc5_.read_int())  # id
        data.append(_loc5_.read_int())  # count credits
        data.append(_loc5_.read_bool())
        data.append(_loc5_.read_bool())
        return data

    def sendBonuses(self, data) -> list:
        _loc5_ = PackageDecoder()
        _loc5_.data = data
        data = []
        data.append(_loc5_.read_int())
        data.append(_loc5_.read_int())
        data.append(_loc5_.read_bool())
        data.append(_loc5_.read_bool())
        return data

    def toRepository(self, data) -> list:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = []
        data.append(_loc3_.read_bytes())
        data.append(_loc3_.read_int())
        return data

    def returnItem(self, data) -> list:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = []
        data.append(_loc3_.read_bytes())
        data.append(_loc3_.read_int())
        return data

    def toClanRepository(self, data) -> list:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = []
        data.append(_loc3_.read_bytes())
        data.append(_loc3_.read_int())
        return data

    def returnItemClan(self, data) -> list:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = []
        data.append(_loc3_.read_bytes())
        data.append(_loc3_.read_int())
        return data

    def loadClan(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_int())
        return data

    def clanLoad(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_int())
        return data

    def checkValue(self, data) -> list:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = []
        data.append(_loc3_.read_int())
        data.append(_loc3_.read_utf())
        return data

    def AcceptedClanInfo(self, data) -> list:
        _loc1_: PackageDecoder = PackageDecoder()
        _loc1_.data = data
        data = []
        return data

    def createClan(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_int())
        return data

    def ClansLetters(self, data) -> list:
        _loc1_: PackageDecoder = PackageDecoder()
        _loc1_.data = data
        data = []
        return data

    def ClansList(self, data) -> list:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = []
        data.append(_loc3_.read_utf())
        data.append(_loc3_.read_int())
        return data

    def joinToClanRequest(self, data) -> list:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = []
        data.append(_loc3_.read_int())
        data.append(_loc3_.read_utf())
        return data

    def bodylessCommand(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        return data

    def guidValueCommand(self, data) -> list:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = []
        data.append(_loc3_.read_bytes())
        return data

    def tradeItemToSell(self, data) -> list:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = []
        data.append(_loc3_.read_bytes())
        data.append(_loc3_.read_short())
        return data

    def intValueCommand(self, data) -> list:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = []
        data.append(_loc3_.read_int())
        return data

    def floatValueCommand(self, data) -> list:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = []
        data.append(_loc3_.read_float())
        return data

    def boolValueCommand(self, data) -> list:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = []
        data.append(_loc3_.read_bool())
        return data

    def submitClanFriendRequests(self, data) -> list:
        _loc4_ = PackageDecoder()
        _loc4_.data = data
        data = []
        for i in range(_loc4_.read_int()):
            data.append(_loc4_.read_int())
            data.append(_loc4_.read_int())

        for i in range(_loc4_.read_int()):
            data.append(_loc4_.read_int())
        return data

    def createPilot(self, data) -> list:
        _loc2_: PackageDecoder = PackageDecoder()
        _loc2_.data = data
        data = []
        data.append(_loc2_.read_short())
        data.append(_loc2_.read_utf())
        return data

    def saveClanJoinRequests(self, data) -> list:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = []
        _loc4_: int = 0
        while True:
            if len(_loc3_.data):
                data.append(_loc3_.read_int())  # playerID)
                data.append(_loc3_.read_bytes())  # result)
            else:
                break
        return data

    def buyItemByBonuses(self, data) -> list:
        _loc5_ = PackageDecoder()
        _loc5_.data = data
        data = []
        data.append(_loc5_.read_short())
        data.append(_loc5_.read_short())
        data.append(_loc5_.read_int())
        data.append(_loc5_.read_short())
        return data

    def buyShipByBonuses(self, data) -> list:
        _loc4_ = PackageDecoder()
        _loc4_.data = data
        data = []
        data.append(_loc4_.read_short())
        data.append(_loc4_.read_int())
        data.append(_loc4_.read_short())
        return data

    def tradeInvitationResult(self, data) -> list:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = []
        data.append(_loc3_.read_int())
        data.append(_loc3_.read_bool())
        return data

    def PlayerRole(self, data) -> list:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = []
        data.append(_loc3_.read_int())
        data.append(_loc3_.read_int())
        return data

    def renamePilot(self, data) -> list:
        _loc3_: PackageDecoder = PackageDecoder()
        _loc3_.data = data
        data = []
        data.append(_loc3_.read_int())
        data.append(_loc3_.read_utf())
        return data
