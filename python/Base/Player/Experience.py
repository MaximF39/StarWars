from python.Static.cfg.cfg_player import cfg_level


class Experience:

    def __get_experience(self, experience):
        self.experience += experience

    def _level_experience(self):
        if self.experience > 0:
            self.level += 1

    @property
    def forNextLevel(self):
        return int(cfg_level[self.level + 1])
