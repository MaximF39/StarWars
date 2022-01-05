import json

from python.Utils.DotMap import DotMap
from python.DataBase.SQL_Table import PlayerDB, ClanDB
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
        res2 = s.query(ClanDB, func.max(ClanDB.id).over(order_by=ClanDB.rating))
        data = []
        for top_clan, _ in res2[:-10:-1] if len(list(res2)) > 10 else res2[::-1]:
            data.append(DotMap({
                'id': top_clan.id,
                'rating': top_clan.rating,
                'leaderID': top_clan.owner_id,
                'leaderName': 'Admin',
                'aliance': top_clan.aliance,
                'level': top_clan.level,
                'name': top_clan.name,
                'shortName': top_clan.shortName,
                'logoFileName': top_clan.logoFileName,
            }))
        return data

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
            "points": Player.points,
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

    def get_clans(self):
        clans = []
        for Clan in s.query(ClanDB).all():
            clans.append({
            'key': Clan.key,
            'id': Clan.id,
            'creator_id': Clan.creator_id,
            'owner_id': Clan.owner_id,
            'members': Clan.members,
            'name': Clan.name,
            'short_name': Clan.short_name,
            'description': Clan.description,
            'level': Clan.level,
            'rating': Clan.rating,
            'cash': Clan.cash,
            'bonus': Clan.bonus,
            'type': Clan.type,
            'repository': Clan.repository,
            'aliance': Clan.aliance,
            'race': Clan.race,
            'enemies': Clan.enemies,
            'friends': Clan.friends,
            'logoFileName': Clan.logoFileName})
        return clans

if __name__ == '__main__':
    cl = PackagesEntry(55, 'ss')
    cl.get_clans()
    # print(len(cl.get_clans()))
    for i in cl.get_clans():
        print(i)

