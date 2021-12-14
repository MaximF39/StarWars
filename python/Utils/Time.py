from datetime import datetime
from . import ticks


class Time:
    last_time_tick: float

    def __init__(self):
        self.last_time_tick = self.time_now_ticks()

    @staticmethod
    def time_now_ticks() -> float:
        res = ticks(datetime.now())
        return res

    def tick(self) -> float:
        old_time = self.last_time_tick
        self.last_time_tick = self.time_now_ticks()
        return ((self.last_time_tick - old_time) / self.last_time_tick) * 60
