from python.Base.Event.E_Planet.E_Shop import E_Shop
from python.Base.SpaceObject.Shop.ShopItem import ShopItem
from python.Base.SpaceObject.Shop.ShipUpdate import ShipUpdate
from python.Base.SpaceObject.Shop.GeneticLab import GeneticLab
from python.Base.SpaceObject.Shop.UpdateResources import UpdateResources
from python.Static.Type.Package.T_ServerRequest import T_ServerRequest


class E_Planet(E_Shop, ShopItem, ShipUpdate, GeneticLab, UpdateResources):

    def open_shop(self, data):
        match data['type']:
            case 1:
                ShopItem.get_shop(self)
                self.Packages.SendPacMan(T_ServerRequest.TRADING_ITEMS)
            # case 2:
            #     ShipFactory.get_shop(self)
            case 3:
                GeneticLab.open(self)
            case 6:
                ShipUpdate.open(self)
            case 8:
                UpdateResources.open(self)


    def repair(self):
        self.health = self.ship['maxHealth']

    def restoreEnergy(self):
        self.energy = self.ship['maxEnergy']
