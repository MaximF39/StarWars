from python.Base.BaseItem.NoQuantitative import NoQuantitative

class Engine(NoQuantitative):

    def __init__(self, Game, data, OwnerClass):
        super().__init__(Game, data, OwnerClass)

    def use(self):
        self.Owner.replace_engine(self)

        self.Owner.PacMan.inventory()

    def unuse(self):
        print('Нельзя снять двигатель')