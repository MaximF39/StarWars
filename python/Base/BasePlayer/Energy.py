import time

from python.Static.cfg.cfg_player import recovery_energy, update_energy
from python.Utils.ThreadBase import ThreadBase

class Energy(ThreadBase):
    ship:"dict"

    def __init__(self, maxEnergy, repairSkills):
        self.maxEnergy = maxEnergy
        self.repairSkills = repairSkills
        self.__check_update_regen_energy()

    def reduce_energy_weapon(self, energy):
        self.__change_energy(-energy)

    def reduce_energy_device(self, energy):
        self.__change_energy(-energy)

    def __regen_energy(self):
        self.__change_energy(recovery_energy(self.maxEnergy,
                                             self.repairSkills))

    def __update_regen_energy(self):
        while self.energy != self.maxEnergy:
            self.__regen_energy()
            time.sleep(update_energy)

    def __check_update_regen_energy(self):
        if not ThreadBase.alive_thread_timer(self, self.__update_regen_energy) \
                and self.repairSkills:
            self.__update_regen_energy()

    def __change_energy(self, energy):
        sum_energy = self.maxEnergy + energy
        if sum_energy > self.maxEnergy:
            self.energy = self.maxEnergy
        elif self.maxEnergy > sum_energy > 0:
            self.energy += energy
            self.__check_update_regen_energy()
        elif 0 > sum_energy:
            self.energy = 0
            self.__check_update_regen_energy()

