from python.Base.Event.PlanetEvent.ShopEvent import ShopEvent
from python.Base.SpaceObject.Shop.ShopItem import ShopItem
from python.Base.SpaceObject.Shop.ShipUpdate import ShipUpdate
from python.Base.SpaceObject.Shop.GeneticLab import GeneticLab
from python.Base.SpaceObject.Shop.ShipFactory import ShipFactory
from python.Base.SpaceObject.Shop.UpdateResources import UpdateResources

class PlanetEvent(ShopEvent, ShopItem, ShipUpdate, GeneticLab, ShipFactory, UpdateResources):

    def open_shop(self, data):
        match data['type']:
            case 1:
                ShopItem.get_shop(self)
                self.Packages.trading_items()
            case 2:
                ShipFactory.get_shop(self)
            case 3:
                GeneticLab.get_shop(self)
            case 6:
                ShipUpdate.get_shop(self)
            case 8:
                UpdateResources.get_shop(self)


    def repair(self):
        self.health = self.ship['maxHealth']

    def restoreEnergy(self):
        self.energy = self.ship['maxEnergy']