from python.Game.Chat import Chat
from python.Static.ParseJson import parse_xml
from python.Game.Clan.Clan import Clan
from .DataBase.Database import DataBase
from python.Game.Entity.Mob import Mob
from python.Game.SpaceObjects.Location import Location
from time import time
from python.Game.Entity.Player import Player
from python.Config.CFG_Mob.CFG_Create_Mob.cfg_create_mobs import get_data_mobs


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

    def create_clan(self, clanId):
        clan_data = DataBase().init_clan(clanId)
        print("clan_data", clan_data)
        setattr(self, f"Clan_{clanId}", Clan(self, clan_data))

    def __create_locations(self):
        for location in parse_xml('GalaxyMap'):
            setattr(self, f"Location_{location['id']}", Location(self, location))

    def __create_mobs(self):
        for data_mob in get_data_mobs():
            setattr(self, f"Mob_{data_mob['id']}", Mob(self, data_mob))
