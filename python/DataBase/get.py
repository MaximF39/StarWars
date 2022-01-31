from python.DataBase.SQL_Table import PlayerDB, ClanDB
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from python.Static.cfg.cfg_postgres import *

engine = create_engine(f"postgresql+psycopg2://{db_name_user}:{db_passwd_user}@{host}:{port}/{db_name}")
session = sessionmaker(bind=engine)
s = session()

def top_list():
    res2 = s.query(PlayerDB, func.max(PlayerDB.id).over(order_by=PlayerDB.experience))
    data = []
    for top_player, _ in res2[:-10:-1] if len(list(res2)) > 10 else res2[::-1]:
        data.append(_get_data_dict(top_player))
    return data

def top_clan_list():
    res2 = s.query(ClanDB, func.max(ClanDB.id).over(order_by=ClanDB.rating))
    data = []
    for top_clan, _ in res2[:-10:-1] if len(list(res2)) > 10 else res2[::-1]:
        data.append(_get_data_dict(top_clan))
    return data


def top_rating_list():
    res2 = s.query(PlayerDB, func.max(PlayerDB.id).over(order_by=PlayerDB.rating))
    data = []
    for top_player, _ in res2[:-10:-1] if len(list(res2)) > 10 else res2[::-1]:
        data.append(_get_data_dict(top_player))
    return data


def info_player(id_):
    for Player in s.query(PlayerDB).filter_by(id=id_):
        return _get_data_dict(Player)

def _get_data_dict(data):
    info = {}
    for key, value in data.__dict__.items():
        if key == "_sa_instance_state":
            continue
        if key in ['repository', 'enemies', 'friends', 'inventory', 'angar', 'skills', 'activeDevices', 'activeWeapons', 'members']:
            info[key] = eval(value)
        else:
            info[key] = value
    return info

def get_clans():
    clans = []
    for Clan in s.query(ClanDB).all():
        clans.append(_get_data_dict(Clan))
    return clans

if __name__ == '__main__':
    print(get_clans())

