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
        self.ship['id'] = dict_['id']
        self.ship['setPosition'] = [dict_['x'], dict_['y']]
        self.ship['team'] = -1
        self.team = -1
        self.type = 2
        self.Location = getattr(self.Game, f'Location_{dict_["Location"]}')
        self.avatar = dict_['avatar']
        self.login: str = dict_["login"]
        self.aliance: int = dict_["aliance"]
        self.maxHealth = self.ship['maxHealth']
        self.maxEnergy = self.ship['maxEnergy']
        self.maxSpeed = self.ship['maxSpeed']
        self.race: int = dict_["race"]
        # self.state: float = dict_["state"]
        self.health = self.ship['health']
        self.SpaceObject = None
        self.ObjectToReach = None
        self.energy = self.ship['energy']
        self.speed = self.ship['speed']
        self.target_x = self.x
        self.target_y = self.y
        self.object_to_reach_id: int = self.Location
        self.object_to_reach_type: int = 7 # getattr(Game, f"Location_{self.object_to_reach_id}").type
        self.PlayerRelation: int = dict_["PlayerRelation"]
        self.skills = ast.literal_eval(dict_['skills'])
        self.level: int = dict_["level"]
        self.status = dict_['status']
        self.experience = dict_['experience']
        self.inventory:list = dict_['inventory']
        self.active_weapons = dict_['active_weapons']
        self.active_devices = dict_['active_devices']
        self.ship["login"] = self.login
        self.ship['race'] = self.race
        self.hold = 0
        self.OldTick = 0
        self.OldTarget = False
        # self.PacMan = PackagesManager(self.id, self.Game)
        self.sendInfoLocation()
        self.upgrade()
        # self.attacking = self.skills['attacking']
        # self.tactics = self.skills['tactics']
        # self.targeting = self.skills['targeting']
        # self.trading = self.skills['trading']
        # self.repairing = self.skills['repairing']
        # self.defending = self.skills['defending'] # ?

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

    def leaveLocation(self):
        print(self.SpaceObject)
        self.x = self.SpaceObject.x
        self.y = self.SpaceObject.y
        self.SpaceObject = None
        self.ObjectToReach = None
        PacMan = PackagesManager(self.id, self.Game)
        PacMan.shipsPosition()
        PacMan.shipsState()
        PacMan.ship()
        PacMan.playerShip()
        PacMan.locationSystem()

    def target(self, x, y):
        self.target_x = x
        self.target_y = y

    def WaitForCord(self):
        self.x = self.target_x
        self.y = self.target_y
        self.OldTarget = False
        if self.ObjectToReach:
            self.ObjectToReach.SetPlayer(self)
            self.SpaceObject = self.ObjectToReach
            self.ObjectToReach = False


    def move(self, targetX, targetY, stop=False):
        if stop:
            if self.OldTarget:
                self.del_thread_timer(self.WaitForCord)
                self.OldTick = self.tick()
                self.x += math.cos(math.atan2(self.target_y - self.y, self.target_x - self.x)) * self.OldTick # x
                self.y += math.sin(math.atan2(self.target_y - self.y, self.target_x - self.x)) * self.OldTick # y
                self.target_x = self.x
                self.target_y = self.y
                self.OldTarget = False
        elif self.OldTarget:
            self.del_thread_timer(self.WaitForCord)
            self.OldTick = self.tick()
            self.x += math.cos(math.atan2(self.target_y - self.y, self.target_x - self.x)) * self.OldTick # x
            self.y += math.sin(math.atan2(self.target_y - self.y, self.target_x - self.x)) * self.OldTick # y
            self.target_x = targetX
            self.target_y = targetY
            distance = self.distance(self.x - self.target_x, self.y - self.target_y)
            TimeSecWait = distance / self.speed
            self.start_timer_update(self.WaitForCord, TimeSecWait)
        else:
            self.OldTarget = True
            self.target_x = targetX
            self.target_y = targetY
            distance = self.distance(self.x - self.target_x, self.y - self.target_y)
            TimeSecWait = distance / self.speed
            self.start_timer_update(self.WaitForCord, TimeSecWait)
            self.tick()


    def attack(self):
        self.attack_now = True

    def set_object_to_reach(self, data):
        match data['type']:
            case 1:
                self.ObjectToReach = getattr(self.Location, f'Planet_{data["id"]}')
                self.move(self.ObjectToReach.x, self.ObjectToReach.y)
            case 4:
                print('data items', data)
                # self.ObjectToReach = self.
                # self.move(self.ObjectToReach.x, self.ObjectToReach.y)
            case 5:
                data['id'] = -1 * data['id']
                match data['id']:
                    case 1:
                        self.ObjectToReach = getattr(self.Location, f'StaticSpaceObject_{data["id"]}')
                        self.move(self.ObjectToReach.x, self.ObjectToReach.y)
                    case 2:
                        self.ObjectToReach = getattr(self.Location, f'StaticSpaceObject_{data["id"]}')
                        self.move(self.ObjectToReach.x, self.ObjectToReach.y)
                    case 4:
                        self.ObjectToReach = getattr(self.Location, f'StaticSpaceObject_{data["id"]}')
                        self.move(self.ObjectToReach.x, self.ObjectToReach.y)
                    case 5:
                        self.ObjectToReach = getattr(self.Location, f'StaticSpaceObject_{data["id"]}')
                        self.move(self.ObjectToReach.x, self.ObjectToReach.y)

    def dead(self):
        self.get_drop() # send req

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

    # @ThreadBase.end_thread
    def _recovery_energy(self):
        if self.energy + self.recovery_energy > self.max_energy:
            self.energy = self.max_energy
        else:
            self.energy += self.repair_health

    # @ThreadBase.end_thread
    def _repair_health(self):
        if self.health + self.repair_health > self.max_health:
            self.health = self.max_health
        else:
            self.health += self.repair_health

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

    def __get_reduction_energy(self, reduction_energy):
        if 0 > self.energy - reduction_energy:
            self.energy = 0
        self.energy -= reduction_energy

