import math

from python.Utils.ThreadBase import ThreadBase
from python.SpaceObjects.Planet import Planet
from .StaticSpaceObjects.Hive import Hive
from .StaticSpaceObjects.Portal import Portal
from .StaticSpaceObjects.RepositoryStation import RepositoryStation
from .StaticSpaceObjects.AsteroidsBelt import AsteroidsBelt
from python.Static.cfg.StaticSpaceObject.get_ore import get_ore
from ..Static.cfg.StaticSpaceObject.portal import get_hive
from ..Static.cfg.cfg_main import RADIUS
from python.Base.SpaceObject.SetPlayer import SetPlayer
from python.Base.Inventory.Inventory import Inventory
if False:
    from python.Player.Player import Player

class Location(ThreadBase, SetPlayer, Inventory):
    id: int

    def __init__(self, StarWars, data: dict):
        self.__dict__.update(data)
        Inventory.__init__(self)
        self.Game = StarWars

        self.players:list["DB_Player"] = []
        self.planets = []
        self.inventory = []
        self.StaticSpaceObjects = []
        self.create_space_object()

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
            data_planet['RADIUS'] = RADIUS * count_planet
            setattr(self, f'Planet_{id_}', Planet(self.Game, data_planet, self))

    def hyper_jump_player(self, Player):
        radius_ = RADIUS * len(self.planets)
        OldLocation = Player.Location

        tan = math.atan2(OldLocation.y - self.y, OldLocation.x - self.x)
        
        Player.x = radius_ * math.cos(tan)
        Player.y = radius_ * math.sin(tan)
        Player.not_target()

        Player.Location.remove_player(Player)
        self.set_player(self, Player)
        Player.Location = self

    def set_player(self, Player):
        Player.Location.remove_player(Player)
        Player.Location = self
        self.players.append(Player)

    def set_planet(self, classPlanet):
        self.planets.append(classPlanet)

    def set_static_space_object(self, StaticSpaceObject_class):
        self.StaticSpaceObjects.append(StaticSpaceObject_class)

    def get_drop(self, drop):
        self.inventory.extend(drop)
