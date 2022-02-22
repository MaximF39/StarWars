import time

from python.Static.cfg.Player.cfg_recovery import recovery_health, update_health
from python.Utils.ThreadBase import ThreadBase


class Health(ThreadBase):
    ship: "dict"

    def __init__(self, maxHealth, shields, repairSkills):
        self.maxHealth = maxHealth
        self.shields = shields
        self.__check_update_regen_health()

    def update_recovery_energy(self):
        while self.health != self.maxHealth:
            self.__get_heath_regen()
            time.sleep(update_health)

    def get_damage_weapon(self, damage):
        self.__change_health(-damage * (1 - 0.01 * self.shields))

    def get_damage_device(self, damage):
        self.__change_health(-damage)

    def __dead(self):
        self.__get_drop()  # send req

    def __get_drop(self):
        drop:["DB_Items"] = []
        self.Location.__get_drop(drop)

    def __check_update_regen_health(self):
        if not ThreadBase.alive_thread_timer(self, self.update_recovery_energy) \
                and self.repairSkills:
            self.__get_heath_regen()

    def __get_heath_regen(self):
        self.__change_health(recovery_health(self.health,
                                             self.repairSkills))

    def __change_health(self, health):
        sum_health = self.maxHealth + health
        if sum_health > self.maxHealth:
            self.health = self.maxHealth
        elif self.maxHealth > sum_health > 0:
            self.health += health
        elif 0 >= sum_health:
            self.health = 0
            self.__dead()


