from .DataBase import *
from .Static.ParseXml import parse_xml
from .SpaceObjects.Location import Location
from time import time
from .Ship.Player import Player
from .packages_entrance.all_packages import *

class StarWars:
    def __init__(self):
        start = time()
        self.__create_game()
        end = time()
        print(end - start)

    def __create_game(self):
        self.__create_locations()

    def create_player(self, id_):
        player_ = create_pilot(id_)
        setattr(self, f"Player_{id_}", Player(self, player_))

    def __create_locations(self):
        for location in parse_xml('GalaxyMap'):
            id_ = location['id']
            print('create loc', location)
            setattr(self, f"Location_{id_}", Location(self, location)) # окация сначала создаёт сама все объекты, а затем добавляет их всех

    def __create_mobs(self):
        pass