from . import Ship

class BasePlayer(Ship):

    def __init__(self, dict_:dict):
        super().__init__(dict_["class_number"])
        self.x: float = dict_["x"]
        self.y: float = dict_["y"]
        self.name: str = dict_["name"]
        self.level: int = dict_["level"]
        self.aliance:int = dict_["aliance"]
        self.race: int = dict_["race"]
        self.state: float = dict_["state"]
        self.target_x: float = dict_["target_x"]
        self.target_y: float = dict_["target_y"]
        self.object_to_reach_id: int = dict_["object_to_reach_id"]
        self.object_to_reach_type: int = dict_["object_to_reach_type"]
        self.Player_relation: int = dict_["Player_relation"]
        self.health = self.max_health
        self.energy = self.max_energy
        self.speed = self.max_speed