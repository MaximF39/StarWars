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
        if self.restrictions is None or self.Player is None or self.Player.__name__ == 'Planet':
            return True
        skills = self.Player.skills
        if self.Control > skills["Control"]:
            return False
        return True

    def use(self):
        self.Player.use_droid(self)
        self.inUsing = True

        PacMan = PackagesManager(self.Player.id, self.Game)
        PacMan.inventory()
        PacMan.droidBuildingDialog(self)

    def unuse(self):
        self.Player.unuse_droid(self)
        self.inUsing = False

        PacMan = PackagesManager(self.Player.id, self.Game)
        PacMan.inventory()

