from python.Config.CFG_Player.Statistics.cfg_level import cfg_level
from python.Config.CFG_Player.Statistics.cfg_level import get_experience_for_kill


class Experience:
    experience: int
    level: int

    def get_experience(self, experience):
        self.__get_experience(experience)

    def __get_experience(self, experience):
        self.experience += experience
        self.__check_level()

    def __check_level(self):
        pass

    def __upgrade_level_experience(self):
        if self.experience > 0:
            self.level += 1
            self.new_level()

    def new_level(self):
        raise NotImplementedError("Переопредели меня")

    @property
    def forNextLevel(self):
        return int(cfg_level[self.level + 1])

    def get_experience_for_kill(self, Whom, coef, level):
        exp = get_experience_for_kill(Whom, coef, level)
        self.get_experience(exp)
