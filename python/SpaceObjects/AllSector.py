from . import Sector

class AllSector:
    cnt: int = 3

    def __init__(self):
        self.create_sector()

    def create_sector(self):
        for id_ in range(1, self.cnt + 1):
            setattr(self, f"sector_{id_}", Sector(id_))
