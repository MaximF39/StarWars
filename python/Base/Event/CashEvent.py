from python.Static.Type.UpdateValueType import UpdateValueType


class CashEvent:
    cash: int

    def get_credits(self, count):
        self.cash += count
        self.PacMan.updateValue(UpdateValueType.PlayerCash)

    def remove_cash(self, count):
        if self.cash >= count:
            self.cash -= count
            self.PacMan.updateValue(UpdateValueType.PlayerCash)
        else:
            exit()