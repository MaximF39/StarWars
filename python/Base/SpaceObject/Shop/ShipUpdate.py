from .BaseShop import BaseShop

class ShipUpdate(BaseShop):

    def open(self, Player:"DB_Player"):
        self.Player.Packages.update
