from python.Base.Event.PlanetEvent.ShopEvent import ShopEvent


class PlanetEvent(ShopEvent):

    def repair(self):
        self.health = self.ship['maxHealth']

    def restoreEnergy(self):
        self.energy = self.ship['maxEnergy']