from datetime import datetime

class MyTime:
    LastTime: float

    def tick(self):
        if not hasattr(self, "LastTime"):
            self.LastTime = self.Hash()
        OldLastTime = self.LastTime
        self.LastTime = self.Hash()
        return self.LastTime - OldLastTime

    @staticmethod
    def Hash() -> float:
        return (datetime.now() - datetime(1, 1, 1)).total_seconds()