from python.Game.Game.Chat import Chat
from python.Static.ParseJson import parse_xml
from python.Game.Game.Clan.Clan import Clan
from .Database.Database import DataBase
from python.Game.Game.Entity import Mob
from python.Game.Game.SpaceObjects import Location
from python.Game.Game.Entity import Player
from python.Config.CFG_Mob.CFG_Create_Mob.cfg_create_mobs import get_data_mobs
from .Static.Type.Keys import Keys


class StarWars:
    def __init__(self, Chat: "Chat", Server):
        self.Chat = Chat
        self.Chat.init_game(self)
        self.online = 0
        self.__create_game()
        self.Server = Server
        self.id_to_conn = self.Server.id_to_conn

    def __create_game(self):
        self.__create_locations()
        self.__create_mobs()

    def create_player(self, id_):
        player_data = DataBase().player_info(id_)
        setattr(self, f"Player_{id_}", Player(self, player_data))
        getattr(self, f"Player_{id_}").init()

    def create_clan(self, clan_id):
        clan_data = DataBase().init_clan(clan_id)
        print("clan_data", clan_data)
        setattr(self, f"Clan_{clan_id}", Clan(self, clan_data))

    def __create_locations(self):
        for location in parse_xml('GalaxyMap'):
            setattr(self, f"Location_{location[Keys.id]}", Location(self, location))

    def __create_mobs(self):
        for data_mob in get_data_mobs():
            setattr(self, f"Mob_{data_mob[Keys.id]}", Mob(self, data_mob))
