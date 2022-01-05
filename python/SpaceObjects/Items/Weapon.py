from .BaseItem.NoQuantitative import NoQuantitative
from ...Packages.PackagesManager import PackagesManager

class Weapon(NoQuantitative):

    def __init__(self, Game, classNumber, OwnerClass):
        super().__init__(Game, classNumber, OwnerClass)
        self.cpu = self.Owner.ship['cpu']

    def use(self):
        self.Owner.use_weapon(self)
        self.inUsing = True

        PacMan = PackagesManager(self.Owner.id, self.Game)
        PacMan.activeWeapons()

    def unuse(self):
        self.Owner.unuse_weapon(self)
        self.inUsing = False

        PacMan = PackagesManager(self.Owner.id, self.Game)
        PacMan.activeWeapons()