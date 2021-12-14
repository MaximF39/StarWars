from ..Utils.Vector2D import Vector2D

id_ = 0
class SpaceObject(Vector2D):
    id: int
    type: int # types: int
    size: int
    speed: float
    race: str

    def __init__(self, data: dict):
        super().__init__()




