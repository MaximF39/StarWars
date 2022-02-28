from python.Config.CFG_StaticSpaceObject.portal import get_hive
from python.Game.SpaceObjects import Planet
from python.Game.SpaceObjects.StaticSpaceObjects.AsteroidsBelt import AsteroidsBelt
from python.Game.SpaceObjects.StaticSpaceObjects.RepositoryStation import RepositoryStation
from python.Game.SpaceObjects.StaticSpaceObjects.Hive import Hive
from python.Game.SpaceObjects.StaticSpaceObjects.Portal import Portal
from python.Config.CFG_StaticSpaceObject.get_ore import get_ore
from python.Config.cfg_main import RADIUS_BETWEEN_PLANET


class C_SpaceObject:
    def create_space_object(self):
        self.create_planets()
        self.create_static_space_objects()

    def create_static_space_objects(self):
        count = 0
        for data_space_object in self.SpaceObjects:
            match data_space_object['type']:
                case 1:  # ASTEROIDS_BELT
                    ore = get_ore(self.id)
                    if not ore:
                        ore = 49
                    id_ = int(f'1{ore}')  # + руда
                    data_space_object['id'] = id_
                    setattr(self, f"StaticSpaceObject_{id_}", AsteroidsBelt(self.Game, data_space_object, self))
                case 2:  # REPOSITORY_STATION
                    race = data_space_object['race']
                    id_ = int(f'2{race}')  # type + raca
                    data_space_object['id'] = id_
                    setattr(self, f"StaticSpaceObject_{id_}", RepositoryStation(self.Game, data_space_object, self))
                case 3:
                    pass
                case 4:
                    count += 1
                    hive = get_hive(self.id, count)
                    id_ = int(f'4{hive}')  # Куда ведёт
                    data_space_object['id'] = id_
                    setattr(self, f"StaticSpaceObject_{id_}", Portal(self.Game, data_space_object, self, count))
                case 5:
                    id_ = 5
                    data_space_object['id'] = id_
                    setattr(self, f"StaticSpaceObject_{id_}", Hive(self.Game, data_space_object, self))

    def create_planets(self):
        count_planet = 0
        for data_planet in self.planets:
            count_planet += 1
            id_ = data_planet['id']
            data_planet['RADIUS_BETWEEN_PLANET'] = RADIUS_BETWEEN_PLANET * count_planet
            setattr(self, f'Planet_{id_}', Planet(self.Game, data_planet, self))
