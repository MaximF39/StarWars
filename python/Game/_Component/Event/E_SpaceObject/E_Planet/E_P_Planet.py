from python.Game import E_Shop
from python.Game import ShopItem
from python.Game import ShipUpdate
from python.Game import GeneticLab
from python.Game import UpdateResources
from python.Static.Type.Keys import Keys
from python.Static.Type.Package.T_ServerRequest import T_ServerRequest


class E_P_Planet(E_Shop, ShopItem, ShipUpdate, GeneticLab, UpdateResources):

    def open_shop(self, data):
        match data[Keys.type]:
            case 1:
                ShopItem.get_shop(self)
                self.SendPacMan(T_ServerRequest.TRADING_ITEMS)
            case 2:
                self.SendPacMan(T_ServerRequest.TRADING_SHIPS)
                # ShipFactory.get_shop(self)
            case 3:
                GeneticLab.open(self)
            case 6:
                ShipUpdate.open(self)
            case 8:
                self.SendPacMan(T_ServerRequest.TRADING_ITEMS)

                # UpdateResources.open(self)


    def repair(self):
        self.health = self.ship['max_health']

    def restoreEnergy(self):
        self.energy = self.ship['max_energy']


