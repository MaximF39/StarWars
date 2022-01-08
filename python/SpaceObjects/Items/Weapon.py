from .BaseItem.NoQuantitative import NoQuantitative
from ...Packages.PackagesManager import PackagesManager
from python.Utils.ThreadBase import ThreadBase
from random import randint
from python.Utils.MyTime import MyTime
from time import sleep

class Weapon(NoQuantitative, ThreadBase, MyTime):

    def __init__(self, Game, classNumber, OwnerClass):
        super().__init__(Game, classNumber, OwnerClass)
        self.reloadTimeNow = 0
        self.autoShots = self.data["autoShots"]
        self.radius = self.data["radius"]
        self.energyCost = self.data["energyCost"]
        self.needAmmo = self.data["needAmmo"]
        self.ammoClass = self.data["ammoClass"]
        self.minDamage = self.data["minDamage"]
        self.maxDamage = self.data["maxDamage"]
        self.reloadTime = self.data["reloadTime"] / 1000
        for type_ in self.data["restrictions"]["data"]:
            if type_["type"] == 4:
                self.cpu = type_["Value"]

    def use(self):
        self.Owner.use_weapon(self)
        self.inUsing = True

        PacMan = PackagesManager(self.Owner.id, self.Game)
        PacMan.activeWeapons()

    def unuse(self):
        self.Owner.unuse_weapon(self)
        self.inUsing = False

        PacMan = PackagesManager(self.Owner.id, self.Game)
        PacMan.activeWeapons()

    def clicked(self):
        self.Owner.attack()

    def attack(self):
        self.bool_attack = True
        while self.bool_attack:
            self.Owner.ObjectToAttack.get_damage(self.autoShots * randint(self.minDamage, self.maxDamage))
            sleep(self.reloadTime)

    def get_reload_time(self):
        self.time += self.tick()
        return self.time

    def unattack(self):
        self.bool_attack = False