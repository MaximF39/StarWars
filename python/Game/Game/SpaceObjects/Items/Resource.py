from python.Game._Component.Body.B_Item.B_BaseItem.B_Quantitative import B_Quantitative


class Resource(B_Quantitative):

    def __init__(self, Game, data, OwnerClass):
        super().__init__(Game, data, OwnerClass)