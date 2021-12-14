

class AllSector:
    cnt: int = 3
    def __init__(self, int):
        self.create_sector()

    def create_sector(self):
        for id_ in range(self.cnt):
            setattr(self, f"sector_{id_}", Sector(id_))
a = AllSector(10)