from python.Config.CFG_Player.Statistics.cfg_level import cfg_level
from python.Config.CFG_Player.Statistics.cfg_level import get_experience_for_kill


class B_Experience:

    def __init__(self, experience):
        self.experience = experience
        self.level = self.__get_level()

    def __get_level(self):
        return 11

    @property
    def forNextLevel(self):
        return int(cfg_level[self.level + 1])