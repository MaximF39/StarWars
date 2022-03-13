from python.Game._Component.Body.B_Item.B_BaseItem.B_Quantitative import B_Quantitative

class Ammo(B_Quantitative):

    def __init__(self, Game, data, OwnerClass):
        B_Quantitative.__init__(self, Game, data, OwnerClass)