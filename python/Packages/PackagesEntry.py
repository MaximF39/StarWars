import json

from python.MyUtils.DotMap import DotMap
from python.DataBase.SQL_Table import PlayerDB
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from python.cfg.cfg_postgres import *
from python.cfg.cfg_const import cfg_const
from sqlalchemy import func

engine = create_engine(f"postgresql+psycopg2://{db_name_user}:{db_passwd_user}@{host}:{port}/{db_name}")
session = sessionmaker(bind=engine)
s = session()

class PackagesEntry:
    def __init__(self, Game, id_):
        self.id = id_
        self.Game = Game

    @property
    def top_list(self):
        res2 = s.query(PlayerDB, func.max(PlayerDB.id).over(order_by=PlayerDB.experience))
        data = []
        for top_player, _ in res2[:-10:-1] if len(list(res2)) > 10 else res2[::-1]:
            data.append(DotMap({
                "login": top_player.login,
                "level": top_player.level,
                "experience": top_player.experience,
                "clan_id": top_player.clan_id,
                "race": top_player.race,
                "shipClass": top_player.ship_class,
            }))
        return data

    @property
    def top_clan_list(self):
        res = [DotMap({
            'id': 184,
            'points': 7343124,
            'leaderID': 1523,
            'aliace': 2,
            'level': 1,
            'name': 'Id 55maxik55 шмот дешего',
            'shortName': 'VK',
            'logoFileName': ''
        })]
        return res

    @property
    def top_rating_list(self):
        res2 = s.query(PlayerDB, func.max(PlayerDB.id).over(order_by=PlayerDB.rating))
        data = []
        for top_player, _ in res2[:-10:-1] if len(list(res2)) > 10 else res2[::-1]:
            data.append(DotMap({
                "login": top_player.login,
                "level": top_player.level,
                "points": top_player.rating,
                "clanId": top_player.clan_id,
                "race": top_player.race,
                "shipClass": top_player.ship_class,
            }))
        return data

    @property
    def logged(self):
        from ..cfg.cfg_const import cfg_const
        res = DotMap({
            'stateLoop': cfg_const['stateLoop'],
            'bankSendOperationFee': cfg_const['bankSendOperationFee'],
            'clanJoinCost': cfg_const['clanJoinCost'],
            'clanCreateLevelNeed': cfg_const['clanCreateLevelNeed'],
            'bonuses': cfg_const['bonuses']
        })
        return res

    @property
    def create_pilot(self):
        for Player in s.query(PlayerDB).filter_by(id=self.id):
            return {
            "id": Player.id,
            "login": Player.login,
            "auth_key": Player.auth_key,
            "passwd": Player.passwd,
            "clan_id": Player.clan_id,
            "credit": Player.credit,
            "bonus": Player.bonus,
            "SpaceObject": Player.SpaceObject,
            "Location": Player.Location,
            "level": Player.level,
            'repository': eval(Player.repository),
            "experience": Player.experience,
            "status": Player.status,
            "clanRequestStatus": Player.clanRequestStatus,
            "clanJoinRequestStatus": Player.clanJoinRequestStatus,
            "PlayerRelation": Player.PlayerRelation,
            "race": Player.race,
            "avatar": Player.avatar,
            "aliance": Player.aliance,
            "role": Player.role,
            "ship_class": Player.ship_class,
            "skills": Player.skills,
            "free_skills": Player.free_skills,
            "expSkillGrowCoef": Player.expSkillGrowCoef,
            "expSkillReduserCoef": Player.expSkillReduserCoef,
            "point": Player.point,
            "x": Player.x,
            "y": Player.y,
            "deleteEnqueued": Player.deleteEnqueued,
            "canDelete": Player.canDelete,
            "logged": Player.logged,
            "active_devices": eval(Player.active_devices)['data'],
            "active_weapons": eval(Player.active_weapons)['data'],
            "rating": Player.rating,
            "inventory": eval(Player.inventory),
            }

    @property
    def active_device(self):
        player = getattr(self.Game, f"Player_{self.id}")
        return player.active_devices

    @property
    def location_system(self):
        Location = getattr(self.Game, f"Player_{self.id}").Location
        location = [Location.id, Location.x, Location.y, Location.sector]
        players = []
        for player_ in Location.players:
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
                "maxSpeed": player_.ship["maxSpeed"],
                "mov_x": player_.mov_x,
                "mov_y": player_.mov_y,
                "droid": player_.droid,
            }))
        planets = []
        for planet in Location.planets:
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
        for static_space_object in Location.StaticSpaceObjects:
            static_space_objects.append(DotMap(({
                "StaticSpaceObjectType": static_space_object.StaticSpaceObjectType,
                "id": static_space_object.id,
                "x": static_space_object.x,
                "y": static_space_object.y,
                "landable": static_space_object.landable,
            })))
        return [location, players, planets, static_space_objects]

    @property
    def player_ship(self):
        ship = getattr(self.Game, f"Player_{self.id}").ship
        return DotMap({
            'id': ship['id'],
            'login': ship['login'],
            'race': ship['race'],
            'size': ship['size'],
            'energy': ship["energy"],
            'maxEnergy': ship["maxEnergy"],
            'setPosition': ship["setPosition"],
            'team': ship["team"],
            'maxSpeed': ship["maxSpeed"],
            'weaponSlots': ship["weaponSlots"],
            'deviceSlots': ship["deviceSlots"],
            'maxHealth': ship["maxHealth"],
            'radarRadius': ship["radar"],
            'cpu': ship["cpu"],
        })

    @property
    def player(self):
        player = getattr(self.Game, f"Player_{self.id}")
        return DotMap({
            "id": player.id,
            "login": player.login,
            "level": player.level,
            "cash": player.cash,
            "race": player.race,
            "avatar": player.avatar,
            "aliance": player.aliance,
            "clanId": player.clanId,
            "role": player.role,
            "clanRequestStatus": player.clanRequestStatus,
            "clanJoinRequestStatus": player.clanJoinRequestStatus,
            "PlayerRelation": player.PlayerRelation,
        })

    @property
    def active_weapon(self):
        player = getattr(self.Game, f"Player_{self.id}")
        return player.active_weapons

    @property
    def logged2(self):
        player_ = getattr(self.Game, f"Player_{self.id}")
        return DotMap({
            'id': player_.id,
            'name': player_.login,
            'shipClass': player_.ship['classNumber'],
            'shipCPU': player_.ship["cpu"],
            'race': player_.race,
            'aliance': player_.aliance,
            'status': player_.status,
            'level': player_.level,
            'clanId': player_.clanId,
            'deleteEnqueued': player_.deleteEnqueued,
            'canDelete': player_.canDelete,
            'logged': player_.logged,
            'skills': player_.skills
        })
