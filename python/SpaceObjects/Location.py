from . import Planet, cfg_update, ThreadBase
from .StaticSpaceObjects import StaticSpaceObjects


class Location(ThreadBase):
    id: int
    location_type: bytes  # name?
    planet: dict
    asteroid:list = []
    static_space_objects: list = []
    planets: list = []
    players: list = []
    items: list = []
    # location_shops: dict
    time_update = cfg_update['location']

    def __init__(self, StarWars, data: dict):
        self.Game = StarWars
        self.id = data['classNumber']
        self.aliance = data['aliance']
        self.Name = data['Name']
        self.sector = data['Sector']
        self.lineTo = data['lineTo']
        self.Priority = data['Priority']
        self.Planets = data['Planets']
        self.SpaceObjects = data['SpaceObjects']
        self.id = data['id']
        self.Types = data['Types']
        self.x = data['x']
        self.y = data['y']
        self.create_space_object()
        # self.ships()


    def set_asteroid(self, dict_):
        self.asteroid.append(dict_)

    def set_item(self, dict_):
        self.items.append(dict_)

    def set_battle(self, dict_):
        pass

    def set_ship(self, dict_:dict):
        self.players.append(dict_)

    def set_static_space_object(self, dict_:dict):
        self.static_space_objects.append(dict_)

    def set_planet(self, dict_:dict):
        self.planets.append(dict_)

    def create_space_object(self):
        self.create_planets()
        self.create_static_space_objects()

    def create_static_space_objects(self):
        for data_space_object in self.SpaceObjects['data']:
            id_ = data_space_object['id']
            data_space_object['location'] = self.id
            setattr(self, f"StaticSpaceObjects_{id_}", StaticSpaceObjects(self.Game, data_space_object))

    def create_planets(self):
        for data_planet in self.Planets['data']:
            id_ = data_planet['id']
            data_planet['location'] = self.id
            setattr(self, f'Planet_{id_}', Planet(self.Game, data_planet))

    def update(self):
        self.location_items: None
        self.location_players: None

    def get_planets(self):
        pass

    def get_ships(self):
        return
