from random import randint

from python.SpaceObjects.Item import item


class Asteroid:
    IronOre: int = 49
    TitanOre: int = 51
    GoldOre: int = 53
    OsmiumOre: int = 55
    Minerals: int = 131
    Organic: int = 132

    def __init__(self, dict_: dict):
        self.id = dict_["id"]
        self.x = dict_["x"]
        self.y = dict_["y"]
        self.targetX = dict_["targetX"]
        self.targetY = dict_["targetY"]
        self.size = dict_["size"]
        self.speed = dict_["speed"]
        self.type_ore = dict_["type_ore"]

    def drop(self, PlayerKill):
        # PlayerKills new add
        if PlayerKill.skills["mining"] >= randint(0, 12):
            ore_size = self.size * (self.type_ore ** -1) // 2 * (randint(1, 10) / 10)
            ore = item()
            ore.drop(ore_size)


