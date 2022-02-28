from python.Base.B_Item.NoQuantitative import NoQuantitative
from python.Base.Event.E_Item.E_Weapon import E_Weapon
from python.Utils.ThreadBase import ThreadBase
from random import randint
from python.Utils.MyTime import MyTime
import time

from python.Utils.Vector2D import Vector2D


class Weapon(NoQuantitative, ThreadBase, MyTime):
    ObjectToAttack: object
    autoShots: int
    radius: int
    energyCost: int
    needAmmo: int
    ammoClass: int
    minDamage: int
    maxDamage: int
    reloadTime: int
    attack_now = False

    def __init__(self, Game, data, OwnerClass):
        NoQuantitative.__init__(self, Game, data, OwnerClass)
        # Effect.__init__(self, StarWars, data["effect"])
        self.reloadTime /= 1000
        for type_ in self.restrictions:
            if type_["type"] == 4:
                self.cpu = type_["Value"]

    def use(self):
        # self = E_Weapon()
        self.Owner.use_weapon(self)
        self.inUsing = True
        self.Owner.SendPacMan.activeWeapons()

    def unuse(self):
        self.Owner.unuse_weapon(self)
        self.inUsing = False
        self.Owner.SendPacMan.activeWeapons()

    def attack(self):
        self.attack_now = True
        while self.attack_now:
            self.Owner.reduce_energy_weapon(-self.energyCost)
            self.check_effect()
            damage = self.autoShots * randint(self.minDamage, self.maxDamage)
            self.Owner.ObjectToAttack.get_damage_weapon(damage)
            if self.ObjectToAttack.health - damage <= 0:
                self.Owner.kill_weapon(self.ObjectToAttack)
                """ Может разнести по разным классам действия и предметы Base/Event/E_Item/E_Weapon"""
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
