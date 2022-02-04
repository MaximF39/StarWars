


class Status:
    status: int
    def __init__(self):
        self.pirateStatus = 0 if self.points > 0 else self.points
        self.policeStatus = 0 if 0 > self.points else self.points

    def __change_status(self, status):
        self.status += status

    def __change_status_lvl(self, count):
        self.status += count