from .B_Shop import B_Shop

class ShipUpdate(B_Shop):

    def open(self, Player:"DB_Player"):
        self.Player.Packages.update
