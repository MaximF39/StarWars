from ...BaseClass.StaticSpaceObject import StaticSpaceObject
import random

class AsteroidsBelt(StaticSpaceObject):
    id: int
    asteroid_id: int = 0
    asteroids = []
    # cnt_asteroid: int

    def __init__(self, Game, data: dict, LocationClass):
        super().__init__(Game, data, LocationClass)
        self.id = data['id']
        # self.LocationClass()
        self.id_location = data['id_location']
        self.sector = 1
        self.players = []
        self.planets = []
        self.StaticSpaceObjects = []
        self.create_asteroid()

    def set_player(self, PlayerClass):
        self.players.append(PlayerClass)

    def create_asteroid(self):
        for i in range(60):
            self.asteroid_id += 1
            x = random.choice([-1, 1]) * random.randint(-3000, 3000)
            y = random.choice([-1, 1]) * random.randint(-3000, 3000)
            targetX = random.random() * -x
            targetY = random.random() * -y
            size = random.randint(600, 2600)
            speed = 60 - size // 100
            asteroid = {
            "id": self.asteroid_id,
            "x": x,  # сделать, чтобы создавались по краям и летели через середину
            "y": y,
            "targetX": targetX,
            "targetY": targetY,
            "size": size,
            "speed": speed,
            }
            self.asteroids.append(asteroid)

    # def update(self):
    #     for id_asteroid in range(self.cnt_asteroid):
    #         setattr(self, f"asteroid_{id_asteroid}", Asteroid(id_asteroid))

