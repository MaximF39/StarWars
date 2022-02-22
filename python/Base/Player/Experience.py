from python.Static.cfg.Player.cfg_level import cfg_level


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

    def __level_experience(self):
        if self.experience > 0:
            self.level += 1

    @property
    def forNextLevel(self):
        return int(cfg_level[self.level + 1])
