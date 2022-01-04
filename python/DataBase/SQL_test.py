from sqlalchemy import create_engine
from sqlalchemy import func as sql_max
from sqlalchemy.orm import sessionmaker
from SQL_Table import PlayerDB
# from .cfg_postgres import *

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
    'Control': 0, 'Defending': 0, 'EnergyWeapons': 0, 'KineticWeapons': 0,
    'Mining': 0, 'Piloting': 3, 'Repairing': 6, 'RocketWeapons': 0, 'Trading': 0,
    'Attacking': 0, 'Tactics': 0, 'Targeting': 0, 'Electronics': 0,
    'Biocemistry': 0, 'Mechanics': 8, 'Cybernetics': 8}

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
    id=255,
    login="Admin",
    auth_key="my_authkey",
    passwd='passwd',
    # clan_id=
    credit=5000000,
    bonus=5000,
    # SpaceObject=
    Location=7,
    level=50,
    experience=468770,
    status=1,
    angar="[]",
    repository="[]",
    # clanRequestStatus=
    # clanJoinRequestStatus=
    # PlayerRelation=
    race=3,
    avatar=2001,
    aliance=3,
    rating=50000,
    # role=
    ship_class=5999,
    skills=str({'Control': 0, 'Defending': 0, 'EnergyWeapons': 0, 'KineticWeapons': 0, 'Mining': 0, 'Piloting': 0, 'Repairing': 0, 'RocketWeapons': 0, 'Trading': 0, 'Attacking': 0, 'Tactics': 0, 'Targeting': 0, 'Electronics': 0, 'Biocemistry': 0, 'Mechanics': 0, 'Cybernetics': 0}),
    free_skills=600,
    # expSkillGrowCoef=
    # expSkillReduserCoef=
    point = 6000,
    x=0,
    y=0,
    # deleteEnqueued=
    # canDelete=
    # logged=
    active_weapons=str({'data': []}),
    active_devices=str({'data': []}),
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
