class cfg_sell_buy:

    def __init__(self, trading):
        self.trading = trading

    @property
    def coef_sell(self):
        return (100 + 2 * int(self.trading ** 1.15)) / 100 # 1 + 0.34 # 1.34

    @property
    def coef_buy(self):
        return (200 - 2 * int(self.trading ** 1.15)) / 100 # 2 - 0.34 = 1.66