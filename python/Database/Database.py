from python.Database.DB_Table.DB_Clan.F_DB_Clan import DB_Clan
from sqlalchemy import literal
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

from python.Database.DB_Table.DB_Player.F_DB_Player import DB_Player
from python.Database.DB_Table.DB_Player.DB_Skills import DB_Skill
from python.Static.Type.T_PlayerSkill import T_PlayerSkill
from .DB_Table.DB_Items import DB_Items
from .DB_Table.DB_Player.DB_B_Player import DB_B_Player
from .DB_Table.engine import engine
from python.Game.Game.SpaceObjects.Item import item
from ..Static.Type.Keys import Keys
from ..Static.Type.T_Where import T_Where


class DataBase:
    def __init__(self):
        session = sessionmaker(bind=engine)
        self.__s = session()

    def top_list(self):
        res2 = self.__s.query(DB_B_Player, func.max(DB_B_Player.id).over(order_by=DB_B_Player.experience))
        data = []
        for top_player, _ in res2[:-10:-1] if res2.count() > 10 else res2[::-1]:
            dict_ = self._get_data_dict(top_player)
            dict_['clan_id'] = top_player.db_clans[0].id
            data.append(dict_)
        return data

    def top_clan_list(self):
        res2 = self.__s.query(DB_Clan, func.max(DB_Clan.id).over(order_by=DB_Clan.rating))
        data = []
        for top_clan, _ in res2[:-10:-1] if res2.count() > 10 else res2[::-1]:
            dict_ = self._get_data_dict(top_clan)
            dict_["leaderName"] = top_clan.leader.login
            data.append(dict_)
        return data

    def top_rating_list(self):
        res2 = self.__s.query(DB_B_Player, func.max(DB_B_Player.id).over(order_by=DB_B_Player.rating))
        data = []
        for top_player, _ in res2[:-10:-1] if len(list(res2)) > 10 else res2[::-1]:
            dict_ = self._get_data_dict(top_player)
            dict_['clan_id'] = top_player.db_clans[0].id
            data.append(dict_)
        return data

    def player_info(self, id_):
        for Player in self.__s.query(DB_Player).filter_by(id=id_):
            player = self._get_data_dict(Player)
            player.update(self._get_data_dict(Player.player))
            player['skills'] = self._get_data_dict(Player.skills, skills=True)
            player['clan'] = self._get_data_dict(Player.clan)
            items = self._get_data_dict(Player.items)
            self.get_items(player, items)
            return player

    def get_items(self, player, items):
        player[Keys.inventory] = []
        player[Keys.angar] = []
        for Item in items['_sa_adapter'].data:
            Item = Item.__dict__
            item(Item[Keys.class_number], Item[Keys.wear])
            match Item[Keys.where]:
                case T_Where.clan_repository:
                    pass
                case T_Where.player_repository:
                    pass
                case T_Where.planet_inventory:
                    pass
                case T_Where.player_inventory:
                    player.inventory.append(Item)
                case T_Where.player_angar:
                    player.angar.append(Item)

    def save_player(self, Player):
        print(self.__dict__)
        self.Player = Player
        self._change_row_db(self.Player.id, DB_Skill, dict_=self.Player.skills)
        self._change_row_db(self.Player.id, DB_Clan, **self.__get_data_for_DB_Clan(self.Player.Clan.__dict__))
        self._change_row_db(self.Player.id, DB_B_Player, **self.__get_data_for_DB(self.Player.__dict__))
        self._change_row_db(self.Player.id, DB_Items, primary_column='ownerId', **self.__get_data_for_DB_Items())

    def __get_data_for_DB_Items(self):
        all_column = ("guid", "class_number", "wear", "in_using",) # where
        dict_ = {}
        for Item in self.Player.inventory:
            print(Item)
            dict_["where"] = 4
            dict_.update({name: Item.__dict__[name] for name in all_column})
        print("dict", dict_)
        print("dict", dict_['_DataBase__s'].__dict__)
        return dict_

    @staticmethod
    def __get_data_for_DB_Clan(dict_):
        all_column = (
            "name", "shortName", "description", "level", "rating", "cash", "bonus",
            "type", "aliance", "race", "enemies", "friends", "logoFileName",)
        return {name: dict_[name] for name in all_column}

    @staticmethod
    def __get_data_for_DB(full_dict_):
        all_column = (
            "login", "password", "cash", "bonus", "spaceObjectId", "locationId",
            "clanRequestStatus", "clanJoinRequestStatus", "PlayerRelation", "race",
            "avatar", "aliance", "role", "class_number", "x", "y", "count_reset_skills",
            "isAdmin", "deleteEnqueued", "canDelete", "rating", "experience", "points",
            "expSkillGrowCoef", "expSkillReduserCoef",)
        return {name: full_dict_[name] for name in all_column}

    def _change_row_db(self, id_, DB_Table, primary_column="id", dict_=None, **kwargs):
        if not kwargs:
            kwargs = {}
            T_PS = T_PlayerSkill()
            for skill, value in dict_.items():
                kwargs[T_PS.get(skill)] = value
        self.__s.query(DB_Table).filter(getattr(DB_Table, primary_column) == id_).\
            update(kwargs, synchronize_session=False)
        self.__s.commit()


    def get_user_id(self, login, password) -> bool | int:
        return self.get_value_exist("id", login=login, password=password, Table=DB_B_Player)

    def get_clan_id(self, id):
        return self.__s.query(DB_Clan).get(id)

    def get_value_exist(self, column:str, /, Table, **kwargs):
        if self._exist(**kwargs, Table=Table):
            for Player in self.__s.query(Table).filter_by(login=kwargs["login"]):
                return getattr(Player, column)
        return

    def _exist(self, /, Table, **kwargs):
        for k, v in kwargs.items():
            q = self.__s.query(Table).filter(getattr(Table, k) == v)
            res = self.__s.query(literal(True)).filter(q.exists()).scalar()
            if not res:
                return
        return True

    def __get_level(self, exp):
        from python.Config.CFG_Player.Statistics.cfg_level import cfg_level
        for lvl, exp_lvl in cfg_level.items():
            if exp_lvl > exp:
                return lvl - 1

    def __get_status(self, status):
        from python.Config.CFG_Player.Statistics.cfg_status import cfg_status
        for status_lvl, stat_lvl in cfg_status.items():
            if stat_lvl > status:
                return status_lvl - 1

    def _get_data_dict(self, data, skills = False):
        info = {}
        for key, value in data.__dict__.items():
            if skills:
                if key in ['_sa_instance_state', 'ownerId', Keys.id]:
                    continue
                info[getattr(T_PlayerSkill, key)] = value
            elif key == 'experience':
                info['experience'] = value
                info['level'] = self.__get_level(value)
            elif key == 'points':
                info['points'] = value
                info['status'] = self.__get_status(value)
            elif key == "_sa_instance_state":
                continue
            elif key in ['player_repository', 'enemies', 'friends', 'members']:
                info[key] = eval(value)
            elif key == 'items':
                info['inventory'] = []
                info['angar'] = []
                info['player_repository'] = []
                info['active_weapons'] = []
                info['active_devices'] = []

            else:
                info[key] = value
        return info

    def get_clans(self):
        clans = []
        for Clan in self.__s.query(DB_Clan).all():
            clans.append(self._get_data_dict(Clan))
        return clans

    def init_clan(self, clan_id):
        for Clan in self.__s.query(DB_Clan).filter_by(id=clan_id):
            return self._get_data_dict(Clan)

    def __del__(self):
        self.__s.close()