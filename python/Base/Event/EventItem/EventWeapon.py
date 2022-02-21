import time
from random import randint


class EventWeapon:

    def __init__(self, classNumber, Owner):
        self.Owner = Owner
        self.classNumber = classNumber
        self.attack_now = False

    def attack(self):
        self.attack_now = True
        while self.attack_now:
            self.Owner.reduce_energy_weapon(-self.energyCost)
            self.check_effect()
            damage = self.autoShots * randint(self.minDamage, self.maxDamage)
            self.Owner.ObjectToAttack.get_damage_weapon(damage)
            if self.ObjectToAttack.health - damage <= 0:
                self.Owner.kill_weapon(self.ObjectToAttack)
                """ Может разнести по разным классам действия и предметы Base/Event/EventItem/EventWeapon"""
                self.unattack()
            self.__recharge()

    def __recharge(self):
        self.reloadedTime = self.reloadTime
        self.tick()
        time.sleep(self.reloadTime)

    def check_effect(self):
        pass

    def get_reloaded_time(self):
        self.reloadedTime -= self.tick()
        return self.reloadedTime

    def unattack(self):
        self.attack_now = False
