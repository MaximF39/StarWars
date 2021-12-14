from . import ThreadBase, cfg_update


class Ship(ThreadBase):
    name: str
    level: int
    alliance: bytes
    status: bytes
    class_number: int
    clan_id: int
    max_health: int
    max_energy: int
    health: int
    energy: int
    max_speed: bytes
    player_relation: int
    target_x: float
    target_y: float
    time_update = cfg_update['ship']

    def __init__(self, dict_: dict):
        super().__init__()
        self.name = dict_['name']
        self.level = dict_['level']
        self.alliance = dict_['alliance']
        self.status = dict_['status']
        self.class_number = dict_['class_number']
        self.clan_id = dict_['clan_id']
        self.max_health = dict_['max_health']
        self.max_energy = dict_['max_energy']
        self.health = dict_['health']
        self.energy = dict_['energy']
        self.max_speed = dict_['max_speed']
        self.player_relation = dict_['player_relation']
        self.target_x = dict_['target_x']
        self.target_y = dict_['target_y']
