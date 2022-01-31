from python.BaseClass.BaseItem.NoQuantitative import NoQuantitative
from python.Packages.PackagesManager import PackagesManager
from python.Utils.ThreadBase import ThreadBase
from python.Utils.MyTime import MyTime
from python.BaseClass.Effect import Effect


class Device(NoQuantitative, ThreadBase, MyTime):
    reloadTime: int
    def __init__(self, Game, classNumber, OwnerClass, data):
        super().__init__(Game, classNumber, OwnerClass, data)
        self.reloadedTime = 0
        self.is_active = False

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

    @property
    def get_reloadedTime(self):
        pass

    def clicked(self, data):
        if not self.is_active:
            self.Owner.cnt_active_device += 1
            self.Owner.add_effect(Effect(
                self.Owner,
                self.effects,
                data
                )
            )
            self.reloadedTime = self.reloadTime
            self.start_timer_update(self.reload, self.reloadTime)
            self.is_active = True
            self.Owner.PacMan.activeDevices()


    def reload(self):
        self.is_active = False
        self.reloadedTime = 0
        self.Owner.cnt_active_device -= 1