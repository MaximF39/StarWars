from python.Base.BasePlayer.Health import Health
from .Energy import Energy
from python.Static.Type.ObjectToReachType import ObjectToReachType
from python.Utils.Vector2D import Vector2D


class Pvp(Health, Energy):

    def __init__(self):
        Health.__init__(self)
        Energy.__init__(self)

    def attack(self, data):
        match data['type']:
            case ObjectToReachType.PLANET:
                pass
            case ObjectToReachType.SHIP:
                pass
            case ObjectToReachType.BATTLE:
                pass
            case ObjectToReachType.ITEM:
                pass
            case ObjectToReachType.STATIC_SPACE_OBJECT:
                pass
            case ObjectToReachType.ASTEROID:
                for Asteroid in self.SpaceObject.asteroids:
                    if Asteroid.id == data['id']:
                        self.ObjectToAttack = Asteroid

        self.attack_now = True
        Vector = Vector2D(self.x, self.y)
        # attack_Vector = Vector2D(self.ObjectToAttack.x, self.ObjectToAttack.y)
        # for weapon in self.activeWeapons:
        #     if Vector.in_radius(attack_Vector, weapon.RADIUS):
        #         weapon.attack()

    def kill_weapon(self):
        self.__get_experience(5)
        self.__get_status(5)

    def kill_device(self):
        self.__get_experience(5)
        self.__get_status(5)


