from python.BaseClass.Item.Quantitative import Quantitative
from python.Packages.PackagesManager import PackagesManager
from ...Static.TypeStr.PlayerSkillTypeStr import PlayerSkillTypeStr


class Droid(Quantitative):

    def __init__(self, Game, classNumber, OwnerClass, count):
        super().__init__(Game, classNumber, OwnerClass, count)
        self.inUsing = True
        self.Control = self.restrictions[0]['Value']

    @property
    def get_satisfying(self):
        if self.restrictions is None or not 'level' in self.Owner.__dict__:
            return True
        skills = self.Owner.skills
        if self.Control > skills["Control"]:
            return False
        return True

    def use(self):
        self.Owner.use_droid(self)
        self.inUsing = True

        PacMan = PackagesManager(self.Owner.id, self.Game)
        PacMan.inventory()
        PacMan.droidBuildingDialog(self)

    def unuse(self):
        self.Owner.unuse_droid(self)
        self.inUsing = False

        PacMan = PackagesManager(self.Owner.id, self.Game)
        PacMan.inventory()

