from .B_Shop import B_Shop

class Repository(B_Shop):

    def open(self, Player:"DB_Player"):
        Player.SendPacMan.player_repository()
