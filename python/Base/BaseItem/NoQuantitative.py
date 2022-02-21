from python.Base.BaseItem.BaseItem import BaseItem


class NoQuantitative(BaseItem):
    FULL_REPAIR = 1000
    mod = 'noq'
    count = 1
    drop = False

    def __init__(self, Game, data, Owner):
        BaseItem.__init__(self, Game, data, Owner)
        self.stability = self.wear
        self.repair_cost = self.cost / 500

    def get_cost(self, wear):
        return self.cost

    @property
    def get_size(self):
        return self.size

    def get_cost_count(self, wear):
        return self.cost

    def repair(self):
        if self.Owner.cash > (self.FULL_REPAIR - self.stability) * self.repair_cost:
            self.stability = self.FULL_REPAIR
            self.Owner.cash -= (self.FULL_REPAIR - self.stability) * self.repair_cost
        else:
            repair_count = self.Owner.cash // self.repair_cost
            self.stability += repair_count
            self.Owner.cash = 0

    def drop(self, wear):
        Player = self.Owner
        BaseItem.set_x_y_owner(self)
        self.transfer(self.Owner.Location)
        Player.PacMan.items()

    def buy(self, Player, wear):
        if BaseItem.check_default_shop(self):
            class_ = self.copy_class()
            class_.transfer(Player)
        else:
            self.transfer(Player)
        BaseItem.good_trade(self, Player)

    def sell(self, Planet, count):
        Player = self.Owner
        self.transfer(Planet)
        BaseItem.good_trade(self, Player)

    def separation(self, Whom, count):
        raise NotImplementedError("No quantitative hasn't attr separation")
