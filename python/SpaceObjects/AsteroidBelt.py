from . import SpaceObject, Asteroid

class AsteroidBelt(SpaceObject):
    id: int
    cnt_asteroid: int

    def __init__(self, id_, data: dict):
        super().__init__(data)
        self.id = id_

    def update(self):
        for id_asteroid in range(self.cnt_asteroid):
            setattr(self, f"asteroid_{id_asteroid}", Asteroid(id_asteroid))

