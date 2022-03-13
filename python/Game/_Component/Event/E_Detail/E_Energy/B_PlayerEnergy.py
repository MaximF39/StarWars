from python.Game._Component.Body.B_Detail.B_Energy.RegenEnergy import RegenEnergy


class B_PlayerEnergy(RegenEnergy):

    def __init__(self, max_energy, repairSkills):
        RegenEnergy.__init__(self, max_energy, repairSkills)

    def reduce_energy_jump(self):
        self.remove_energy(100)

    def reduce_energy_weapon(self, energy):
        self.remove_energy(energy)

    def reduce_energy_device(self, energy):
        self.remove_energy(energy)
