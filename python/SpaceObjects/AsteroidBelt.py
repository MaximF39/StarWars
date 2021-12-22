from ..BaseClass.SpaceObject import SpaceObject
from .Asteroid import Asteroid

class AsteroidBelt(SpaceObject):
    id: int
    # cnt_asteroid: int

    def __init__(self, Game, data: dict):
        data['Types'] = 4
        super().__init__(Game, data)
        self.id = data['id']
        self.id_location = data['id_location']

        self.set_space_object_on_location(self.id_location)

    # def update(self):
    #     for id_asteroid in range(self.cnt_asteroid):
    #         setattr(self, f"asteroid_{id_asteroid}", Asteroid(id_asteroid))

