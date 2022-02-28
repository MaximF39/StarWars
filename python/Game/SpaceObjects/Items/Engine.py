from python.Base.B_Item.NoQuantitative import NoQuantitative


class Engine(NoQuantitative):
    def __init__(self, Game, data, OwnerClass):
        NoQuantitative.__init__(self, Game, data, OwnerClass)

    def use(self):
        self.Owner.replace_engine(self)
        self.Owner.SendPacMan.inventory()

    def unuse(self):
        print('Нельзя снять двигатель')
