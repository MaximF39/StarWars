from python.Game import I_SpaceObjectSetter
from python.Static.Type.Package.T_ServerRequest import T_ServerRequest


class AsteroidBeltSetter(I_SpaceObjectSetter):
    def __init__(self):
        super().__init__()

    def set_entity(self, Entity):
        super()._set_entity(Entity)
        Entity.SpaceObject = self
        if Entity.__class__.__name__ == "B_Player":
            super()._send_package_players(T_ServerRequest.LOCATION_BATTLE, T_ServerRequest.ASTEROIDS)

    def remove_entity(self, Entity):
        super()._remove_entity(Entity)
        Entity.SpaceObject = Entity.Location
        Entity.set_x_y(self.x, self.y)
        Entity.not_target()
        if Entity.__class__.__name__ == "B_Player":
            Entity.SendPacMan(T_ServerRequest.LOCATION_SYSTEM)
            super()._send_package_players(T_ServerRequest.LOCATION_BATTLE)

    def exit_entity(self, Entity):
        super()._exit_entity(Entity)

        if Entity.__class__.__name__ == "B_Player":
            super()._send_package_players(T_ServerRequest.LOCATION_BATTLE)