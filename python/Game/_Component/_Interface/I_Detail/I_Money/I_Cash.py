from python.Game._Component.Body.B_Detail.B_Cash.B_Cash import B_Cash
from python.Game._Component.Event.E_Detail.E_Cash.E_Cash import E_Cash


class I_Cash(B_Cash, E_Cash):

    def __init__(self, cash):
        super().__init__(cash)
