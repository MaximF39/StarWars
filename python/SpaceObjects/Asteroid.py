import random
from . import ThreadBase, cfg_update
from ..BaseClass.MovableSpaceObject import MovableSpaceObject


class Asteroid(MovableSpaceObject, ThreadBase):
    def __init__(self, Game, data):
        super().__init__(Game, data)
        self.x = random.randint(100, 400)  # сделать, чтобы создавались по краям и летели через середину
        self.y = random.randint(100, 400)
        self.target_x = random.randint(800, 1000)
        self.target_y = random.randint(800, 1000)
        self.size = random.randint(600, 2300)
        self.speed = random.randint(10, 30)
