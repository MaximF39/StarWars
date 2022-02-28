from python.Base.B_Item.NoQuantitative import NoQuantitative
from python.Utils.ThreadBase import ThreadBase
from python.Utils.MyTime import MyTime
from python.Game.Effect import Effect


class Device(NoQuantitative, ThreadBase, MyTime):
    reloadTime: int
    def __init__(self, Game, data, OwnerClass):
        super().__init__(Game, data, OwnerClass)
        self.reloadedTime = 0
        self.is_active = False

    def use(self):
        self.Owner.use_device(self)
        self.inUsing = True
        self.Owner.SendPacMan.activeDevices()

    def unuse(self):
        self.Owner.unuse_device(self)
        self.inUsing = False
        self.Owner.SendPacMan.activeDevices()

    @property
    def get_reloadedTime(self):
        pass

    def clicked(self, data):
        if not self.is_active:
            if self.energy - self.energyCost >= 0:
                self.get_reduction_energy_device(self.energyCost)
                self.Owner.cnt_active_device += 1
                self.Owner.add_effect(Effect(
                    self.Owner,
                    self.effects,
                    data
                    )
                )
                self.reloadedTime = self.reloadTime
                self.start_timer_update(self.reload, self.reloadTime / 1000)
                self.is_active = True
                self.Owner.SendPacMan.activeDevices()


    def reload(self):
        self.is_active = False
        self.reloadedTime = 0
        self.Owner.cnt_active_device -= 1