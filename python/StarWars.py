from python.Class.Chat import Chat
from python.Static.ParseJson import parse_xml
from .Clan.Clan import Clan
from .DataBase.get import player_info
from .SpaceObjects.Location import Location
from time import time
from .Player.Player import Player
from python.DataBase.get import init_clan

class StarWars:
    id_to_conn = {}
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

    def update_online(self, online):
        self.online = online

    def connect_user(self, id_, conn):
        self.id_to_conn[id_] = conn

    def create_player(self, id_):
        setattr(self, f"Player_{id_}", Player(self, player_info(id_)))
        getattr(self, f"Player_{id_}").init_packages_manager()
        getattr(self, f"Player_{id_}").send_entry_packages()

    def create_clan(self, clanId):
        setattr(self, f"Clan_{clanId}", Clan(self, init_clan(clanId)))

    def __create_locations(self):
        for location in parse_xml('GalaxyMap'):
            setattr(self, f"Location_{location['id']}", Location(self, location))

    def __create_mobs(self):
        pass
