from .Static.ParseXml import parse_xml
from .SpaceObjects.Location import Location
from time import time

class StarWars:
    def __init__(self):
        start = time()
        self.__create_game()
        end = time()
        print(self.Location_1.Planet_1.name)
        print(end - start)

    def __create_game(self):
        self.__create_locations()

    def __create_locations(self):
        for location in parse_xml('GalaxyMap'):
            id_ = location['id']
            setattr(self, f"Location_{id_}", Location(location))

    def __create_mobs(self):
        pass