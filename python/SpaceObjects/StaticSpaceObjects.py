from ..BaseClass.SpaceObject import SpaceObject

class StaticSpaceObjects(SpaceObject):
    class_number: int
    laudable: bool


    def __init__(self, Game, data):
        super().__init__(Game, data)
        self.location = data["location"]
        self.laudable = True
        self.set_space_object_on_location(self.location)


    def set_space_object_on_location(self, id_location):
        getattr(self.Game, f"Location_{id_location}").set_static_space_object(self.__dict__)

