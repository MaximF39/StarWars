from python.Utils.Vector2D import Vector2D
import math
# from ..Packages.
import ast
import json
import threading
import time
from . import Ship
from ..Utils.ThreadBase import ThreadBase
from ..Packages.PackagesManager import PackagesManager
from ..Utils.MyTime import MyTime


class BasePlayer(Ship, ThreadBase, MyTime):
    # ObjectToReach:  = {}
    # attack_now: dict = {}

    def __init__(self, Game, dict_: dict):
        super().__init__(Game, dict_)
        MyTime.__init__(self)
        self.speed = self.ship['maxSpeed']
        self.health = self.ship['maxHealth']
        self.energy = self.ship['maxEnergy']

        self.Location = getattr(self.Game, f'Location_{dict_["Location"]}')
        self.SpaceObject = None
        self.ObjectToReach = None

        self.targetX = self.x
        self.targetY = self.y

        self.object_to_reach_id: int = self.Location
        # self.object_to_reach_type: int = 7  # getattr(Game, f"Location_{self.object_to_reach_id}").type

        self.effects = []
        self.hold = 0
        self.OldTick = self.tick()
        self.OldTarget = False
        self.sendInfoLocation()
        self.upgrade()

    def sendInfoLocation(self):
        self.Location.EntryPlayer(self)

    def object_to_reach_system(self, type_, id_):
        self.object_to_reach_type = type_
        self.object_to_reach_id = id_

    def add_item_inventory(self, ItemClass):
        self.hold += ItemClass.allSize
        self.inventory.append(ItemClass)

    def remove_item_inventory(self, ItemClass):
        self.hold -= ItemClass.size
        self.inventory.remove(ItemClass)

    def upgrade(self):
        pass
        # a = threading.Thread(target=self.move)
        # a.start()

    def not_target(self):
        self.targetX = self.x
        self.targetY = self.y

    def leaveLocation(self):
        print(self.SpaceObject)
        self.SpaceObject.leaveLocation(self)
        self.x = self.SpaceObject.x
        self.y = self.SpaceObject.y
        self.not_target()
        self.SpaceObject = None
        self.ObjectToReach = None
        PacMan = PackagesManager(self.id, self.Game)
        PacMan.shipsPosition()
        PacMan.shipsState()
        PacMan.ship()
        PacMan.playerShip()
        PacMan.locationSystem()

    def target(self, x, y):
        self.targetX = x
        self.targetY = y

    def WaitForCord(self):
        self.OldTarget = False
        print(self.ObjectToReach)
        if self.ObjectToReach:
            self.ObjectToReach.SetPlayer(self)
            self.ObjectToReach = False
        else:
            self._set_x_y(self.targetX, self.targetY)


    def _set_x_y(self, x=None, y=None, Vector2d=None):
        if not ((x and y) or Vector2d):
            raise NotImplementedError('Not x, y OR Vector2d')
        if x and y:
            self.x = x
            self.y = y
        else:
            self.x = Vector2d.x
            self.y = Vector2d.y

    def _set_target_x_y(self, targetX=None, targetY=None, Vector2d=None):
        if not ((targetX and targetY) or Vector2d):
            raise NotImplementedError('Not targetX, targetY OR Vector2d')
        if targetX and targetY:
            self.targettargetX = targetX
            self.targettargetY = targetY
        else:
            self.x = Vector2d.x
            self.y = Vector2d.y

    def _default_move(self, mod, player_vector, target_vector):
        if (mod == 'move_to_move' or mod == 'stop') and self.OldTarget:
            self.del_thread_timer(self.WaitForCord)
            self.OldTick = self.tick()
            Vector = player_vector.move(target_vector, self.OldTick)
            self.x = Vector.x
            self.y = Vector.y
        else:
            self.tick()
        if mod == 'stop':
            self.not_target()
        else:
            self.targetX = target_vector.x
            self.targetY = target_vector.y
            time_w = player_vector.time_wait(Vector2D(self.targetX, self.targetY))
            self.start_timer_update(self.WaitForCord, time_w)
            print(f'{time_w=}, {self.targetX=}, {self.targetY=}')


    def move(self, targetX=None, targetY=None, *, stop=False, SpaceObject=None):
        if not ((targetX and targetY) or SpaceObject or stop):
            raise NotImplementedError('Не указано что-то из этого \n (targetX and targetY) or SpaceObject:')
        if SpaceObject:
            self.ObjectToReach = SpaceObject
            self.targetX = SpaceObject.x
            self.targetY = SpaceObject.y
        else:
            if targetX and targetY:
                self.targetX = targetX
                self.targetY = targetY
        player_vector = Vector2D(self.x, self.y, self.speed)
        target_vector = Vector2D(self.targetX, self.targetY)
        if stop:  # just stop
            if self.OldTarget:
                self._default_move('stop', player_vector, target_vector)
                self.OldTarget = False
        elif self.OldTarget:  # move to move
            self._default_move('move_to_move', player_vector, target_vector)
            self.OldTarget = True
        else:  # stop to move
            self._default_move('stop_to_move', player_vector, target_vector)
            self.OldTarget = True

    def attack(self, data):
        match data['ObjectToReachType']:
            case 1:  # planet
                pass
            case 2:  # Owner
                self.ObjectToAttack = getattr(self.Game, f'Player_{data["id"]}')
            case 3:  # battle
                pass
            case 4:  # item
                pass
            case 5:  # static space object
                pass
            case 6:  # asteroid
                for Asteroid in self.SpaceObject.asteroids:
                    if Asteroid.id == data['id']:
                        self.ObjectToAttack = Asteroid

        self.attack_now = True
        Vector = Vector2D(self.x, self.y)
        attack_Vector = Vector2D(self.ObjectToAttack.x, self.ObjectToAttack.y)
        for weapon in self.activeWeapons:
            if Vector.in_radius(attack_Vector, weapon.radius):
                weapon.attack()

    def set_object_to_reach(self, data):
        match data['type']:
            case 1:
                self.move(SpaceObject=getattr(self.Location, f'Planet_{data["id"]}'))
            case 4:
                print('data items', data)
                # self.ObjectToReach = self.
                # self.move(self.ObjectToReach.x, self.ObjectToReach.y)
            case 5:
                match int(str(data['id'])[0]):
                    case 1:
                        self.move(SpaceObject=getattr(self.Location, f'StaticSpaceObject_{data["id"]}'))
                    case 2:
                        self.move(SpaceObject=getattr(self.Location, f'StaticSpaceObject_{data["id"]}'))
                    case 4:
                        self.move(SpaceObject=getattr(self.Location, f'StaticSpaceObject_{data["id"]}'))
                    case 5:
                        self.move(SpaceObject=getattr(self.Location, f'StaticSpaceObject_{data["id"]}'))

    def dead(self):
        self.get_drop()  # send req

    # @ThreadBase.end_thread
    def _level_experience(self):
        if self.experience > 0:
            self.level += 1

    # @ThreadBase.end_thread
    def _level_status(self):
        if self.point:
            self.status += 1

    def ship_position(self):
        return self.x, self.y

    def kill_weapon(self):
        self.__get_experience(5)
        self.__get_status(5)

    def kill_device(self):
        self.__get_experience(5)
        self.__get_status(5)

    def get_drop(self):  # TODO return experiences (maybe credits) and return items
        drop = {}
        for count, dict_ in enumerate(self.inventory.copy()):
            if dict_['drop']:
                name = dict_['name']
                value = dict_['value']
                drop[name] = 0.8 * value
                self.inventory[count][name] = 0.2 * value
        return drop

    def __get_experience(self, experience):
        self.experience += experience

    def __get_status(self, status):
        self.status += status

    def __get_skills(self):
        self.__get_parameter_repair()
        self.__get_parameter_recovery_energy()

    def __get_parameter_repair(self):
        self.repair_health = int(self.max_health / 200 + self.skills['repairing'] * 4)

    def __get_parameter_recovery_energy(self):
        self.recovery_energy = int(self.max_energy / 50 + self.skills['recovery_energy'] * 4)

    def get_energy(self, energy):
        if self.energy + energy > self.max_energy:
            self.energy = self.max_energy
        else:
            self.energy += energy

    def get_health(self, health):
        if self.health + health > self.ship['max_health']:
            self.health = self.ship['max_health']
        else:
            self.health += health

    def get_effect(self, effect_type, active_time):
        if effect_type in self.effects:
            for k, v in self.effects:
                if effect_type == k:
                    self.effects[k] += active_time
                    # self.del_thread_timer()
                    self.start_timer_update(self.remove_effect, active_time)

        pass

    def remove_effect(self, effect_type):
        self.effects.remove(effect_type)

    def get_damage_weapon(self, damage):
        self.__get_damage(damage)

    def get_reduction_energy_weapon(self, energy):
        self.__get_reduction_energy(energy)

    def get_damage_device(self, damage):
        self.__get_damage(damage)

    def get_reduction_energy_device(self, energy):
        self.__get_reduction_energy(energy)

    def __get_damage(self, damage):
        if 0 >= self.health - damage:
            self.health = 0
            self.dead()
        self.health -= damage
        PacMan = PackagesManager(self.id, self.Game)
        PacMan.locationSystem()

    def __get_reduction_energy(self, reduction_energy):
        if 0 > self.energy - reduction_energy:
            self.energy = 0
        self.energy -= reduction_energy
