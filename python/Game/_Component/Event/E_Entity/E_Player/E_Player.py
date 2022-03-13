from python.Game import E_Cash
from python.Game import E_Skills
from python.Game import E_Location
from python.Game import E_P_Planet
from python.Game import E_Trade


class E_Player(E_Cash, E_Skills, E_Trade, E_P_Planet, E_Location):

    def __init__(self):
        E_Cash.__init__(self)
        E_Skills.__init__(self)
        E_P_Planet.__init__(self)
        E_Trade.__init__(self)
        E_Location.__init__(self)

