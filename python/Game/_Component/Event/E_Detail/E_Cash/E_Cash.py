from python.Static.Type.Package.T_UpdateValue import T_UpdateValue


class E_Cash:
    cash: int

    def __add__(self, other):
        if isinstance(other, int):
            self.cash += other
            self.Packages.updateValue(T_UpdateValue.PlayerCash)

    def __sub__(self, other):
        if isinstance(other, int):
            if self.cash >= other:
                self.cash -= other
                self.Packages.updateValue(T_UpdateValue.PlayerCash)
            else:
                exit()