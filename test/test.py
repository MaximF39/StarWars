import time
from datetime import datetime

class MyTime:
    LastTime: float
    Milliseconds: float
    FPS = 60

    def __init__(self):
        self.LastTime = self.Hash()

    def tick(self):
        OldLastTime = self.LastTime
        self.LastTime = self.Hash()
        return ((self.LastTime - OldLastTime) / 10000000) * self.FPS

    def Hash(self) -> float:
        return (datetime.now() - datetime(1, 1, 1)).total_seconds() * 10000000
e = MyTime()

print(e.tick())
time.sleep(1)
print(e.tick())
print(e.tick())
