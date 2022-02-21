from .BaseShop import BaseShop

class ClanRepository(BaseShop):

    def open(self, Player:"DB_Player"):
        Player.PacMan.clan_repository()
