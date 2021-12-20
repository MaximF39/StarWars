from ..Utils.Vector2D import Vector2D

class SpaceObject:
    id: int
    type: int
    size: int
    race: str
    aliance: int

    def __init__(self, data):
        self.id = data['id']
        self.type = data['type'] if 'type' in data else None
        self.size = data['size'] if 'size' in data else 10000
        self.race = data['race']
        self.aliance = data['aliance']


