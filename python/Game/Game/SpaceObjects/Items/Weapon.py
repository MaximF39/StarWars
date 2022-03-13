from python.Game._Component.Body.B_Item.B_BaseItem.B_NoQuantitative import B_NoQuantitative
from python.Static.Type.Package.T_ServerRequest import T_ServerRequest
from python.Game._Component.Utils.ThreadBase import ThreadBase
from random import randint
from python.Game._Component.Utils.MyTime import MyTime
import time


class Weapon(B_NoQuantitative, ThreadBase, MyTime):
    ObjectToAttack: object
    autoShots: int
    radius: int
    energy_cost: int
    needAmmo: int
    ammoClass: int
    min_damage: int
    max_damage: int
    reload_time: int
    attack_now = False

    def __init__(self, Game, data, OwnerClass):
        B_NoQuantitative.__init__(self, Game, data, OwnerClass)
        # Effect.__init__(self, StarWars, data["effect"])
        self.reload_time /= 1000
        for type_ in self.restrictions:
            if type_["type"] == 4:
                self.cpu = type_["value"]

    def use(self):
        # self = E_Weapon()
        self.Owner.use_weapon(self)
        self.in_using = True
        self.Owner.SendPacMan(T_ServerRequest.ACTIVE_WEPONS)

    def unuse(self):
        self.Owner.unuse_weapon(self)
        self.in_using = False
        self.Owner.SendPacMan(T_ServerRequest.ACTIVE_WEPONS)

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
