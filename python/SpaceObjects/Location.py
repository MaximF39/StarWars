from . import Planet, cfg_update, ThreadBase
import threading

from .StaticSpaceObjects import StaticSpaceObjects


class Location(ThreadBase):
    id: int
    location_type: bytes  # name?
    location_ships: dict
    location_planets: dict
    location_asteroids: dict
    location_static_space_objects: dict
    location_items: dict  # What ir
    location_shops: dict
    location_players: dict
    data: dict  # what it x, y ?
    time_update = cfg_update['location']

    def __init__(self, data: dict):
        super().__init__()
        self.classNumber = data['classNumber']
        self.aliance = data['aliance']
        self.Name = data['Name']
        self.Sector = data['Sector']
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
        # self.create_items()
        # self.create_shops()
        # self.create_players()

    def create_space_object(self):
        self.create_planets()
        self.create_static_space_objects()

    def create_static_space_objects(self):
        for id_, data_space_object in enumerate(self.SpaceObjects['data']):
            data_space_object['id'] = id_
            setattr(self, f"StaticSpaceObjects_{id_}", StaticSpaceObjects(data_space_object))

    def create_planets(self):
        for data_planet in self.Planets['data']:
            id_ = data_planet['id']
            setattr(self, f'Planet_{id_}', Planet(data_planet))

    def update(self):
        self.location_items: None
        self.location_players: None

    def get_planets(self):
        pass

    def get_ships(self):
        return
