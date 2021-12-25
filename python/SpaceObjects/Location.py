from ..Packages.PackagesManager import PackagesManager
from . import Planet, cfg_update, ThreadBase
from .StaticSpaceObject import StaticSpaceObject


class Location(ThreadBase):
    id: int
    # location_type


    def __init__(self, StarWars, data: dict):
        self.Game = StarWars
        self.id = data['classNumber']
        self.aliance = data['aliance']
        self.Name = data['Name']
        self.sector = data['Sector']
        self.lineTo = data['lineTo']
        self.Priority = data['Priority']
        self.json_data_planets = data['Planets']
        self.SpaceObjects = data['SpaceObjects']
        self.id = data['id']
        self.Types = data['Types']
        self.x = data['x']
        self.y = data['y']
        self.players = []
        self.planets = []
        self.items = []
        self.asteroids = []
        self.static_space_objects = []
        self.create_space_object()


    def remove_location(self, playerClass):
        self.players.remove(playerClass)

    def set_player(self, Player_class):
        self.players.append(Player_class)

    def remove_player(self, PlayerClass):
        self.players.remove(PlayerClass)

    def create_space_object(self):
        self.create_planets()
        self.create_static_space_objects()

    def create_static_space_objects(self):
        for data_space_object in self.SpaceObjects['data']:
            id_ = data_space_object['id']
            setattr(self, f"Static_space_object_{id_}", StaticSpaceObject(self.Game, data_space_object, self))

    def create_planets(self):
        count_planet = 0
        for data_planet in self.json_data_planets['data']:
            count_planet += 1
            id_ = data_planet['id']
            data_planet['radius'] = 140 * count_planet**2
            setattr(self, f'Planet_{id_}', Planet(self.Game, data_planet, self))

    def set_planet(self, classPlanet):
        self.planets.append(classPlanet)

    def set_static_space_object(self, Static_space_object_class):
        self.static_space_objects.append(Static_space_object_class)

    def update(self):
        self.location_items: None
        self.location_players: None
        self.start_update("update_info", 1)

    # @ThreadBase.end_thread
    # def update_info(self):
    #     PacMan = PackagesManager(self.Game, self.id)

    def get_info_ship(self):
        return
