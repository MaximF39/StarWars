from python.Static.Type.DroidEventType import DroidEventType
from python.Base.BaseItem.Quantitative import Quantitative

class Droid(Quantitative):

    def __init__(self, Game, data, OwnerClass):
        Quantitative.__init__(self, Game, data, OwnerClass)
        self.inUsing = True
        self.Control = self.restrictions[0]['Value']

    @property
    def get_satisfying(self):
        return True
        if self.restrictions is None or self.Owner is None or self.Owner.__name__ == 'DB_Planet':
            return True
        skills = self.Owner.skills
        if self.Control > skills["Control"]:
            return False
        return True

    def use(self):
        self.Owner.use_droid(self - 1)
        self.inUsing = True

        self.Owner.PacMan.inventory()
        self.Owner.PacMan.droidEvent(DroidEventType.Builded, self)

    def unuse(self):
        self.Owner.unuse_droid(self)
        self.inUsing = False
        self.Owner.PacMan.inventory()
        self.Owner.PacMan.droidEvent(DroidEventType.Removed, self)

    def unuse_all(self):
        self.inUsing = False
        self.Owner.PacMan.inventory()
        self.Owner.PacMan.droidEvent(DroidEventType.RemovedAll, self)



