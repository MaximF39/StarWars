if False:
    pass


class SetMob:
    def __init__(self):
        self.mobs: list["CFG_Mob"] = []

    def _set_mob(self, Mob):
        self.mobs.append(Mob)
        Mob.set_space_object(self)

    def _remove_mob(self, Mob):
        if Mob in self.mobs:
            Mob.not_target()
            self.mobs.remove(Mob)
