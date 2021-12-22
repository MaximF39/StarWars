from sqlalchemy import create_engine
from sqlalchemy import func as sql_max
from sqlalchemy.orm import sessionmaker
from SQL_Table import PlayerDB
# from .cfg_postgres import *
import psycopg2

host = "127.0.0.1"
db_name_user = "postgres"
db_passwd_user = "123"
db_name = "test_main"
port = 5432

debug = False
engine = create_engine(f"postgresql+psycopg2://{db_name_user}:{db_passwd_user}@{host}:{port}/{db_name}", echo=debug)

# Флаг echo включает ведение лога через стандартный модуль logging Питона.
# Когда он включен, мы увидим все созданные нами SQL-запросы. 
session = sessionmaker(bind=engine)
s = session()

# u = s.get(PlayerDB, 1)
# s.delete(u)
# s.commit()
#
# exit()

# print(s.query(PlayerDB).filter(PlayerDB.name == 'PlayerDB').one().name)

import json

player_skills = {
    'control': 0, 'defending': 0, 'energyWeapons': 0, 'kineticWeapons': 0,
    'mining': 0, 'piloting': 3, 'repairing': 6, 'rocketWeapons': 0, 'trading': 0,
    'attacking': 0, 'tactics': 0, 'targeting': 0, 'electronics': 0,
    'biocemistry': 0, 'mechanics': 8, 'cybernetics': 8}

player_skills_str = str(player_skills)

res = s.query(PlayerDB).filter_by(id=6)
for i in res:
    dict_ = i.__dict__
    del dict_['_sa_instance_state']


def listToString(list_):
    str1 = ''
    count = len(list_)
    for i in range(count):
        str1 += str(list_[i])
        if i == count - 1:
            return str1
        str1 += ', '


player = PlayerDB(
    id=1656,
    login="Max4",
    auth_key="my_authkey",
    passwd='passwd',
    # clan_id=
    credit=500000,
    bonus=500,
    # planet=
    location=7,
    level=25,
    experience=46877,
    status=0,
    # clanRequestStatus=
    # clanJoinRequestStatus=
    # PlayerRelation=
    race=3,
    avatar=2001,
    aliance=3,
    rating=50000,
    # role=
    ship_class=2003,
    skills=str({'control': 0, 'defending': 0, 'energyWeapons': 0, 'kineticWeapons': 0, 'mining': 0, 'piloting': 3, 'repairing': 6, 'rocketWeapons': 0, 'trading': 0, 'attacking': 0, 'tactics': 0, 'targeting': 0, 'electronics': 0, 'biocemistry': 0, 'mechanics': 8, 'cybernetics': 8}),
    free_skills=6,
    # expSkillGrowCoef=
    # expSkillReduserCoef=
    pointStatus = 6000,
    x=1308,
    y=869,
    # deleteEnqueued=
    # canDelete=
    # logged=
    active_weapons=str({'data': [{'classfloat': 61, 'index': 0}]}),
    active_devices=str({'data': [{'id': 122, 'guid': bytearray(b'P:\x1e+{mcN\x82j\x0cK\x7f4&\xd2'), 'reloadedTime': 0.0}, {'id': 122, 'guid': bytearray(b'5\xc6\xf5-\x84\xc5\xecH\xba\xd0\x89\xd1\tq\x1a\x1e'), 'reloadedTime': 0.0}, {'id': 122, 'guid': bytearray(b'\x84\xea\xc8\x87\xc4\xc8;E\x8f\x04@\xf7\xc5J\x86h'), 'reloadedTime': 0.0}, {'id': 122, 'guid': bytearray(b'@\x9a\x1f\x95\xb3\x13\xf5J\xbba\xe0\x03\x14<\x80b'), 'reloadedTime': 0.0}, {'id': 124, 'guid': bytearray(b',g\xc3\xe0\x16s\xc7M\x99\xdd\xa37\x8a\xa1\x85L'), 'reloadedTime': 0.0}]}),
)
s.add(player)
s.commit()

# res2 = s.query(func.max(PlayerDB.rating))
res2 = s.query(PlayerDB, sql_max.max(PlayerDB.id).over(order_by=PlayerDB.rating))
# res2 = s.query(PlayerDB, sql_max.max(PlayerDB.rating).over(order_by=PlayerDB.id))

data = []
# for top_player in res2[:-10:-1] if len(list(res2)) > 10 else res2[::-1]:
# for top_player, i in res2:
#     print(top_player.id)

# s.add_all([ClanDB(id=1, create_id=1),
#            ClanDB(id=2, create_id=2),
#            ClanDB(id=3, create_id=3)
#            ])
# s.commit()

# print(s.query(ClanDB).first().title)
# s.query(ClanDB)
# exit()
# for title, price in s.query(ClanDB.title, ClanDB.price).order_by(ClanDB.title).limit(2):
#     print(title, price)
#
#
# for row in s.query(ClanDB, PlayerDB).filter(ClanDB.author_id == PlayerDB.id_author).filter(ClanDB.price > 1000).group_by(
#         PlayerDB.name):
#     print(row.ClanDB.title, ' ', row.PlayerDB.name)

# print('\n\n\n')

# print([(row.ClanDB.create_id, row.PlayerDB.id) for row in s.query(ClanDB, PlayerDB).join(PlayerDB).all()])
