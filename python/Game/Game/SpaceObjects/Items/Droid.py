from python.Static.Type.T_DroidEvent import T_DroidEvent
from python.Game._Component.Body.B_Item.B_BaseItem.B_Quantitative import B_Quantitative

class Droid(B_Quantitative):

    def __init__(self, Game, data, OwnerClass):
        B_Quantitative.__init__(self, Game, data, OwnerClass)
        self.in_using = True

        # self.Control = self.restrictions[0]['value']

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
        self.in_using = True

        self.Owner.SendPacMan.inventory()
        self.Owner.SendPacMan.droidEvent(T_DroidEvent.Builded, self)

    def unuse(self):
        self.Owner.unuse_droid(self)
        self.in_using = False
        self.Owner.SendPacMan.inventory()
        self.Owner.SendPacMan.droidEvent(T_DroidEvent.Removed, self)

    def unuse_all(self):
        self.in_using = False
        self.Owner.SendPacMan.inventory()
        self.Owner.SendPacMan.droidEvent(T_DroidEvent.RemovedAll, self)



