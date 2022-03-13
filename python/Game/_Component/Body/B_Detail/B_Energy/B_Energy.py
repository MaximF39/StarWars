from python.Game._Component.Utils.ThreadBase import ThreadBase

class B_Energy(ThreadBase):
    ship:"dict"

    def __init__(self, max_energy):
        ThreadBase.__init__(self)
        self.energy = max_energy
        self.max_energy = max_energy


    def _change_energy(self, energy):
        sum_energy = self.max_energy + energy
        if sum_energy > self.max_energy:
            self.energy = self.max_energy
        elif self.max_energy > sum_energy > 0:
            self.energy += energy
        elif 0 > sum_energy:
            self.energy = 0

