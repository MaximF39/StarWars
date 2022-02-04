from python.Static.cfg.cfg_player import recovery_energy
class Energy:

    def __init__(self):
        self.energy = self.ship['maxEnergy']

    def get_reduction_energy_weapon(self, energy):
        self.__change_energy(energy)

    def get_reduction_energy_device(self, energy):
        self.__change_energy(energy)

    def recovery_energy(self):
        self.__change_energy(recovery_energy(self.ship['maxEnergy'],
                                             self.skills['Repairing']))
    def __change_energy(self, energy):
        sum_energy = self.energy + energy
        if self.ship['maxEnergy'] > sum_energy > 0:
            self.energy += energy
        elif sum_energy > self.ship['maxEnergy']:
            self.energy = self.ship['maxEnergy']
        elif 0 > sum_energy:
            self.energy = 0
        else:
            raise NotImplementedError("error")



