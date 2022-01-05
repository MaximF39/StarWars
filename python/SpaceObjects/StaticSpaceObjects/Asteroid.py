import random
from random import randint
from python.Packages.PackagesManager import PackagesManager
from python.SpaceObjects.Item import item


class Asteroid:
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

    def __init__(self, dict_: dict, Game):
        self.id = dict_["id"]
        self.x = dict_["x"]
        self.y = dict_["y"]
        self.targetX = dict_["targetX"]
        self.targetY = dict_["targetY"]
        self.size = dict_["size"]
        self.speed = dict_["speed"]
        self.Game = Game
        # self.type_ore = dict_["type_ore"] # number

    def drop(self, PlayerKill):
        item_dict = {}
        item_dict['count'] = int(self.size * self.coef[self.type_ore] * (random.randint(90, 110) / 100) * ((100 + PlayerKill.skills['Mining'] ** 1.2) / 100))
        item_dict['x'] = self.x
        item_dict['y'] = self.y
        ore = item()

        PacMan = PackagesManager(PlayerKill.id, self.Game)
        PacMan.locationBattle()
        PacMan.items()


