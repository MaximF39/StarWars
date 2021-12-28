import json

from python.Utils.DotMap import DotMap
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


