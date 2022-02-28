from python.Base.Pvp.Health import Health
from .Energy import Energy
from python.Static.Type.T_ObjectToReach import T_ObjectToReach
from python.Utils.Vector2D import Vector2D
from python.Static.Type.T_PlayerSkill import T_PlayerSkill


class Pvp(Health, Energy):
    activeWeapons: list["T_Weapon"]
    ObjectToAttack: "SpaceObject"
    x: int
    y: int
    def __init__(self, maxHealth, maxEnergy, shields, data_skills: dict):
        repair = data_skills[T_PlayerSkill.Repairing]
        self.Defending = data_skills[T_PlayerSkill.Defending]
        self.Attacking = data_skills[T_PlayerSkill.Attacking]
        self.Tactics = data_skills[T_PlayerSkill.Targeting]
        Health.__init__(self, maxHealth, shields, repair)
        Energy.__init__(self, maxEnergy, repair)

    def attack(self, data):
        match data['type']:
            case T_ObjectToReach.SHIP:
                pass
            case T_ObjectToReach.BATTLE:
                pass
            case T_ObjectToReach.ASTEROID:
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
