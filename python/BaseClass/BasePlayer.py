# from ..Packages.
import ast
import json
import time

from . import Ship
from ..MyUtils.ThreadBase import ThreadBase
from ..Packages.PackagesManager import PackagesManager


class BasePlayer(Ship, ThreadBase):
    # object_to_reach:  = {}
    # attack_now: dict = {}

    def __init__(self, Game, dict_: dict):
        super().__init__(Game, dict_)
        self.type = 2
        self.location = dict_["location"]
        self.avatar = dict_['avatar']
        self.login: str = dict_["login"]
        self.aliance: int = dict_["aliance"]
        self.race: int = dict_["race"]
        # self.state: float = dict_["state"]
        self.health = self.ship['health']
        self.on_planet = None
        self.energy = self.ship['energy']
        self.speed = self.ship['speed']
        self.target_x: float = self.x
        self.target_y: float = self.y
        self.object_to_reach_id: int = self.location
        self.object_to_reach_type: int = 7 # getattr(Game, f"Location_{self.object_to_reach_id}").type
        self.PlayerRelation: int = dict_["PlayerRelation"]
        self.skills = ast.literal_eval(dict_['skills'])
        self.level: int = dict_["level"]
        self.status = dict_['status']
        self.experience = dict_['experience']
        self.pointStatus = dict_['pointStatus']
        self.inventory = dict_['inventory']
        self.active_weapons = dict_['active_weapons']
        self.active_devices = dict_['active_devices']
        self.ship["login"] = self.login
        self.ship['race'] = self.race
        self.upgrade()
        # self.attacking = self.skills['attacking']
        # self.tactics = self.skills['tactics']
        # self.targeting = self.skills['targeting']
        # self.trading = self.skills['trading']
        # self.repairing = self.skills['repairing']
        # self.defending = self.skills['defending'] # ?

    def object_to_reach_system(self, type_, id_):
        self.object_to_reach_type = type_
        self.object_to_reach_id = id_


    def upgrade(self):
        pass
        # self.start_update("land_on_space_object", 1)
        # self.start_update("_repair_health", 1)
        # self.start_update("_recovery_energy", 1)
        # self.start_update("_level_status", 1)
        # self.start_update("_level_experience", 1)


    def move(self, x, y):
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.packages_move()


    def packages_move(self):
        pass
        # PacMan = PackagesManager(self.id, self.Game)
        # print(type(self.Game.id_to_conn[self.id]))
        # self.Game.id_to_conn[self.id].send(PacMan.shipsPosition([{'id':self.id, 'x':self.x, 'y':self.y,
        #                                                           "targetX":self.target_x, "targetY":self.target_y}]))
        # self.Game.id_to_conn[self.id].send(PacMan.shipsState([{'id':self.id, 'speed':self.speed, 'health':self.health,
        #                                                           "energy":self.energy, "PlayerRelation":self.PlayerRelation}]))

        # self.Game.id_to_conn[self.id].send(PacMan.shipsPosition([self.x, self.y]))
        # self.Game.id_to_conn[self.id].send(PacMan.shipsState())
        # self.Game.id_to_conn[self.id].send(PacMan.npcMessage())

    def attack(self):
        self.attack_now = True

    def set_object_to_reach(self, data):
        match data['type']:
            case 1:
                self.object_to_reach = getattr(getattr(self.Game, f"Location_{self.location}"), f'Planet_{data["id"]}')
                time.sleep(1)
                # if self.x == self.object_to_reach.x and self.y == self.object_to_reach.y:
                self.on_planet = self.object_to_reach
                PackagesManager(self.id, self.Game).locationPlanet()
            case 5:
                self.object_to_reach = getattr(getattr(self.Game, f"Location_{self.location}"), f'Static_space_object_{data["id"]}')
                time.sleep(1)
                # if self.x == self.object_to_reach.x and self.y == self.object_to_reach.y:
                self.on_planet = self.object_to_reach
                PackagesManager(self.id, self.Game).locationPlanet()




    def dead(self):
        self.get_drop() # send req

    def use_device(self):
        pass # send request

    # @ThreadBase.end_thread
    def _level_status(self):
        if self.experience > 0:
            self.level_experience += 1

    # @ThreadBase.end_thread
    def _level_experience(self):
        if self.status:
            self.level_status += 1

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

