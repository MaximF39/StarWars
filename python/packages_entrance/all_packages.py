import json

from ..MyUtils.DotMap import DotMap
from python.DataBase.SQL_Table import PlayerDB
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from python.cfg.cfg_postgres import *
from ..cfg.cfg_const import cfg_const
from sqlalchemy import func

engine = create_engine(f"postgresql+psycopg2://{db_name_user}:{db_passwd_user}@{host}:{port}/{db_name}")
session = sessionmaker(bind=engine)
s = session()


def top_list():
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


def top_clan_list():
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


def top_rating_list():
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


def logged():
    from ..cfg.cfg_const import cfg_const
    res = DotMap({
        'stateLoop': cfg_const['stateLoop'],
        'bankSendOperationFee': cfg_const['bankSendOperationFee'],
        'clanJoinCost': cfg_const['clanJoinCost'],
        'clanCreateLevelNeed': cfg_const['clanCreateLevelNeed'],
        'bonuses': cfg_const['bonuses']
    })
    return res

def create_pilot(id_):
    for i in s.query(PlayerDB).filter_by(id=id_):
        return {
        "id": i.id,
        "login": i.login,
        "auth_key": i.auth_key,
        "passwd": i.passwd,
        "clan_id": i.clan_id,
        "credit": i.credit,
        "bonus": i.bonus,
        "planet": i.planet,
        "location": i.location,
        "level": i.level,
        "experience": i.experience,
        "status": i.status,
        "clanRequestStatus": i.clanRequestStatus,
        "clanJoinRequestStatus": i.clanJoinRequestStatus,
        "PlayerRelation": i.PlayerRelation,
        "race": i.race,
        "avatar": i.avatar,
        "aliance": i.aliance,
        "role": i.role,
        "ship_class": i.ship_class,
        "skills": i.skills,
        "free_skills": i.free_skills,
        "expSkillGrowCoef": i.expSkillGrowCoef,
        "expSkillReduserCoef": i.expSkillReduserCoef,
        "pointStatus": i.pointStatus,
        "x": i.x,
        "y": i.y,
        "deleteEnqueued": i.deleteEnqueued,
        "canDelete": i.canDelete,
        "logged": i.logged,
        "active_devices": eval(i.active_devices)['data'],
        "active_weapons": eval(i.active_weapons)['data'],
        "rating": i.rating,
        "inventory": i.inventory,
        "repository_station": i.repository_station,
        }

def ship_position(Game, id_):
    player = getattr(Game, f"Player_{id_}")
    return [{'id': player.id, 'x': player.x, 'y': player.y, 'targetX': player.target_x, 'targetY': player.target_y}]


def hide_ship(Game, id_):
    return -13


def ship_state(Game, id_):
    player = getattr(Game, f"Player_{id_}")
    return [
        {'id': player.ship["id"], 'speed': player.ship["speed"], 'health': player.ship["health"], 'energy': player.ship["energy"],
         'PlayerRelation': player.PlayerRelation}]


def player_skills(Game, id_):
    player = getattr(Game, f"Player_{id_}")
    return player.skills

def player_skills_data(Game, id_):
    player = getattr(Game, f"Player_{id_}")
    return [{'level': player.level, 'experience': player.experience, 'expForNext': player.expForNext,
             'skills': player_skills(Game, id_), 'freeSkills': player.freeSkills,
             'expForFirstSkillLevel': player.expForFirstSkillLevel, 'expSkillGrowCoef': player.expSkillGrowCoef,
             'expSkillReduserCoef': player.expSkillReduserCoef, 'maxSkill': cfg_const['maxSkill']},
            {'status': player.status, 'level': 0, 'pirateStatus': player.pointStatus if 0 > player.pointStatus else 0,
             'policeStatus': player.pointStatus if  player.pointStatus > 0 else 0}] # level don't player level


def active_weapons(Game, id_):
    player = getattr(Game, f"Player_{id_}")
    return player.active_weapons


def active_devices(Game, id_):
    player = getattr(Game, f"Player_{id_}")
    return player.active_devices


def active_device(Game, id_):
    player = getattr(Game, f"Player_{id_}")
    return player.active_devices


def location_system(Game, id_player):
    id_location = getattr(Game, f"Player_{id_player}").location
    Location = getattr(Game, f"Location_{id_location}")
    location = [Location.id, Location.x, Location.y, Location.sector]
    players = []
    for player_ in Location.players:
        players.append(DotMap({
            "player": DotMap({
                "level": player_['level'],
                "avatar": player_['avatar'],
                "aliance": player_['aliance'],
                "status": player_['status'],
                "clanId": player_['clan'],
            }),
            "race": player_["race"],
            "id": player_["id"],
            "Name": player_["login"],

            "size": player_["ship"]["size"],
            "set_x": player_["x"],
            "set_y": player_["y"],
            "maxHealth": player_["ship"]["maxHealth"],
            "maxEnergy": player_["ship"]["maxEnergy"],
            "maxSpeed": player_["ship"]["maxSpeed"],
            "mov_x": player_["mov_x"],
            "mov_y": player_["mov_y"],
            "droid": player_["droid"],
        }))
    planets = []
    for planet in Location.planets:
        planets.append(DotMap({
            "PlanetClass": planet.class_number,
            "id": planet.id,
            "race": planet.race,
            "radius": planet.radius,
            "size": planet.size,
            "angle": planet.angle,
            "landable": planet.landable,
            "aliance": planet.aliance,
            "clanID": planet.clanID,
        }))
    static_space_objects = []
    for static_space_object in Location.static_space_objects:
        static_space_objects.append(DotMap(({
            "StaticSpaceObjectType": static_space_object.StaticSpaceObjectType,
            "id": static_space_object.id,
            "x": static_space_object.x,
            "y": static_space_object.y,
            "landable": static_space_object.landable,
        })))
    print(location, players, planets, static_space_objects)
    return location, players, planets, static_space_objects

def player_ship(Game, id_):
    ship = getattr(Game, f"Player_{id_}").ship
    return DotMap({
        'id': ship['id'],
        'login': ship['login'],
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


def player(Game, id_):
    player = getattr(Game, f"Player_{id_}")
    return DotMap({
        "id": player.id,
        "login": player.login,
        "level": player.level,
        "cash": player.cash,
        "race": player.race,
        "avatar": player.avatar,
        "aliance": player.aliance,
        "clanId": player.clan,
        "role": player.role,
        "clanRequestStatus": player.clanRequestStatus,
        "clanJoinRequestStatus": player.clanJoinRequestStatus,
        "PlayerRelation": player.PlayerRelation,
    })

def active_weapon(Game, id_):
    player = getattr(Game, f"Player_{id_}")
    return player.active_weapons

def logged2(Game, id_):
    player = getattr(Game, f"Player_{id_}")
    return DotMap({
        'id': player.id,
        'name': player.login,
        'shipClass': player.ship['classNumber'],
        'shipCPU': player.ship["cpu"],
        'race': player.race,
        'aliance': player.aliance,
        'status': player.status,
        'level': player.level,
        'clanId': player.clan,
        'deleteEnqueued': player.deleteEnqueued,
        'canDelete': player.canDelete,
        'logged': player.logged,
        'skills': player.skills
    })
