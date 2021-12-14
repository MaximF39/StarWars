import math
# from . import parse_galaxy_map
from . import ThreadBase, cfg_update


class Planet(ThreadBase):
    id: int  # my
    name: str  # my
    class_number: int  #be bytes
    race: bytes  # str
    radius: int = 100
    laudable: bool = True
    is_sun: bool
    aliance: bytes  # str
    # clan_id: int # Зачем планете клан ид?
    x: int  # add
    y: int  # add
    x0: int = 300  # центр окружности по х
    y0: int = 300  # центр окружности по y
    speed: int = 12  #
    time_update: int = cfg_update['planet']  # сек
    _i = 1  # Уголобразующий

    def __init__(self, data:dict):
        super().__init__()
        self.id = data['id']
        self.name = data['name']
        self.race = data['race']
        self.class_number = data['classNumber']
        self.aliance = data["aliance"]
        self.is_sun = bool(6 > self.class_number)
        self.x = 0
        self.y = 0
        self.update()


    def update(self):  # ready
        self.start_update('move', self.time_update)

    @ThreadBase.end_thread
    def move(self):
        self._i += self.speed
        if self._i > 360:
            self._i = 1
        angle = self._i * 3.14 / 180
        self.x = int(100 * math.cos(angle) + self.x0) + self.radius
        self.y = int(100 * math.sin(angle) + self.y0) + self.radius
