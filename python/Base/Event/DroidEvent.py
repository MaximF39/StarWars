from python.SpaceObjects.Items.Droid import Droid

class DroidEvent:
    ControlUsed = 0
    droids: list[Droid] = []

    def __init__(self):
        self.ControlLeft = self.skills['Control'] - self.ControlUsed
