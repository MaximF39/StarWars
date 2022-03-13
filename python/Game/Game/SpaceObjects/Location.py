from python.Game._Component.Event.E_SpaceObject.Set.SpaceObjectSetter.LocationSetter import LocationSetter
from python.Game._Component.Utils.ThreadBase import ThreadBase
from python.Game._Component.Body.B_Detail.B_Inventory.Inventory import Inventory
from python.Game._Component.Body.B_SpaceObject.Create import C_SpaceObject

class Location(LocationSetter, Inventory, C_SpaceObject, ThreadBase):
    id: int

    def __init__(self, StarWars, data: dict):
        self.__dict__.update(data)
        super().__init__()
        self.Game = StarWars
        C_SpaceObject.create_space_object(self)

    def get_drop(self, drop):
        self.inventory.extend(drop)

    def kill(self, Entity):
        self.__remove_entity(Entity)
