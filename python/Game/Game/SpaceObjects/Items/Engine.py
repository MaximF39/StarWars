from python.Game._Component.Body.B_Item.B_BaseItem.B_NoQuantitative import B_NoQuantitative
from python.Static.Type.Package.T_ServerRequest import T_ServerRequest


class Engine(B_NoQuantitative):
    def __init__(self, Game, data, OwnerClass):
        B_NoQuantitative.__init__(self, Game, data, OwnerClass)

    def use(self):
        self.Owner.replace_engine(self)
        self.Owner.Packages.SendPacMan(T_ServerRequest.INVENTORY)

    def unuse(self):
        # print('Нельзя снять двигатель')
        pass