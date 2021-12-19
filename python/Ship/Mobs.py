from . import ThreadBase, BasePlayer

from time import sleep
from random import randint


class Mobs(BasePlayer, ThreadBase):
    _variable: list = ["player", "mob", "object", ""]
    isTaking: bool = False
    isAttack: bool = False
    x_max = 2000  # and minimum -
    y_max = 2000  # and minimum -
    x_move = 300
    y_move = 300

    def __init__(self, dict_: dict):
        super().__init__(dict_)
        self.device: list = dict_["device"]
        self.weapons: list = dict_["weapons"]

        self.repair_health = dict_["repair_health"]  # восстановление хп (int)
        self.recovery_energy = dict_["recovery_energy"]  # восстановление энки (int)

        self.update()

    def send_dev(self, object=None):
        typeObject: str = self._examination(object)
        if typeObject == self._variable[0]:
            self._attack(object)
        elif typeObject == self._variable[1] and object.class_number != self.class_number:
            self._attack(object)
        elif typeObject == self._variable[2]:
            self._take(object)

    def update(self):
        self.start_update("_repair_health", 1)
        self.start_update("_recovery_energy", 1)
        self.start_update("trigger", 1)
        self.start_update("move", 3)

    @ThreadBase.end_thread
    def trigger(self): # TODO
        objects = self.request_location()  # get locations
        if self.isTaking or self.isAttack:
            if self.object_to_reach_id not in objects:
                self.isTaking: bool = False
                self.isAttack: bool = False

    @ThreadBase.end_thread
    def move(self):
        x, y = self.move_random()
        x_move = self.x + x
        y_move = self.y + y
        if abs(x_move) > self.x_max:
            self.x -= x
        else:
            self.x += x
        if abs(y_move) > self.y_max:
            self.y -= y
        else:
            self.y += y

    def move_random(self) -> tuple:
        return randint(-1 * self.x_move, self.x_move), randint(-1 * self.y_move, self.y_move)

    def get_player_damage(self, id_: int, hp: int):
        self.get_damage(hp)
        if not self.isAttack:
            self.isAttack = True
            self.object_to_reach_id = id_

    def use_device(self) -> list: # use device if have player and energy and check lvl player.
        pass

    def request_location(self):
        # запрос к локации, ответ в переменную response
        response = None
        objects = response.object  # все объекты на локации
        return objects

    def dead(self):
        self.drop = self.get_drop()
        # send("i'm dead")
        self.del_all_update()
        sleep(60)
        self.update()
        self.new_cords()
        # send('I live')

    def get_drop(self): # TODO return experiences (maybe credits) and return items
        drop = dict()  # list(map(self.ratio, self.device + self.weapons))
        return drop

    def new_cords(self):
        self.x = randint(-1 * self.x_max, self.x_max)
        self.y = randint(-1 * self.y_max, self.y_max)

    def _examination(self, object) -> str:
        if object.id > 0:
            return self._variable[0]
        elif object.id < 0:
            return self._variable[1]
        elif object.guid is not None:
            return self._variable[2]
        else:
            return self._variable[3]

    @ThreadBase.end_thread
    def _repair_health(self):
        if self.health + self.repair_health > self.max_health:
            self.health = self.max_health
        else:
            self.health += self.repair_health

    @ThreadBase.end_thread
    def _recovery_energy(self):
        if self.energy + self.recovery_energy > self.max_energy:
            self.energy = self.max_energy
        else:
            self.energy += self.repair_health

    def _attack(self, object):
        self.isTaking = False
        self.isAttack = True
        self.object_to_reach_id = object.id
        self.to_object(object)

    def _take(self, object):
        self.isTaking = True
        self.object_to_reach_id = object.guid
        self.to_object(object)

    def to_object(self, object):
        self.x = object.x
        self.y = object.y

    def get_damage(self, damage: int):
        if 0 >= self.health - damage:
            self.health = 0
            self.dead()
        self.health -= damage

    def remove_energy(self, remove_energy: int):
        if 0 > self.energy - remove_energy:
            self.energy = 0
        self.energy -= remove_energy