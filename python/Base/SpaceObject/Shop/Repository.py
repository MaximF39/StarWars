from .BaseShop import BaseShop

class Repository(BaseShop):

    def open(self, Player:"DB_Player"):
        Player.PacMan.repository()
