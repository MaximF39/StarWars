import time

from ...Packages.ShipState import ShipState
from ...MyUtils.ThreadBase import ThreadBase

from random import randint


class Mobs(ShipState, ThreadBase):
    class_number: int = 0
    __variable: list = ["player", "mob", "object", ""]
    isTaking: bool = False
    isAttack: bool = False
    
    def __init__(self, dict_: dict):
        self.device: list = dict_["device"]
        self.weapons: list = dict_["weapons"]

        self.x: float = dict_["x"]
        self.y: float = dict_["y"]
        self.state: float = dict_["state"]
        self.target_x: float = dict_["target_x"]
        self.target_y: float = dict_["target_y"]
        self.object_to_reach_id: int = dict_["object_to_reach_id"]
        self.object_to_reach_type: int = dict_["object_to_reach_type"]
        self.Player_relation: int = dict_["Player_relation"]
        self.id = dict_["id"]
        self.health = dict_["health"]
        self.energy = dict_["energy"]
        self.speed = dict_["speed"]
        self.repairHealth = dict_["repairHealth"]  # восстановление хп (int)
        self.repairEnergy = dict_["repairEnergy"]  # восстановление энки (int)
        self.max_health = self.health
        self.max_energy = self.energy

    def main(self):
        self.start_update("__all_repair", 1)
        self.start_update("start", 200 // self.speed)

    def start(self):
        objects = self.request_location()
        if not self.isTaking and not self.isAttack:
            self.update()
            for obj in objects:
                self.send_dev(obj)
        else:
            if self.object_to_reach_id not in objects:
                self.__to_begin()

    def send_dev(self, object=None):
        typeObject: str = self.__examination(object)
        if typeObject == self.__variable[0]:
            self.__attack(object)
        elif typeObject == self.__variable[1] and object.class_number != self.class_number:
            self.__attack(object)
        elif typeObject == self.__variable[2]:
            self.__take(object)

    def update(self):
        self.move()

    def move(self):
        x, y = self.get_random_coords()
        self.x += x
        self.y += y

    def get_random_coords(self) -> tuple:
        return randint(-200, 200), randint(-200, 200)

    def get_player_damage(self, id: int, hp: int):
        self.__set_health(hp)
        self.object_to_reach_id = id

    def get_device(self) -> list:
        return self.device

    def get_weapons(self) -> list:
        return self.weapons

    def request_location(self):
        # запрос к локации, ответ в переменную response
        response = None
        objects = response.object  # все объекты на локации
        return objects

    def dead(self):
        self.health = 0
        self.new_coords()
        self.drop = list(map(self.ratio, self.device + self.weapons))

    def ratio(self, object: int):
        dict_: dict # словарь с коэфами для объектов
        return dict_[object]

    def new_coords(self):
        self.x = randint(0, 800)
        self.y = randint(0, 800)

    def __examination(self, object) -> str:
        if object.id > 0:
            return self.__variable[0]
        elif object.id < 0:
            return self.__variable[1]
        elif object.guid is not None:
            return self.__variable[2]
        else:
            return self.__variable[3]

    def __all_repair(self):
        self.health = self.__repair(self.health, self.max_health, self.repairHealth)
        self.energy = self.__repair(self.energy, self.max_energy, self.repairEnergy)

    def __repair(self, param: int, max_params: int, repair: int):
        if param < max_params:
            param += repair
        else:
            param = max_params
        return param

    def __attack(self, object):
        self.isTaking = False
        self.isAttack = True
        self.object_to_reach_id = object.id
        self.toObject(object)

    def __take(self, object):
        self.isTaking = True
        self.object_to_reach_id = object.guid
        self.toObject(object)

    def toObject(self, object):
        self.x = object.x
        self.y = object.y

    def __set_health(self, health: int):
        self.health -= health
        if self.health <= 0:
            self.dead()

    def __set_energy(self, energy: int):
        self.energy -= energy if self.energy >= 0 else 0
