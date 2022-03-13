

class E_Location:

    def hyperJump(self):
        B_PlayerEnergy.reduce_energy_jump(self)
        self.Location = self.NextLocation
        # self.Packages.
        # Игрок меняет у себя локацию, сообщая об этом Локаций
        # Пакеты
        pass