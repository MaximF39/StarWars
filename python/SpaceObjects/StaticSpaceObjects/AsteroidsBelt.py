from ...BaseClass.StaticSpaceObject import StaticSpaceObject
import random
from ...Packages.PackagesManager import PackagesManager

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
        self.create_asteroid()

    def create_asteroid(self):
        for i in range(60):
            self.asteroid_id += 1
            # mod = random.choice([0.1, -0.1, 1, -1])
            # x = mod * random.randint(-3000, 3000)
            # targetX = -mod * random.randint(-3000, 3000)
            # if 301 > abs(x):
            #     y = random.randint(-3000, 3000)
            #     targetY = -y
            # else:
            #     y = random.choice([-1, 1]) * random.randint(2700, 3000)
            #     targetY = -y
            x = 0
            y = 0
            targetX = 1
            targetY = 1
            size = random.randint(600, 3000)
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

    def SetPlayer(self, PlayerClass):
        self.players.append(PlayerClass)
        PlayerClass.SpaceObject = self
        PacMan = PackagesManager(PlayerClass.id, self.Game)
        PacMan.locationBattle()
        PacMan.asteroids()

    # def update(self):
    #     for id_asteroid in range(self.cnt_asteroid):
    #         setattr(self, f"asteroid_{id_asteroid}", Asteroid(id_asteroid))

