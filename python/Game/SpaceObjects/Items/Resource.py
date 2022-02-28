from python.Base.B_Item.Quantitative import Quantitative


class Resource(Quantitative):

    def __init__(self, Game, data, OwnerClass):
        super().__init__(Game, data, OwnerClass)