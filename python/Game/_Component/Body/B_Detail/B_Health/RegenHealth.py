import time

from python.Game._Component.Body.B_Detail.B_Health.B_Health import B_Health
from python.Config.CFG_Player.cfg_recovery import recovery_health, update_health
from python.Game._Component.Utils.ThreadBase import ThreadBase


class RegenHealth(B_Health):

    def __init__(self, max_health, shields, repairSkills):
        super().__init__(max_health, shields)

        self.repairSkills = repairSkills
        # self.__check_update_regen_health()

    def add_health(self, health):
        B_Health._change_health(self, health)

    def remove_health(self, health):
        B_Health._change_health(self, -health)

    def update_recovery_energy(self):
        while self.health != self.max_health:
            self.__get_heath_regen()
            time.sleep(update_health)

    def __check_update_regen_health(self):
        if not ThreadBase.alive_thread_timer(self, self.update_recovery_energy):
            self.__get_heath_regen()

    def __get_heath_regen(self):
        self.add_health(recovery_health(self.health,
                                            self.repairSkills))
