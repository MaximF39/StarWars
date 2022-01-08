from .BaseItem.NoQuantitative import NoQuantitative
from python.Packages.PackagesManager import PackagesManager
from python.Utils.ThreadBase import ThreadBase
from python.Utils.MyTime import MyTime


class Device(NoQuantitative, ThreadBase, MyTime):

    def __init__(self, Game, classNumber, OwnerClass):
        super().__init__(Game, classNumber, OwnerClass)
        self.effects = self.data["effects"]["data"]
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

    def clicked(self):
        self.Owner.add_effect(self.effects["effectType"])
        self.reloadedTime = self.data["reloadTime"]
        self.speed = 1
        self.tick()
        self.time = self.tick()
        self.start_timer_update(self.update_reload, self.reloadedTime)

        PacMan = PackagesManager(self.Owner.id, self.Game)
        PacMan.effectCreated(self)

    def update_reload(self):
        self.reloadedTime = 0

    def get_reload_time(self):
        self.time += self.tick()
        return self.time

    def remove_effect(self):
        self.Owner.remove_effect(self)