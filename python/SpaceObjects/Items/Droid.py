from .BaseItem.Quantitative import Quantitative
from python.Packages.PackagesManager import PackagesManager
from ...Static.TypeStr.PlayerSkillTypeStr import PlayerSkillTypeStr


class Droid(Quantitative):

    def __init__(self, Game, classNumber, OwnerClass, count):
        super().__init__(Game, classNumber, OwnerClass, count)
        self.inUsing = True

    @property
    def get_satisfying(self):
        if self.restrictions is None or not 'level' in self.Owner.__dict__:
            return True
        skills = self.Owner.skills
        for skill in self.restrictions:
            if skill['type'] == 3 and skills["Control"] > skill['Value']:
                return False
        return True

    def use(self):
        self.Owner.droids.append(self)
        raise 'Dont do'
        # PacMan = PackagesManager(self.Owner.id, self.Game)
        # PacMan.dr()