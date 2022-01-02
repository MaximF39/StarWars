from .BaseItem.NoQuantitative import NoQuantitative
from ...Packages.PackagesManager import PackagesManager

class Weapon(NoQuantitative):

    def __init__(self, Game, classNumber, OwnerClass):
        super().__init__(Game, classNumber, OwnerClass)

    def use(self):
        self.Owner.active_weapons.append(self)

        PacMan = PackagesManager(self.Owner.id, self.Game)
        PacMan.activeWeapons()