from python.DataBase.DB_Table.DB_Player.DB_BasePlayer import DB_BasePlayer
from python.DataBase.DB_Table.DB_Clan.DB_Clan import DB_Clan
from sqlalchemy import literal
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

from python.DataBase.DB_Table.DB_Player.DB_Player import DB_Player
from python.DataBase.DB_Table.DB_Player.DB_Skills import DB_Skills
from .DB_Table.engine import engine


class DataBase:
    def __init__(self):
        session = sessionmaker(bind=engine)
        self.__s = session()

    def top_list(self):
        res2 = self.__s.query(DB_BasePlayer, func.max(DB_BasePlayer.id).over(order_by=DB_BasePlayer.experience))
        data = []
        for top_player, _ in res2[:-10:-1] if len(list(res2)) > 10 else res2[::-1]:
            data.append(self._get_data_dict(top_player))
        return data

    def top_clan_list(self):
        res2 = self.__s.query(DB_Clan, func.max(DB_Clan.id).over(order_by=DB_Clan.rating))
        data = []
        for top_clan, _ in res2[:-10:-1] if len(list(res2)) > 10 else res2[::-1]:
            data.append(self._get_data_dict(top_clan))
        return data

    def top_rating_list(self):
        res2 = self.__s.query(DB_BasePlayer, func.max(DB_BasePlayer.id).over(order_by=DB_BasePlayer.rating))
        data = []
        for top_player, _ in res2[:-10:-1] if len(list(res2)) > 10 else res2[::-1]:
            data.append(self._get_data_dict(top_player))
        return data

    def player_info(self, id_):
        for Player in self.__s.query(DB_BasePlayer).filter_by(id=id_):
            return self._get_data_dict(Player)

    def save_player(self, dict_:dict):
        id_ = dict_['id']
        self._change_row_db(id_, DB_Skills, **dict_['skills'])
        self._change_row_db(id_, DB_BasePlayer, **self.__get_data_for_DB(dict_))

    @staticmethod
    def __get_data_for_DB(full_dict_):
        all_column = (
            "login", "passwd", "cash", "bonus", "clanId", "spaceObjectId", "locationId",
            "clanRequestStatus", "clanJoinRequestStatus", "PlayerRelation", "race", "avatar",
            "aliance", "role", "classNumber", "x", "y", "count_reset_skills", "isAdmin", "deleteEnqueued",
            "canDelete", "rating", "experience", "points", "expSkillGrowCoef", "expSkillReduserCoef",)
        return {name: full_dict_[name] for name in all_column}

    def _change_row_db(self, id, DB_Table, /, **kwargs):
        self.__s.query(DB_Table).filter(DB_Table.id == id).\
            update(kwargs, synchronize_session=False)
        self.__s.commit()

    def get_user_id(self, login, password) -> bool | int:
        return self.get_value_exist("id", login=login, password=password)

    def get_value_exist(self, column:str, **kwargs):
        if self._exist(**kwargs):
            for Player in self.__s.query(DB_Player).filter_by(login=kwargs["login"]):
                return getattr(Player, column)
        return

    def _exist(self, **kwargs):
        for k, v in kwargs.items():
            q = self.__s.query(DB_Player).filter(getattr(DB_Player, k) == v)
            res = self.__s.query(literal(True)).filter(q.exists()).scalar()
            if not res:
                return
        return True

    def __get_level(self, exp):
        from python.Static.cfg.Player.cfg_level import cfg_level
        for lvl, exp_lvl in cfg_level.items():
            if exp_lvl > exp:
                return lvl - 1

    def __get_status(self, status):
        from python.Static.cfg.Player.cfg_status import cfg_status
        for status_lvl, stat_lvl in cfg_status.items():
            if stat_lvl > status:
                return status_lvl - 1

    def _get_data_dict(self, data):
        info = {}
        if hasattr(data, 'skills'):
            data.skills.__dict__.items()  # It's just work &!&!&!&!?!?!?!?!
        for key, value in data.__dict__.items():
            if key == 'skills':
                info[key] = {}
                for i in value:
                    for skill_name, skill_value in i.__dict__.items():
                        if skill_name in ['_sa_instance_state', 'playerId']:
                            continue
                        info[key][skill_name] = skill_value
            elif key == 'experience':
                info['level'] = self.__get_level(value)
            elif key == 'points':
                info['status'] = self.__get_status(value)
            elif key == "_sa_instance_state":
                continue
            elif key in ['repository', 'enemies', 'friends', 'members']:
                info[key] = eval(value)
            elif key == 'items':
                info['inventory'] = []
                info['angar'] = []
                info['repository'] = []
                info['active_weapons'] = []
                info['active_devices'] = []
                for item in value:
                    for key_item, value_item in item.__dict__.items():
                        if key_item in ['_sa_instance_state', 'playerId']:
                            continue
                        match key_item['where']:
                            case 1:
                                info['repository'].append(value_item)
                            case 2:
                                if value_item['type'] == 3 and value_item["inUsing"]:
                                    info['active_weapons'] = value_item
                                elif value_item['type'] == 4 and value_item["inUsing"]:
                                    info['active_devices'] = value_item
                                elif value_item['type'] == 5 and value_item["inUsing"]:
                                    info['engineId'] = value_item['classNumber']
                                else:
                                    info['inventory'].append(value_item)
                            case 3:
                                info['angar'].append(value_item['classNumber'])
            else:
                info[key] = value
        return info

    def get_clans(self):
        clans = []
        for Clan in self.__s.query(DB_Clan).all():
            clans.append(self._get_data_dict(Clan))
        return clans

    def init_clan(self, clanId):
        return self._get_data_dict(self.__s.query(DB_Clan).get_packages(clanId))

    def __del__(self):
        self.__s.close()


if __name__ == '__main__':
    DB = DataBase()
    print(DB.player_info(255))
