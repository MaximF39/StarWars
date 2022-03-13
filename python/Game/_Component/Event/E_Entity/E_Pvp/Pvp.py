from python.Game._Component.Body.B_Detail.B_Energy.B_PlayerEnergy import B_PlayerEnergy
from python.Game._Component.Body.B_Detail.B_Health import RegenHealth
from python.Static.Type.Keys import Keys
from python.Static.Type.T_ObjectToReach import T_ObjectToReach
from python.Game._Component.Utils.Vector2D import Vector2D
from python.Static.Type.T_PlayerSkill import T_PlayerSkill


class Pvp(B_PlayerEnergy, RegenHealth):

    def __init__(self):
        print('send pvp')
        RegenHealth.__init__(self, self.ship[Keys.max_health], self.ship['shields'], self.skills[T_PlayerSkill.Repairing])
        B_PlayerEnergy.__init__(self, self.ship['max_energy'], self.skills[T_PlayerSkill.Repairing])

    def attack(self, data):
        match data[Keys.type]:
            case T_ObjectToReach.SHIP:
                pass
            case T_ObjectToReach.BATTLE:
                pass
            case T_ObjectToReach.ASTEROID:
                for Asteroid in self.SpaceObject.asteroids:
                    if Asteroid.id == data[Keys.id]:
                        self.ObjectToAttack = Asteroid
            case _:
                pass

        for Weapon in self.activeWeapons:
            Vector = Vector2D(self.x, self.y)
            attack_Vector = Vector2D(self.ObjectToAttack.x, self.ObjectToAttack.y)
            if Vector.in_radius(attack_Vector, Weapon.radius):
                if self.energy - Weapon.energy_cost >= 0:
                    Weapon.attack()

    def kill_weapon(self):
        self.__kill()

    def kill_device(self):
        self.__kill()

    def __kill(self):
        raise NotImplementedError('do __kill')
