from . import ThreadBase, BasePlayer

from time import sleep
from random import randint


class Mobs(BasePlayer, ThreadBase):
    _variable: list = ["player", "mob", "object", ""]
    x_max = 2000  # and minimum -
    y_max = 2000  # and minimum -
    x_move = 300
    y_move = 300

    def __init__(self, dict_: dict):
        super().__init__(dict_)
        self.update()

    def update(self):
        self.start_update("trigger", 1)
        self.start_update("move", 3)

    @ThreadBase.end_thread
    def trigger(self): # TODO
        objects = self.request_location()  # packages_entrance locations
        if self.pick_up_item or self.attack:
            if self.object_to_reach_id not in objects:
                self.pick_up_item: bool = False
                self.attack: bool = False

    @ThreadBase.end_thread
    def move_mobs(self):
        x, y = self.move_random()
        x_move = self.x + x
        y_move = self.y + y
        if abs(x_move) > self.x_max:
            x = -1 * x
        else:
            x = x
        if abs(y_move) > self.y_max:
            y = -1 * y
        else:
            y = y
        self.move(x, y)

    def move_random(self) -> tuple:
        return randint(-1 * self.x_move, self.x_move), randint(-1 * self.y_move, self.y_move)

    def get_player_damage(self, id_: int, hp: int):
        self.get_damage_weapon(hp)
        if not self.attack:
            self.attack = True
            self.object_to_reach_id = id_

    def use_device(self) -> list: # use device if have player and energy and check lvl player.
        pass

    def request_location(self):
        # запрос к локации, ответ в переменную response
        response = None
        objects = response.object  # все объекты на локации
        return objects

    def dead(self):
        self.get_drop() # send request
        # send("i'm dead")
        self.del_all_update()
        sleep(60)
        self.update()
        self.new_cords()
        # send('I live')

    def get_drop(self): # TODO return experiences (maybe credits) and return items
        drop = super(Mobs, self).get_drop()
        for key, value in self.__add_drop().items():
            if not drop[key]:
                drop[key] = value
            else:
                drop[key] += value
        return drop

    def __add_drop(self): # todo drop
        return dict()

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

    def _attack(self, object):
        self.pick_up_item = False
        self.attack = True
        self.object_to_reach_id = object.id
        self.to_object(object)

    def _take(self, object):
        self.pick_up_item = True
        self.object_to_reach_id = object.guid
        self.to_object(object)

    def to_object(self, object):
        self.x = object.x
        self.y = object.y
