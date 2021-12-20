from ..Base.SpaceObject import SpaceObject

class StaticSpaceObjects(SpaceObject):
    class_number: int
    laudable: bool


    def __init__(self, data):
        super().__init__(data)
        self.class_number = data['type']
        self.laudable = True

