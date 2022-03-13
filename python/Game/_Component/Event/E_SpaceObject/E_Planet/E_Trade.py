# from python._Component.I_Item.FakeShip import FakeShip
from python.Game.Game.SpaceObjects import item
from python.Config.CFG_Shop.cfg_trading import cfg_trading
from python.Static.Type.Keys import Keys


class E_Trade:
    inventory: list
    cash: int
    bonus: int
    skills: dict
    SpaceObject: object
    Game: object
    trading:bool = False

    def sell_item(self, data): # Продавать и покукпать может только игрок
        if self.SpaceObject.inventory:
            for item_ in self.inventory:
                if item_.guid == data[Keys.guid]:
                    self.cash += int(item_.get_cost(data[Keys.wear]) * cfg_trading(self.skills['E_Trade']).coef_sell)
                    item_.sell(self.SpaceObject, data[Keys.wear])
                    break
        else:
            pass
    def buy_item(self, data):
        if self.SpaceObject.inventory:
            for item_ in self.SpaceObject.inventory:
                if item_.guid == data['guid']:
                    self.cash -= int(item_.get_cost(data['wear']) * cfg_trading(self.skills['E_Trade']).coef_buy)
                    item_.buy(self, data['wear'])
                    break
        else:
            pass

    def buyItemByBonuses(self, dict_):
        Item_ = item(Game=self.Game, class_number=dict_[Keys.class_number], OwnerClass=self, wear=dict_[Keys.wear])
        bonus = Item_.cost // 1000
        if self.bonus - bonus >= 0:
            self.bonus -= bonus
            self.add_item(Item_)



    def trading_player(self, Player):
        self.trading = True

    def end_trading_player(self, Player):
        self.trading = False

    # def buyShip(self, data):
    #     self.angar.append(FakeShip(self.StarWars, data['id_ship']))
