from python.Game._Component.Body.B_Item.B_BaseItem.B_NoQuantitative import B_NoQuantitative
from python.Static.Type.Package.T_ServerRequest import T_ServerRequest
from python.Game._Component.Utils.ThreadBase import ThreadBase
from python.Game._Component.Utils.MyTime import MyTime
from python.Game.Game.Effect import Effect


class Device(B_NoQuantitative, ThreadBase, MyTime):
    reload_time: int
    effects: dict

    def __init__(self, Game, data, OwnerClass):
        super().__init__(Game, data, OwnerClass)
        self.reloadedTime = 0
        self.is_active = False

    def use(self):
        self.Owner.use_device(self)
        self.in_using = True
        if self.reload_time == 0:
            Effect.const_effect(**self.effects)
        self.Owner.Packages.SendPacMan(T_ServerRequest.ACTIVE_DEVICES)

    def unuse(self):
        self.Owner.unuse_device(self)
        self.in_using = False
        self.Owner.Packages.SendPacMan(T_ServerRequest.ACTIVE_DEVICES)

    @property
    def get_reloadedTime(self):
        pass

    def clicked(self, data):
        if not self.is_active:
            if self.energy - self.energy_cost >= 0:
                self.get_reduction_energy_device(self.energy_cost)
                self.Owner.cnt_active_device += 1
                self.Owner.add_effect(Effect(
                    self.Owner,
                    self.effects,
                    data
                    )
                )
                self.reloadedTime = self.reload_time
                self.start_timer_update(self.reload, self.reload_time / 1000)
                self.is_active = True
                self.Owner.SendPacMan.activeDevices()


    def reload(self):
        self.is_active = False
        self.reloadedTime = 0
        self.Owner.cnt_active_device -= 1