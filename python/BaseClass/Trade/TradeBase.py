from python.Static.cfg.shops.cfg_trading import cfg_trading
from python.Packages.PackagesManager import PackagesManager
from python.Static.Type.UpdateValueType import UpdateValueType


class TradeBase:
    inventory: list["item"]
    cash: int
    PacMan: "PackagesManager"
    def sell_item(self, data): # Продавать и покукпать может только игрок
        for item_ in self.inventory:
            if item_.guid == data['guid']:
                if item_.wear >= data['count']:
                    self.cash += int(item_.get_cost(data['count']) *
                                     cfg_trading(self.skills['Trading']).coef_sell)
                    item_.separation(self.SpaceObject, data['count'])
                    self.PacMan.updateValue(UpdateValueType.PlayerCash)
                    self.PacMan.tradingItems()
                break

    def buy_item(self, data):
        if self.SpaceObject.inventory:
            for item_ in self.SpaceObject.inventory:
                if item_.guid == data['guid']:
                    if self.cash >= item_.get_cost(data['count']) \
                            and item_.wear >= data['count']:
                        self.cash -= int(item_.get_cost(data['count']) *
                                    cfg_trading(self.skills['Trading']).coef_buy)
                        item_.separation(self, data['count'])
                        self.PacMan.updateValue(UpdateValueType.PlayerCash)
                        self.PacMan.tradingItems()
                    break
        else:
            print("Не на планете")


