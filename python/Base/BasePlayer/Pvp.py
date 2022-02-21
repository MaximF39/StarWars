from python.Base.BasePlayer.Health import Health
from .Energy import Energy
from python.Static.Type.ObjectToReachType import ObjectToReachType
from python.Utils.Vector2D import Vector2D
from python.Base.BasePlayer.ShipEvent.MoveEvent import MoveEvent


class Pvp(Health, Energy):
    activeWeapons: list
    ObjectToAttack: "SpaceObject"
    x: int
    y: int
    def __init__(self, maxHealth, maxEnergy, shields, data_skills: dict):
        self.init_pvp_skills(data_skills)
        Health.__init__(self, maxHealth, shields, self.Repairing)
        Energy.__init__(self, maxEnergy, self.Repairing)

    def init_pvp_skills(self, data):
        self.Repairing = data['Repairing']
        self.Defending = data['Defending']
        self.Attacking = data['Attacking']
        self.Tactics = data['Targeting']

    def attack(self, data):
        match data['type']:
            case ObjectToReachType.SHIP:
                pass
            case ObjectToReachType.BATTLE:
                pass
            case ObjectToReachType.ASTEROID:
                for Asteroid in self.SpaceObject.asteroids:
                    if Asteroid.id == data['id']:
                        self.ObjectToAttack = Asteroid
            case _:
                pass

        for Weapon in self.activeWeapons:
            Vector = Vector2D(self.x, self.y)
            attack_Vector = Vector2D(self.ObjectToAttack.x, self.ObjectToAttack.y)
            if Vector.in_radius(attack_Vector, self.Weapon.radius):
                if self.energy - self.Weapon.energyCost >= 0:
                    Weapon.attack()

    def kill_weapon(self):
        self.__kill()

    def kill_device(self):
        self.__kill()

    def __kill(self):
        raise NotImplementedError('do __kill')
