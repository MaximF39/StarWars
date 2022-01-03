from .BaseItem.NoQuantitative import NoQuantitative
from python.Packages.PackagesManager import PackagesManager

class Device(NoQuantitative):

    def __init__(self, Game, classNumber, OwnerClass):
        super().__init__(Game, classNumber, OwnerClass)
        self.reloadedTime = 0

    def use(self):
        self.Owner.use_device(self)
        self.inUsing = True

        PacMan = PackagesManager(self.Owner.id, self.Game)
        PacMan.activeDevices()

    def unuse(self):
        self.Owner.unuse_device(self)
        self.inUsing = False

        PacMan = PackagesManager(self.Owner.id, self.Game)
        PacMan.activeDevices()