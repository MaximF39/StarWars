from .B_Shop import B_Shop

class Angar(B_Shop):

    def open(self, Player:"DB_Player"):
        Player.SendPacMan.playerAngar()