from python.Base.BaseItem.NoQuantitative import NoQuantitative
from python.Utils.ThreadBase import ThreadBase
from random import randint
from python.Utils.MyTime import MyTime
from time import sleep


class Weapon(NoQuantitative, ThreadBase, MyTime):

    def __init__(self, Game, classNumber, OwnerClass, data):
        super().__init__(Game, classNumber, OwnerClass, data)
        # Effect.__init__(self, Game, data["effect"])
        self.reloadTimeNow = 0
        self.autoShots = self.autoShots
        self.radius = self.radius
        self.energyCost = self.energyCost
        self.needAmmo = self.needAmmo
        self.ammoClass = self.ammoClass
        self.minDamage = self.minDamage
        self.maxDamage = self.maxDamage
        self.reloadTime = self.reloadTime / 1000
        for type_ in self.restrictions:
            if type_["type"] == 4:
                self.cpu = type_["Value"]


    def use(self):
        self.Owner.use_weapon(self)
        self.inUsing = True

        self.Owner.PacMan.activeWeapons()

    def unuse(self):
        self.Owner.unuse_weapon(self)
        self.inUsing = False

        self.Owner.PacMan.activeWeapons()

    def attack(self):
        self.bool_attack = True
        while self.bool_attack:
            damage = self.autoShots * randint(self.minDamage, self.maxDamage)
            self.Owner.ObjectToAttack.get_damage_weapon(damage)
            # self.get_effect(damage)
            sleep(self.reloadTime)

    def get_reload_time(self):
        self.time += self.tick()
        return self.time

    def unattack(self):
        self.bool_attack = False