from python.Static.cfg.cfg_main import cfg_main
from python.Static.cfg.cfg_player import get_cost_reset_skills
from python.Static.ParseJson import parse_xml
from python.Utils.DotMap import DotMap
from python.Static.Type.ServerRequest import ServerRequest
from python.Packages.PackageCreator import PackageCreator
from python.Static.cfg.shops.cfg_trading import cfg_trading
from ..DataBase.Database import DataBase
from python.Static.cfg.cfg_main import cfg_const
from ..SpaceObjects.Items.FakeShip import FakeShip
from ..Static.cfg.cfg_upgrade_ship import cfg_upgrade


class PackagesManager:
    def __init__(self, Player: "Player"):
        self.id = Player.id
        self.Game = Player.Game
        self.Player = Player
        self.Location = self.Player.Location

    @staticmethod
    def isValidPackageLength(creator: int) -> bool:
        return 0 <= creator < 60000

    def processPackages(self, _loc1_: ServerRequest, *args):
        _loc2_: list = list()
        match _loc1_:
            case ServerRequest.SHIPS_POSITION:
                return self.shipsPosition()
            case ServerRequest.SHIPS_STASE:
                return self.shipsState()
            case ServerRequest.MESSAGE:
                return self.message()
            case ServerRequest.PLAYER_SHIP_UPDATE:
                return self.playerShipUpdate()
            case ServerRequest.PLANETS_STATE:
                return self.planetsState()
            case ServerRequest.PLANETS_UPDATE:
                return self.planetsUpdate()
            case ServerRequest.REPOSITORY:
                return self.repository()
            case ServerRequest.CLAN_REPOSITORY:
                return self.clan_repository()
            case ServerRequest.WEAPON_TROUBLES:
                return self.weaponTroubles()
            case ServerRequest.SHIP:
                return self.ship()
            case ServerRequest.SHOOTS:
                return self.shoots()
            case ServerRequest.ITEMS:
                return self.items()
            case ServerRequest.ACTIVE_DEVICES:
                return self.activeDevices()
            case ServerRequest.ACTIVE_WEPONS:
                return self.activeWeapons()
            case ServerRequest.HIDE_SHIP:
                return self.hideShip()
            case ServerRequest.SHIP_DESTROYED:
                return self.shipDestroyed()
            case ServerRequest.SHIP_JUMPED:
                return self.shipJumped()
            case ServerRequest.PLANET:
                return self.planet()
            case ServerRequest.INVENTORY:
                return self.inventory()
            case ServerRequest.TRADING_ITEMS:
                return self.tradingItems()
            case ServerRequest.RESOURCE_UPDATE_INFO:
                return self.resourceUpdate()
            case ServerRequest.ASTEROIDS:
                return self.asteroids()
            case ServerRequest.EFFECT_CREATED:
                return self.effectCreated()
            case ServerRequest.LOCATION_PLANET:
                return self.locationPlanet()
            case ServerRequest.LOCATION_SYSTEM:
                return self.locationSystem()
            case ServerRequest.LOCATION_BATTLE:
                return self.locationBattle()
            case ServerRequest.PLAYER:
                return self.player()
            case ServerRequest.QUEST_MESSAGE:
                return self.questMessage()
            case ServerRequest.PLAYER_SKILLS:
                return self.playerSkills()
            case ServerRequest.PLAYER_SKILLS_DATA:
                return self.playerSkillsData()
            case ServerRequest.PLAYER_SHIP:
                return self.playerShip()
            case ServerRequest.DROID_BUILDING_DIALOG:
                return self.droidBuildingDialog()
            case ServerRequest.TRADING_SHIPS:
                return self.tradingShips()
            case ServerRequest.WEAPONS_PARAMETERS:
                return self.weaponsParameters()
            case ServerRequest.ENGINES_PARAMETERS:
                return self.engineParameters()
            case ServerRequest.AMMOS_PARAMETERS:
                return self.ammoParameters()
            case ServerRequest.RESOURCE_PARAMETERS:
                return self.resourceParameters()
            case ServerRequest.DEVICE_PARAMETERS:
                return self.deviceParameters()
            case ServerRequest.DROID_PARAMETERS:
                return self.droidParameters()
            case ServerRequest.SHIP_PARAMETERS:
                return self.shipParameters()
            case ServerRequest.LOGGED:
                return self.logged()
            case ServerRequest.REACHABLE_SYSTEMS:
                return self.reachableSystems()
            case ServerRequest.SYSTEM_MESSAGE:
                return self.systemMessage()
            case ServerRequest.LOG_MESSAGE:
                return self.logMessage()
            case ServerRequest.LOG_MESSAGE_STRING:
                return self.logMessagestr()
            case ServerRequest.SYSTEM_MESSAGE_STRING:
                return self.systemMessagestr()
            case ServerRequest.MAP:
                return self.map()
            case ServerRequest.QUESTS_JOURNAL:
                return self.questsJournal()
            case ServerRequest.ARENA_REQUESTS:
                return self.arenaRequests()
            case ServerRequest.PLANET_QUESTS:
                return self.planetQuests()
            case ServerRequest.ADDITIONAL_QUEST_MESSAGE:
                return self.additionalQuestMessage()
            case ServerRequest.BATTLE_REQUEST_CHANGED:
                return self.battleRequestChanged()
            case ServerRequest.TOP_LIST:
                return self.topList()
            case ServerRequest.TOP_RATING_LIST:
                return self.topRatingList()
            case ServerRequest.TOP_CLANS_LIST:
                return self.topClansList()
            case ServerRequest.NEWS_LIST:
                return self.newsList()
            case ServerRequest.ONLINE:
                return self.online()
            case ServerRequest.VERSION:
                return self.version()
            case ServerRequest.SHIP_HEALTH:
                return self.shipHealth()
            case ServerRequest.NPC_MESSAGE:
                return self.npcMessage()
            case ServerRequest.UPDATE_HOLD:
                return self.updateHold()
            case ServerRequest.GINETIC_LAB_OPTIONS:
                return self.gineticLabOptions()
            case ServerRequest.CLAN:
                return self.clan()
            case ServerRequest.CHECK_VALUE_RESULT:
                return self.checkValueResult()
            case ServerRequest.ACCEPTED_CLAN_INFO:
                return self.acceptedClanInfo()
            case ServerRequest.clanId:
                return self.clanId()
            case ServerRequest.CLANS_LETTERS:
                return self.clansLetters()
            case ServerRequest.CLANS_LIST:
                return self.clansList()
            case ServerRequest.CLAN_JOIN_REQUESTS:
                return self.clanJoinRequests()
            case ServerRequest.PLAYER_INFO:
                return self.playerInfo()
            case ServerRequest.PLAYER_LOGGED_ON:
                return self.playerLoggedOn()
            case ServerRequest.PLAYER_LOGGED_OFF:
                return self.playerLoggedOff()
            case ServerRequest.PLAYER_CLAN:
                return self.playerClan()
            case ServerRequest.FRIEND_CLANS:
                return self.friendClans()
            case ServerRequest.ENEMY_CLANS:
                return self.enemyClans()
            case ServerRequest.UPDATE_VALUE:
                return self.updateValue(*args)
            case ServerRequest.FRIEND_REQUESTS:
                return self.friendRequests()
            case ServerRequest.DROID_EVENT:
                return self.droidEvent()
            case ServerRequest.EFFECT_REMOVED:
                return self.effectRemoved()
            case ServerRequest.MISSIONS:
                return self.missions()
            case ServerRequest.TO_GAME:
                return self.toGame()
            case ServerRequest.PLAYER_ANGAR:
                return self.playerAngar()
            case ServerRequest.TRADE_INVITATION:
                return self.tradeInvitation()
            case ServerRequest.SHOW_TRADING:
                return self.showTrading()
            case ServerRequest.TRADING_CASH:
                return self.tradingCash()
            case ServerRequest.TRADE_SELL_ITEMS:
                return self.tradeSellItems()
            case ServerRequest.EVIL:
                return self.Evil()
            case ServerRequest.TRADE_ACCEPTED:
                return self.tradeAccept()
            case ServerRequest.TRADE_BUY_ITEMS:
                return self.tradeBuyItems()
            case ServerRequest.FINISH_TRADING:
                return self.finishTrading()
            case ServerRequest.SHIP_UPDATE_INFO:
                return self.shipUpdateInfo()
            case ServerRequest.TEAM_LIST:
                return self.teamList()

    def tradingCash(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TRADING_CASH
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.TRADING_CASH))
        creator.write_int(5)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def tradeAccept(self, accept: bool):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TRADE_ACCEPTED
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.TRADE_ACCEPTED))
        creator.write_bool(accept)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def shipUpdateInfo(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIP_UPDATE_INFO
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.SHIP_UPDATE_INFO))
        _loc6_ = DotMap(FakeShip(self.Game, self.Player.ship['classNumber']).ship)
        creator.write_short(_loc6_.classNumber)
        creator.write_short(_loc6_.size)
        creator.write_unsigned_byte(_loc6_.weaponSlots)
        creator.write_unsigned_byte(_loc6_.deviceSlots)
        creator.write_unsigned_byte(_loc6_.armor)
        creator.write_unsigned_byte(_loc6_.shields)
        creator.write_short(_loc6_.maxEnergy)
        creator.write_short(_loc6_.maxHealth)
        creator.write_short(_loc6_.cpu)
        creator.write_short(_loc6_.radar)
        creator.write_unsigned_byte(_loc6_.maxSpeed)
        rest = _loc6_.restrictions
        creator.write_unsigned_byte(len(rest))
        for r in rest:
            _loc2_ = DotMap(r)
            creator.write_unsigned_byte(_loc2_.type)
            creator.write_unsigned_byte(_loc2_.valueType)
            creator.write_int(_loc2_.Value)

        feat = _loc6_.features
        creator.write_unsigned_byte(len(feat))
        for f in feat:
            _loc3_ = DotMap(f)
            creator.write_unsigned_byte(_loc3_.type)
            creator.write_int(_loc3_.Value)

        _loc9_ = DotMap(FakeShip(self.Game, cfg_upgrade[self.Player.ship['classNumber']]).ship)

        creator.write_short(_loc9_.classNumber)
        creator.write_short(_loc9_.size)
        creator.write_unsigned_byte(_loc9_.weaponSlots)
        creator.write_unsigned_byte(_loc9_.deviceSlots)
        creator.write_unsigned_byte(_loc9_.armor)
        creator.write_unsigned_byte(_loc9_.shields)
        creator.write_short(_loc9_.maxEnergy)
        creator.write_short(_loc9_.maxHealth)
        creator.write_short(_loc9_.cpu)
        creator.write_short(_loc9_.radar)
        creator.write_unsigned_byte(_loc9_.maxSpeed)
        rest = _loc9_.restrictions
        creator.write_unsigned_byte(len(rest))
        for i in rest:
            _loc2_ = DotMap(i)
            creator.write_unsigned_byte(_loc2_.type)
            creator.write_unsigned_byte(_loc2_.valueType)
            creator.write_int(_loc2_.value)
        data = []
        creator.write_unsigned_byte(len(data))
        for i in data:
            _loc3_ = DotMap(i)
            creator.write_unsigned_byte(_loc3_.type)
            creator.write_int(_loc3_.Value)
        creator.write_bool(_loc9_.satisfying)

        UpdateCost = []
        _loc10_ = DotMap()
        creator.write_int(_loc10_.cash)
        for i in UpdateCost:
            _loc5_ = DotMap(i)
            creator.write_short(_loc5_.classNumber)
            creator.write_int(_loc5_.count)
            creator.write_bool(_loc5_.enough)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def finishTrading(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.FINISH_TRADING
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.FINISH_TRADING))
        _loc2_ = 0
        creator.write_int(_loc2_)
        self._write_items(creator, True, False, False)
        _loc4_: int = 0
        creator.write_int(_loc4_)
        self._write_items(creator, True, False, False)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def tradeSellItems(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TRADE_SELL_ITEMS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.TRADE_SELL_ITEMS))
        self._write_items(creator, True, True)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def tradeBuyItems(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TRADE_BUY_ITEMS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.TRADE_BUY_ITEMS))
        self._write_items(creator, True, True)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def playerAngar(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_ANGAR
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.PLAYER_ANGAR))
        angar = self.Player.angar
        creator.write_unsigned_byte(len(angar))
        for FakeShip in angar:
            ship = DotMap(FakeShip.ship)
            creator.write_short(ship.classNumber)
            creator.write_int(ship.cost)
            creator.write_short(ship.size)
            creator.write_unsigned_byte(ship.weaponSlots)
            creator.write_unsigned_byte(ship.deviceSlots)
            creator.write_unsigned_byte(ship.armor)  # до 127 броня. 128 == - 128. if armor > 127: armor = 256 - armor
            creator.write_unsigned_byte(ship.shields)
            creator.write_short(ship.maxEnergy)
            creator.write_short(ship.maxHealth)
            creator.write_short(ship.cpu)
            creator.write_short(ship.radar)
            creator.write_unsigned_byte(ship.maxSpeed)
            data_restr = ship.restrictions
            creator.write_unsigned_byte(len(data_restr))
            for rest in data_restr:
                _loc4_ = DotMap(rest)
                creator.write_unsigned_byte(_loc4_.type)
                creator.write_unsigned_byte(_loc4_.valueType)
                creator.write_int(_loc4_.Value)
            data_feat = ship.features
            creator.write_unsigned_byte(len(data_feat))
            for feat in data_feat:
                _loc5_ = DotMap(feat)
                creator.write_unsigned_byte(_loc5_.type)
                creator.write_int(_loc5_.Value)
            creator.write_bool(ship.satisfying)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def updateHold(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.UPDATE_HOLD
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.UPDATE_HOLD))
        update_hold = bool()
        creator.write_bool(update_hold)
        self._write_items(creator, True, True, True, update_hold)
        self._write_items(creator, True, True, True, update_hold)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def gineticLabOptions(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.GINETIC_LAB_OPTIONS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.GINETIC_LAB_OPTIONS))
        count = 1
        creator.write_unsigned_byte(count)
        # for i in data:
        creator.write_unsigned_byte(1)  # _loc2_.option)
        creator.write_int(get_cost_reset_skills(self.Player.count_reset_skills))
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def npcMessage(self, text=4, avatar=2001):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.NPC_MESSAGE
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.NPC_MESSAGE))
        creator.write_int(text)  # message SystemMessageType
        creator.write_int(avatar)  # avatar
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def additionalQuestMessage(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ADDITIONAL_QUEST_MESSAGE
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.ADDITIONAL_QUEST_MESSAGE))
        _loc2_: int = 0
        _loc3_: int = 0
        creator.write_int(_loc2_)
        creator.write_int(_loc3_)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def arenaRequests(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ARENA_REQUESTS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.ARENA_REQUESTS))
        data = []
        creator.write_int(len(data))
        _loc5_: int = 0
        for quest in data:
            _loc2_ = DotMap(quest)
            creator.write_int(_loc2_.id)
            creator.write_int(_loc2_.playersCount)
            creator.write_int(_loc2_.maxPlayers)
            creator.write_int(_loc2_.maxShipType)
            creator.write_int(_loc2_.minShipType)
            creator.write_unsigned_byte(_loc2_.type)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def battleRequestChanged(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.BATTLE_REQUEST_CHANGED
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.BATTLE_REQUEST_CHANGED))
        _loc3_ = DotMap()
        creator.write_int(_loc3_.id)
        creator.write_int(_loc3_.playersCount)
        creator.write_int(_loc3_.maxPlayers)
        creator.write_int(_loc3_.maxShipType)
        creator.write_int(_loc3_.minShipType)
        creator.write_unsigned_byte(_loc3_.type)
        creator.write_int(_loc3_.award)
        _loc3_.cost = (_loc3_.type - 1) * 2000
        for i in _loc3_.playersCoun:
            _loc2_ = DotMap(i)
            creator.write_bool(_loc2_.isReady)
            creator.write_int(_loc2_.id)
            creator.write_utf(_loc2_.login)
            creator.write_int(_loc2_.level)
            creator.write_int(_loc2_.classNumber)
            creator.write_int(_loc2_.race)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def questsJournal(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.QUESTS_JOURNAL
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.QUESTS_JOURNAL))
        data = []
        creator.write_int(len(data))
        _loc5_: int = 0
        for quest in data:
            _loc2_ = DotMap(quest)
            creator.write_int(_loc2_.questId)
            creator.write_int(_loc2_.giverType)
            creator.write_utf(_loc2_.giverName)
            creator.write_utf(_loc2_.Name)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def activeDevices(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ACTIVE_DEVICES
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.ACTIVE_DEVICES))
        data_active_device = self.Player.activeDevices
        creator.write_unsigned_byte(len(data_active_device))
        for _loc3_ in data_active_device:
            creator.write_short(_loc3_.classNumber)
            creator.write_bytes(_loc3_.guid)
            creator.write_float(_loc3_.reloadedTime)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def activeWeapons(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ACTIVE_WEPONS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.ACTIVE_WEPONS))
        activeWeapons = self.Player.activeWeapons
        creator.write_unsigned_byte(len(activeWeapons))
        print('activeWeapons', activeWeapons)
        for index, active_weapon in enumerate(activeWeapons):
            creator.write_short(active_weapon.classNumber)
            creator.write_unsigned_byte(index)  # active_weapon.index) # hz
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def playerShipUpdate(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_SHIP_UPDATE
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.PLAYER_SHIP_UPDATE))
        creator.write_short(self.Player.energy)
        creator.write_short(self.Player.health)
        creator.write_unsigned_byte(self.Player.controlLeft)
        creator.write_unsigned_byte(self.Player.controlUsed)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def tradingShips(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TRADING_SHIPS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.TRADING_SHIPS))

        data = self.Player.SpaceObject.ships

        creator.write_int(self.Player.ship['classNumber'])  # ship.id)  # id
        creator.write_int(self.Player.ship['cost'])  # ship.cost)  # ship cost

        creator.write_float(cfg_trading(self.Player.skills['Trading']).coef_buy)  # ship.buy_coef)  # buyCoeficient
        creator.write_float(cfg_trading(self.Player.skills['Trading']).coef_sell)  # ship.sell_coef)  # sellCoeficient

        creator.write_int(len(data))

        for _loc6_ in data:
            creator.write_bytes(_loc6_.ship['guid'])
            creator.write_short(_loc6_.ship["classNumber"])
            creator.write_int(_loc6_.ship["cost"])
            creator.write_short(_loc6_.ship["size"])
            creator.write_unsigned_byte(_loc6_.ship["weaponSlots"])
            creator.write_unsigned_byte(_loc6_.ship["deviceSlots"])
            creator.write_unsigned_byte(_loc6_.ship["armor"])
            creator.write_unsigned_byte(_loc6_.ship["shields"])
            creator.write_short(_loc6_.ship["maxEnergy"])
            creator.write_short(_loc6_.ship["maxHealth"])
            creator.write_short(_loc6_.ship["cpu"])
            creator.write_short(_loc6_.ship["radar"])
            creator.write_unsigned_byte(_loc6_.ship["maxSpeed"])
            data_restr = _loc6_.ship["restrictions"]
            creator.write_unsigned_byte(len(data_restr))
            for restr in data_restr:
                creator.write_unsigned_byte(restr['type'])
                creator.write_unsigned_byte(restr['valueType'])
                creator.write_int(restr['Value'])
            data_ship_feature = _loc6_.ship["features"]
            creator.write_unsigned_byte(len(data_ship_feature))
            for feat in data_ship_feature:
                _loc5_ = DotMap(feat)
                creator.write_unsigned_byte(_loc5_.type)
                creator.write_int(_loc5_.Value)

            creator.write_bool(_loc6_.ship["satisfying"])
        print(creator.get_package())
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def tradingItems(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TRADING_ITEMS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.TRADING_ITEMS))
        Planet = self.Player.SpaceObject

        creator.write_int(1)  # type shop

        creator.write_float(cfg_trading(self.Player.skills['Trading']).coef_sell)  # sellCoeficient
        creator.write_float(cfg_trading(self.Player.skills['Trading']).coef_buy)  # buyCoeficient

        self._write_items(creator, self.Player.inventory, True, True, True, True)

        self._write_items(creator, Planet.fake_items(self.Player), True, True, True, True)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def resourceUpdate(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.RESOURCE_UPDATE_INFO
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.RESOURCE_UPDATE_INFO))
        creator.write_int(1)  # self.PlayerItems.id)  # id
        self._write_items(creator, self.Player.inventory, True, True)
        self._write_items(creator, self.Player.inventory, True, True)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def _write_items(self, creator: PackageCreator, items, param2: bool, param3: bool, param4: bool = True,
                     param5: bool = False) -> None:

        creator.write_int(len(items))
        for item in items:
            creator.write_int(item.classNumber)
            creator.write_bytes(item.guid)
            creator.write_int(item.get_wear)
            if param4:
                creator.write_int(0)  # item.level)
            if param2:
                creator.write_bool(False)  # zeroCost
            if param5:
                creator.write_int(12)  # random don't use
            if param3:
                creator.write_bool(item.satisfying)

    def shipsPosition(self):
        """ id, x, y, targetX, targetY """
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIPS_POSITION
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.SHIPS_POSITION))
        players = self.Location.players
        creator.write_int(len(players))
        for player in players:
            creator.write_int(player.id)
            creator.write_float(player.x)
            creator.write_float(player.y)
            creator.write_float(player.targetX)
            creator.write_float(player.targetY)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def shipsState(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIPS_STASE
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.SHIPS_STASE))
        players = self.Location.players
        for _loc2_ in players:
            creator.write_int(_loc2_.id)
            creator.write_unsigned_byte(_loc2_.speed)
            creator.write_short(_loc2_.health)
            creator.write_short(_loc2_.energy)
            creator.write_short(_loc2_.PlayerRelation)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def weaponTroubles(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.WEAPON_TROUBLES
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.WEAPON_TROUBLES))
        data = []
        creator.write_unsigned_byte(len(data))
        for trouble in data:
            _loc2_ = DotMap(trouble)
            creator.write_unsigned_byte(_loc2_.trouble)
            creator.write_unsigned_byte(_loc2_.index)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def repository(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.REPOSITORY
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.REPOSITORY))

        self._write_items(creator, self.Player.repository, False, False)

        creator.write_float(1.0)  # costCoef _loc4_.costCoef # проверить пакет хранилища
        data = self.Player.inventory
        print('data', data)
        creator.write_int(len(data))
        for _loc2_ in data:
            creator.write_int(_loc2_.classNumber)
            creator.write_bytes(_loc2_.guid)
            creator.write_int(_loc2_.wear)
            creator.write_int(_loc2_.level)
            creator.write_int(12)  # random don't use
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def clan_repository(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CLAN_REPOSITORY
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.CLAN_REPOSITORY))
        items = self.Player.Clan.repository
        self._write_items(creator, items, False, False)
        creator.write_float(1)  # _loc4_.costCoef)
        items = self.Player.inventory
        creator.write_int(len(items))
        for i in items:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.classNumber)
            creator.write_bytes(_loc2_.guid)
            creator.write_int(_loc2_.wear)
            creator.write_int(_loc2_.level)
            creator.write_int(12)  # don't use
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def planetsState(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLANETS_STATE
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.PLANETS_STATE))
        data = []
        creator.write_unsigned_byte(len(data))
        for i in data:
            _loc1_ = DotMap(i)
            creator.write_int(_loc1_.id)  # id SpaceObjectItems
            creator.write_float(_loc1_.angel)  # angel
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def planetsUpdate(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLANETS_UPDATE
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.PLANETS_UPDATE))
        data = []
        creator.write_unsigned_byte(len(data))
        for i in data:
            _loc1_ = DotMap(i)
            creator.write_int(_loc1_.id)
            creator.write_float(_loc1_.angel)
            creator.write_bytes(_loc1_.race)
            creator.write_bytes(_loc1_.aliance)
            creator.write_int(_loc1_.clanId)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def ship(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIP
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.SHIP))
        _loc3_ = self.Player
        creator.write_short(_loc3_.race)
        creator.write_int(_loc3_.id)
        creator.write_utf(_loc3_.login)
        creator.write_short(_loc3_.size)
        creator.write_float(_loc3_.x)
        creator.write_float(_loc3_.y)
        creator.write_int(_loc3_.level)
        creator.write_short(_loc3_.ship['maxHealth'])
        creator.write_short(_loc3_.ship['maxEnergy'])
        creator.write_int(_loc3_.avatar)
        creator.write_unsigned_byte(_loc3_.ship['maxSpeed'])
        creator.write_float(_loc3_.targetX)
        creator.write_float(_loc3_.targetY)
        creator.write_unsigned_byte(_loc3_.aliance)
        creator.write_unsigned_byte(_loc3_.status)
        creator.write_int(_loc3_.clanId)
        droids = _loc3_.droids
        creator.write_unsigned_byte(len(droids))
        for droid in droids:
            _loc2_ = DotMap(droid)
            creator.write_unsigned_byte(_loc2_.id)
            creator.write_short(_loc2_.type)
            creator.write_short(_loc2_.weaponClass)
            creator.write_short(_loc2_.health)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def planet(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLANET
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.PLANET))
        creator.write_bytes(self.Player.SpaceObject.classNumber)
        creator.write_int(self.Player.SpaceObject.id)
        creator.write_unsigned_byte(self.Player.SpaceObject.race)
        creator.write_int(self.Player.SpaceObject.radius)
        creator.write_int(self.Player.SpaceObject.size)
        creator.write_float(self.Player.SpaceObject.serverAngle)
        creator.write_bool(self.Player.SpaceObject.landable)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def inventory(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.INVENTORY
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.INVENTORY))
        inventory = self.Player.inventory
        _loc5_: int = creator.write_short(len(inventory))
        for ItemClass in inventory:
            creator.write_short(ItemClass.classNumber)
            creator.write_bytes(ItemClass.guid)
            creator.write_short(ItemClass.wear)
            creator.write_bool(ItemClass.inUsing)
            creator.write_unsigned_byte(ItemClass.level)
            creator.write_bool(ItemClass.satisfying)
        print('hold', self.Player.hold)
        creator.write_unsigned_byte(self.Player.ship['armor'])
        creator.write_unsigned_byte(self.Player.ship['shields'])
        creator.write_short(int(self.Player.hold))  # Трюм
        creator.write_short(self.Player.ship['cpu'])
        creator.write_short(0)#self.PlayerItems.ship['cpuUsed'])  # ship.cpuUsed
        creator.write_unsigned_byte(self.Player.ship['level'])
        creator.write_unsigned_byte(3)  # ship.maxDroids

        # for i in data: # Какие-то дополнительные предметы
        #     _loc2_ = DotMap(i)
        #     creator.write_short(_loc2_.ItemClass)
        #     creator.write_bytes(_loc2_.id)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def player(self, mode=False):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.PLAYER))

        creator.write_int(self.Player.id)
        creator.write_utf(self.Player.login)
        creator.write_int(self.Player.level)
        creator.write_int(self.Player.cash)
        creator.write_unsigned_byte(self.Player.race)
        creator.write_int(self.Player.avatar)
        creator.write_unsigned_byte(self.Player.aliance)
        creator.write_int(self.Player.clanId)
        creator.write_int(self.Player.role)
        creator.write_unsigned_byte(self.Player.clanRequestStatus)
        creator.write_unsigned_byte(self.Player.clanJoinRequestStatus)
        creator.write_int(self.Player.PlayerRelation)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def questMessage(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.QUEST_MESSAGE
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.QUEST_MESSAGE))
        quest = DotMap()
        creator.write_int(quest.questId)
        creator.write_int(quest.nextQuestId)
        creator.write_int(quest.giverType)
        creator.write_int(quest.status)
        creator.write_utf(quest.giverName)
        data = []
        creator.write_int(len(data))
        for i in data:  # ? maybe messagee
            _loc2_ = ''
            creator.write_utf(_loc2_)
        creator.write_int(quest.ParentSystemID)
        creator.write_unsigned_byte(quest.LocationType)
        creator.write_int(quest.LocationID)
        quest_award = []
        creator.write_int(len(quest_award))
        for award in quest_award:
            _loc3_ = DotMap(award)
            creator.write_int(_loc3_.classNumber)
            creator.write_int(_loc3_.level)
            creator.write_int(_loc3_.type)
            creator.write_int(_loc3_.value)
        quest_target = []
        creator.write_int(quest_target)
        for target in quest_target:
            _loc4_ = DotMap(target)
            creator.write_int(_loc4_.targetId)
            creator.write_int(_loc4_.targetSystemId)
            creator.write_int(_loc4_.targetPlanetId)
            creator.write_int(_loc4_.type)
            creator.write_int(_loc4_.value)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def playerSkills(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_SKILLS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.PLAYER_SKILLS))
        Player = getattr(self.Game, f"Player_{self.id}")
        creator.write_unsigned_byte(Player.level)
        creator.write_int(Player.experience)
        creator.write_int(Player.forNextLevel)
        self.write_skills(creator, Player.skills)
        creator.write_int(Player.freeSkills)
        creator.write_int(Player.expForFirstSkillLevel)
        creator.write_float(Player.expSkillGrowCoef)
        creator.write_float(Player.expSkillReduserCoef)
        creator.write_unsigned_byte(cfg_const['maxSkill'])
        creator.write_unsigned_byte(Player.status)
        creator.write_unsigned_byte(Player.level)
        if Player.points > 0:
            creator.write_int(0)
            creator.write_int(Player.points)
        else:
            creator.write_int(Player.points)
            creator.write_int(0)
        creator.write_int(Player.forNextLevel)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    @staticmethod
    def write_skills(creator, param2) -> None:
        if isinstance(param2, DotMap):
            param2 = dict(param2)
        creator.write_unsigned_byte(param2["Control"])
        creator.write_unsigned_byte(param2["Defending"])
        creator.write_unsigned_byte(param2["EnergyWeapons"])
        creator.write_unsigned_byte(param2["KineticWeapons"])
        creator.write_unsigned_byte(param2["Mining"])
        creator.write_unsigned_byte(param2["Piloting"])
        creator.write_unsigned_byte(param2["Repairing"])
        creator.write_unsigned_byte(param2["RocketWeapons"])
        creator.write_unsigned_byte(param2["Trading"])
        creator.write_unsigned_byte(param2["Attacking"])
        creator.write_unsigned_byte(param2["Tactics"])
        creator.write_unsigned_byte(param2["Targeting"])
        creator.write_unsigned_byte(param2["Electronics"])
        creator.write_unsigned_byte(param2["Biocemistry"])
        creator.write_unsigned_byte(param2["Mechanics"])
        creator.write_unsigned_byte(param2["Cybernetics"])

    def playerSkillsData(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_SKILLS_DATA
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.PLAYER_SKILLS_DATA))
        Player = getattr(self.Game, f"Player_{self.id}")
        creator.write_unsigned_byte(Player.level)
        creator.write_int(Player.experience)
        creator.write_int(Player.forNextLevel)
        self.write_skills(creator, Player.skills)
        creator.write_int(Player.freeSkills)
        creator.write_int(Player.expForFirstSkillLevel)
        creator.write_float(Player.expSkillGrowCoef)
        creator.write_float(Player.expSkillReduserCoef)
        creator.write_unsigned_byte(Player.maxSkill)
        creator.write_unsigned_byte(Player.status)
        creator.write_unsigned_byte(Player.level)
        creator.write_int(Player.pirateStatus)
        creator.write_int(Player.policeStatus)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def playerShip(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_SHIP
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.PLAYER_SHIP))

        creator.write_int(self.Player.ship['classNumber'])  # raca
        creator.write_int(self.Player.id)
        creator.write_utf(self.Player.login)
        creator.write_int(self.Player.ship['size'])
        creator.write_int(self.Player.energy)
        creator.write_int(self.Player.ship['maxEnergy'])
        creator.write_float(self.Player.x)
        creator.write_float(self.Player.y)
        creator.write_int(self.Player.team)
        creator.write_unsigned_byte(self.Player.ship['maxSpeed'])
        creator.write_unsigned_byte(self.Player.ship['weaponSlots'])
        creator.write_unsigned_byte(self.Player.ship['deviceSlots'])
        creator.write_int(self.Player.ship['maxHealth'])
        creator.write_short(self.Player.ship['radar'])
        creator.write_short(self.Player.ship['cpu'])
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def weaponsParameters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.WEAPONS_PARAMETERS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.WEAPONS_PARAMETERS))
        data_weapons = parse_xml("WeaponParameters")
        creator.write_int(len(data_weapons))
        for weapon in data_weapons:
            _loc2_ = DotMap(weapon)
            creator.write_int(_loc2_.classNumber)
            creator.write_int(_loc2_.autoShots)
            creator.write_int(_loc2_.radius)
            creator.write_int(_loc2_.reloadTime)
            creator.write_int(_loc2_.energyCost)
            creator.write_float(_loc2_.size)
            creator.write_int(_loc2_.cost)
            creator.write_bool(_loc2_.needAmmo)
            creator.write_int(_loc2_.ammoClass)
            creator.write_int(_loc2_.minDamage)
            creator.write_int(_loc2_.maxDamage)
            creator.write_unsigned_byte(_loc2_.type)
            creator.write_unsigned_byte(_loc2_.effect)
            creator.write_int(_loc2_.maxWear)
            restr = _loc2_.restrictions
            creator.write_unsigned_byte(restr['Length'])
            for rest in restr['data']:
                _loc5_ = DotMap(rest)
                creator.write_unsigned_byte(_loc5_.type)
                creator.write_unsigned_byte(_loc5_.valueType)
                creator.write_int(_loc5_.Value)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def ammoParameters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.AMMOS_PARAMETERS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.AMMOS_PARAMETERS))
        data_ammo = parse_xml("AmmoParameters")
        creator.write_int(len(data_ammo))
        for ammo in data_ammo:
            _loc2_ = DotMap(ammo)  # AmmoParameters()
            creator.write_int(_loc2_.classNumber)
            creator.write_float(_loc2_.size)
            creator.write_int(_loc2_.cost)
            creator.write_int(_loc2_.damage)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def resourceParameters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.RESOURCE_PARAMETERS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.RESOURCE_PARAMETERS))
        data_resourse = parse_xml('ResourseParameters')
        creator.write_int(len(data_resourse))
        for resourse in data_resourse:
            _loc2_ = DotMap(resourse)  # ResourceParameters()
            creator.write_int(_loc2_.classNumber)
            creator.write_float(_loc2_.size)
            creator.write_int(_loc2_.cost)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def deviceParameters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.DEVICE_PARAMETERS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.DEVICE_PARAMETERS))
        data_device = parse_xml("DeviceParameters")
        creator.write_int(len(data_device))
        for device in data_device:
            _loc4_ = DotMap(device)
            creator.write_int(_loc4_.classNumber)
            creator.write_float(_loc4_.size)
            creator.write_int(_loc4_.cost)
            creator.write_int(_loc4_.energyCost)
            creator.write_int(_loc4_.reloadTime)
            creator.write_int(_loc4_.maxWear)

            cnt_dev_eff = _loc4_.effects['Length']
            creator.write_unsigned_byte(cnt_dev_eff)
            data_dev_eff = _loc4_.effects['data']
            for dev_eff in data_dev_eff:
                _loc3_ = DotMap(dev_eff)  # DeviceEffect()
                creator.write_unsigned_byte(_loc3_.targetType)
                creator.write_int(_loc3_.value)
                creator.write_int(_loc3_.effectTime)
                creator.write_unsigned_byte(_loc3_.effectType)

            cnt_dev_restr = _loc4_.restrictions['Length']
            creator.write_unsigned_byte(cnt_dev_restr)
            data_dev_restr = _loc4_.restrictions["data"]
            for restr in data_dev_restr:
                _loc8_ = DotMap(restr)  # Restriction()
                creator.write_unsigned_byte(_loc8_.type)
                creator.write_unsigned_byte(_loc8_.valueType)
                creator.write_int(_loc8_.Value)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def droidParameters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.DROID_PARAMETERS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.DROID_PARAMETERS))
        data_droids = parse_xml("DroidParameters")
        creator.write_int(len(data_droids))
        for droid_param in data_droids:
            _loc2_ = DotMap(droid_param)  # DroidParameters()
            creator.write_short(_loc2_.classNumber)
            creator.write_float(_loc2_.size)
            creator.write_int(_loc2_.cost)
            creator.write_unsigned_byte(_loc2_.energyCost)
            creator.write_unsigned_byte(_loc2_.armor)
            creator.write_short(_loc2_.droidType)
            creator.write_short(_loc2_.weaponClass)
            creator.write_short(_loc2_.health)
            cnt_restr = _loc2_.restrictions['Length']
            creator.write_unsigned_byte(cnt_restr)
            data_restr = _loc2_.restrictions['data']
            for restr in data_restr:
                _loc5_ = DotMap(restr)  # Restriction()
                creator.write_unsigned_byte(_loc5_.type)
                creator.write_unsigned_byte(_loc5_.valueType)
                creator.write_int(_loc5_.Value)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def shipParameters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIP_PARAMETERS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.SHIP_PARAMETERS))
        data_ship = parse_xml('ShipParameters')
        creator.write_int(len(data_ship))
        for ship in data_ship:
            _loc2_ = DotMap(ship)
            creator.write_short(_loc2_.classNumber)
            creator.write_int(_loc2_.cost)
            creator.write_short(_loc2_.size)
            creator.write_unsigned_byte(_loc2_.weaponSlots)
            creator.write_unsigned_byte(_loc2_.deviceSlots)
            creator.write_unsigned_byte(_loc2_.armor)
            creator.write_unsigned_byte(_loc2_.shields)
            creator.write_short(_loc2_.maxEnergy)
            creator.write_short(_loc2_.maxHealth)
            creator.write_short(_loc2_.cpu)
            creator.write_short(_loc2_.radar)
            creator.write_unsigned_byte(_loc2_.maxSpeed)
            cnt_restr = _loc2_.restrictions['Length']
            creator.write_unsigned_byte(cnt_restr)
            data_restr = _loc2_.restrictions['data']
            for restr in data_restr:
                _loc7_ = DotMap(restr)
                creator.write_unsigned_byte(_loc7_.type)
                creator.write_unsigned_byte(_loc7_.valueType)
                creator.write_int(_loc7_.Value)
            cnt_ship_feat = _loc2_.features['Length']
            creator.write_unsigned_byte(cnt_ship_feat)
            data_ship_feat = _loc2_.features['data']
            for ship_feat in data_ship_feat:
                _loc8_ = DotMap(ship_feat)
                creator.write_unsigned_byte(_loc8_.type)
                creator.write_int(_loc8_.Value)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def engineParameters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ENGINES_PARAMETERS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.ENGINES_PARAMETERS))
        data_engine = parse_xml("EngineParameters")
        creator.write_int(len(data_engine))
        for engine_ in data_engine:
            engine_ = DotMap(engine_)  # EngineParameters()
            creator.write_short(engine_.classNumber)
            creator.write_float(engine_.size)
            creator.write_int(engine_.cost)
            creator.write_unsigned_byte(engine_.hyperjumpRadius)
            creator.write_int(engine_.maxWear)
            creator.write_unsigned_byte(engine_.energyCost)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def map(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.MAP
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.MAP))
        data_system = parse_xml('GalaxyMap')
        creator.write_short(len(data_system))
        for system in data_system:
            _loc2_ = DotMap(system)  # ReachableSystem()
            creator.write_unsigned_byte(_loc2_.id)
            creator.write_unsigned_byte(_loc2_.classNumber)
            creator.write_short(_loc2_.x)
            creator.write_short(_loc2_.y)
            creator.write_unsigned_byte(_loc2_.sector)
            creator.write_unsigned_byte(_loc2_.lineTo)
            cnt_planet = _loc2_.Planets['Length']
            creator.write_unsigned_byte(cnt_planet)
            data_planet = _loc2_.Planets['data']
            for planet in data_planet:
                planet = DotMap(planet)  # PlanetData()
                creator.write_short(planet.id)
                creator.write_unsigned_byte(planet.race)
                creator.write_unsigned_byte(planet.classNumber)
                creator.write_unsigned_byte(planet.aliance)
            cnt_space_objects = _loc2_.SpaceObjects['Length']
            creator.write_unsigned_byte(cnt_space_objects)
            data_space_objects = _loc2_.SpaceObjects['data']
            for static_space_object in data_space_objects:
                static_space_object = DotMap(static_space_object)  # StaticObjectData()
                creator.write_unsigned_byte(static_space_object.type)
                creator.write_unsigned_byte(static_space_object.aliance)
                creator.write_unsigned_byte(static_space_object.race)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def reachableSystems(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.REACHABLE_SYSTEMS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.REACHABLE_SYSTEMS))
        data_system = []
        creator.write_unsigned_byte(len(data_system))
        for system in data_system:
            _loc2_ = DotMap(system)
            creator.write_unsigned_byte(_loc2_.id)
            creator.write_bool(_loc2_.current)
            creator.write_short(_loc2_.energyForJump)
        _loc6_: int = 0
        creator.write_unsigned_byte(_loc6_)  # radiuse
        _loc7_: int = 0
        creator.write_unsigned_byte(_loc7_)  # sector
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def version(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.VERSION
        version = cfg_main['version']
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.VERSION))
        creator.write_utf(version)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def shipHealth(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIP_HEALTH
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.SHIP_HEALTH))
        creator.write_int(self.Player.id)
        creator.write_int(self.Player.health)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def online(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ONLINE
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.ONLINE))
        creator.write_int(1)
        creator.write_int(self.Game.online)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def topList(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TOP_LIST
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.TOP_LIST))
        all_player = DataBase().top_list()

        creator.write_int(len(all_player))
        for player in all_player:
            creator.write_utf(player['login'])
            creator.write_int(player['level'])
            creator.write_int(player['experience'])
            creator.write_int(player['clanId'])
            creator.write_unsigned_byte(player['race'])
            creator.write_short(player['classNumber'])
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def topRatingList(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TOP_RATING_LIST
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.TOP_RATING_LIST))
        top_players = DataBase().top_rating_list()
        creator.write_int(len(top_players))
        for player in top_players:
            creator.write_utf(player['login'])
            creator.write_int(player['level'])
            creator.write_int(player['points'])
            creator.write_int(player['clanId'])
            creator.write_unsigned_byte(player['race'])
            creator.write_short(player['classNumber'])
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def topClansList(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TOP_CLANS_LIST
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.TOP_CLANS_LIST))
        clans = DataBase().top_clan_list()
        creator.write_int(len(clans))
        print('clan', clans)
        for clan in clans:
            creator.write_int(clan['id'])
            creator.write_int(clan['rating'])
            creator.write_int(clan['leaderId'])
            creator.write_unsigned_byte(clan['aliance'])
            creator.write_unsigned_byte(clan['level'])
            creator.write_utf(clan['name'])
            creator.write_utf(clan['shortName'])
            creator.write_utf(clan['logoFileName'])
        self.Game.id_to_conn[self.id].send(creator.get_package())

        #
        # def auctionList(self):
        #     creator = PackageCreator()
        #     creator.PackageNumber = ServerRequest.AUCTION_SHOP_PACKAGE
        # Pac = ServerRequest()
        # print('Пакет отправлен', Pac.get_packages(ber = ServerRequest))
        #     data = []
        #     creator.write_int(len(data))
        #     for i in data:
        #         _loc3_ = DotMap(i)
        #         creator.write_int(_loc2_.ItemClass)
        #         creator.write_guid(_loc3_.guid)
        #         creator.write_int(_loc3_.wear)
        #         creator.write_int(_loc3_.ownerid)
        #         creator.write_int(_loc3_.price)
        #         creator.write_int(_loc3_.ransom)
        #         creator.write_int(_loc3_.lastPlayerID)
        #         creator.write_utf(_loc3_.ownerName)
        #         creator.write_utf(_loc3_.lastPlayerName)
        #     self.Game.id_to_conn[self.id].send(creator.get_package())

    def newsList(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.NEWS_LIST
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.NEWS_LIST))
        data = []
        creator.write_int(len(data))
        for text in data:
            creator.write_utf(text)  # text
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def Evil(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.EVIL
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.EVIL))
        _loc2_ = ''
        creator.write_utf(_loc2_)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def locationPlanet(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOCATION_PLANET
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.LOCATION_PLANET))

        player = getattr(self.Game, f'Player_{self.id}')
        SpaceObject = player.SpaceObject

        creator.write_unsigned_byte(SpaceObject.classNumber)
        creator.write_int(SpaceObject.id)
        creator.write_unsigned_byte(SpaceObject.race)
        creator.write_int(9999)#SpaceObjectItems.RADIUS)
        creator.write_int(SpaceObject.size)
        creator.write_unsigned_byte(SpaceObject.aliance)
        creator.write_int(SpaceObject.clanId)
        creator.write_float(SpaceObject.angle)
        creator.write_unsigned_byte(SpaceObject.QCount)
        shops = SpaceObject.shops
        creator.write_short(len(shops))  # len(shop_data))

        for type_shop in shops:
            creator.write_int(type_shop)  # SpaceObjectItems.id) #_loc3_.id)
            creator.write_unsigned_byte(type_shop)  # _loc3_.type)

        player_info_data = []
        for player in player_info_data:
            _loc2_ = DotMap(player)
            creator.write_int(_loc2_.id)
            creator.write_utf(_loc2_.name)
            creator.write_int(_loc2_.clanId)
            creator.write_int(_loc2_.level)

        self.Game.id_to_conn[self.id].send(creator.get_package())

    def planetQuests(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLANET_QUESTS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.PLANET_QUESTS))
        data = []
        creator.write_short(len(data))
        for quest in data:
            _loc2_ = DotMap(quest)
            creator.write_int(_loc2_.questId)
            creator.write_int(_loc2_.giverType)
            creator.write_utf(_loc2_.giverName)
            creator.write_utf(_loc2_.Name)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def locationSystem(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOCATION_SYSTEM
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.LOCATION_SYSTEM))
        Location = self.Player.Location
        creator.write_int(Location.id)  # id
        creator.write_float(Location.x)  # Location.x
        creator.write_float(Location.y)  # Location.y
        creator.write_unsigned_byte(Location.sector)  # Location.sector
        creator.write_short(len(Location.players))
        for Player in Location.players:
            creator.write_short(Player.race)  #
            creator.write_int(Player.id)
            creator.write_utf(Player.login)
            creator.write_short(Player.ship['size'])
            creator.write_float(Player.x)  # setPosition
            creator.write_float(Player.y)
            creator.write_int(Player.level)
            creator.write_short(Player.health)
            creator.write_short(Player.energy)
            creator.write_int(Player.avatar)
            creator.write_unsigned_byte(int(Player.speed))
            creator.write_float(Player.targetX)
            creator.write_float(Player.targetY)  # setMovePoint
            creator.write_unsigned_byte(Player.aliance)
            creator.write_unsigned_byte(Player.status)
            creator.write_int(Player.clanId)

            creator.write_unsigned_byte(len(Player.droids))

            for Driod in Player.droids:
                creator.write_unsigned_byte(Driod.id)
                creator.write_short(Driod.type)
                creator.write_short(Driod.weaponClass)
                creator.write_short(Driod.health)

        creator.write_short(len(Location.planets))
        for planet in Location.planets:
            creator.write_unsigned_byte(planet.classNumber)
            creator.write_int(planet.id)
            creator.write_unsigned_byte(planet.race)
            creator.write_int(planet.RADIUS)
            creator.write_int(planet.size)
            creator.write_float(planet.angle)
            creator.write_bool(planet.landable)
            creator.write_unsigned_byte(planet.aliance)
            creator.write_int(planet.clanId)

        creator.write_short(len(Location.StaticSpaceObjects))
        for StaticSpaceObject in Location.StaticSpaceObjects:
            creator.write_int(StaticSpaceObject.StaticSpaceObjectType)
            creator.write_int(StaticSpaceObject.id)
            creator.write_float(StaticSpaceObject.x)
            creator.write_float(StaticSpaceObject.y)
            creator.write_bool(StaticSpaceObject.landable)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def locationBattle(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOCATION_BATTLE
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.LOCATION_BATTLE))

        creator.write_int(self.Player.id)
        creator.write_float(self.Player.x)
        creator.write_float(self.Player.y)
        player_info_data = self.Player.ObjectToReach.players
        creator.write_short(len(player_info_data))
        for ship_data in player_info_data:
            creator.write_short(ship_data.classNumber)
            creator.write_int(ship_data.id)
            creator.write_utf(ship_data.login)
            creator.write_short(ship_data.size)
            creator.write_float(ship_data.x)
            creator.write_float(ship_data.y)
            creator.write_int(ship_data.ship['classNumber'])  # hz
            creator.write_short(ship_data.ship['maxHealth'])
            creator.write_short(ship_data.ship['maxEnergy'])
            creator.write_int(ship_data.ship['classNumber'])  # hz
            creator.write_unsigned_byte(ship_data.aliance)
            creator.write_unsigned_byte(ship_data.status)
            creator.write_int(ship_data.clanId)
            droids = ship_data.droids
            creator.write_unsigned_byte(len(droids))
            for _loc4_ in droids:
                creator.write_unsigned_byte(_loc4_.guid)
                creator.write_short(_loc4_.type)
                creator.write_short(_loc4_.weaponClass)
                creator.write_short(_loc4_.health)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def shoots(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHOOTS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.SHOOTS))
        data = []
        creator.write_short(len(data))
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.id)
            shoot_data = _loc2_.shoot
            creator.write_short(len(shoot_data))
            for shoot in shoot_data:
                _loc5_ = DotMap(shoot)
                creator.write_short(_loc5_.classNumber)
                creator.write_short(_loc5_.damage)
                creator.write_unsigned_byte(_loc5_.destroyedTarget)
                creator.write_int(_loc5_.targetId)
                creator.write_unsigned_byte(_loc5_.targetType)
                creator.write_unsigned_byte(_loc5_.muzzleIndex)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def items(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ITEMS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.ITEMS))
        for item_ in self.Location.inventory:
            creator.write_int(self.Location.id)
            creator.write_short(item_.classNumber)
            creator.write_short(int(item_.x))
            creator.write_short(int(item_.y))
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def message(self, Player, data: dict):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.MESSAGE
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.MESSAGE))
        _loc2_ = DotMap({
            "from_player": Player.login,
            "text": data["text"],
            "type": data['type_chat'],
            "isPrivate": bool(data['private_id']),
            "isAdmin": Player.isAdmin,
        })
        creator.write_utf(_loc2_.from_player)  # name player
        creator.write_utf(_loc2_.text)
        creator.write_unsigned_byte(_loc2_.type)  # 1 - global  2 - local 3 - clanId 4 - trade 5 - client chat
        creator.write_bool(_loc2_.isPrivate)
        creator.write_bool(_loc2_.isAdmin)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def asteroids(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ASTEROIDS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.ASTEROIDS))
        for asteroid in self.Player.SpaceObject.asteroids:
            creator.write_int(asteroid.id)
            creator.write_float(asteroid.x)
            creator.write_float(asteroid.y)
            creator.write_float(asteroid.targetX)
            creator.write_float(asteroid.targetY)
            creator.write_unsigned_byte(asteroid.speed)
            creator.write_int(asteroid.size)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def effectCreated(self, effect_type):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.EFFECT_CREATED
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.EFFECT_CREATED))
        creator.write_int(self.Player.id)
        effects = self.Player.effects
        creator.write_unsigned_byte(len(effects))
        for effect in effects:
            print(f"{effect.targetId=}")
            creator.write_int(effect.targetId)  # time 255)# _loc2_.targetId)
            creator.write_unsigned_byte(2)  # _loc2_.destroyedTarget)
            creator.write_bool(False)  # Мб энергон _loc2_.effectFailed)
        creator.write_unsigned_byte(effect_type)  # EffectType
        _loc8_: float = 20.0
        creator.write_float(_loc8_)  # don't use
        _loc9_: int = 200
        creator.write_int(_loc9_)  # damage damageToShow
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def effectRemoved(self, effect_type):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.EFFECT_REMOVED
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.EFFECT_REMOVED))
        creator.write_int(self.Player.id)
        creator.write_unsigned_byte(effect_type)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def logMessage(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOG_MESSAGE
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.LOG_MESSAGE))
        _loc2_: int = 0
        _loc3_: int = 0
        creator.write_int(_loc2_)
        creator.write_int(_loc3_)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def logMessagestr(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOG_MESSAGE_STRING
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.LOG_MESSAGE_STRING))
        _loc2_: str = ''
        creator.write_utf(_loc2_)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def systemMessage(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SYSTEM_MESSAGE
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.SYSTEM_MESSAGE))
        _loc2_ = 6
        _loc3_ = 5
        creator.write_int(_loc2_)  # SystemMessageType
        creator.write_int(_loc3_)  # hz
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def systemMessagestr(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SYSTEM_MESSAGE_STRING
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.SYSTEM_MESSAGE_STRING))
        _loc2_: str = ''
        creator.write_utf(_loc2_)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def droidBuildingDialog(self, droid):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.DROID_BUILDING_DIALOG
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.DROID_BUILDING_DIALOG))
        creator.write_bytes(droid.guid)  # hz _loc3_.deviceGuid)
        creator.write_int(1)  # len(self.Owner.droids))#len(data))
        # for droids in self.Owner.droids:
        creator.write_bytes(droid.guid)
        creator.write_int(droid.classNumber)
        creator.write_int(droid.level)
        creator.write_int(droid.energyCost)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def hideShip(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.HIDE_SHIP
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.HIDE_SHIP))
        creator.write_int(-13)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def shipDestroyed(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIP_DESTROYED
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.SHIP_DESTROYED))
        creator.write_int(self.Player.id)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def shipJumped(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIP_JUMPED
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.SHIP_JUMPED))
        location = DotMap()
        creator.write_int(location.id)  # findShip
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def clan(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CLAN
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.CLAN))
        data = DataBase().top_clan_list()
        for clan in data:
            clan = DotMap(clan)
            creator.write_int(clan.id)
            creator.write_int(clan.leaderId)
            creator.write_utf(clan.leaderName)
            creator.write_utf(clan.logoFileName)
            creator.write_utf(clan.name)
            creator.write_utf(clan.shortName)
            creator.write_unsigned_byte(clan.aliance)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def playerClan(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_CLAN
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.PLAYER_CLAN))
        _loc5_ = DotMap()
        creator.write_int(_loc5_.id)
        creator.write_int(_loc5_.leaderID)
        creator.write_utf(_loc5_.leaderName)
        creator.write_utf(_loc5_.logoFileName)
        creator.write_utf(_loc5_.name)
        creator.write_utf(_loc5_.shortName)
        creator.write_unsigned_byte(_loc5_.aliace)
        creator.write_utf(_loc5_.description)
        creator.write_short(_loc5_.joinRequestsCount)
        creator.write_int(_loc5_.points)
        creator.write_int(_loc5_.cash)
        creator.write_unsigned_byte(_loc5_.level)
        creator.write_unsigned_byte(_loc5_.maxMembers)
        creator.write_unsigned_byte(_loc5_.maxFriends)
        creator.write_short(_loc5_.friendRequests)
        creator.write_int(_loc5_.currentLevelPoints)
        creator.write_int(_loc5_.nextLevelPoints)
        creator.write_int(_loc5_.nextLevelCash)
        creator.write_int(_loc5_.bonuses)
        # cnt = _loc2_
        data2 = self.Player.Clan
        creator.write_int(len(data2))
        for enemy in data2:
            creator.write_int(enemy)  # _loc5_.enemyClans)
        data2 = []
        creator.write_int(len(data2))
        for friend in data2:
            creator.write_int(friend)  # _loc5_.friendClans)
        data2 = []
        creator.write_int(len(data2))
        for member in data2:
            member = DotMap(member)
            creator.write_int(member.id)
            creator.write_int(member.role)
            creator.write_utf(member.name)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def teamList(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TEAM_LIST
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.TEAM_LIST))
        _loc4_ = None  # : PlayerInfoData
        data = []
        cnt_player_team = len(data)  #
        creator.write_int(cnt_player_team)
        if cnt_player_team > 0:
            Player = DotMap()
            Player.team = DotMap()
            creator.write_int(Player.team.leaderID)
            creator.write_int(Player.team.maxMembers)
            for team in data:
                team = DotMap(team)
                creator.write_int(team.shipId)
                creator.write_int(team.id)
                creator.write_utf(team.name)
        data = []
        creator.write_int(len(data))
        for team in data:
            player = DotMap(team)
            creator.write_int(player.shipId)
            creator.write_int(player.id)
            creator.write_utf(player.name)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def checkValueResult(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CHECK_VALUE_RESULT
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.CHECK_VALUE_RESULT))
        _loc2_ = 5
        _loc3_ = True
        creator.write_int(_loc2_)
        creator.write_bool(_loc3_)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def acceptedClanInfo(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ACCEPTED_CLAN_INFO
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.ACCEPTED_CLAN_INFO))
        _loc2_: int = 0
        _loc3_: str = ''
        _loc4_: str = ''
        _loc5_: str = ''
        _loc6_: int = 0
        creator.write_int(_loc2_)
        creator.write_utf(_loc3_)
        creator.write_utf(_loc4_)
        creator.write_utf(_loc5_)
        creator.write_int(_loc6_)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def clanId(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.clanId
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.clanId))
        player = DotMap()
        creator.write_int(player.clanId)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def clansLetters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CLANS_LETTERS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.CLANS_LETTERS))
        data = []
        for clan in data:
            creator.write_utf(clan)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def clansList(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CLANS_LIST
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.CLANS_LIST))
        data = []
        _loc3_ = self.Player.clan
        creator.write_utf(_loc3_)
        for clan in data:
            creator.write_int(clan)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def clanJoinRequests(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CLAN_JOIN_REQUESTS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.CLAN_JOIN_REQUESTS))
        data = []
        for jounRequest in data:
            player = DotMap(jounRequest)
            creator.write_int(player.playerID)
            creator.write_utf(player.playerName)
            creator.write_utf(player.message)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def logged(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOGGED

        creator.write_int(cfg_const['stateLoop'])
        creator.write_unsigned_byte(cfg_const['bankSendOperationFee'])
        creator.write_int(cfg_const['clanJoinCost'])
        creator.write_unsigned_byte(cfg_const['clanCreateLevelNeed'])
        creator.write_int(cfg_const['bonuses'])

        creator.write_int(self.Player.id)
        creator.write_utf(self.Player.login)
        creator.write_short(self.Player.classNumber)  #
        creator.write_short(self.Player.ship['cpu'])
        creator.write_unsigned_byte(self.Player.race)
        creator.write_unsigned_byte(self.Player.aliance)
        creator.write_unsigned_byte(self.Player.status)
        creator.write_unsigned_byte(self.Player.level)
        creator.write_int(self.Player.clanId)
        creator.write_bool(self.Player.deleteEnqueued)
        creator.write_bool(self.Player.canDelete)
        creator.write_bool(True)
        self.write_skills(creator, self.Player.skills)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def playerInfo(self, id_):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_INFO  # PlayerInfoData
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.PLAYER_INFO))
        Player = DataBase().player_info(id_)
        if not Player:
            return
        creator.write_int(Player.id)
        creator.write_utf(Player.login)
        creator.write_unsigned_byte(Player.level)
        creator.write_unsigned_byte(Player.status)
        creator.write_short(Player.classNumber)
        creator.write_int(Player.clanId)
        creator.write_unsigned_byte(Player.aliance)
        creator.write_unsigned_byte(Player.race)
        creator.write_int(Player.points)
        creator.write_int(Player.role)
        print(
            f"PLAYER info {Player.id=}, {Player.login=}, {Player.level=}, {Player.status=}, {Player.classNumber=}, {Player.clanId=}, {Player.aliance=}, {Player.race=}, {Player.points=}, {Player.role=}")
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def playerLoggedOn(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_LOGGED_ON
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.PLAYER_LOGGED_ON))
        creator.write_int(self.Player.id)
        creator.write_utf(self.Player.name)
        creator.write_int(self.Player.clanId)
        creator.write_int(self.Player.level)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def playerLoggedOff(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_LOGGED_OFF
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.PLAYER_LOGGED_OFF))
        creator.write_int(self.Player.id)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def friendClans(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.FRIEND_CLANS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.FRIEND_CLANS))
        data = []
        for friend in data:
            ClanData = DotMap(friend)
            creator.write_int(ClanData.id)
            creator.write_int(ClanData.leaderID)
            creator.write_utf(ClanData.leaderName)
            creator.write_utf(ClanData.logoFileName)
            creator.write_utf(ClanData.name)
            creator.write_utf(ClanData.shortName)
            creator.write_unsigned_byte(ClanData.aliace)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def enemyClans(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ENEMY_CLANS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.ENEMY_CLANS))
        data = []
        for enemy in data:
            ClanData = DotMap(enemy)
            creator.write_int(ClanData.id)
            creator.write_int(ClanData.leaderID)
            creator.write_utf(ClanData.leaderName)
            creator.write_utf(ClanData.logoFileName)
            creator.write_utf(ClanData.name)
            creator.write_utf(ClanData.shortName)
            creator.write_unsigned_byte(ClanData.aliace)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def friendRequests(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.FRIEND_REQUESTS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.FRIEND_REQUESTS))
        data = []
        for friend in data:  # clanId Data
            friendRequests = DotMap(friend)
            creator.write_int(friendRequests.id)
            creator.write_int(friendRequests.leaderID)
            creator.write_utf(friendRequests.leaderName)
            creator.write_utf(friendRequests.logoFileName)
            creator.write_utf(friendRequests.name)
            creator.write_utf(friendRequests.shortName)
            creator.write_unsigned_byte(friendRequests.aliace)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def droidEvent(self, event_type, Droid):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.DROID_EVENT
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.DROID_EVENT))

        creator.write_unsigned_byte(event_type)
        creator.write_short(Droid.classNumber)
        creator.write_short(Droid.weaponClass)
        creator.write_int(self.Player.id)
        print(len(self.Player.droids))
        creator.write_unsigned_byte(len(self.Player.droids))
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def updateValue(self, num_pack):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.UPDATE_VALUE
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.UPDATE_VALUE))
        creator.write_unsigned_byte(num_pack)
        match num_pack:
            case 1:
                value = self.Player.Clan.cash  # clan Cash
            case 2:
                value = self.Player.Clan.get_rating
            case 3:
                value = self.Player.points  # Owner.point
            case 4:
                value = ClanFriendRequests
            case 5:
                value = self.Player.Clan.level
            case 6:
                value = self.Player.Clan.nextLevelPointsValue
            case 7:
                value = self.Player.Clan.maxMembers
            case 8:
                value = ClanJoinRequestStatus
            case 9:
                value = self.Player.cash
            case 10:
                value = self.Player.ControlUsed
            case 11:
                value = self.Player.ControlLeft
            case 12:
                value = self.Player.clanId
            case 13:
                value = self.Player.bonus
            case 14:
                value = 20  # self.Owner.HyperRadius
            case 15:
                value = 20  # self.Owner.HyperCost
            case 16:
                value = self.Player.ClanLeader
            case 17:
                value = self.Player.ClanBonuses
        creator.write_int(int(value))
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def missions(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.MISSIONS
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.MISSIONS))
        _loc5_ = DotMap()
        creator.write_int(_loc5_.id)
        _loc5_.current = True
        _loc6_ = 6
        _loc7_ = 7
        creator.write_unsigned_byte(_loc6_)
        creator.write_unsigned_byte(_loc7_)
        data_reachable_system = []
        creator.write_unsigned_byte(len(data_reachable_system))
        for system in data_reachable_system:
            system = DotMap(system)
            creator.write_int(system.id)
        data = []  # PlanetData
        for planet in data:
            planet = DotMap(planet)
            creator.write_int(planet.id)
            creator.write_bytes(planet.classNumber)
            creator.write_unsigned_byte(planet.aliance)
            creator.write_unsigned_byte(planet.race)
            creator.write_int(planet.starId)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def tradeInvitation(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TRADE_INVITATION
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.TRADE_INVITATION))
        _loc2_: int = 0
        _loc3_: int = 0
        _loc4_: str = ''
        creator.write_int(_loc2_)
        creator.write_int(_loc3_)
        creator.write_utf(_loc4_)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def showTrading(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHOW_TRADING
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.SHOW_TRADING))
        _loc2_: int = 0
        _loc3_: int = 0
        _loc4_: str = ''
        _loc5_: list = []
        creator.write_int(_loc2_)
        creator.write_int(_loc3_)
        creator.write_utf(_loc4_)
        self._write_items(creator, True, True)
        self.Game.id_to_conn[self.id].send(creator.get_package())

    def toGame(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TO_GAME
        Pac = ServerRequest()
        print('Пакет отправлен', Pac.get(ServerRequest.TO_GAME))
        self.Game.id_to_conn[self.id].send(creator.get_package())
