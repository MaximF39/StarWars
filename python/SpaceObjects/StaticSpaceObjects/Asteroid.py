import random
from random import randint
from python.Packages.PackagesManager import PackagesManager
from python.SpaceObjects.Item import item
from python.Utils.ThreadBase import ThreadBase
from python.Utils.Vector2D import Vector2D

class Asteroid(ThreadBase):
    IronOre: int = 49
    TitanOre: int = 51
    GoldOre: int = 53
    OsmiumOre: int = 55
    Minerals: int = 131
    Organic: int = 132

    coef = {
        49: 1,
        51: 0.45,
        53: 0.2,
        55: 0.1,
        131: 0.3,
        132: 0.2
    }

    def __init__(self, id_, Game, AsteroidsBelt):
        self.id = id_
        self.Game = Game
        self.AsteroidsBelt = AsteroidsBelt

        type_ = random.choice([1, 2])
        mod_x = random.choice([-1, 1])
        mod_y = random.choice([-1, 1])
        match type_:
            case 1:  # big X small Y # 1
                random_x = (0, 3000)
                random_y = (2700, 3000)
            case _:  # Big Y small x # 2
                random_x = (2700, 3000)
                random_y = (0, 3000)

        self.x = mod_x * random.randint(*random_x)
        self.targetX = -mod_x * random.randint(*random_x)
        self.y = mod_y * random.randint(*random_y)
        self.targetY = -mod_y * random.randint(*random_y)

        self.size = random.randint(600, 3000)
        self.speed = 60 - self.size // 100

        self.start_timer_update(self.end_target, Vector2D(self.x, self.y, self.speed).time_wait(Vector2D(self.targetX, self.targetY)))
        # self.type_ore = dict_["type_ore"] # number

    def get_coords(self):
        pass

    def drop(self, PlayerKill):
        item_dict = {}
        item_dict['count'] = int(self.size * self.coef[self.type_ore] * (random.randint(90, 110) / 100) * ((100 + PlayerKill.skills['Mining'] ** 1.2) / 100))
        item_dict['x'] = self.x
        item_dict['y'] = self.y
        ore = item()

        PacMan = PackagesManager(PlayerKill.id, self.Game)
        PacMan.locationBattle()
        PacMan.items()

    def end_target(self):
        self.AsteroidsBelt.remove_asteroid(self)

    def get_damage(self, damage):
        self.size -= damage
        if 0 >= self.size:
            # self.drop()
            print('kill asteroid')
