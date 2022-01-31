from python.BaseClass.BaseItem.NoQuantitative import NoQuantitative
from python.Packages.PackagesManager import PackagesManager

class Ship(NoQuantitative):

    def __init__(self, Game, classNumber, OwnerClass, data):
        super().__init__(Game, classNumber, OwnerClass, data)

    # def use(self):
    #     pass