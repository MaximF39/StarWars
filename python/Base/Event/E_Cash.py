from python.Static.Type.Package.T_UpdateValue import T_UpdateValue


class E_Cash:
    cash: int

    def get_credits(self, count):
        self.cash += count
        self.Packages.updateValue(T_UpdateValue.PlayerCash)

    def remove_cash(self, count):
        if self.cash >= count:
            self.cash -= count
            self.Packages.updateValue(T_UpdateValue.PlayerCash)
        else:
            exit()