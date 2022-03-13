import time
from random import randint


class E_Weapon:

    def __init__(self, class_number, Owner):
        self.Owner = Owner
        self.class_number = class_number
        self.attack_now = False

    def attack(self):
        self.attack_now = True
        while self.attack_now:
            self.Owner.reduce_energy_weapon(-self.energy_cost)
            self.check_effect()
            damage = self.autoShots * randint(self.min_damage, self.max_damage)
            self.Owner.ObjectToAttack.get_damage_weapon(damage)
            if self.ObjectToAttack.health - damage <= 0:
                self.Owner.kill_weapon(self.ObjectToAttack)
                """ Может разнести по разным классам действия и предметы _Component/Event/E_Item/E_Weapon"""
                self.unattack()
            self.__recharge()

    def __recharge(self):
        self.reloadedTime = self.reload_time
        self.tick()
        time.sleep(self.reload_time)

    def check_effect(self):
        pass

    def get_reloaded_time(self):
        self.reloadedTime -= self.tick()
        return self.reloadedTime

    def unattack(self):
        self.attack_now = False
