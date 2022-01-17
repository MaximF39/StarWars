from .PackagesEntry import PackagesEntry
from ..Utils.DotMap import DotMap
from python.Static.Type.ServerRequest import ServerRequest
from ..Packages.PackageCreator import PackageCreator
from python.Static.ParseXml import parse_xml

class EntryPac:

    def __init__(self, id_: int, StarWars):
        self.id = id_
        self.Game = StarWars
        self.Player = getattr(self.Game, f'Player_{self.id}')
        self.Location = self.Player.Location

    @staticmethod
    def isValidPackageLength(creator: int) -> bool:
        return 0 <= creator < 60000

    def processPackages(self, _loc1_: ServerRequest, *args):
        _loc2_: list = list()
        match _loc1_:
            case ServerRequest.VERSION:
                return self.version()
            case ServerRequest.ONLINE:
                return self.online()
            case ServerRequest.TOP_LIST:
                return self.topList()
            case ServerRequest.TOP_RATING_LIST:
                return self.topRatingList()
            case ServerRequest.TOP_CLANS_LIST:
                return self.topClansList(*args)
            case ServerRequest.WEAPONS_PARAMETERS:
                return self.weaponsParameters()
            case ServerRequest.RESOURCE_PARAMETERS:
                return self.resourceParameters()
            case ServerRequest.ENGINES_PARAMETERS:
                return self.engineParameters()
            case ServerRequest.DEVICE_PARAMETERS:
                return self.deviceParameters()
            case ServerRequest.DROID_PARAMETERS:
                return self.droidParameters()
            case ServerRequest.MAP:
                return self.map()
            case ServerRequest.SHIP_PARAMETERS:
                return self.shipParameters()
            case ServerRequest.LOGGED:
                return self.logged()
            case ServerRequest.PLAYER:
                return self.player()
            case ServerRequest.PLAYER_SHIP:
                return self.playerShip()
            case ServerRequest.TO_GAME:
                return self.toGame(*args)
            case ServerRequest.LOCATION_SYSTEM:
                return self.locationSystem()
            case ServerRequest.ACTIVE_DEVICES:
                return self.activeDevices()
            case ServerRequest.ACTIVE_WEPONS:
                return self.activeWeapons()
            case ServerRequest.UPDATE_VALUE:
                return self.updateValue(*args)
            case ServerRequest.PLAYER_SKILLS_DATA:
                return self.playerSkillsData()
            case ServerRequest.CLAN:
                return self.clan()
            case ServerRequest.SHIPS_POSITION:
                return self.shipsPosition()
            case ServerRequest.SHIPS_STASE:
                return self.shipsState()
            case ServerRequest.HIDE_SHIP:
                return self.hideShip()
            case ServerRequest.AMMOS_PARAMETERS:
                return self.ammoParameters()

    def version(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.VERSION
        version = '0.9.0.1'
        creator.write_utf(version)
        return creator.get_package()

    def online(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ONLINE
        creator.write_int(1)
        creator.write_int(self.Game.online)
        return creator.get_package()

    def topList(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TOP_LIST
        all_player = PackagesEntry(self.Game, self.id).top_list
        cnt: int = len(all_player)
        creator.write_int(cnt)
        for i in all_player:
            _loc2_ = i
            creator.write_utf(_loc2_.login)
            creator.write_int(_loc2_.level)
            creator.write_int(_loc2_.experience)
            creator.write_int(_loc2_.clan_id)
            creator.write_unsigned_byte(_loc2_.race)
            creator.write_short(_loc2_.shipClass)
        return creator.get_package()

    def topRatingList(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TOP_RATING_LIST
        top_players = PackagesEntry(self.Game, self.id).top_rating_list
        cnt: int = len(top_players)
        creator.write_int(cnt)
        for i in top_players:
            _loc2_ = i
            creator.write_utf(_loc2_.login)
            creator.write_int(_loc2_.level)
            creator.write_int(_loc2_.points)
            creator.write_int(_loc2_.clanId)
            creator.write_unsigned_byte(_loc2_.race)
            creator.write_short(_loc2_.shipClass)
        return creator.get_package()

    def topClansList(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TOP_CLANS_LIST
        players = PackagesEntry(self.Game, self.id).top_clan_list
        cnt: int = len(players)
        creator.write_int(cnt)
        for i in players:
            _loc2_ = i
            creator.write_int(_loc2_.id)
            creator.write_int(_loc2_.points)
            creator.write_int(_loc2_.leaderID)
            creator.write_unsigned_byte(_loc2_.aliance)
            creator.write_unsigned_byte(_loc2_.level)
            creator.write_utf(_loc2_.name)
            creator.write_utf(_loc2_.shortName)
            creator.write_utf(_loc2_.logoFileName)
        return creator.get_package()

    def weaponsParameters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.WEAPONS_PARAMETERS
        data_weapons = parse_xml("WeaponParameters")
        cnt_weapon: int = len(data_weapons)
        creator.write_int(cnt_weapon)
        for i in data_weapons:
            _loc2_ = DotMap(i)
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
            for i in restr['data']:
                _loc5_ = DotMap(i)
                creator.write_unsigned_byte(_loc5_.type)
                creator.write_unsigned_byte(_loc5_.valueType)
                creator.write_int(_loc5_.Value)
        return creator.get_package()

    def ammoParameters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.AMMOS_PARAMETERS
        data_ammo = parse_xml("AmmoParameters")
        cnt_ammo: int = len(data_ammo)
        creator.write_int(cnt_ammo)
        for i in data_ammo:
            _loc2_ = DotMap(i)  # AmmoParameters()
            creator.write_int(_loc2_.classNumber)
            creator.write_float(_loc2_.size)
            creator.write_int(_loc2_.cost)
            creator.write_int(_loc2_.damage)
        return creator.get_package()

    def resourceParameters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.RESOURCE_PARAMETERS
        data_resourse = parse_xml('ResourseParameters')
        creator.write_int(len(data_resourse))
        for i in data_resourse:
            _loc2_ = DotMap(i)  # ResourceParameters()
            creator.write_int(_loc2_.classNumber)
            creator.write_float(_loc2_.size)
            creator.write_int(_loc2_.cost)
        return creator.get_package()

    def deviceParameters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.DEVICE_PARAMETERS
        data_device = parse_xml("DeviceParameters")
        creator.write_int(len(data_device))
        for i in data_device:
            _loc4_ = DotMap(i)
            creator.write_int(_loc4_.classNumber)
            creator.write_float(_loc4_.size)
            creator.write_int(_loc4_.cost)
            creator.write_int(_loc4_.energyCost)
            creator.write_int(_loc4_.reloadTime)
            creator.write_int(_loc4_.maxWear)

            cnt_dev_eff = _loc4_.effects['Length']
            creator.write_unsigned_byte(cnt_dev_eff)
            data_dev_eff = _loc4_.effects['data']
            for effect in data_dev_eff:
                _loc3_ = DotMap(effect)  # DeviceEffect()
                creator.write_unsigned_byte(_loc3_.targetType)
                creator.write_int(_loc3_.value)
                creator.write_int(_loc3_.effectTime)
                creator.write_unsigned_byte(_loc3_.effectType)

            cnt_dev_restr = _loc4_.restrictions['Length']
            creator.write_unsigned_byte(cnt_dev_restr)
            data_dev_restr = _loc4_.restrictions["data"]
            for rest in data_dev_restr:
                _loc8_ = DotMap(rest)  # Restriction()
                creator.write_unsigned_byte(_loc8_.type)
                creator.write_unsigned_byte(_loc8_.valueType)
                creator.write_int(_loc8_.Value)
        return creator.get_package()

    def droidParameters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.DROID_PARAMETERS
        data_droids = parse_xml("DroidParameters")
        creator.write_int(len(data_droids))
        for i in data_droids:
            _loc2_ = DotMap(i)  # DroidParameters()
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
            for i in data_restr:
                _loc5_ = DotMap(i)  # Restriction()
                creator.write_unsigned_byte(_loc5_.type)
                creator.write_unsigned_byte(_loc5_.valueType)
                creator.write_int(_loc5_.Value)
        return creator.get_package()

    #     #
    def shipParameters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIP_PARAMETERS
        data_ship = parse_xml('ShipParameters')
        creator.write_int(len(data_ship))
        for i in data_ship:
            _loc2_ = DotMap(i)
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
            for i in data_restr:
                _loc7_ = DotMap(i)
                creator.write_unsigned_byte(_loc7_.type)
                creator.write_unsigned_byte(_loc7_.valueType)
                creator.write_int(_loc7_.Value)
            cnt_ship_feat = _loc2_.features['Length']
            creator.write_unsigned_byte(cnt_ship_feat)
            data_ship_feat = _loc2_.features['data']
            for i in data_ship_feat:
                _loc8_ = DotMap(i)
                creator.write_unsigned_byte(_loc8_.type)
                creator.write_int(_loc8_.Value)
        return creator.get_package()

    def engineParameters(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ENGINES_PARAMETERS
        data_engine = parse_xml("EngineParameters")
        creator.write_int(len(data_engine))
        for i in data_engine:
            _loc2_ = DotMap(i)  # EngineParameters()
            creator.write_short(_loc2_.classNumber)
            creator.write_float(_loc2_.size)
            creator.write_int(_loc2_.cost)
            creator.write_unsigned_byte(_loc2_.hyperjumpRadius)
            creator.write_int(_loc2_.maxWear)
            creator.write_unsigned_byte(_loc2_.energyCost)
        return creator.get_package()

    #     #
    def map(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.MAP
        data_system = parse_xml('GalaxyMap')
        creator.write_short(len(data_system))
        for i in data_system:
            _loc2_ = DotMap(i)  # ReachableSystem()
            creator.write_unsigned_byte(_loc2_.id)
            creator.write_unsigned_byte(_loc2_.classNumber)
            creator.write_short(_loc2_.x)
            creator.write_short(_loc2_.y)
            creator.write_unsigned_byte(_loc2_.Sector)
            creator.write_unsigned_byte(_loc2_.lineTo)
            cnt_planet = _loc2_.Planets['Length']
            creator.write_unsigned_byte(cnt_planet)
            data_planet = _loc2_.Planets['data']
            for i in data_planet:
                _loc7_ = DotMap(i)  # PlanetData()
                creator.write_short(_loc7_.id)
                creator.write_unsigned_byte(_loc7_.race)
                creator.write_unsigned_byte(_loc7_.classNumber)
                creator.write_unsigned_byte(_loc7_.aliance)
            cnt_space_objects = _loc2_.SpaceObjects['Length']
            creator.write_unsigned_byte(cnt_space_objects)
            data_space_objects = _loc2_.SpaceObjects['data']
            for i in data_space_objects:
                _loc8_ = DotMap(i)  # StaticObjectData()
                creator.write_unsigned_byte(_loc8_.type)
                creator.write_unsigned_byte(_loc8_.aliance)
                creator.write_unsigned_byte(_loc8_.race)
        return creator.get_package()

    def logged(self):
        from ..cfg.cfg_const import cfg_const
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOGGED
        logged = DotMap({
            'stateLoop': cfg_const['stateLoop'],
            'bankSendOperationFee': cfg_const['bankSendOperationFee'],
            'clanJoinCost': cfg_const['clanJoinCost'],
            'clanCreateLevelNeed': cfg_const['clanCreateLevelNeed'],
            'bonuses': cfg_const['bonuses']
        })
        creator.write_int(logged.stateLoop)
        creator.write_unsigned_byte(logged.bankSendOperationFee)
        creator.write_int(logged.clanJoinCost)
        creator.write_unsigned_byte(logged.clanCreateLevelNeed)
        creator.write_int(logged.bonuses)
        # while True:
        logged2 = DotMap({
            'id': self.Player.id,
            'name': self.Player.login,
            'shipClass': self.Player.ship['classNumber'],
            'shipCPU': self.Player.ship["cpu"],
            'race': self.Player.race,
            'aliance': self.Player.aliance,
            'status': self.Player.status,
            'level': self.Player.level,
            'clanId': self.Player.clanId,
            'deleteEnqueued': self.Player.deleteEnqueued,
            'canDelete': self.Player.canDelete,
            'logged': self.Player.logged,
            'skills': self.Player.skills
        })
        creator.write_int(logged2.id)
        creator.write_utf(logged2.name)
        creator.write_short(logged2.shipClass) #
        creator.write_short(logged2.shipCPU)
        creator.write_unsigned_byte(logged2.race)
        creator.write_unsigned_byte(logged2.aliance)
        creator.write_unsigned_byte(logged2.status)
        creator.write_unsigned_byte(logged2.level)
        creator.write_int(logged2.clanId)
        creator.write_bool(logged2.deleteEnqueued)
        creator.write_bool(logged2.canDelete)
        creator.write_bool(logged2.logged) # Отвечает за вход
        self.write_skills(creator, logged2.skills)
        return creator.get_package()

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

    def player(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER
        Player = DotMap({
            "id": self.Player.id,
            "login": self.Player.login,
            "level": self.Player.level,
            "cash": self.Player.cash,
            "race": self.Player.race,
            "avatar": self.Player.avatar,
            "aliance": self.Player.aliance,
            "clanId": self.Player.clanId,
            "role": self.Player.role,
            "clanRequestStatus": self.Player.clanRequestStatus,
            "clanJoinRequestStatus": self.Player.clanJoinRequestStatus,
            "PlayerRelation": self.Player.PlayerRelation,
        })
        creator.write_int(Player.id)
        creator.write_utf(Player.login)
        creator.write_int(Player.level)
        creator.write_int(Player.cash)
        creator.write_unsigned_byte(Player.race)
        creator.write_int(Player.avatar)
        creator.write_unsigned_byte(Player.aliance)
        creator.write_int(Player.clanId)
        creator.write_int(Player.role)
        creator.write_unsigned_byte(Player.clanRequestStatus)
        creator.write_unsigned_byte(Player.clanJoinRequestStatus)
        creator.write_int(Player.PlayerRelation)
        return creator.get_package()


    def playerShip(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_SHIP
        ship = DotMap({
            'id': self.Player.ship['id'],
            'login': self.Player.ship['login'],
            'race': self.Player.ship['race'],
            'size': self.Player.ship['size'],
            'energy': self.Player.ship["energy"],
            'maxEnergy': self.Player.ship["maxEnergy"],
            'setPosition': self.Player.ship["setPosition"],
            'team': self.Player.ship["team"],
            'maxSpeed': 180, # self.Player.ship["maxSpeed"]
            'weaponSlots': self.Player.ship["weaponSlots"],
            'deviceSlots': self.Player.ship["deviceSlots"],
            'maxHealth': self.Player.ship["maxHealth"],
            'radarRadius': self.Player.ship["radar"],
            'cpu': self.Player.ship["cpu"],
        })
        creator.write_int(ship.race) # raca
        creator.write_int(ship.id)
        creator.write_utf(ship.login)
        creator.write_int(ship.size)
        creator.write_int(ship.energy)
        creator.write_int(ship.maxEnergy)
        creator.write_float(ship.setPosition[0])
        creator.write_float(ship.setPosition[1])
        creator.write_int(ship.team)
        creator.write_unsigned_byte(180) # ship.maxSpeed
        creator.write_unsigned_byte(ship.weaponSlots)
        creator.write_unsigned_byte(ship.deviceSlots)
        creator.write_int(ship.maxHealth)
        creator.write_short(ship.radarRadius)
        creator.write_short(ship.cpu)
        return creator.get_package()

    def toGame(self, mod=False):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.TO_GAME
        if not mod:
            pass
        else:
            return creator.get_package()


    def locationSystem(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.LOCATION_SYSTEM
        
        location = [self.Location.id, self.Location.x, self.Location.y, self.Location.sector]
        players = []
        for player_ in self.Location.players:
            players.append(DotMap({
                "player": DotMap({
                    "level": player_.level,
                    "avatar": player_.avatar,
                    "aliance": player_.aliance,
                    "status": player_.status,
                    "clanId": player_.clanId,
                }),
                "race": player_.race,
                "id": player_.id,
                "Name": player_.login,

                "size": player_.ship["size"],
                "set_x": player_.x,
                "set_y": player_.y,
                "maxHealth": player_.ship["maxHealth"],
                "maxEnergy": player_.ship["maxEnergy"],
                "maxSpeed": 180, # player_.ship["maxSpeed"]
                "mov_x": player_.mov_x,
                "mov_y": player_.mov_y,
                "droid": player_.droid,
            }))
        planets = []
        for planet in self.Location.planets:
            planets.append(DotMap({
                "PlanetClass": planet.classNumber,
                "id": planet.id,
                "race": planet.race,
                "radius": planet.radius,
                "size": planet.size,
                "angle": planet.angle,
                "landable": planet.landable,
                "aliance": planet.aliance,
                "clanId": planet.clanId,
            }))
        static_space_objects = []
        for static_space_object in self.Location.StaticSpaceObjects:
            static_space_objects.append(DotMap(({
                "StaticSpaceObjectType": static_space_object.StaticSpaceObjectType,
                "id": static_space_object.id,
                "x": static_space_object.x,
                "y": static_space_object.y,
                "landable": static_space_object.landable,
            })))

        creator.write_int(location[0]) # id
        creator.write_float(location[1])  # Location.x
        creator.write_float(location[2])  # Location.y
        creator.write_unsigned_byte(location[3])  # Location.sector
        creator.write_short(len(players))
        for i in players:
            _loc2_ = DotMap(i)
            creator.write_short(_loc2_.race) #
            creator.write_int(_loc2_.id)
            creator.write_utf(_loc2_.Name)
            creator.write_short(_loc2_.size)
            creator.write_float(_loc2_.set_x)  # setPosition
            creator.write_float(_loc2_.set_y)
            creator.write_int(_loc2_.player.level)
            creator.write_short(_loc2_.maxHealth)
            creator.write_short(_loc2_.maxEnergy)
            creator.write_int(_loc2_.player.avatar)
            creator.write_unsigned_byte(int(_loc2_.maxSpeed))
            creator.write_float(_loc2_.mov_x)
            creator.write_float(_loc2_.mov_y)  # setMovePoint
            creator.write_unsigned_byte(_loc2_.player.aliance)
            creator.write_unsigned_byte(_loc2_.player.status)
            creator.write_int(_loc2_.player.clanId)

            creator.write_unsigned_byte(len(_loc2_.droid))

            for droid in _loc2_.droid:
                _loc4_ = DotMap(droid)
                creator.write_unsigned_byte(_loc4_.id)
                creator.write_short(_loc4_.type)
                creator.write_short(_loc4_.weaponClass)
                creator.write_short(_loc4_.health)

        creator.write_short(len(planets))
        for planet in planets:
            _loc6_ = DotMap(planet)
            creator.write_unsigned_byte(_loc6_.PlanetClass)
            creator.write_int(_loc6_.id)
            creator.write_unsigned_byte(_loc6_.race)
            creator.write_int(_loc6_.radius)
            creator.write_int(_loc6_.size)
            creator.write_float(_loc6_.angle)
            creator.write_bool(_loc6_.landable)
            creator.write_unsigned_byte(_loc6_.aliance)
            creator.write_int(_loc6_.clanId)

        creator.write_short(len(static_space_objects))
        for static_space_object in static_space_objects:
            _loc7_ = DotMap(static_space_object)
            creator.write_int(_loc7_.StaticSpaceObjectType)
            creator.write_int(_loc7_.id)
            creator.write_float(_loc7_.x)
            creator.write_float(_loc7_.y)
            creator.write_bool(_loc7_.landable)

        return creator.get_package()

    def activeDevices(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ACTIVE_DEVICES
        player = getattr(self.Game, f"Player_{self.id}")
        data_active_device = player.active_devices
        creator.write_unsigned_byte(len(data_active_device))
        for i in data_active_device:
            _loc3_ = DotMap(i)
            creator.write_short(_loc3_.id)
            creator.write_bytes(_loc3_.guid)
            creator.write_float(_loc3_.reloadedTime)

        return creator.get_package()

    def activeWeapons(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.ACTIVE_WEPONS
        player = getattr(self.Game, f"Player_{self.id}")
        data_active_weapons = player.active_weapons
        creator.write_unsigned_byte(len(data_active_weapons))
        for i in data_active_weapons:
            _loc2_ = i
            creator.write_short(_loc2_['classfloat'])
            creator.write_unsigned_byte(_loc2_["index"])
        return creator.get_package()

    def updateValue(self, num_pack, value=0):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.UPDATE_VALUE
        creator.write_unsigned_byte(num_pack)
        creator.write_int(value)
        return creator.get_package()


    def playerSkillsData(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.PLAYER_SKILLS_DATA
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
        return creator.get_package()

    def clan(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.CLAN
        data = parse_xml('Clan')  # Если больше 1 клан, то сломается
        for i in data:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.id)
            creator.write_int(_loc2_.leaderID)
            creator.write_utf(_loc2_.leaderName)
            creator.write_utf(_loc2_.logoFileName)
            creator.write_utf(_loc2_.name)
            creator.write_utf(_loc2_.shortName)
            creator.write_unsigned_byte(_loc2_.alliance)
        return creator.get_package()

    def shipsPosition(self):
        """ id, x, y, targetX, targetY """
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIPS_POSITION
        player = getattr(self.Game, f"Player_{self.id}")
        data_ship_position = [{'id': player.id, 'x': player.x, 'y': player.y, 'targetX': player.target_x, 'targetY': player.target_y}]
        creator.write_int(len(data_ship_position))
        for dict_ in data_ship_position:
            creator.write_int(dict_["id"])
            creator.write_float(dict_["x"])
            creator.write_float(dict_["y"])
            creator.write_float(dict_["targetX"])
            creator.write_float(dict_["targetY"])
        return creator.get_package()

    def shipsState(self):
        """id, speed, health, energy, PlayerRelation"""
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.SHIPS_STASE
        player = getattr(self.Game, f"Player_{self.id}")
        data_ship_state = [
            {'id': player.ship["id"], 'speed': player.ship["speed"], 'health': player.ship["health"],
             'energy': player.ship["energy"],
             'PlayerRelation': player.PlayerRelation}]
        for i in data_ship_state:
            _loc2_ = DotMap(i)
            creator.write_int(_loc2_.id)
            creator.write_unsigned_byte(_loc2_.speed)
            creator.write_short(_loc2_.health)
            creator.write_short(_loc2_.energy)
            creator.write_short(_loc2_.PlayerRelation)
        return creator.get_package()

    def hideShip(self):
        creator = PackageCreator()
        creator.PackageNumber = ServerRequest.HIDE_SHIP
        creator.write_int(-15)
        return creator.get_package()



