from time import sleep
from random import randint

from python.Base.B_Player.B_Player import B_Player
from python.Base.Pvp.Health import Health
from python.Config.CFG_Mob.cfg_mob import time_revive
from python.Utils.ThreadBase import ThreadBase


class Mob(B_Player, ThreadBase):
    RADIUS: int
    max_x: int
    max_y: int
    min_x: int
    min_y: int
    target = None  # Предмет
    alive = True
    attack: "Player" = None

    def __init__(self, Game, dict_: dict):
        ThreadBase.__init__(self)
        B_Player.__init__(self, Game, dict_)
        self.__dict__.update({
            "max_x": self.RADIUS,
            "max_y": self.RADIUS,
            "min_x": -self.RADIUS,
            "min_y": -self.RADIUS,
        })
        self.update()

    def update(self):
        pass
        # self.start_const_update(self.move, 5)

    def move_mobs(self):
        if not self.target and self.alive and not self.attack:
            x, y = self.__move_random()
            x_move = self.x + x
            y_move = self.y + y
            if abs(x_move) > self.max_x:
                x = -1 * x
            else:
                x = x
            if abs(y_move) > self.max_y:
                y = -1 * y
            else:
                y = y
            self.move(x, y)

    def __move_random(self) -> tuple:
        return randint(self.max_x, self.min_x), randint(self.max_y, self.min_y)

    def get_player_damage_weapon(self, Who: int, hp: int):
        Health.get_damage_weapon(self, hp)
        if not self.attack:
            self.attack = Who

    def dead(self):
        self.alive = False
        self.__get_drop()
        sleep(time_revive)
        self.revive()
        self.Location._remove_player(self)

    def revive(self):
        self.spawn()
        self.alive = True

    def spawn(self):
        x = randint(-1 * self.max_x, self.max_x)
        y = randint(-1 * self.max_y, self.max_y)
        self._set_x_y(x, y)
        self.Location.set_entity(self)

    def _attack(self, Who):
        self.pick_up_item = False
        self.attack = Who

    def __get_drop(self):  # TODO return experiences (maybe credits) and return items
        drop = None
        for key, value in self.__add_drop().items():
            if not drop[key]:
                drop[key] = value
            else:
                drop[key] += value
        return drop
