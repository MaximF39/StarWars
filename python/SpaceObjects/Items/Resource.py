from python.Base.BaseItem.Quantitative import Quantitative


class Resource(Quantitative):

    def __init__(self, Game, data, OwnerClass):
        super().__init__(Game, data, OwnerClass)