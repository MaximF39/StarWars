from python.BaseClass.BaseItem.NoQuantitative import NoQuantitative
from python.Packages.PackagesManager import PackagesManager

class Engine(NoQuantitative):

    def __init__(self, Game, classNumber, OwnerClass, data):
        super().__init__(Game, classNumber, OwnerClass, data)

    def use(self):
        self.Owner.replace_engine(self)

        PacMan = PackagesManager(self.Owner.id, self.Game)
        PacMan.inventory()

    def unuse(self):
        print('Нельзя снять двигатель')