from .BaseItem.NoQuantitative import NoQuantitative
from python.Packages.PackagesManager import PackagesManager

class Device(NoQuantitative):

    def __init__(self, Game, classNumber, OwnerClass):
        super().__init__(Game, classNumber, OwnerClass)

    def use(self):
        self.Owner.active_devices.append(self)

        PacMan = PackagesManager(self.Owner.id, self.Game)
        PacMan.activeDevices()
