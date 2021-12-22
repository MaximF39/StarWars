from ..BaseClass.SpaceObject import SpaceObject

class StaticSpaceObjects(SpaceObject):
    class_number: int
    laudable: bool


    def __init__(self, Game, data):
        data['Types'] = 5
        super().__init__(Game, data)
        self.laudable = True

