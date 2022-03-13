from python.Game._Component.Utils.ThreadBase import ThreadBase


class B_Health(ThreadBase):
    ship: "dict"

    def __init__(self, max_health, shields):
        ThreadBase.__init__(self)
        self.health = max_health
        self.max_health = max_health
        self.shields = shields

    def get_damage_weapon(self, damage):
        self._change_health(-damage * (1 - 0.01 * self.shields))

    def get_damage_device(self, damage):
        self._change_health(-damage)

    def __dead(self):
        self.__get_drop()  # send req

    def __get_drop(self):
        drop:["DB_Items"] = []
        self.Location.get_drop(drop)

    def _change_health(self, health):
        sum_health = self.max_health + health
        if sum_health > self.max_health:
            self.health = self.max_health
        elif self.max_health > sum_health > 0:
            self.health += health
        elif 0 >= sum_health:
            self.health = 0
            self.__dead()


