import random
from . import ThreadBase, cfg_update

class Asteroid(ThreadBase):
    id: int
    x: float
    y: float
    target_x: float
    target_y: float
    size: int
    speed: float
    time_update = cfg_update['asteroid']

    def __init__(self, id_):
        super().__init__()
        self.id = id_
        self.x = random.randint(100, 400)  # сделать, чтобы создавались по краям и летели через середину
        self.y = random.randint(100, 400)
        self.target_x = random.randint(800, 1000)
        self.target_y = random.randint(800, 1000)
        self.size = random.randint(600, 2300)
        self.speed = random.randint(10, 30)
