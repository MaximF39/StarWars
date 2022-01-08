from python.BaseClass.Item.Quantitative import Quantitative

class Ammo(Quantitative):

    def __init__(self, Game, classNumber, OwnerClass, count):
        super().__init__(Game, classNumber, OwnerClass, count)