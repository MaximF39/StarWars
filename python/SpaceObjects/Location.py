import math

from ..Packages.PackagesManager import PackagesManager
from python.Utils.ThreadBase import ThreadBase
from python.SpaceObjects.Planet import Planet
from .StaticSpaceObjects.Hive import Hive
from .StaticSpaceObjects.Portal import Portal
from .StaticSpaceObjects.RepositoryStation import RepositoryStation
from .StaticSpaceObjects.AsteroidsBelt import AsteroidsBelt
from python.Static.cfg.StaticSpaceObject.get_ore import get_ore
from ..Static.cfg.StaticSpaceObject.portal import get_hive
from ..Static.cfg.cfg_main import radius
from ..Utils.JSONClass import JSONClass


class Location(JSONClass, ThreadBase):
    id: int

    def __init__(self, StarWars, data: dict):
        super().__init__(data)
        self.Game = StarWars

        self.players = []
        self.planets = []
        self.inventory = []
        self.asteroids = []
        self.StaticSpaceObjects = []
        self.create_space_object()

    def remove_player(self, PlayerClass):
        self.players.remove(PlayerClass)

    def create_space_object(self):
        self.create_planets()
        self.create_static_space_objects()

    def create_static_space_objects(self):
        count = 0
        for data_space_object in self.SpaceObjects['data']:
            match data_space_object['type']:
                case 1: # ASTEROIDS_BELT
                    ore = get_ore(self.id)
                    if not ore:
                        ore = 49
                    id_ = int(f'1{ore}') # + руда
                    data_space_object['id'] = id_
                    setattr(self, f"StaticSpaceObject_{id_}", AsteroidsBelt(self.Game, data_space_object, self))
                case 2: # REPOSITORY_STATION
                    race = data_space_object['race']
                    id_ = int(f'2{race}') # type + raca
                    data_space_object['id'] = id_
                    setattr(self, f"StaticSpaceObject_{id_}", RepositoryStation(self.Game, data_space_object, self))
                case 3:
                    pass
                case 4:
                    count += 1
                    hive = get_hive(self.id, count)
                    id_ = int(f'4{hive}') # Куда ведёт

                    data_space_object['id'] = id_
                    setattr(self, f"StaticSpaceObject_{id_}", Portal(self.Game, data_space_object, self, count))
                case 5:
                    id_ = 5
                    data_space_object['id'] = id_
                    setattr(self, f"StaticSpaceObject_{id_}", Hive(self.Game, data_space_object, self))

    def create_planets(self):
        count_planet = 0
        for data_planet in self.Planets['data']:
            count_planet += 1
            id_ = data_planet['id']
            data_planet['radius'] = radius * count_planet
            setattr(self, f'Planet_{id_}', Planet(self.Game, data_planet, self))

    def EntryPlayer(self, PlayerClass):
        self.players.append(PlayerClass)

    def SetPlayer(self, PlayerClass, x_y:tuple = None):
        radius_ = radius * len(self.planets)
        OldLocation = PlayerClass.Location

        tan = math.atan2(OldLocation.y - self.y, OldLocation.x - self.x)
        if x_y:
            PlayerClass.x = x_y[0]
            PlayerClass.y = x_y[1]
        else:
            PlayerClass.x = radius_ * math.cos(tan)
            PlayerClass.y = radius_ * math.sin(tan)
        PlayerClass.targetX = PlayerClass.x
        PlayerClass.targetY = PlayerClass.y

        PlayerClass.Location.remove_player(PlayerClass)
        self.players.append(PlayerClass)
        PlayerClass.Location = self

        PacMan = PackagesManager(PlayerClass.id, self.Game)
        PacMan.locationSystem()

    def set_planet(self, classPlanet):
        self.planets.append(classPlanet)

    def set_static_space_object(self, StaticSpaceObject_class):
        self.StaticSpaceObjects.append(StaticSpaceObject_class)

    def update(self):
        self.start_update("update_info", 1)

    # @ThreadBase.end_thread
    # def update_info(self):
    #     PacMan = PackagesManager(self.Game, self.id)

    def get_info_ship(self):
        return
