class SpaceObject:
    id: int
    type: int
    size: int
    race: str
    aliance: int

    def __init__(self, StarWars, data):
        self.__dict__.update(data)
        self.Game = StarWars
        if not 'size' in data:
            self.size = 10000
