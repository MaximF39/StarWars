from python.Game._Component.Body.B_Clan.B_Clan import B_Clan
from python.Game._Component.Event.E_Clan.E_Clan import E_Clan


class I_Clan(B_Clan, E_Clan):

    def __init__(self, Game, data):
        super().__init__(Game, data)