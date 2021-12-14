class ShipState:
    id: int
    x: float
    y: float
    speed: float
    state: float = 0
    target_x: float
    target_y: float
    object_to_reach_id: int
    object_to_reach_type: int
    energy: int
    health: int
    Player_relation: int