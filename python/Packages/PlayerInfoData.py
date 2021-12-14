from ClansManager import ClansManager
from Clan import Clan


class PlayerInfoData:
    _i_clan_id: int
    _o_clan: None  # Clans
    id: int
    name: str
    level: int
    status: int
    ship_class: int
    ship_id: int
    ship_gpu: int
    aliance: int
    race: int
    clan_points: int
    delete_enqueued: bool
    can_delete: bool
    logged: bool
    role: int
    skills: None  # PlayerSkills
    statistics: None  # player_statistics

    def clan_id(self, param1) -> None:
        self._i_clan_id = param1
        self._o_clan = ClansManager.find(param1)

    def clan(self) -> Clan:
        if self._o_clan == None and self._i_clan_id > 0:
            self._o_clan = ClansManager.find(self._iClanId)
        return self._o_clan
