
from python.Base.SpaceObject.Set.SetPlayer import SetPlayer
from python.Base.SpaceObject.Set.SetMob import SetMob

class SetLocation(SetPlayer, SetMob):

    def __init__(self):
        SetMob.__init__(self)
        SetPlayer.__init__(self)
        self.players: list["CFG_Player"] = []
        self.mobs: list["CFG_Mob"] = []
        self.planets:list = []
        self.StaticSpaceObjects:list = []

    def set_entity(self, Entity): #CFG_Player or CFG_Mob
        Entity.Location.remove_entity(Entity)
        Entity.Location = self
        self.__append_entity(Entity)

    def remove_entity(self, Entity):
        self.__remove_entity(Entity)

    def set_planet(self, classPlanet):
        self.planets.append(classPlanet)

    def set_static_space_object(self, StaticSpaceObject):
        self.StaticSpaceObjects.append(StaticSpaceObject)

    def __remove_entity(self, Entity):
        entity_name = Entity.__class__.__name__
        if entity_name == "CFG_Mob":
            self._remove_mob(Entity)
        elif entity_name == "CFG_Player":
            self._remove_player(Entity)

    def __append_entity(self, Entity):
        entity_name = Entity.__class__.__name__
        if entity_name == "CFG_Mob":
            SetPlayer._set_player(self, Entity)
        elif entity_name == "CFG_Player":
            SetMob._set_mob(self, Entity)