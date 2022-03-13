

from python.Game import B_SpaceObjectSetter


class Mob_SpaceObjectSetter(B_SpaceObjectSetter):

    def __init__(self):
        super().__init__()
        self.mobs = []

    def _set_mob(self, Mob):
        super()._set_entity(Mob)
        self.mobs.append(Mob)

    def _entry_mob(self, Mob):
        super()._entry_entity(Mob)
        self.mobs.append(Mob)

    def _remove_mob(self, Mob):
        super()._remove_entity(Mob)
        self.mobs.remove(Mob)

    def _exit_mob(self, Mob):
        super()._remove_entity(Mob)
        self.mobs.remove(Mob)
