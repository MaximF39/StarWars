from python.Static.ParseXml import parse_xml
from .SpaceObjects.Location import Location
from time import time
from .Player.Player import Player
from python.Packages.PackagesEntry import *

class StarWars:
    id_to_conn = {}
    def __init__(self):
        self.online = 0
        start = time()
        self.__create_game()
        end = time()
        print(end - start)

    def __create_game(self):
        self.__create_locations()
        # self.__create_clans()

    def update_online(self, online):
        self.online = online

    def connect_user(self, id_, conn):
        self.id_to_conn[id_] = conn

    def create_player(self, id_):
        player_ = PackagesEntry(self, id_).create_pilot
        setattr(self, f"Player_{id_}", Player(self, player_))

    def __create_locations(self):
        for location in parse_xml('GalaxyMap'):
            id_ = location['id']
            setattr(self, f"Location_{id_}", Location(self, location))

    def __create_mobs(self):
        pass