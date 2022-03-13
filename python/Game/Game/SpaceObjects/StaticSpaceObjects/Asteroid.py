import random

from python.Game.Game.Drop import Drop
from python.Static.Type.Keys import Keys
from python.Game._Component.Utils.ThreadBase import ThreadBase
from python.Game._Component.Utils.Vector2D import Vector2D

class Asteroid(ThreadBase):
    IronOre: int = 49
    TitanOre: int = 51
    GoldOre: int = 53
    OsmiumOre: int = 55
    Minerals: int = 131
    Organic: int = 132

    __coef = {
        49: 1,
        51: 0.45,
        53: 0.2,
        55: 0.1,
        131: 0.3,
        132: 0.2
    }

    def __init__(self, id_, Game, AsteroidsBelt):
        ThreadBase.__init__(self)
        self.id = id_
        self.Game = Game
        self.AsteroidsBelt = AsteroidsBelt
        self.ore = 49 #TODO

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
        self.speed = 40 - self.size // 100

        self.start_timer_update(self.exit_borders, Vector2D(self.x, self.y, self.speed).time_wait(Vector2D(self.targetX, self.targetY)) * 1.8)
        # self.type_ore = dict_[Keys.type_ore] # number

    def check_coord(self):
        if abs(self.x - self.targetX) < 500 or abs(self.y - self.targetY) < 500:
            self.exit_borders()

    def drop(self):
        drop = Drop({
        'wear': int(self.size * self.__coef[self.type_ore] * (random.randint(90, 110) / 100) * ((100 + PlayerKill.skills['Mining'] ** 1.2) / 100)),
        'x': self.x,
        'y': self.y,
        Keys.class_number: self.ore,
        })
        self.AsteroidsBelt.destroyed_asteroid(self, drop)

    def exit_borders(self):
        self.AsteroidsBelt.exit_borders(self)

    def get_damage(self, damage, Who):
        self.size -= damage
        if 0 >= self.size:
            Who.kill_weapon(self)
            self.drop()

            print('kill asteroid')
