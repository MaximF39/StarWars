# from python.Base.B_Item.FakeShip import FakeShip
from python.Game.SpaceObjects.Item import item
from python.Config.CFG_Shop.cfg_trading import cfg_trading


class E_Trade:
    inventory: list["item"]
    cash: int
    bonus: int
    skills: dict
    SpaceObject: "DB_Planet | CFG_StaticSpaceObject"
    Game: "StarWars"
    trading:bool = False

    def sell_item(self, data): # Продавать и покукпать может только игрок
        if self.SpaceObject.inventory:
            for item_ in self.inventory:
                if item_.guid == data['guid']:
                    self.cash += int(item_.get_cost(data['wear']) * cfg_trading(self.skills['E_Trade']).coef_sell)
                    item_.sell(self.SpaceObject, data['wear'])
                    break
        else:
            print("Не на планете")

    def buy_item(self, data):
        if self.SpaceObject.inventory:
            for item_ in self.SpaceObject.inventory:
                if item_.guid == data['guid']:
                    self.cash -= int(item_.get_cost(data['wear']) * cfg_trading(self.skills['E_Trade']).coef_buy)
                    item_.buy(self, data['wear'])
                    break
        else:
            print("Не на планете")


    def buyItemByBonuses(self, dict_):
        Item_ = item(Game=self.Game, classNumber=dict_["classNumber"], OwnerClass=self, wear=dict_['wear'])
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
