from python.Class.Chat import Chat
from python.Static.ParseJson import parse_xml
from .Clan.Clan import Clan
from .DataBase.Database import DataBase
from .SpaceObjects.Location import Location
from time import time
from .Player.Player import Player

class StarWars:
    Chat: "Chat"

    def __init__(self, Chat: "Chat"):
        start = time()
        self.Chat = Chat
        self.Chat.init_game(self)
        self.online = 0
        self.__create_game()
        end = time()
        print(end - start)

    def __create_game(self):
        self.__create_locations()

    def create_player(self, id_):
        setattr(self, f"Player_{id_}", Player(self, DataBase().player_info(id_)))
        getattr(self, f"Player_{id_}").init()

    def create_clan(self, clanId):
        setattr(self, f"Clan_{clanId}", Clan(self, DataBase().init_clan(clanId)))

    def __create_locations(self):
        for location in parse_xml('GalaxyMap'):
            setattr(self, f"Location_{location['id']}", Location(self, location))

    def __create_mobs(self):
        pass
