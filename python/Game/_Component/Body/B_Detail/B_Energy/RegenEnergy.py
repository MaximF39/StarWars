import time

from python.Game._Component.Body.B_Detail.B_Energy.B_Energy import B_Energy
from python.Config.CFG_Player.cfg_recovery import update_energy, recovery_energy
from python.Game._Component.Utils.ThreadBase import ThreadBase


class RegenEnergy(B_Energy):

    def __init__(self, max_energy, repairSkills):
        super().__init__(max_energy)
        self.repairSkills = repairSkills
        self.__check_update_regen_energy()

    def remove_energy(self, energy):
        self._change_energy(-energy)

    def add_energy(self, energy):
        self._change_energy(energy)

    def __check_update_regen_energy(self):
        if not ThreadBase.alive_thread_timer(self, 
                                        self.__update_regen_energy):
            self.__update_regen_energy()

    def __update_regen_energy(self):
        while self.energy != self.max_energy:
            self.__regen_energy()
            time.sleep(update_energy)

    def __regen_energy(self):
        self._change_energy(recovery_energy(self.max_energy,
                                            self.repairSkills))

