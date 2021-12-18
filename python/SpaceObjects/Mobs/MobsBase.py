import time

from ...Packages.ShipState import ShipState
from ...MyUtils.ThreadBase import ThreadBase


class Mobs(ShipState, ThreadBase):
    class_number: int = 0
    __variable: list = ["player", "mob", "object", ""]

    def __init__(self, dict_: dict):
        self.__to_begin()

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
        self.repairHealth = dict_["repairHealth"]  # восстановление хп
        self.repairEnergy = dict_["repairEnergy"]  # восстановление энки
        self.max_health = self.health
        self.max_energy = self.energy

    def main(self):
        self.start_update("__all_repair", 1)
        self.start_update("start", 5)

    def start(self):
        objects = self.request_location()
        if not self.__isTaking and not self.__isAttack:
            for obj in objects:
                self.send_dev(obj)
        else:
            if self.object_to_reach_id not in objects:
                self.__to_begin()

    def send_dev(self, object=None):
        typeObject: str = self.__examination(object)
        if typeObject == self.__variable[0]:
            self.__attack(object.id)
        elif typeObject == self.__variable[1] and object.class_number != self.class_number:
            self.__attack(object.id)
        elif typeObject == self.__variable[2]:
            self.__take(object.guid)

    def update(self):
        self.move()

    def move(self):
        pass

    def get_player_damage(self, id: int, hp: int) -> None:
        self.__set_health(hp)
        self.__attack(id)

    def get_device(self) -> list:
        return self.device

    def get_weapons(self) -> list:
        return self.weapons

    def request_location(self):
        # запрос к локации, ответ в переменную response
        response = None
        objects = response.object  # все объекты на локации
        return objects

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

    def __repair(self, param, max_params, repair):
        if param < max_params:
            param += repair
        else:
            param = max_params
        return param

    def __to_begin(self):
        self.__isTaking: bool = False
        self.__isAttack: bool = False

    def __attack(self, id: int):
        self.__isTaking = False
        self.__isAttack = True
        self.object_to_reach_id = id
        pass

    def __take(self, guid: int):
        self.__isTaking = True
        self.object_to_reach_id = guid
        pass

    def __set_health(self, health: int):
        self.health -= health

    def __set_energy(self, energy: int):
        self.energy -= energy
