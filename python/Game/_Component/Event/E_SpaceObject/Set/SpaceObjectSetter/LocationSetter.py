import math

from python.Game import I_SpaceObjectSetter
from python.Config.cfg_main import RADIUS_BETWEEN_PLANET
from python.Static.Type.Package.T_ServerRequest import T_ServerRequest


class LocationSetter(I_SpaceObjectSetter):

    def __init__(self):
        super().__init__()
        self.staticSpaceObjects:list = []
        self.planets:list = []

    def set_entity(self, Entity):
        Entity.remove_energy(100)

        radius_ = RADIUS_BETWEEN_PLANET * len(self.planets)

        tan = math.atan2(Entity.SpaceObject.map_y - self.map_y, Entity.SpaceObject.map_x - self.map_x)

        x = radius_ * math.cos(tan)
        y = radius_ * math.sin(tan)
        Entity.set_x_y(x, y)

        Entity.Location.remove_entity(Entity)

        Entity.SpaceObject = self
        Entity.Location = self

        super()._set_entity(Entity)

        if Entity.__class__.__name__ == "B_Player":
            Entity.send_entry_location()

        super()._send_package_players(T_ServerRequest.LOCATION_SYSTEM)

    def entry_entity(self, Entity):
        super()._set_entity(Entity)

        if Entity.__class__.__name__ == "B_Player":
            Entity.send_entry_location()

        super()._send_package_players(T_ServerRequest.LOCATION_SYSTEM)

    def remove_entity(self, Entity):
        super()._remove_entity(Entity)
        Entity.SpaceObject = None
        super()._send_package_players(T_ServerRequest.LOCATION_SYSTEM)

    def exit_entity(self, Entity):
        super()._exit_entity(Entity)

        super()._send_package_players(T_ServerRequest.LOCATION_SYSTEM)

    def set_planet(self, classPlanet):
        self.planets.append(classPlanet)

    def set_static_space_object(self, StaticSpaceObject):
        self.staticSpaceObjects.append(StaticSpaceObject)


