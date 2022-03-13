from .B_Shop import B_Shop

class ClanRepository(B_Shop):

    def open(self, Player:"DB_Player"):
        Player.SendPacMan.clan_repository()
