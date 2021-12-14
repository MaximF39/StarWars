from . import parse_location
from . import Planet, cfg_update, ThreadBase, SpaceObject
import threading


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
        self.id = data['id']
        self.data = data
        # self.create_location()
        self.create_planet()
        # self.ships()
        # self.create_asteroids()
        # self.create_static_space_objects()
        # self.create_items()
        # self.create_shops()
        # self.create_players()

    def space_object(self):
        """
        ASTEROIDS_BELT: int = 1
        REPOSITORY_STATION: int = 2
        GARBALE_DUMP: int = 3
        PORTAL: int = 4
        HIVE: int = 5
        """
        for id_, data_space_object in enumerate(self.data['SpaceObjects']['data']):
            setattr(self, f"space_object{id_}", SpaceObject(data_space_object))

    def create_planet(self):
        self.location_planets = self.data['Planets']
        for data_planet in self.location_planets['data']:
            id_ = data_planet['id']
            setattr(self, f'planet_{id_}', Planet(data_planet))

    def update(self):
        self.location_items: None
        self.location_players: None

    def get_planets(self):
        pass

    def get_ships(self):
        return
