from .BaseShop import BaseShop

class Angar(BaseShop):

    def open(self, Player:"DB_Player"):
        Player.PacMan.playerAngar()