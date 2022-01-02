from .BaseItem.NoQuantitative import NoQuantitative
from python.Packages.PackagesManager import PackagesManager

class Engine(NoQuantitative):

    def __init__(self, Game, classNumber, OwnerClass):
        super().__init__(Game, classNumber, OwnerClass)

    def use(self):
        self.Owner.active_weapons.append(self)
        raise 'dont'
        # PacMan = PackagesManager(self.Owner.id, self.Game)
        # PacMan.()